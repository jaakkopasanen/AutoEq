package com.autoeq.mobile.search

import com.autoeq.mobile.models.Entry
import com.autoeq.mobile.models.MeasurementData

/**
 * Search engine for AutoEq measurements.
 * Provides fuzzy search functionality matching the webapp's search bar behavior.
 */
class MeasurementSearch(
    private val entries: List<Entry>
) {
    /**
     * Search for measurements matching the query
     * Returns entries sorted by relevance
     */
    fun search(query: String, maxResults: Int = 50): List<Entry> {
        if (query.isBlank()) {
            return emptyList()
        }

        val lowerQuery = query.lowercase().trim()

        // Score each entry based on match quality
        val scoredEntries = entries.mapNotNull { entry ->
            val score = calculateRelevanceScore(entry, lowerQuery)
            if (score > 0) {
                ScoredEntry(entry, score)
            } else {
                null
            }
        }

        // Sort by score (descending) and take top results
        return scoredEntries
            .sortedByDescending { it.score }
            .take(maxResults)
            .map { it.entry }
    }

    /**
     * Calculate relevance score for an entry
     * Higher score = better match
     */
    private fun calculateRelevanceScore(entry: Entry, query: String): Int {
        var score = 0
        val lowerLabel = entry.label.lowercase()
        val lowerSource = entry.source.lowercase()
        val lowerRig = entry.rig.lowercase()
        val lowerForm = entry.form.lowercase()

        // Exact match (highest priority)
        if (lowerLabel == query) {
            score += 1000
        }

        // Starts with query (high priority)
        if (lowerLabel.startsWith(query)) {
            score += 500
        }

        // Contains query (medium priority)
        if (lowerLabel.contains(query)) {
            score += 100
        }

        // Match in source
        if (lowerSource.contains(query)) {
            score += 50
        }

        // Match in rig
        if (lowerRig.contains(query)) {
            score += 30
        }

        // Match in form
        if (lowerForm.contains(query)) {
            score += 20
        }

        // Word boundary matches (boost score if query matches a word boundary)
        val words = lowerLabel.split(Regex("\\s+|[-_]"))
        if (words.any { it.startsWith(query) }) {
            score += 200
        }

        return score
    }

    /**
     * Filter entries by source
     */
    fun filterBySource(source: String): List<Entry> {
        return entries.filter { it.source.equals(source, ignoreCase = true) }
    }

    /**
     * Filter entries by rig
     */
    fun filterByRig(rig: String): List<Entry> {
        return entries.filter { it.rig.equals(rig, ignoreCase = true) }
    }

    /**
     * Filter entries by form
     */
    fun filterByForm(form: String): List<Entry> {
        return entries.filter { it.form.equals(form, ignoreCase = true) }
    }

    /**
     * Get all unique sources
     */
    fun getAllSources(): List<String> {
        return entries.map { it.source }.distinct().sorted()
    }

    /**
     * Get all unique rigs
     */
    fun getAllRigs(): List<String> {
        return entries.map { it.rig }.distinct().sorted()
    }

    /**
     * Get all unique forms
     */
    fun getAllForms(): List<String> {
        return entries.map { it.form }.distinct().sorted()
    }

    /**
     * Get suggestions for autocomplete (returns headphone names that start with query)
     */
    fun getSuggestions(query: String, maxSuggestions: Int = 10): List<String> {
        if (query.isBlank()) {
            return emptyList()
        }

        val lowerQuery = query.lowercase()

        return entries
            .map { it.label }
            .distinct()
            .filter { it.lowercase().startsWith(lowerQuery) }
            .sorted()
            .take(maxSuggestions)
    }

    private data class ScoredEntry(val entry: Entry, val score: Int)
}

/**
 * Search result item that combines entry with additional context
 */
data class SearchResult(
    val entry: Entry,
    val resultPath: String,          // Path to the result folder
    val hasParametricEQ: Boolean,    // Whether parametric EQ file exists
    val hasFixedBandEQ: Boolean,     // Whether fixed band EQ file exists
    val hasGraphicEQ: Boolean        // Whether graphic EQ file exists
) {
    /**
     * Get display text for this search result
     * Format: "Headphone Name by Source on Rig"
     */
    fun getDisplayText(): String = entry.getDisplayString()

    /**
     * Get primary display text (just the headphone name)
     */
    fun getPrimaryText(): String = entry.label

    /**
     * Get secondary display text (source and rig info)
     */
    fun getSecondaryText(): String {
        val parts = mutableListOf<String>()

        if (entry.source != "unknown") {
            parts.add("by ${entry.source}")
        }

        if (entry.rig != "unknown") {
            parts.add("on ${entry.rig}")
        }

        return parts.joinToString(" ")
    }
}
