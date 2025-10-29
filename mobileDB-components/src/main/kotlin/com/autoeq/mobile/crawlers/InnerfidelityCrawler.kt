package com.autoeq.mobile.crawlers

import com.autoeq.mobile.indexing.NameIndex
import com.autoeq.mobile.models.NameItem
import java.io.File

/**
 * Crawler for Innerfidelity measurements.
 * Corresponds to Python's InnerfidelityCrawler from innerfidelity_crawler.py:19-23
 *
 * This crawler generates a name index for the Innerfidelity source
 * which doesn't have a name_index.tsv file. All measurements are hardcoded
 * to use the "HMS II.3" rig.
 */
class InnerfidelityCrawler(
    measurementsPath: File
) : AbstractCrawler(measurementsPath, "Innerfidelity") {

    /**
     * Secondary constructor accepting a string path
     */
    constructor(measurementsPathStr: String) : this(File(measurementsPathStr))

    /**
     * Read the name index by scanning the data directory
     * All measurements use the hardcoded rig "HMS II.3"
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

                    // All Innerfidelity measurements use HMS II.3 rig (hardcoded)
                    val item = NameItem(
                        name = name,
                        form = form,
                        rig = "HMS II.3"
                    )

                    nameIndex.add(item)
                } catch (e: Exception) {
                    println("Warning: Failed to process file: ${csvFile.absolutePath}")
                    println("Error: ${e.message}")
                }
            }

        println("InnerfidelityCrawler: Loaded ${nameIndex.size()} measurements")
        return nameIndex
    }

    companion object {
        const val DEFAULT_RIG = "HMS II.3"
    }
}
