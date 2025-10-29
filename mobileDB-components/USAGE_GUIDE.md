# AutoEq Mobile Components - Usage Guide

This guide shows you exactly how to integrate AutoEq search functionality into your mobile app, step by step.

## Table of Contents

1. [Setup & Installation](#setup--installation)
2. [Basic Search Implementation](#basic-search-implementation)
3. [UI Integration Examples](#ui-integration-examples)
4. [EQ Application](#eq-application)
5. [Advanced Features](#advanced-features)

---

## Setup & Installation

### Step 1: Add to Your Project

#### For Android (Gradle)

```kotlin
// settings.gradle.kts
include(":mobileDB-components")
project(":mobileDB-components").projectDir = File("path/to/mobileDB-components")

// app/build.gradle.kts
dependencies {
    implementation(project(":mobileDB-components"))
}
```

#### For Kotlin Multiplatform

```kotlin
kotlin {
    sourceSets {
        commonMain {
            dependencies {
                implementation(project(":mobileDB-components"))
            }
        }
    }
}
```

### Step 2: Bundle Data Files

You need to include the AutoEq data in your app. Two options:

#### Option A: Bundle with App (Recommended for smaller datasets)

```
app/src/main/assets/
  AutoEq/
    results/
    measurements/
```

Access in Android:
```kotlin
val resultsPath = "${context.filesDir}/AutoEq/results"
val measurementsPath = "${context.filesDir}/AutoEq/measurements"

// Copy from assets on first run
copyAssetsToInternalStorage(context)
```

#### Option B: Download on First Run (Recommended for full dataset)

```kotlin
class DataDownloader(private val context: Context) {
    suspend fun downloadAutoEqData(): Boolean {
        val baseUrl = "https://your-cdn.com/AutoEq/"
        val targetDir = File(context.filesDir, "AutoEq")

        // Download and extract results.zip
        // Download and extract measurements.zip

        return true
    }
}
```

---

## Basic Search Implementation

### Step 1: Initialize AutoEq

```kotlin
class AudioApp : Application() {
    lateinit var autoEq: AutoEqMobileApp
        private set

    override fun onCreate() {
        super.onCreate()

        val resultsPath = "${filesDir}/AutoEq/results"
        val measurementsPath = "${filesDir}/AutoEq/measurements"

        autoEq = AutoEqMobileApp(resultsPath, measurementsPath)

        // Initialize in background
        lifecycleScope.launch(Dispatchers.IO) {
            val success = autoEq.initialize()
            if (success) {
                Log.d("AutoEq", "Initialized successfully")
                val stats = autoEq.getStatistics()
                Log.d("AutoEq", "Indexed ${stats.totalEntries} entries")
            } else {
                Log.e("AutoEq", "Failed to initialize")
            }
        }
    }
}
```

### Step 2: Create Search Activity/Fragment

```kotlin
class SearchFragment : Fragment() {
    private val autoEq by lazy { (requireActivity().application as AudioApp).autoEq }
    private lateinit var binding: FragmentSearchBinding
    private lateinit var adapter: SearchResultsAdapter

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setupSearchBar()
        setupRecyclerView()
    }

    private fun setupSearchBar() {
        binding.searchBar.addTextChangedListener { text ->
            val query = text.toString()
            if (query.length >= 2) {
                performSearch(query)
            }
        }
    }

    private fun performSearch(query: String) {
        lifecycleScope.launch(Dispatchers.IO) {
            val results = autoEq.search(query, maxResults = 50)
            withContext(Dispatchers.Main) {
                adapter.submitList(results)
            }
        }
    }

    private fun setupRecyclerView() {
        adapter = SearchResultsAdapter { entry ->
            onEntrySelected(entry)
        }
        binding.recyclerView.adapter = adapter
    }

    private fun onEntrySelected(entry: Entry) {
        // Load and apply EQ for this entry
        lifecycleScope.launch(Dispatchers.IO) {
            val eq = autoEq.loadParametricEQ(entry)
            if (eq != null) {
                withContext(Dispatchers.Main) {
                    applyEQ(eq, entry.label)
                }
            } else {
                withContext(Dispatchers.Main) {
                    Toast.makeText(context, "No EQ available", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }
}
```

### Step 3: Create Adapter for Results

```kotlin
class SearchResultsAdapter(
    private val onItemClick: (Entry) -> Unit
) : ListAdapter<Entry, SearchResultsAdapter.ViewHolder>(EntryDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemSearchResultBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class ViewHolder(
        private val binding: ItemSearchResultBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(entry: Entry) {
            binding.apply {
                // Primary text: headphone name
                textHeadphoneName.text = entry.label

                // Secondary text: source and rig
                val secondaryText = buildString {
                    if (entry.source != "unknown") {
                        append("by ${entry.source}")
                    }
                    if (entry.rig != "unknown") {
                        if (isNotEmpty()) append(" ")
                        append("on ${entry.rig}")
                    }
                }
                textSourceRig.text = secondaryText

                // Form badge
                chipForm.text = entry.form

                root.setOnClickListener {
                    onItemClick(entry)
                }
            }
        }
    }

    private class EntryDiffCallback : DiffUtil.ItemCallback<Entry>() {
        override fun areItemsTheSame(oldItem: Entry, newItem: Entry): Boolean {
            return oldItem.label == newItem.label &&
                   oldItem.source == newItem.source &&
                   oldItem.rig == newItem.rig
        }

        override fun areContentsTheSame(oldItem: Entry, newItem: Entry): Boolean {
            return oldItem == newItem
        }
    }
}
```

---

## UI Integration Examples

### Example 1: Search Bar with Autocomplete

```kotlin
class SearchActivity : AppCompatActivity() {
    private val autoEq by lazy { (application as AudioApp).autoEq }

    private fun setupAutocomplete() {
        val autoCompleteTextView = findViewById<AutoCompleteTextView>(R.id.searchInput)

        autoCompleteTextView.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable?) {
                val query = s.toString()
                if (query.length >= 2) {
                    lifecycleScope.launch(Dispatchers.IO) {
                        val suggestions = autoEq.getSuggestions(query, 10)
                        withContext(Dispatchers.Main) {
                            val adapter = ArrayAdapter(
                                this@SearchActivity,
                                android.R.layout.simple_dropdown_item_1line,
                                suggestions
                            )
                            autoCompleteTextView.setAdapter(adapter)
                            adapter.notifyDataSetChanged()
                        }
                    }
                }
            }

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
        })

        autoCompleteTextView.setOnItemClickListener { _, _, position, _ ->
            val selectedName = autoCompleteTextView.adapter.getItem(position) as String
            performFullSearch(selectedName)
        }
    }
}
```

### Example 2: Filter Chips

```kotlin
class SearchWithFiltersFragment : Fragment() {
    private val autoEq by lazy { (requireActivity().application as AudioApp).autoEq }
    private var selectedSource: String? = null
    private var selectedForm: String? = null
    private var selectedRig: String? = null

    private fun setupFilterChips() {
        // Source filter
        binding.chipGroupSources.removeAllViews()
        autoEq.getAllSources().forEach { source ->
            val chip = Chip(requireContext()).apply {
                text = source
                isCheckable = true
                setOnCheckedChangeListener { _, isChecked ->
                    selectedSource = if (isChecked) source else null
                    applyFilters()
                }
            }
            binding.chipGroupSources.addView(chip)
        }

        // Form filter
        binding.chipGroupForms.removeAllViews()
        autoEq.getAllForms().forEach { form ->
            val chip = Chip(requireContext()).apply {
                text = form
                isCheckable = true
                setOnCheckedChangeListener { _, isChecked ->
                    selectedForm = if (isChecked) form else null
                    applyFilters()
                }
            }
            binding.chipGroupForms.addView(chip)
        }
    }

    private fun applyFilters() {
        lifecycleScope.launch(Dispatchers.IO) {
            var results = autoEq.getEntries()

            selectedSource?.let { source ->
                results = results.filter { it.source == source }
            }

            selectedForm?.let { form ->
                results = results.filter { it.form == form }
            }

            selectedRig?.let { rig ->
                results = results.filter { it.rig == rig }
            }

            withContext(Dispatchers.Main) {
                adapter.submitList(results)
            }
        }
    }
}
```

### Example 3: Recent Searches / Favorites

```kotlin
class SearchHistoryManager(private val context: Context) {
    private val prefs = context.getSharedPreferences("search_history", Context.MODE_PRIVATE)
    private val gson = Gson()

    fun addToHistory(entry: Entry) {
        val history = getHistory().toMutableList()
        history.remove(entry) // Remove if already exists
        history.add(0, entry) // Add to front
        if (history.size > 10) {
            history.removeLast()
        }
        saveHistory(history)
    }

    fun getHistory(): List<Entry> {
        val json = prefs.getString("history", "[]") ?: "[]"
        val type = object : TypeToken<List<Entry>>() {}.type
        return gson.fromJson(json, type)
    }

    private fun saveHistory(history: List<Entry>) {
        prefs.edit().putString("history", gson.toJson(history)).apply()
    }

    fun addToFavorites(entry: Entry) {
        val favorites = getFavorites().toMutableList()
        if (!favorites.contains(entry)) {
            favorites.add(entry)
            saveFavorites(favorites)
        }
    }

    fun removeFromFavorites(entry: Entry) {
        val favorites = getFavorites().toMutableList()
        favorites.remove(entry)
        saveFavorites(favorites)
    }

    fun getFavorites(): List<Entry> {
        val json = prefs.getString("favorites", "[]") ?: "[]"
        val type = object : TypeToken<List<Entry>>() {}.type
        return gson.fromJson(json, type)
    }

    private fun saveFavorites(favorites: List<Entry>) {
        prefs.edit().putString("favorites", gson.toJson(favorites)).apply()
    }
}
```

---

## EQ Application

### Android Audio System Integration

```kotlin
class AudioEQManager(private val audioSessionId: Int) {
    private var equalizer: Equalizer? = null
    private var currentEQ: ParametricEQ? = null

    fun applyParametricEQ(eq: ParametricEQ) {
        // Release old equalizer
        equalizer?.release()

        // Note: Android's built-in Equalizer only supports fixed bands
        // This is a simplified example. For true parametric EQ,
        // you'd need a DSP library like Superpowered or custom AudioEffect

        try {
            equalizer = Equalizer(0, audioSessionId).apply {
                enabled = false

                // Get available bands
                val numBands = numberOfBands.toInt()
                Log.d("EQ", "Available bands: $numBands")

                // Apply bands (limited to available bands)
                eq.bands.take(numBands).forEachIndexed { index, band ->
                    // Find closest frequency band
                    val centerFreq = getCenterFreq(index.toShort()) / 1000.0 // Hz
                    Log.d("EQ", "Band $index: ${centerFreq} Hz")

                    // Set level (convert dB to millibels)
                    val levelMillibels = (band.gain * 100).toInt().toShort()
                    setBandLevel(index.toShort(), levelMillibels)
                }

                enabled = true
            }

            currentEQ = eq
            Log.d("EQ", "Applied EQ: ${eq.bands.size} bands, preamp: ${eq.preamp} dB")

        } catch (e: Exception) {
            Log.e("EQ", "Failed to apply EQ", e)
        }
    }

    fun disable() {
        equalizer?.enabled = false
    }

    fun enable() {
        equalizer?.enabled = true
    }

    fun release() {
        equalizer?.release()
        equalizer = null
    }

    fun getCurrentEQ() = currentEQ
}

// Usage in Activity/Service
class MusicPlayerActivity : AppCompatActivity() {
    private lateinit var eqManager: AudioEQManager
    private lateinit var mediaPlayer: MediaPlayer

    private fun setupAudio() {
        mediaPlayer = MediaPlayer().apply {
            setDataSource(musicFilePath)
            prepare()
        }

        // Create EQ manager with media player's audio session ID
        eqManager = AudioEQManager(mediaPlayer.audioSessionId)
    }

    private fun applyEQ(eq: ParametricEQ, headphoneName: String) {
        eqManager.applyParametricEQ(eq)
        Toast.makeText(this, "Applied EQ for $headphoneName", Toast.LENGTH_SHORT).show()
    }

    override fun onDestroy() {
        super.onDestroy()
        eqManager.release()
        mediaPlayer.release()
    }
}
```

### Using a Professional DSP Library (Superpowered)

```kotlin
class SuperpoweredEQManager {
    private var filter: SuperpoweredFilter? = null

    fun applyParametricEQ(eq: ParametricEQ, sampleRate: Int) {
        eq.bands.forEachIndexed { index, band ->
            when (band.filterType) {
                ParametricEQBand.FilterType.PK -> {
                    // Parametric/Peaking filter
                    SuperpoweredFilter.Parametric(
                        sampleRate,
                        band.frequency.toFloat(),
                        band.q.toFloat(),
                        band.gain.toFloat()
                    )
                }
                ParametricEQBand.FilterType.LSC -> {
                    // Low shelf
                    SuperpoweredFilter.LowShelf(
                        sampleRate,
                        band.frequency.toFloat(),
                        band.gain.toFloat()
                    )
                }
                ParametricEQBand.FilterType.HSC -> {
                    // High shelf
                    SuperpoweredFilter.HighShelf(
                        sampleRate,
                        band.frequency.toFloat(),
                        band.gain.toFloat()
                    )
                }
                // etc...
            }
        }
    }
}
```

---

## Advanced Features

### Feature 1: Compare Multiple Measurements

```kotlin
class CompareFragment : Fragment() {
    private val autoEq by lazy { (requireActivity().application as AudioApp).autoEq }
    private val selectedEntries = mutableListOf<Entry>()

    fun addToComparison(entry: Entry) {
        if (selectedEntries.size < 4) {
            selectedEntries.add(entry)
            updateComparisonView()
        }
    }

    private fun updateComparisonView() {
        binding.comparisonLayout.removeAllViews()

        selectedEntries.forEach { entry ->
            val entryView = layoutInflater.inflate(
                R.layout.item_comparison_entry,
                binding.comparisonLayout,
                false
            )

            entryView.findViewById<TextView>(R.id.textName).text = entry.label
            entryView.findViewById<TextView>(R.id.textSource).text = entry.source
            entryView.findViewById<TextView>(R.id.textRig).text = entry.rig

            entryView.findViewById<Button>(R.id.btnApply).setOnClickListener {
                applyEQForEntry(entry)
            }

            binding.comparisonLayout.addView(entryView)
        }
    }
}
```

### Feature 2: Export/Import EQ Settings

```kotlin
class EQExporter {
    fun exportToFile(eq: ParametricEQ, outputFile: File) {
        val content = ParametricEQParser.toFileFormat(eq)
        outputFile.writeText(content)
    }

    fun exportToJson(eq: ParametricEQ, outputFile: File) {
        val json = Json.encodeToString(eq)
        outputFile.writeText(json)
    }

    fun importFromFile(inputFile: File): ParametricEQ {
        return ParametricEQParser.parseFile(inputFile)
    }

    fun shareEQ(context: Context, eq: ParametricEQ, headphoneName: String) {
        val tempFile = File(context.cacheDir, "${headphoneName}_EQ.txt")
        exportToFile(eq, tempFile)

        val uri = FileProvider.getUriForFile(
            context,
            "${context.packageName}.fileprovider",
            tempFile
        )

        val shareIntent = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_STREAM, uri)
            putExtra(Intent.EXTRA_TEXT, "EQ settings for $headphoneName")
        }

        context.startActivity(Intent.createChooser(shareIntent, "Share EQ"))
    }
}
```

### Feature 3: EQ Presets Management

```kotlin
class EQPresetsManager(private val context: Context) {
    private val prefs = context.getSharedPreferences("eq_presets", Context.MODE_PRIVATE)

    data class EQPreset(
        val name: String,
        val entry: Entry,
        val eq: ParametricEQ,
        val timestamp: Long = System.currentTimeMillis()
    )

    fun savePreset(name: String, entry: Entry, eq: ParametricEQ) {
        val preset = EQPreset(name, entry, eq)
        val json = Json.encodeToString(preset)
        prefs.edit().putString("preset_$name", json).apply()
    }

    fun loadPreset(name: String): EQPreset? {
        val json = prefs.getString("preset_$name", null) ?: return null
        return Json.decodeFromString(json)
    }

    fun getAllPresets(): List<EQPreset> {
        return prefs.all.mapNotNull { (key, value) ->
            if (key.startsWith("preset_") && value is String) {
                try {
                    Json.decodeFromString<EQPreset>(value)
                } catch (e: Exception) {
                    null
                }
            } else {
                null
            }
        }
    }

    fun deletePreset(name: String) {
        prefs.edit().remove("preset_$name").apply()
    }
}
```

---

## Performance Tips

### 1. Lazy Initialization

```kotlin
class AudioApp : Application() {
    val autoEq by lazy {
        AutoEqMobileApp(
            "${filesDir}/AutoEq/results",
            "${filesDir}/AutoEq/measurements"
        ).apply {
            // Initialize in background
            GlobalScope.launch(Dispatchers.IO) {
                initialize()
            }
        }
    }
}
```

### 2. Cache Search Results

```kotlin
class CachedSearchEngine(private val autoEq: AutoEqMobileApp) {
    private val cache = LruCache<String, List<Entry>>(50) // Cache last 50 queries

    fun search(query: String): List<Entry> {
        return cache.get(query) ?: run {
            val results = autoEq.search(query)
            cache.put(query, results)
            results
        }
    }
}
```

### 3. Debounce Search Input

```kotlin
class DebouncedSearchBar(
    private val searchAction: (String) -> Unit,
    private val delayMillis: Long = 300
) : TextWatcher {
    private var searchJob: Job? = null

    override fun afterTextChanged(s: Editable?) {
        searchJob?.cancel()
        searchJob = lifecycleScope.launch {
            delay(delayMillis)
            searchAction(s.toString())
        }
    }

    override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
    override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
}
```

---

## Complete Example App

See `examples/` directory for a complete sample app demonstrating:
- Search with autocomplete
- Filter by source/rig/form
- Apply EQ to MediaPlayer
- Save favorites
- Recent searches
- Export/share EQ settings

---

## Need Help?

Common issues and solutions:

1. **Index building is slow**: Run in background with progress indicator
2. **Search returns unexpected results**: Check relevance scoring in `MeasurementSearch`
3. **EQ not applying**: Verify audio session ID is correct for your player
4. **File not found errors**: Ensure data directories are extracted correctly

For more help, check the main README.md or open an issue.
