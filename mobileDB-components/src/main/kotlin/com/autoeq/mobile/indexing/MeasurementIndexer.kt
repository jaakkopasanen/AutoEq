package com.autoeq.mobile.indexing

import com.autoeq.mobile.crawlers.HeadphonecomCrawler
import com.autoeq.mobile.crawlers.InnerfidelityCrawler
import com.autoeq.mobile.crawlers.RtingsCrawler
import com.autoeq.mobile.models.Entry
import com.autoeq.mobile.models.MeasurementData
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import java.io.File

/**
 * Main indexer for AutoEq measurements.
 * Corresponds to Python's update_result_indexes.py:367-399
 *
 * This class scans the results directory and creates:
 * 1. A list of entries for the search functionality
 * 2. A mapping of measurement data paths
 *
 * Usage:
 *   val indexer = MeasurementIndexer(
 *       resultsPath = File("/path/to/results"),
 *       measurementsPath = File("/path/to/measurements")
 *   )
 *   indexer.buildIndex()
 *   val entries = indexer.getEntries()
 *   val measurements = indexer.getMeasurementDataList()
 */
class MeasurementIndexer(
    private val resultsPath: File,
    private val measurementsPath: File
) {
    private val nameIndexes = mutableMapOf<String, NameIndex>()
    private val entries = mutableListOf<Entry>()
    private val measurementDataList = mutableListOf<MeasurementData>()

    // Pretty JSON serializer for output
    private val json = Json {
        prettyPrint = true
        encodeDefaults = true
    }

    /**
     * Initialize name indexes from TSV files and crawlers
     * Corresponds to update_result_indexes.py:22-26
     */
    fun loadNameIndexes() {
        nameIndexes.clear()

        // Load all name_index.tsv files
        measurementsPath.listFiles()?.forEach { sourceDir ->
            if (sourceDir.isDirectory) {
                val tsvFile = File(sourceDir, "name_index.tsv")
                if (tsvFile.exists()) {
                    try {
                        val nameIndex = NameIndex.fromTsvFile(tsvFile)
                        nameIndexes[sourceDir.name] = nameIndex
                        println("Loaded name index for ${sourceDir.name}: ${nameIndex.size()} items")
                    } catch (e: Exception) {
                        println("Warning: Failed to load name index for ${sourceDir.name}")
                        println("Error: ${e.message}")
                    }
                }
            }
        }

        // Add hardcoded crawlers for sources without TSV files
        // Corresponds to update_result_indexes.py:25-26
        val headphonecomPath = File(measurementsPath, "Headphone.com Legacy")
        if (headphonecomPath.exists()) {
            nameIndexes["Headphone.com Legacy"] = HeadphonecomCrawler(headphonecomPath).getNameIndex()
        }

        val innerfidelityPath = File(measurementsPath, "Innerfidelity")
        if (innerfidelityPath.exists()) {
            nameIndexes["Innerfidelity"] = InnerfidelityCrawler(innerfidelityPath).getNameIndex()
        }

        // Note: Rtings typically has a name_index.tsv, but can fall back to crawler if needed
        val rtingsPath = File(measurementsPath, "Rtings")
        if (rtingsPath.exists() && !nameIndexes.containsKey("Rtings")) {
            nameIndexes["Rtings"] = RtingsCrawler(rtingsPath).getNameIndex()
        }

        println("Total name indexes loaded: ${nameIndexes.size}")
    }

    /**
     * Build the complete index by scanning the results directory
     * Corresponds to update_result_indexes.py:367-399
     */
    fun buildIndex() {
        entries.clear()
        measurementDataList.clear()

        // Load name indexes first
        if (nameIndexes.isEmpty()) {
            loadNameIndexes()
        }

        // Scan all result paths
        val resultPaths = ResultPath.scanResultsDirectory(resultsPath)
        println("Found ${resultPaths.size} result paths")

        resultPaths.forEach { path ->
            try {
                // Extract rig from path or name index
                // Corresponds to update_result_indexes.py:378-385
                var rig = path.rig

                if (rig.isEmpty()) {
                    // Fallback to name index lookup
                    try {
                        val nameIndex = nameIndexes[path.sourceName]
                        if (nameIndex != null) {
                            rig = nameIndex.findOne(name = path.headphoneName).rig
                        }
                    } catch (e: Exception) {
                        println("Warning: Could not find rig for ${path.headphoneName} from ${path.sourceName}")
                        rig = "unknown"
                    }
                }

                // Create entry
                val entry = Entry(
                    label = path.headphoneName,
                    form = path.form,
                    rig = rig,
                    source = path.sourceName
                )

                entries.add(entry)

                // Create measurement data reference
                // Note: Actual frequency response data would need to be loaded from CSV files
                // For mobile use, you'd typically load this on-demand rather than all at once
                val measurementData = MeasurementData(
                    headphoneName = path.headphoneName,
                    source = path.sourceName,
                    rig = rig,
                    measurement = com.autoeq.mobile.models.Measurement(
                        frequency = emptyList(),  // Load on-demand
                        raw = emptyList()          // Load on-demand
                    ),
                    resultPath = path.resultDir.absolutePath
                )

                measurementDataList.add(measurementData)

            } catch (e: Exception) {
                println("Warning: Failed to process result path: $path")
                println("Error: ${e.message}")
            }
        }

        println("Indexed ${entries.size} entries")
    }

    /**
     * Get all entries (for search)
     */
    fun getEntries(): List<Entry> = entries.toList()

    /**
     * Get all measurement data references
     */
    fun getMeasurementDataList(): List<MeasurementData> = measurementDataList.toList()

    /**
     * Get entries grouped by headphone name
     * This matches the webapp's entries.json format
     */
    fun getEntriesGroupedByName(): Map<String, List<Entry>> {
        return entries.groupBy { it.label }
    }

    /**
     * Export entries to JSON file
     * Format matches webapp's entries.json
     */
    fun exportEntriesToJson(outputFile: File) {
        val grouped = getEntriesGroupedByName()
        val jsonString = json.encodeToString(grouped)
        outputFile.writeText(jsonString)
        println("Exported entries to ${outputFile.absolutePath}")
    }

    /**
     * Export entries as a flat list to JSON file
     */
    fun exportEntriesListToJson(outputFile: File) {
        val jsonString = json.encodeToString(entries)
        outputFile.writeText(jsonString)
        println("Exported entries list to ${outputFile.absolutePath}")
    }

    /**
     * Get statistics about the index
     */
    fun getStatistics(): IndexStatistics {
        val sourceCount = entries.groupBy { it.source }.size
        val rigCount = entries.groupBy { it.rig }.size
        val formCount = entries.groupBy { it.form }.size
        val headphoneCount = entries.groupBy { it.label }.size

        return IndexStatistics(
            totalEntries = entries.size,
            uniqueHeadphones = headphoneCount,
            uniqueSources = sourceCount,
            uniqueRigs = rigCount,
            uniqueForms = formCount,
            sourceBreakdown = entries.groupBy { it.source }.mapValues { it.value.size },
            rigBreakdown = entries.groupBy { it.rig }.mapValues { it.value.size },
            formBreakdown = entries.groupBy { it.form }.mapValues { it.value.size }
        )
    }

    companion object {
        /**
         * Quick helper to build index from string paths
         */
        fun buildIndex(resultsPath: String, measurementsPath: String): MeasurementIndexer {
            val indexer = MeasurementIndexer(
                File(resultsPath),
                File(measurementsPath)
            )
            indexer.buildIndex()
            return indexer
        }
    }
}

/**
 * Statistics about the measurement index
 */
data class IndexStatistics(
    val totalEntries: Int,
    val uniqueHeadphones: Int,
    val uniqueSources: Int,
    val uniqueRigs: Int,
    val uniqueForms: Int,
    val sourceBreakdown: Map<String, Int>,
    val rigBreakdown: Map<String, Int>,
    val formBreakdown: Map<String, Int>
) {
    override fun toString(): String {
        return """
            |Index Statistics:
            |  Total Entries: $totalEntries
            |  Unique Headphones: $uniqueHeadphones
            |  Unique Sources: $uniqueSources
            |  Unique Rigs: $uniqueRigs
            |  Unique Forms: $uniqueForms
            |
            |Sources:
            |${sourceBreakdown.entries.joinToString("\n") { "  ${it.key}: ${it.value}" }}
            |
            |Rigs:
            |${rigBreakdown.entries.joinToString("\n") { "  ${it.key}: ${it.value}" }}
            |
            |Forms:
            |${formBreakdown.entries.joinToString("\n") { "  ${it.key}: ${it.value}" }}
        """.trimMargin()
    }
}
