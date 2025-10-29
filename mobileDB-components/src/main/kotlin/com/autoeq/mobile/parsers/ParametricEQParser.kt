package com.autoeq.mobile.parsers

import com.autoeq.mobile.models.ParametricEQ
import com.autoeq.mobile.models.ParametricEQBand
import java.io.File

/**
 * Parser for AutoEq ParametricEQ.txt files.
 * These files contain parametric EQ settings that can be applied to audio devices.
 *
 * File format:
 *   Preamp: -5.2 dB
 *   Filter 1: ON LSC Fc 105 Hz Gain 8.8 dB Q 0.70
 *   Filter 2: ON PK Fc 70 Hz Gain -6.7 dB Q 0.29
 *   ...
 *
 * Where:
 *   - LSC = Low Shelf
 *   - HSC = High Shelf
 *   - PK = Peaking filter
 *   - LPQ = Low Pass
 *   - HPQ = High Pass
 */
object ParametricEQParser {

    /**
     * Parse a ParametricEQ file
     */
    fun parseFile(file: File): ParametricEQ {
        if (!file.exists()) {
            throw IllegalArgumentException("File does not exist: ${file.absolutePath}")
        }

        return parseText(file.readText())
    }

    /**
     * Parse a ParametricEQ file from a path string
     */
    fun parseFile(filePath: String): ParametricEQ {
        return parseFile(File(filePath))
    }

    /**
     * Parse ParametricEQ text content
     */
    fun parseText(content: String): ParametricEQ {
        val lines = content.lines()
        var preamp = 0.0
        val bands = mutableListOf<ParametricEQBand>()
        val metadata = mutableMapOf<String, String>()

        for (line in lines) {
            val trimmedLine = line.trim()
            if (trimmedLine.isEmpty()) continue

            when {
                // Parse preamp line: "Preamp: -5.2 dB"
                trimmedLine.startsWith("Preamp:", ignoreCase = true) -> {
                    preamp = parsePreamp(trimmedLine)
                }

                // Parse filter line: "Filter 1: ON LSC Fc 105 Hz Gain 8.8 dB Q 0.70"
                trimmedLine.startsWith("Filter", ignoreCase = true) -> {
                    val band = parseFilterLine(trimmedLine)
                    if (band != null) {
                        bands.add(band)
                    }
                }

                // Store other lines as metadata
                else -> {
                    val parts = trimmedLine.split(":", limit = 2)
                    if (parts.size == 2) {
                        metadata[parts[0].trim()] = parts[1].trim()
                    }
                }
            }
        }

        return ParametricEQ(
            preamp = preamp,
            bands = bands,
            metadata = metadata
        )
    }

    /**
     * Parse the preamp line
     * Example: "Preamp: -5.2 dB"
     */
    private fun parsePreamp(line: String): Double {
        val regex = Regex("""Preamp:\s*([-+]?\d+\.?\d*)\s*dB""", RegexOption.IGNORE_CASE)
        val match = regex.find(line)
        return match?.groupValues?.get(1)?.toDoubleOrNull() ?: 0.0
    }

    /**
     * Parse a filter line
     * Example: "Filter 1: ON LSC Fc 105 Hz Gain 8.8 dB Q 0.70"
     */
    private fun parseFilterLine(line: String): ParametricEQBand? {
        try {
            // Check if filter is ON
            if (!line.contains("ON", ignoreCase = true)) {
                return null
            }

            // Extract filter type (LSC, HSC, PK, LPQ, HPQ)
            val filterType = parseFilterType(line) ?: return null

            // Extract frequency: "Fc 105 Hz"
            val frequency = parseValue(line, "Fc", "Hz") ?: return null

            // Extract gain: "Gain 8.8 dB"
            val gain = parseValue(line, "Gain", "dB") ?: return null

            // Extract Q factor: "Q 0.70"
            val q = parseValue(line, "Q", null) ?: return null

            return ParametricEQBand(
                filterType = filterType,
                frequency = frequency,
                gain = gain,
                q = q
            )
        } catch (e: Exception) {
            println("Warning: Failed to parse filter line: $line")
            println("Error: ${e.message}")
            return null
        }
    }

    /**
     * Parse filter type from line
     */
    private fun parseFilterType(line: String): ParametricEQBand.FilterType? {
        return when {
            line.contains("LSC", ignoreCase = true) -> ParametricEQBand.FilterType.LSC
            line.contains("HSC", ignoreCase = true) -> ParametricEQBand.FilterType.HSC
            line.contains("PK", ignoreCase = true) -> ParametricEQBand.FilterType.PK
            line.contains("LPQ", ignoreCase = true) -> ParametricEQBand.FilterType.LPQ
            line.contains("HPQ", ignoreCase = true) -> ParametricEQBand.FilterType.HPQ
            else -> null
        }
    }

    /**
     * Parse a numeric value from the line
     * Example: parseValue("... Fc 105 Hz ...", "Fc", "Hz") -> 105.0
     */
    private fun parseValue(line: String, keyword: String, unit: String?): Double? {
        val unitPattern = if (unit != null) "\\s*$unit" else ""
        val regex = Regex("""$keyword\s+([-+]?\d+\.?\d*)$unitPattern""", RegexOption.IGNORE_CASE)
        val match = regex.find(line)
        return match?.groupValues?.get(1)?.toDoubleOrNull()
    }

    /**
     * Convert ParametricEQ to a human-readable string
     */
    fun toString(eq: ParametricEQ): String {
        val sb = StringBuilder()
        sb.appendLine("Preamp: ${eq.preamp} dB")
        eq.bands.forEachIndexed { index, band ->
            sb.appendLine(
                "Filter ${index + 1}: ${band.filterType} Fc ${band.frequency} Hz " +
                "Gain ${band.gain} dB Q ${band.q}"
            )
        }
        return sb.toString()
    }

    /**
     * Format ParametricEQ for export to file
     */
    fun toFileFormat(eq: ParametricEQ): String {
        val sb = StringBuilder()
        sb.appendLine("Preamp: ${eq.preamp} dB")
        eq.bands.forEachIndexed { index, band ->
            sb.appendLine(
                "Filter ${index + 1}: ON ${band.filterType} " +
                "Fc ${band.frequency.toInt()} Hz " +
                "Gain ${band.gain} dB " +
                "Q ${String.format("%.2f", band.q)}"
            )
        }
        return sb.toString()
    }
}
