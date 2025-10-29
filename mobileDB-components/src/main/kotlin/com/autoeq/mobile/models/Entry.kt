package com.autoeq.mobile.models

import kotlinx.serialization.Serializable

/**
 * Represents a searchable entry in the measurement database.
 * Corresponds to the entries structure in the webapp's entries.json
 */
@Serializable
data class Entry(
    val label: String,          // Display name (headphone name)
    val form: String,           // Form factor: "in-ear", "over-ear", "earbud"
    val rig: String,            // Measurement rig: "HMS II.3", "Bruel & Kjaer 5128", "711", etc.
    val source: String          // Source: "oratory1990", "crinacle", "HypetheSonics", etc.
) {
    /**
     * Returns a display string for this entry
     * Format: "{label} by {source} on {rig}"
     */
    fun getDisplayString(): String {
        val parts = mutableListOf(label)

        if (source != "unknown") {
            parts.add("by $source")
        }

        if (rig != "unknown") {
            parts.add("on $rig")
        }

        return parts.joinToString(" ")
    }

    /**
     * Checks if this entry matches a search query
     */
    fun matchesQuery(query: String): Boolean {
        val lowerQuery = query.lowercase()
        return label.lowercase().contains(lowerQuery) ||
               source.lowercase().contains(lowerQuery) ||
               rig.lowercase().contains(lowerQuery) ||
               form.lowercase().contains(lowerQuery)
    }
}
