package com.autoeq.mobile.indexing

import com.autoeq.mobile.models.NameItem
import java.io.File

/**
 * Name index for looking up headphone metadata.
 * Corresponds to Python's NameIndex class from name_index.py
 */
class NameIndex {
    private val items = mutableListOf<NameItem>()
    private val nameToItemMap = mutableMapOf<String, MutableList<NameItem>>()

    /**
     * Add a NameItem to the index
     */
    fun add(item: NameItem) {
        items.add(item)
        nameToItemMap.getOrPut(item.name) { mutableListOf() }.add(item)
    }

    /**
     * Find all items matching the given name
     */
    fun find(name: String): List<NameItem> {
        return nameToItemMap[name] ?: emptyList()
    }

    /**
     * Find a single item matching the given criteria.
     * Throws exception if no match or multiple matches found.
     */
    fun findOne(
        name: String,
        form: String? = null,
        rig: String? = null
    ): NameItem {
        var matches = find(name)

        if (matches.isEmpty()) {
            throw NoSuchElementException("No NameItem found with name: $name")
        }

        // Filter by form if specified
        if (form != null) {
            matches = matches.filter { it.form == form }
            if (matches.isEmpty()) {
                throw NoSuchElementException("No NameItem found with name: $name and form: $form")
            }
        }

        // Filter by rig if specified
        if (rig != null) {
            matches = matches.filter { it.rig == rig }
            if (matches.isEmpty()) {
                throw NoSuchElementException("No NameItem found with name: $name and rig: $rig")
            }
        }

        if (matches.size > 1) {
            throw IllegalStateException("Multiple NameItems found for name: $name, form: $form, rig: $rig")
        }

        return matches.first()
    }

    /**
     * Get all items in the index
     */
    fun getAll(): List<NameItem> = items.toList()

    /**
     * Get the count of items
     */
    fun size(): Int = items.size

    /**
     * Clear all items from the index
     */
    fun clear() {
        items.clear()
        nameToItemMap.clear()
    }

    companion object {
        /**
         * Read a name index from a TSV file
         * TSV format: name\tform\trig\tmanufacturer\ttrue_model\tfalse_name
         */
        fun fromTsvFile(file: File): NameIndex {
            val index = NameIndex()

            if (!file.exists()) {
                throw IllegalArgumentException("TSV file does not exist: ${file.absolutePath}")
            }

            file.useLines { lines ->
                lines.forEachIndexed { lineNumber, line ->
                    // Skip empty lines and comments
                    if (line.isBlank() || line.trim().startsWith("#")) {
                        return@forEachIndexed
                    }

                    // Skip header line
                    if (lineNumber == 0 && line.trim().lowercase().startsWith("name")) {
                        return@forEachIndexed
                    }

                    try {
                        val item = NameItem.fromTsvLine(line)
                        if (item != null) {
                            index.add(item)
                        }
                    } catch (e: Exception) {
                        println("Warning: Failed to parse line ${lineNumber + 1}: $line")
                        println("Error: ${e.message}")
                    }
                }
            }

            return index
        }

        /**
         * Read a name index from a TSV file path string
         */
        fun fromTsvFile(filePath: String): NameIndex {
            return fromTsvFile(File(filePath))
        }
    }

    /**
     * Merge another NameIndex into this one
     */
    fun merge(other: NameIndex) {
        other.items.forEach { add(it) }
    }

    override fun toString(): String {
        return "NameIndex(items=${items.size})"
    }
}
