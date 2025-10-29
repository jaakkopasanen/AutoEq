package com.autoeq.mobile

import com.autoeq.mobile.models.Entry
import com.autoeq.mobile.models.ParametricEQ
import com.autoeq.mobile.parsers.ParametricEQParser
import java.io.File

/**
 * Simplified search interface for local AutoEq data.
 *
 * This class assumes you have already bundled /results and /measurements
 * directories in your app. No network access or downloading required.
 *
 * Usage:
 * ```kotlin
 * val search = LocalAutoEqSearch(
 *     resultsPath = "/path/to/local/results",
 *     measurementsPath = "/path/to/local/measurements"
 * )
 *
 * // Build index from local files (one time)
 * search.buildIndex()
 *
 * // Search
 * val results = search.search("AirPods")
 *
 * // Load EQ
 * val eq = search.loadEQ(results[0])
 * ```
 */
class LocalAutoEqSearch(
    private val resultsPath: String,
    private val measurementsPath: String
) {
    private val entries = mutableListOf<Entry>()
    private var isIndexed = false

    /**
     * Build the search index by scanning local /results directory.
     * Call this once when your app starts.
     */
    fun buildIndex(): Boolean {
        return try {
            println("Scanning local results directory: $resultsPath")

            val resultsDir = File(resultsPath)
            if (!resultsDir.exists()) {
                println("ERROR: Results directory not found: $resultsPath")
                return false
            }

            entries.clear()

            // Scan all result directories
            // Structure: results/{source}/{rig form}/{headphone_name}/README.md
            resultsDir.walkTopDown()
                .filter { it.name == "README.md" }
                .forEach { readmePath ->
                    try {
                        val entry = parseEntryFromPath(readmePath, resultsDir)
                        entries.add(entry)
                    } catch (e: Exception) {
                        // Skip invalid entries
                    }
                }

            isIndexed = true
            println("Indexed ${entries.size} entries from local storage")
            true
        } catch (e: Exception) {
            println("Failed to build index: ${e.message}")
            false
        }
    }

    /**
     * Search for headphones matching the query.
     * Searches in model name, source, and rig.
     */
    fun search(query: String, maxResults: Int = 50): List<Entry> {
        if (!isIndexed) {
            println("WARNING: Index not built. Call buildIndex() first.")
            return emptyList()
        }

        if (query.isBlank()) return emptyList()

        val lowerQuery = query.lowercase().trim()

        return entries
            .filter { entry ->
                entry.label.lowercase().contains(lowerQuery) ||
                entry.source.lowercase().contains(lowerQuery) ||
                entry.rig.lowercase().contains(lowerQuery)
            }
            .sortedWith(compareByDescending<Entry> { entry ->
                // Prioritize exact matches
                when {
                    entry.label.lowercase() == lowerQuery -> 1000
                    entry.label.lowercase().startsWith(lowerQuery) -> 500
                    else -> 100
                }
            }.thenBy { it.label })
            .take(maxResults)
    }

    /**
     * Get autocomplete suggestions
     */
    fun getSuggestions(query: String, maxSuggestions: Int = 10): List<String> {
        if (!isIndexed || query.isBlank()) return emptyList()

        val lowerQuery = query.lowercase()
        return entries
            .map { it.label }
            .distinct()
            .filter { it.lowercase().startsWith(lowerQuery) }
            .sorted()
            .take(maxSuggestions)
    }

    /**
     * Load the parametric EQ for a selected entry
     */
    fun loadEQ(entry: Entry): ParametricEQ? {
        try {
            val eqFile = getEQFile(entry)
            if (!eqFile.exists()) {
                println("EQ file not found: ${eqFile.absolutePath}")
                return null
            }
            return ParametricEQParser.parseFile(eqFile)
        } catch (e: Exception) {
            println("Failed to load EQ: ${e.message}")
            return null
        }
    }

    /**
     * Get all indexed entries
     */
    fun getAllEntries(): List<Entry> = entries.toList()

    /**
     * Filter by source
     */
    fun filterBySource(source: String): List<Entry> {
        return entries.filter { it.source.equals(source, ignoreCase = true) }
    }

    /**
     * Filter by form (in-ear, over-ear, earbud)
     */
    fun filterByForm(form: String): List<Entry> {
        return entries.filter { it.form.equals(form, ignoreCase = true) }
    }

    /**
     * Filter by rig
     */
    fun filterByRig(rig: String): List<Entry> {
        return entries.filter { it.rig.equals(rig, ignoreCase = true) }
    }

    /**
     * Get all unique sources available
     */
    fun getAllSources(): List<String> {
        return entries.map { it.source }.distinct().sorted()
    }

    /**
     * Get all unique forms available
     */
    fun getAllForms(): List<String> {
        return entries.map { it.form }.distinct().sorted()
    }

    /**
     * Get all unique rigs available
     */
    fun getAllRigs(): List<String> {
        return entries.map { it.rig }.distinct().sorted()
    }

    /**
     * Get index statistics
     */
    fun getStatistics(): Map<String, Any> {
        return mapOf(
            "total_entries" to entries.size,
            "unique_headphones" to entries.map { it.label }.distinct().size,
            "sources" to getAllSources(),
            "forms" to getAllForms(),
            "rigs" to getAllRigs()
        )
    }

    // Private helper methods

    private fun parseEntryFromPath(readmePath: File, resultsRoot: File): Entry {
        val relativePath = readmePath.toRelativeString(resultsRoot)
        val parts = relativePath.split(File.separator)

        if (parts.size < 4) {
            throw IllegalArgumentException("Invalid path structure")
        }

        // Path structure: {source}/{rig form}/{headphone_name}/README.md
        val source = parts[0]
        val formRig = parts[1]
        val headphoneName = parts[2]

        // Parse form and rig from combined string
        val (rig, form) = parseFormAndRig(formRig)

        return Entry(
            label = headphoneName,
            form = form,
            rig = rig,
            source = source
        )
    }

    private fun parseFormAndRig(formRig: String): Pair<String, String> {
        val formKeywords = listOf("in-ear", "over-ear", "earbud")

        val foundForm = formKeywords.firstOrNull {
            formRig.contains(it, ignoreCase = true)
        } ?: "unknown"

        val rig = formRig.replace(foundForm, "", ignoreCase = true).trim()

        return Pair(rig.ifEmpty { "unknown" }, foundForm)
    }

    private fun getEQFile(entry: Entry): File {
        val formRig = if (entry.rig != "unknown" && entry.rig.isNotEmpty()) {
            "${entry.rig} ${entry.form}"
        } else {
            entry.form
        }

        return File(
            "$resultsPath/${entry.source}/$formRig/${entry.label}/${entry.label} ParametricEQ.txt"
        )
    }
}
