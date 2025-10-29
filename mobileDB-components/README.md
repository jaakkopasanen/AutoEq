# AutoEq Mobile Components

Kotlin implementation of AutoEq search functionality for mobile applications (Android/iOS via Kotlin Multiplatform).

## Overview

This library provides the same search functionality as the AutoEq webapp, allowing mobile apps to:
- Index and search through local AutoEq measurements
- Display headphone models with their source and measurement rig
- Load and apply parametric EQ settings from result files

## Architecture

The library replicates the Python implementation's architecture:

```
mobileDB-components/
├── models/              # Data models (Entry, ParametricEQ, etc.)
├── indexing/            # Index building (MeasurementIndexer, NameIndex, ResultPath)
├── crawlers/            # Crawlers for sources without name_index.tsv
├── search/              # Search engine (MeasurementSearch)
├── parsers/             # File parsers (ParametricEQParser)
└── AutoEqMobileApp.kt   # Main integration class
```

## Prerequisites

Your mobile app needs:
1. Local copy of the `/results` directory (headphone EQ files)
2. Local copy of the `/measurements` directory (metadata and name indexes)
3. Kotlin support (Android native or Kotlin Multiplatform)

## Quick Start

### 1. Basic Integration

```kotlin
import com.autoeq.mobile.AutoEqMobileApp

// Initialize with local data paths
val autoEq = AutoEqMobileApp(
    resultsPath = "/sdcard/AutoEq/results",
    measurementsPath = "/sdcard/AutoEq/measurements"
)

// Build the index (do this once on app startup)
autoEq.initialize()

// Search for headphones
val results = autoEq.search("AirPods Pro")

// Display results
results.forEach { entry ->
    println("${entry.label}")
    println("  by ${entry.source} on ${entry.rig}")
}
```

### 2. Load and Apply EQ

```kotlin
// User selects a measurement from search results
val selectedEntry = results[0]

// Load the parametric EQ configuration
val eq = autoEq.loadParametricEQ(selectedEntry)

if (eq != null) {
    // Apply to your app's EQ system
    autoEq.applyEQ(eq)  // Implement this with your EQ integration
}
```

### 3. Search with Autocomplete

```kotlin
// As user types in search bar
fun onSearchQueryChanged(query: String) {
    val suggestions = autoEq.getSuggestions(query, maxSuggestions = 10)
    // Display suggestions in dropdown
    displaySuggestions(suggestions)
}
```

## Core Components

### 1. MeasurementIndexer

Scans the local `/results` directory and builds a searchable index.

```kotlin
val indexer = MeasurementIndexer(
    resultsPath = File("/path/to/results"),
    measurementsPath = File("/path/to/measurements")
)
indexer.buildIndex()

// Get statistics
val stats = indexer.getStatistics()
println("Indexed ${stats.totalEntries} measurements")
println("From ${stats.uniqueSources} sources")
```

**How it works:**
- Scans all `README.md` files in `/results/{source}/{rig form}/{headphone}/`
- Extracts rig from directory structure (e.g., "Bruel & Kjaer 5128 in-ear")
- Falls back to `name_index.tsv` files when rig not in path
- Uses hardcoded crawlers for sources without TSV files (Headphone.com Legacy, Innerfidelity)

### 2. MeasurementSearch

Provides fuzzy search functionality with relevance scoring.

```kotlin
val searchEngine = MeasurementSearch(entries)

// Search with relevance scoring
val results = searchEngine.search("Sony WH-1000XM4", maxResults = 20)

// Filter by source
val oratoryResults = searchEngine.filterBySource("oratory1990")

// Filter by rig
val b_and_k_5128_results = searchEngine.filterByRig("Bruel & Kjaer 5128")

// Filter by form
val inEarResults = searchEngine.filterByForm("in-ear")
```

**Scoring algorithm:**
- Exact match: +1000 points
- Starts with query: +500 points
- Contains query: +100 points
- Word boundary match: +200 points
- Source/rig/form match: +20-50 points

### 3. ParametricEQParser

Parses AutoEq's `ParametricEQ.txt` files.

```kotlin
val eq = ParametricEQParser.parseFile("/path/to/headphone ParametricEQ.txt")

println("Preamp: ${eq.preamp} dB")
println("Bands: ${eq.bands.size}")

eq.bands.forEach { band ->
    println("${band.filterType} @ ${band.frequency} Hz, Gain: ${band.gain} dB, Q: ${band.q}")
}
```

**Supported filter types:**
- `PK` - Peaking filter
- `LSC` - Low shelf
- `HSC` - High shelf
- `LPQ` - Low pass
- `HPQ` - High pass

### 4. Crawlers

For sources without `name_index.tsv` files:

```kotlin
// Headphone.com Legacy (hardcoded to "HMS II.3")
val crawler = HeadphonecomCrawler("/path/to/measurements/Headphone.com Legacy")
val nameIndex = crawler.readNameIndex()

// Innerfidelity (hardcoded to "HMS II.3")
val innerfidelityCrawler = InnerfidelityCrawler("/path/to/measurements/Innerfidelity")

// Rtings (version-dependent: "Bruel & Kjaer 5128" or "HMS II.3")
val rtingsCrawler = RtingsCrawler("/path/to/measurements/Rtings")
```

## Data Models

### Entry

Represents a searchable measurement entry.

```kotlin
data class Entry(
    val label: String,          // "Apple AirPods Pro"
    val form: String,           // "in-ear"
    val rig: String,            // "Bruel & Kjaer 5128"
    val source: String          // "HypetheSonics"
)
```

### ParametricEQ

Represents a parametric EQ configuration.

```kotlin
data class ParametricEQ(
    val preamp: Double,                    // -5.2 dB
    val bands: List<ParametricEQBand>,     // List of EQ bands
    val metadata: Map<String, String>      // Additional metadata
)

data class ParametricEQBand(
    val filterType: FilterType,            // PK, LSC, HSC, etc.
    val frequency: Double,                 // 105.0 Hz
    val gain: Double,                      // 8.8 dB
    val q: Double                          // 0.70
)
```

## Integration Examples

### Android Integration

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var autoEq: AutoEqMobileApp
    private lateinit var searchView: SearchView
    private lateinit var resultsAdapter: SearchResultsAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize AutoEq with local data paths
        val resultsPath = "${getExternalFilesDir(null)}/AutoEq/results"
        val measurementsPath = "${getExternalFilesDir(null)}/AutoEq/measurements"

        autoEq = AutoEqMobileApp(resultsPath, measurementsPath)

        // Build index in background
        lifecycleScope.launch(Dispatchers.IO) {
            autoEq.initialize()
            withContext(Dispatchers.Main) {
                setupSearch()
            }
        }
    }

    private fun setupSearch() {
        searchView.setOnQueryTextListener(object : SearchView.OnQueryTextListener {
            override fun onQueryTextChange(newText: String): Boolean {
                // Get autocomplete suggestions
                val suggestions = autoEq.getSuggestions(newText, 10)
                // Update suggestions dropdown
                return true
            }

            override fun onQueryTextSubmit(query: String): Boolean {
                // Perform search
                lifecycleScope.launch(Dispatchers.IO) {
                    val results = autoEq.search(query, 50)
                    withContext(Dispatchers.Main) {
                        resultsAdapter.updateResults(results)
                    }
                }
                return true
            }
        })
    }

    private fun onResultSelected(entry: Entry) {
        // Load and apply EQ
        lifecycleScope.launch(Dispatchers.IO) {
            val eq = autoEq.loadParametricEQ(entry)
            if (eq != null) {
                withContext(Dispatchers.Main) {
                    applyEQToAudioSystem(eq)
                }
            }
        }
    }

    private fun applyEQToAudioSystem(eq: ParametricEQ) {
        // Integrate with your audio system
        // Example using Android AudioEffect Equalizer:

        val equalizer = Equalizer(0, audioSessionId)
        equalizer.enabled = true

        // Note: Android's built-in Equalizer is limited to fixed bands
        // For parametric EQ, you'd need a custom audio processing library
        // or use bands that approximate the parametric settings

        // For demonstration with fixed band EQ:
        val bandCount = equalizer.numberOfBands.toInt()
        eq.bands.take(bandCount).forEachIndexed { index, band ->
            // Convert dB to millibels (Android format)
            val levelMillibels = (band.gain * 100).toInt().toShort()
            equalizer.setBandLevel(index.toShort(), levelMillibels)
        }
    }
}
```

### iOS Integration (via Kotlin Multiplatform)

```kotlin
// Shared Kotlin code
class AutoEqManager(
    private val resultsPath: String,
    private val measurementsPath: String
) {
    private val autoEq = AutoEqMobileApp(resultsPath, measurementsPath)

    fun initialize(completion: (Boolean) -> Unit) {
        // Use coroutines or callback-based approach
        val success = autoEq.initialize()
        completion(success)
    }

    fun search(query: String): List<Entry> {
        return autoEq.search(query)
    }

    fun loadEQ(entry: Entry): ParametricEQ? {
        return autoEq.loadParametricEQ(entry)
    }
}
```

```swift
// Swift/iOS side
import AutoEqMobile

class AudioViewController: UIViewController {
    let autoEqManager: AutoEqManager
    let audioEngine = AVAudioEngine()
    var eqNode: AVAudioUnitEQ?

    func setupAutoEq() {
        let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0].path
        let resultsPath = "\(documentsPath)/AutoEq/results"
        let measurementsPath = "\(documentsPath)/AutoEq/measurements"

        autoEqManager = AutoEqManager(resultsPath: resultsPath, measurementsPath: measurementsPath)
        autoEqManager.initialize { success in
            if success {
                print("AutoEq initialized successfully")
            }
        }
    }

    func applyEQ(parametricEQ: ParametricEQ) {
        // Create AVAudioUnitEQ with bands
        let eq = AVAudioUnitEQ(numberOfBands: parametricEQ.bands.count)

        for (index, band) in parametricEQ.bands.enumerated() {
            let filter = eq.bands[index]
            filter.filterType = convertFilterType(band.filterType)
            filter.frequency = Float(band.frequency)
            filter.gain = Float(band.gain)
            filter.bandwidth = calculateBandwidth(Float(band.q))
            filter.bypass = false
        }

        eq.globalGain = Float(parametricEQ.preamp)

        // Attach to audio engine
        audioEngine.attach(eq)
        // Connect nodes...
    }
}
```

## Performance Considerations

### Initialization

Building the index can take 1-5 seconds depending on the number of measurements:
- ~5000 measurements: ~2 seconds on modern devices
- Run initialization in a background thread
- Cache the index if possible (serialize to JSON)

### Search

Search is fast (< 50ms for typical queries) with proper indexing:
- Uses in-memory data structures
- Relevance scoring is O(n) where n = number of entries
- Results are sorted and limited to maxResults

### File Loading

Parametric EQ files are small (~1-2 KB):
- Loading is nearly instantaneous
- Can be done on UI thread if needed
- Consider caching frequently used EQ configurations

## File Structure Requirements

Your app should bundle or download these directories:

```
/results/
  /{source}/
    /{rig} {form}/
      /{headphone_name}/
        README.md
        {headphone_name} ParametricEQ.txt
        {headphone_name} FixedBandEQ.txt  (optional)
        {headphone_name} GraphicEQ.txt    (optional)

/measurements/
  /{source}/
    name_index.tsv  (for most sources)
    /data/
      /{form}/
        {headphone_name}.csv
```

## Rig Determination Logic

The library determines which rig was used for each measurement using this priority:

1. **Directory structure** (highest priority)
   - Extract from path: `results/{source}/{rig} {form}/{headphone}/`
   - Example: `results/crinacle/711 in-ear/` → rig = "711"

2. **name_index.tsv lookup** (fallback)
   - Read from `measurements/{source}/name_index.tsv`
   - TSV format: `name\tform\trig\tmanufacturer\ttrue_model\tfalse_name`

3. **Hardcoded crawlers** (special sources)
   - **Headphone.com Legacy**: Always `"HMS II.3"`
   - **Innerfidelity**: Always `"HMS II.3"`
   - **Rtings**: Version-dependent (`"Bruel & Kjaer 5128"` or `"HMS II.3"`)

## Dependencies

Required Kotlin dependencies:

```kotlin
dependencies {
    // Kotlin standard library
    implementation("org.jetbrains.kotlin:kotlin-stdlib:1.9.0")

    // Kotlinx Serialization (for JSON export)
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.0")

    // Coroutines (for async operations)
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
}
```

## Testing

Example test data structure:

```
testdata/
  results/
    TestSource/
      Test Rig in-ear/
        Test Headphone/
          README.md
          Test Headphone ParametricEQ.txt
  measurements/
    TestSource/
      name_index.tsv
      data/
        in-ear/
          Test Headphone.csv
```

## Troubleshooting

### "No NameItem found with name: X"

This means:
- The headphone exists in `/results` but not in the corresponding `name_index.tsv`
- Or the rig couldn't be extracted from the directory structure
- Solution: Ensure your local data is complete and synchronized

### "Results directory does not exist"

Check that:
- Paths are absolute and correct for your platform
- Directories have been extracted/downloaded to the device
- App has read permissions for the directories

### Search returns no results

Verify:
- Index was built successfully (`initialize()` returned true)
- Query string is not empty
- Directory structure matches expected format

## License

This implementation follows the structure of the AutoEq project. Refer to the main AutoEq repository for license information.

## Credits

Based on the AutoEq project by jaakkopasanen:
- Python implementation: `dbtools/update_result_indexes.py`
- Webapp: `webapp/ui/src/`
- Crawlers: `dbtools/*_crawler.py`
