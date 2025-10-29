package com.autoeq.mobile.indexing

import java.io.File

/**
 * Parses and represents a result path in the AutoEq directory structure.
 * Corresponds to Python's ResultPath class from update_result_indexes.py:85-91
 *
 * Expected structure: results/{source}/{rig} {form}/{headphone_name}/README.md
 * Examples:
 *   - results/HypetheSonics/Bruel & Kjaer 5128 in-ear/Apple AirPods Pro/README.md
 *   - results/crinacle/711 in-ear/64 Audio Nio/README.md
 *   - results/oratory1990/over-ear/AKG K371/README.md
 */
class ResultPath(val path: File, private val resultsRoot: File) {
    val sourceName: String
    val formRig: String
    val rig: String
    val form: String
    val headphoneName: String
    val absolutePath: String = path.absolutePath
    val resultDir: File

    init {
        // Get path relative to results root
        val relativePath = path.toRelativeString(resultsRoot)
        val parts = relativePath.split(File.separator)

        if (parts.size < 4) {
            throw IllegalArgumentException(
                "Invalid result path structure: $relativePath\n" +
                "Expected: {source}/{rig form}/{headphone_name}/README.md"
            )
        }

        // Parse path components
        // parts[0] = source name (e.g., "HypetheSonics", "crinacle", "oratory1990")
        // parts[1] = form and rig (e.g., "Bruel & Kjaer 5128 in-ear", "711 in-ear", "over-ear")
        // parts[2] = headphone name (e.g., "Apple AirPods Pro")
        // parts[3] = "README.md"

        sourceName = parts[0]
        formRig = parts[1]
        headphoneName = parts[2]
        resultDir = File(resultsRoot, "$sourceName/$formRig/$headphoneName")

        // Extract rig and form from the combined string
        // Form keywords: "in-ear", "over-ear", "earbud"
        val (extractedRig, extractedForm) = parseFormRig(formRig)
        rig = extractedRig
        form = extractedForm
    }

    /**
     * Parse the form-rig string to extract rig and form separately
     * Examples:
     *   - "Bruel & Kjaer 5128 in-ear" -> rig: "Bruel & Kjaer 5128", form: "in-ear"
     *   - "711 in-ear" -> rig: "711", form: "in-ear"
     *   - "over-ear" -> rig: "", form: "over-ear"
     *   - "HMS II.3 earbud" -> rig: "HMS II.3", form: "earbud"
     */
    private fun parseFormRig(formRig: String): Pair<String, String> {
        val formKeywords = listOf("in-ear", "over-ear", "earbud")

        // Find which form keyword is present
        val foundForm = formKeywords.firstOrNull { formRig.contains(it, ignoreCase = true) }
            ?: return Pair("", "unknown")

        // Extract rig by removing the form keyword
        val rigPart = formRig.replace(foundForm, "", ignoreCase = true).trim()

        return Pair(rigPart, foundForm)
    }

    /**
     * Get the file path for the parametric EQ file
     */
    fun getParametricEQFile(): File {
        return File(resultDir, "${headphoneName} ParametricEQ.txt")
    }

    /**
     * Get the file path for the fixed band EQ file
     */
    fun getFixedBandEQFile(): File {
        return File(resultDir, "${headphoneName} FixedBandEQ.txt")
    }

    /**
     * Get the file path for the graphic EQ file
     */
    fun getGraphicEQFile(): File {
        return File(resultDir, "${headphoneName} GraphicEQ.txt")
    }

    /**
     * Check if parametric EQ file exists
     */
    fun hasParametricEQ(): Boolean {
        return getParametricEQFile().exists()
    }

    /**
     * Check if this result has valid data
     */
    fun isValid(): Boolean {
        return resultDir.exists() && resultDir.isDirectory
    }

    companion object {
        /**
         * Scan the results directory and find all valid result paths
         */
        fun scanResultsDirectory(resultsRoot: File): List<ResultPath> {
            val results = mutableListOf<ResultPath>()

            if (!resultsRoot.exists() || !resultsRoot.isDirectory) {
                println("Warning: Results directory does not exist: ${resultsRoot.absolutePath}")
                return results
            }

            // Find all README.md files in the structure
            resultsRoot.walkTopDown()
                .filter { it.name == "README.md" }
                .forEach { readmePath ->
                    try {
                        val resultPath = ResultPath(readmePath, resultsRoot)
                        if (resultPath.isValid()) {
                            results.add(resultPath)
                        }
                    } catch (e: Exception) {
                        println("Warning: Failed to parse result path: ${readmePath.absolutePath}")
                        println("Error: ${e.message}")
                    }
                }

            return results
        }

        /**
         * Scan from a string path
         */
        fun scanResultsDirectory(resultsRootPath: String): List<ResultPath> {
            return scanResultsDirectory(File(resultsRootPath))
        }
    }

    override fun toString(): String {
        return "ResultPath(source=$sourceName, rig=$rig, form=$form, name=$headphoneName)"
    }
}
