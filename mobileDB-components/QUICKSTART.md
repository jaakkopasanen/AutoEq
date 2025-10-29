# Quick Start Guide

Get up and running with AutoEq mobile search in 5 minutes.

## 1. Copy Data Files

First, ensure you have the AutoEq data directories on your device:

```bash
# If testing locally, you can use the existing directories
# For production, copy to your app's files directory
```

## 2. Initialize in Your App

```kotlin
import com.autoeq.mobile.AutoEqMobileApp

class MyApp : Application() {
    lateinit var autoEq: AutoEqMobileApp

    override fun onCreate() {
        super.onCreate()

        // Use absolute paths to your local AutoEq directories
        val resultsPath = "${filesDir.parent}/AutoEq-Testing/results"
        val measurementsPath = "${filesDir.parent}/AutoEq-Testing/measurements"

        autoEq = AutoEqMobileApp(resultsPath, measurementsPath)

        // Build index (takes 2-5 seconds)
        lifecycleScope.launch(Dispatchers.IO) {
            autoEq.initialize()
        }
    }
}
```

## 3. Implement Search UI

```kotlin
class SearchActivity : AppCompatActivity() {
    private val autoEq by lazy { (application as MyApp).autoEq }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val searchBar: EditText = findViewById(R.id.searchBar)
        val resultsView: RecyclerView = findViewById(R.id.resultsView)

        searchBar.addTextChangedListener { text ->
            lifecycleScope.launch(Dispatchers.IO) {
                val results = autoEq.search(text.toString())
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
        // Load the parametric EQ file
        val eq = autoEq.loadParametricEQ(entry)

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
val results = autoEq.search("AirPods Pro")
results.forEach { entry ->
    println("Found: ${entry.label} by ${entry.source}")
}

// Test autocomplete
val suggestions = autoEq.getSuggestions("Sony")
println("Suggestions: $suggestions")

// Test EQ loading
val eq = autoEq.loadParametricEQ(results[0])
println("EQ has ${eq?.bands?.size} bands")
```

## Complete Minimal Example

```kotlin
import com.autoeq.mobile.AutoEqMobileApp

fun main() {
    // Initialize
    val autoEq = AutoEqMobileApp(
        resultsPath = "/absolute/path/to/results",
        measurementsPath = "/absolute/path/to/measurements"
    )

    autoEq.initialize()

    // Search
    val results = autoEq.search("Sony WH-1000XM4")

    // Display
    results.forEach { entry ->
        println("${entry.label} by ${entry.source} on ${entry.rig}")
    }

    // Load EQ
    if (results.isNotEmpty()) {
        val eq = autoEq.loadParametricEQ(results[0])
        println("\nEQ Configuration:")
        println("Preamp: ${eq?.preamp} dB")
        println("Bands: ${eq?.bands?.size}")
    }
}
```

## Next Steps

- Read [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed integration examples
- See [README.md](README.md) for architecture and API reference
- Check `AutoEqMobileApp.kt` for all available methods

## Troubleshooting

### "Failed to initialize"
- Check that resultsPath and measurementsPath point to correct directories
- Ensure directories contain the expected structure (results/{source}/{rig form}/{headphone}/)

### "No results found"
- Verify index was built successfully (`initialize()` returned true)
- Try with a simple query like "Sony" or "Apple"
- Check that result directories contain README.md files

### "ParametricEQ file not found"
- Not all measurements have parametric EQ files
- Check `SearchResult.hasParametricEQ` before trying to load

## Performance Notes

- Index building: 2-5 seconds for ~5000 measurements
- Search: < 50ms for typical queries
- EQ loading: < 5ms per file

Always run `initialize()` in a background thread!
