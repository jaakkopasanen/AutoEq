# Quick Start Guide

Get up and running with AutoEq mobile search in 5 minutes.

**Important:** This library is for **local-only** operation. No web scraping or network access. You need to bundle the `/results` and `/measurements` directories with your app.

## 1. Bundle Data Files

Ensure the AutoEq data directories are bundled with your app:
- `/results` - Contains all headphone EQ files
- `/measurements` - Contains metadata (optional for basic search)

## 2. Initialize (Simple Version - Recommended)

```kotlin
import com.autoeq.mobile.LocalAutoEqSearch

class MyApp : Application() {
    lateinit var search: LocalAutoEqSearch

    override fun onCreate() {
        super.onCreate()

        // Point to your bundled local directories
        val resultsPath = "${filesDir}/AutoEq/results"
        val measurementsPath = "${filesDir}/AutoEq/measurements"

        search = LocalAutoEqSearch(resultsPath, measurementsPath)

        // Build index from local files (takes 2-5 seconds)
        lifecycleScope.launch(Dispatchers.IO) {
            search.buildIndex()
        }
    }
}
```

**Note:** This only reads from local directories already in your app - no internet required!

## 3. Implement Search UI

```kotlin
class SearchActivity : AppCompatActivity() {
    private val search by lazy { (application as MyApp).search }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val searchBar: EditText = findViewById(R.id.searchBar)
        val resultsView: RecyclerView = findViewById(R.id.resultsView)

        searchBar.addTextChangedListener { text ->
            lifecycleScope.launch(Dispatchers.IO) {
                val results = search.search(text.toString())
                withContext(Dispatchers.Main) {
                    displayResults(results)
                }
            }
        }
    }

    private fun displayResults(entries: List<Entry>) {
        entries.forEach { entry ->
            println("${entry.label}")
            println("  by ${entry.source} on ${entry.rig}")
        }
    }
}
```

## 4. Load and Apply EQ

```kotlin
fun onHeadphoneSelected(entry: Entry) {
    lifecycleScope.launch(Dispatchers.IO) {
        // Load the parametric EQ file from local storage
        val eq = search.loadEQ(entry)

        if (eq != null) {
            withContext(Dispatchers.Main) {
                // Apply to your audio system
                applyToAudioSystem(eq)

                Toast.makeText(
                    this@SearchActivity,
                    "Applied EQ for ${entry.label}",
                    Toast.LENGTH_SHORT
                ).show()
            }
        }
    }
}

fun applyToAudioSystem(eq: ParametricEQ) {
    // PLACEHOLDER - Integrate with your EQ
    println("Applying EQ:")
    println("Preamp: ${eq.preamp} dB")
    eq.bands.forEach { band ->
        println("  ${band.filterType} @ ${band.frequency} Hz: ${band.gain} dB (Q=${band.q})")
    }
}
```

## 5. Test It

```kotlin
// Test search
val results = search.search("AirPods Pro")
results.forEach { entry ->
    println("Found: ${entry.label} by ${entry.source}")
}

// Test autocomplete
val suggestions = search.getSuggestions("Sony")
println("Suggestions: $suggestions")

// Test EQ loading
val eq = search.loadEQ(results[0])
println("EQ has ${eq?.bands?.size} bands")
```

## Complete Minimal Example

```kotlin
import com.autoeq.mobile.LocalAutoEqSearch

fun main() {
    // Initialize with local paths
    val search = LocalAutoEqSearch(
        resultsPath = "/path/to/local/results",
        measurementsPath = "/path/to/local/measurements"
    )

    // Build index from local files
    search.buildIndex()

    // Search locally
    val results = search.search("Sony WH-1000XM4")

    // Display
    results.forEach { entry ->
        println("${entry.label} by ${entry.source} on ${entry.rig}")
    }

    // Load EQ from local file
    if (results.isNotEmpty()) {
        val eq = search.loadEQ(results[0])
        println("\nEQ Configuration:")
        println("Preamp: ${eq?.preamp} dB")
        println("Bands: ${eq?.bands?.size}")
    }
}
```

## Next Steps

- **NEW:** See [SIMPLE_USAGE.md](SIMPLE_USAGE.md) for complete Android UI examples
- Read [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed integration examples
- See [README.md](README.md) for architecture and API reference

## Two Implementation Options

1. **LocalAutoEqSearch** (Recommended for most apps)
   - Simplified API
   - Only local directory scanning
   - See [SIMPLE_USAGE.md](SIMPLE_USAGE.md)
   - ✅ **No network code, no web scraping**

2. **AutoEqMobileApp** (Full-featured)
   - More advanced features
   - Additional metadata support
   - See [USAGE_GUIDE.md](USAGE_GUIDE.md)

## Troubleshooting

### "Failed to initialize" or "Indexed 0 entries"
- Verify that resultsPath points to correct local directory
- Ensure the `/results` directory is properly bundled with your app
- Check directory structure: `results/{source}/{rig form}/{headphone}/README.md`
- **This library does NOT download data** - files must already be present locally

### "No results found"
- Make sure you called `buildIndex()` first
- Try with a simple query like "Sony" or "Apple"
- Check that result directories contain README.md files

### "ParametricEQ file not found"
- Not all measurements have parametric EQ files
- The library will return `null` if the file doesn't exist

## Performance Notes

- Building index: 2-5 seconds for ~5000 measurements
- Search: < 50ms for typical queries
- EQ loading: < 5ms per file
- **All operations are local** - No network latency!

Always run `buildIndex()` in a background thread!
