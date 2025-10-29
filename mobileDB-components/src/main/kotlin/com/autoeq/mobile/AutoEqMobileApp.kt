package com.autoeq.mobile

import com.autoeq.mobile.indexing.MeasurementIndexer
import com.autoeq.mobile.models.Entry
import com.autoeq.mobile.models.ParametricEQ
import com.autoeq.mobile.parsers.ParametricEQParser
import com.autoeq.mobile.search.MeasurementSearch
import com.autoeq.mobile.search.SearchResult
import java.io.File

/**
 * Main integration class for AutoEq mobile functionality.
 * This class demonstrates how to use all the components together.
 *
 * Usage in your mobile app:
 *
 * ```kotlin
 * // Initialize the app with local data paths
 * val autoEq = AutoEqMobileApp(
 *     resultsPath = "/sdcard/AutoEq/results",
 *     measurementsPath = "/sdcard/AutoEq/measurements"
 * )
 *
 * // Build the index (do this once on app startup or in background)
 * autoEq.initialize()
 *
 * // Search for headphones
 * val results = autoEq.search("AirPods")
 *
 * // Load and apply EQ for a selected result
 * val eq = autoEq.loadParametricEQ(results[0])
 * autoEq.applyEQ(eq)
 * ```
 */
class AutoEqMobileApp(
    private val resultsPath: String,
    private val measurementsPath: String
) {
    private lateinit var indexer: MeasurementIndexer
    private lateinit var searchEngine: MeasurementSearch
    private var isInitialized = false

    /**
     * Initialize the app by building the measurement index.
     * This should be called once on app startup or when data is updated.
     *
     * @param forceRebuild If true, rebuilds the index even if cached
     * @return True if initialization was successful
     */
    fun initialize(forceRebuild: Boolean = false): Boolean {
        return try {
            println("Initializing AutoEq Mobile App...")
            println("Results path: $resultsPath")
            println("Measurements path: $measurementsPath")

            // Build the index
            indexer = MeasurementIndexer(
                resultsPath = File(resultsPath),
                measurementsPath = File(measurementsPath)
            )

            indexer.buildIndex()

            // Initialize search engine
            searchEngine = MeasurementSearch(indexer.getEntries())

            // Print statistics
            val stats = indexer.getStatistics()
            println("Initialization complete!")
            println(stats)

            isInitialized = true
            true
        } catch (e: Exception) {
            println("Failed to initialize AutoEq Mobile App: ${e.message}")
            e.printStackTrace()
            false
        }
    }

    /**
     * Search for headphones matching the query.
     *
     * @param query The search query (headphone name, source, or rig)
     * @param maxResults Maximum number of results to return
     * @return List of matching entries
     */
    fun search(query: String, maxResults: Int = 50): List<Entry> {
        checkInitialized()
        return searchEngine.search(query, maxResults)
    }

    /**
     * Search and return full search results with additional metadata.
     *
     * @param query The search query
     * @param maxResults Maximum number of results to return
     * @return List of SearchResult objects with full metadata
     */
    fun searchWithMetadata(query: String, maxResults: Int = 50): List<SearchResult> {
        checkInitialized()
        val entries = searchEngine.search(query, maxResults)

        return entries.map { entry ->
            // Build the result path
            val resultPath = buildResultPath(entry)
            val resultDir = File(resultPath)

            // Check which EQ files exist
            val parametricEQFile = File(resultDir, "${entry.label} ParametricEQ.txt")
            val fixedBandEQFile = File(resultDir, "${entry.label} FixedBandEQ.txt")
            val graphicEQFile = File(resultDir, "${entry.label} GraphicEQ.txt")

            SearchResult(
                entry = entry,
                resultPath = resultPath,
                hasParametricEQ = parametricEQFile.exists(),
                hasFixedBandEQ = fixedBandEQFile.exists(),
                hasGraphicEQ = graphicEQFile.exists()
            )
        }
    }

    /**
     * Get autocomplete suggestions for the search query.
     *
     * @param query The partial search query
     * @param maxSuggestions Maximum number of suggestions
     * @return List of suggested headphone names
     */
    fun getSuggestions(query: String, maxSuggestions: Int = 10): List<String> {
        checkInitialized()
        return searchEngine.getSuggestions(query, maxSuggestions)
    }

    /**
     * Load the parametric EQ configuration for a specific entry.
     *
     * @param entry The entry to load EQ for
     * @return ParametricEQ object, or null if file doesn't exist
     */
    fun loadParametricEQ(entry: Entry): ParametricEQ? {
        checkInitialized()

        try {
            val resultPath = buildResultPath(entry)
            val eqFile = File(resultPath, "${entry.label} ParametricEQ.txt")

            if (!eqFile.exists()) {
                println("Parametric EQ file not found: ${eqFile.absolutePath}")
                return null
            }

            return ParametricEQParser.parseFile(eqFile)
        } catch (e: Exception) {
            println("Failed to load parametric EQ: ${e.message}")
            e.printStackTrace()
            return null
        }
    }

    /**
     * Apply parametric EQ to the device's audio system.
     * PLACEHOLDER: Integrate with your app's actual EQ implementation.
     *
     * @param eq The ParametricEQ configuration to apply
     * @return True if EQ was applied successfully
     */
    fun applyEQ(eq: ParametricEQ): Boolean {
        // PLACEHOLDER CODE - Replace with your actual EQ integration
        println("=== Applying Parametric EQ ===")
        println("Preamp: ${eq.preamp} dB")
        println("Bands: ${eq.bands.size}")

        eq.bands.forEachIndexed { index, band ->
            println("Band ${index + 1}: ${band.filterType} @ ${band.frequency} Hz, Gain: ${band.gain} dB, Q: ${band.q}")
        }

        /*
         * YOUR CODE HERE:
         * Integrate with your mobile app's EQ system.
         *
         * Example for Android with AudioEffect:
         *
         * val equalizer = Equalizer(0, audioSessionId)
         * equalizer.enabled = true
         *
         * // Set preamp (if supported)
         * // Note: Not all Android devices support preamp
         *
         * // Apply bands
         * eq.bands.forEachIndexed { index, band ->
         *     if (index < equalizer.numberOfBands) {
         *         equalizer.setBandLevel(
         *             index.toShort(),
         *             (band.gain * 100).toInt().toShort() // Convert to millibels
         *         )
         *     }
         * }
         *
         * Example for iOS with AVAudioUnitEQ:
         *
         * let eq = AVAudioUnitEQ(numberOfBands: bands.count)
         * for (index, band) in eq.bands.enumerated() {
         *     let filter = eq.bands[index]
         *     filter.filterType = convertFilterType(band.filterType)
         *     filter.frequency = Float(band.frequency)
         *     filter.gain = Float(band.gain)
         *     filter.bandwidth = calculateBandwidth(band.q)
         *     filter.bypass = false
         * }
         * eq.globalGain = Float(parametricEQ.preamp)
         */

        return true
    }

    /**
     * Filter entries by source (e.g., "oratory1990", "crinacle")
     */
    fun filterBySource(source: String): List<Entry> {
        checkInitialized()
        return searchEngine.filterBySource(source)
    }

    /**
     * Filter entries by rig (e.g., "HMS II.3", "Bruel & Kjaer 5128")
     */
    fun filterByRig(rig: String): List<Entry> {
        checkInitialized()
        return searchEngine.filterByRig(rig)
    }

    /**
     * Filter entries by form (e.g., "in-ear", "over-ear", "earbud")
     */
    fun filterByForm(form: String): List<Entry> {
        checkInitialized()
        return searchEngine.filterByForm(form)
    }

    /**
     * Get all available sources
     */
    fun getAllSources(): List<String> {
        checkInitialized()
        return searchEngine.getAllSources()
    }

    /**
     * Get all available rigs
     */
    fun getAllRigs(): List<String> {
        checkInitialized()
        return searchEngine.getAllRigs()
    }

    /**
     * Get all available forms
     */
    fun getAllForms(): List<String> {
        checkInitialized()
        return searchEngine.getAllForms()
    }

    /**
     * Get statistics about the indexed measurements
     */
    fun getStatistics() = indexer.getStatistics()

    /**
     * Build the file system path for a result entry
     */
    private fun buildResultPath(entry: Entry): String {
        // Determine the form-rig directory name
        val formRig = if (entry.rig.isNotEmpty() && entry.rig != "unknown") {
            "${entry.rig} ${entry.form}"
        } else {
            entry.form
        }

        return "$resultsPath/${entry.source}/$formRig/${entry.label}"
    }

    /**
     * Check if the app has been initialized
     */
    private fun checkInitialized() {
        if (!isInitialized) {
            throw IllegalStateException(
                "AutoEqMobileApp not initialized. Call initialize() first."
            )
        }
    }
}

/**
 * Example usage and integration guide
 */
fun main() {
    println("=== AutoEq Mobile App Example ===\n")

    // Initialize the app
    // Replace these paths with actual paths on your device
    val app = AutoEqMobileApp(
        resultsPath = "/path/to/AutoEq/results",
        measurementsPath = "/path/to/AutoEq/measurements"
    )

    // Build the index
    if (!app.initialize()) {
        println("Failed to initialize app")
        return
    }

    println("\n=== Example 1: Search for headphones ===")
    val searchResults = app.search("AirPods", maxResults = 5)
    searchResults.forEach { entry ->
        println("${entry.label} by ${entry.source} on ${entry.rig}")
    }

    println("\n=== Example 2: Get autocomplete suggestions ===")
    val suggestions = app.getSuggestions("Sony", maxSuggestions = 5)
    suggestions.forEach { println("  - $it") }

    println("\n=== Example 3: Load and apply EQ ===")
    if (searchResults.isNotEmpty()) {
        val firstResult = searchResults[0]
        println("Loading EQ for: ${firstResult.label}")

        val eq = app.loadParametricEQ(firstResult)
        if (eq != null) {
            println("Loaded EQ with ${eq.bands.size} bands")
            app.applyEQ(eq)
        } else {
            println("No parametric EQ available for this measurement")
        }
    }

    println("\n=== Example 4: Browse by source ===")
    val oratory1990Entries = app.filterBySource("oratory1990")
    println("Found ${oratory1990Entries.size} measurements from oratory1990")

    println("\n=== Example 5: Get available filters ===")
    println("Available sources: ${app.getAllSources().joinToString(", ")}")
    println("Available rigs: ${app.getAllRigs().joinToString(", ")}")
    println("Available forms: ${app.getAllForms().joinToString(", ")}")
}
