package com.autoeq.mobile.models

import kotlinx.serialization.Serializable

/**
 * Represents a single parametric EQ filter/band
 */
@Serializable
data class ParametricEQBand(
    val filterType: FilterType,     // Filter type (PK, LSC, HSC, etc.)
    val frequency: Double,          // Center frequency in Hz
    val gain: Double,               // Gain in dB
    val q: Double                   // Q factor (bandwidth)
) {
    enum class FilterType {
        PK,     // Peaking filter
        LSC,    // Low shelf
        HSC,    // High shelf
        LPQ,    // Low pass
        HPQ     // High pass
    }
}

/**
 * Represents a complete parametric EQ configuration for a headphone
 * Parsed from device_parametricEQ.txt files
 */
@Serializable
data class ParametricEQ(
    val preamp: Double,                         // Preamp/gain in dB (to prevent clipping)
    val bands: List<ParametricEQBand>,          // List of EQ bands
    val metadata: Map<String, String> = emptyMap()  // Additional metadata from file
) {
    companion object {
        const val MAX_BANDS = 10  // Typical maximum for mobile EQ implementations
    }

    /**
     * Returns a limited version with maximum number of bands
     * (useful for hardware EQs with band limitations)
     */
    fun limitToBands(maxBands: Int): ParametricEQ {
        if (bands.size <= maxBands) return this

        // Sort bands by absolute gain (descending) to keep most impactful bands
        val sortedBands = bands.sortedByDescending { kotlin.math.abs(it.gain) }

        return ParametricEQ(
            preamp = preamp,
            bands = sortedBands.take(maxBands),
            metadata = metadata
        )
    }

    /**
     * Applies this EQ configuration to a device/app EQ
     * PLACEHOLDER: This is where you'd integrate with your app's EQ system
     */
    fun applyToEqualizer(/* equalizerInstance: YourEQInterface */): Boolean {
        // PLACEHOLDER CODE - Replace with your actual EQ implementation
        /*
        try {
            // Set preamp/gain
            equalizerInstance.setPreamp(preamp)

            // Apply each band
            bands.forEachIndexed { index, band ->
                equalizerInstance.setBand(
                    bandNumber = index,
                    frequency = band.frequency,
                    gain = band.gain,
                    q = band.q,
                    filterType = band.filterType
                )
            }

            // Enable the equalizer
            equalizerInstance.setEnabled(true)

            return true
        } catch (e: Exception) {
            return false
        }
        */

        // For now, just log the configuration
        println("Applying EQ Configuration:")
        println("Preamp: $preamp dB")
        bands.forEachIndexed { index, band ->
            println("Band ${index + 1}: ${band.filterType} @ ${band.frequency} Hz, Gain: ${band.gain} dB, Q: ${band.q}")
        }

        return true
    }
}
