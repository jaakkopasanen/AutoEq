package com.autoeq.mobile.crawlers

import com.autoeq.mobile.indexing.NameIndex
import com.autoeq.mobile.models.NameItem
import java.io.File

/**
 * Crawler for Rtings measurements.
 * Corresponds to Python's RtingsCrawler from rtings_crawler.py:141-149
 *
 * This crawler generates a name index for the Rtings source.
 * The rig used depends on the measurement methodology version:
 *   - v1.8 and later: "Bruel & Kjaer 5128"
 *   - v1.7 and earlier: "HMS II.3"
 *
 * Note: This is a simplified version. The full Python implementation
 * parses methodology versions from the actual measurement files.
 * For mobile use, you may want to use a pre-generated index or
 * a simplified version based on file modification dates.
 */
class RtingsCrawler(
    measurementsPath: File,
    private val defaultRig: String = DEFAULT_RIG_V18
) : AbstractCrawler(measurementsPath, "Rtings") {

    /**
     * Secondary constructor accepting a string path
     */
    constructor(measurementsPathStr: String, defaultRig: String = DEFAULT_RIG_V18)
        : this(File(measurementsPathStr), defaultRig)

    /**
     * Read the name index by scanning the data directory
     *
     * SIMPLIFIED IMPLEMENTATION:
     * This version uses a default rig for all measurements.
     * The full Python implementation parses JSON files to determine
     * the methodology version for each measurement.
     *
     * For production use, you could:
     * 1. Pre-generate the name_index.tsv using the Python tools
     * 2. Implement full JSON parsing here
     * 3. Use file dates as a heuristic (newer files likely use v1.8)
     */
    override fun readNameIndex(): NameIndex {
        val nameIndex = NameIndex()
        val dataDir = File(measurementsPath, "data")

        if (!dataDir.exists() || !dataDir.isDirectory) {
            println("Warning: Data directory not found: ${dataDir.absolutePath}")
            return nameIndex
        }

        // Scan for all CSV files
        dataDir.walkTopDown()
            .filter { it.extension == "csv" }
            .forEach { csvFile ->
                try {
                    // Get headphone name from filename (remove .csv extension)
                    val name = csvFile.nameWithoutExtension

                    // Get form from parent directory name
                    // Directory structure: data/{form}/{name}.csv
                    val form = csvFile.parentFile.name

                    // Determine rig based on methodology version
                    // SIMPLIFIED: Using default rig (should parse JSON for accuracy)
                    val rig = determineRig(csvFile)

                    val item = NameItem(
                        name = name,
                        form = form,
                        rig = rig
                    )

                    nameIndex.add(item)
                } catch (e: Exception) {
                    println("Warning: Failed to process file: ${csvFile.absolutePath}")
                    println("Error: ${e.message}")
                }
            }

        println("RtingsCrawler: Loaded ${nameIndex.size()} measurements")
        return nameIndex
    }

    /**
     * Determine the rig used for a measurement
     *
     * SIMPLIFIED IMPLEMENTATION:
     * Returns the default rig. In a full implementation, this would:
     * 1. Find the corresponding JSON file
     * 2. Parse the methodology version
     * 3. Return "Bruel & Kjaer 5128" for v1.8+, "HMS II.3" for earlier
     */
    private fun determineRig(csvFile: File): String {
        // TODO: Implement full version detection
        // For now, use the default rig passed in constructor
        return defaultRig
    }

    companion object {
        const val DEFAULT_RIG_V18 = "Bruel & Kjaer 5128"  // For methodology v1.8+
        const val DEFAULT_RIG_V17 = "HMS II.3"             // For methodology v1.7 and earlier

        /**
         * Parse methodology version from version string
         * Example: "1.8" -> Pair(1, 8)
         */
        fun parseMethodologyVersion(versionStr: String): Pair<Int, Int> {
            val parts = versionStr.split(".")
            return Pair(
                parts.getOrNull(0)?.toIntOrNull() ?: 0,
                parts.getOrNull(1)?.toIntOrNull() ?: 0
            )
        }

        /**
         * Compare methodology versions
         * Returns: -1 if v1 < v2, 0 if equal, 1 if v1 > v2
         */
        fun compareVersions(v1: Pair<Int, Int>, v2: Pair<Int, Int>): Int {
            return when {
                v1.first != v2.first -> v1.first.compareTo(v2.first)
                else -> v1.second.compareTo(v2.second)
            }
        }

        /**
         * Determine rig from methodology version
         */
        fun rigFromMethodologyVersion(major: Int, minor: Int): String {
            return if (major > 1 || (major == 1 && minor >= 8)) {
                DEFAULT_RIG_V18
            } else {
                DEFAULT_RIG_V17
            }
        }
    }
}
