package com.autoeq.mobile.models

import kotlinx.serialization.Serializable

/**
 * Represents the frequency response measurement data.
 * Corresponds to the measurements structure in the webapp's measurements.json
 */
@Serializable
data class Measurement(
    val frequency: List<Double>,    // Frequency points in Hz
    val raw: List<Double>            // Raw frequency response in dB
) {
    /**
     * Get the measurement value at a specific frequency (interpolated if needed)
     */
    fun getValueAtFrequency(targetFreq: Double): Double? {
        if (frequency.isEmpty() || raw.isEmpty()) return null

        // Find the closest frequency points
        val index = frequency.binarySearch(targetFreq)

        return when {
            index >= 0 -> raw[index]  // Exact match
            index == -1 -> raw[0]     // Before first point
            -index - 1 >= frequency.size -> raw.last()  // After last point
            else -> {
                // Interpolate between two points
                val insertPoint = -index - 1
                val lowerIndex = insertPoint - 1
                val upperIndex = insertPoint

                val lowerFreq = frequency[lowerIndex]
                val upperFreq = frequency[upperIndex]
                val lowerVal = raw[lowerIndex]
                val upperVal = raw[upperIndex]

                // Linear interpolation
                val ratio = (targetFreq - lowerFreq) / (upperFreq - lowerFreq)
                lowerVal + ratio * (upperVal - lowerVal)
            }
        }
    }
}

/**
 * Multi-level nested structure for measurements
 * Structure: Map<headphone_name, Map<source, Map<rig, Measurement>>>
 */
typealias MeasurementDatabase = Map<String, Map<String, Map<String, Measurement>>>

/**
 * Container for measurement data with metadata
 */
data class MeasurementData(
    val headphoneName: String,
    val source: String,
    val rig: String,
    val measurement: Measurement,
    val resultPath: String          // Path to the result folder (for loading EQ file)
)
