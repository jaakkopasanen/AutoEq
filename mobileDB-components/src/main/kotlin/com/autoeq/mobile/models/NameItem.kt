package com.autoeq.mobile.models

/**
 * Represents a single entry in the name index with headphone information.
 * Corresponds to Python's NameItem class from name_index.py
 */
data class NameItem(
    val name: String,
    val form: String = "unknown",
    val rig: String = "unknown",
    val manufacturer: String? = null,
    val trueModel: String? = null,
    val falseName: String? = null
) {
    /**
     * Creates a copy with updated fields, merging non-null values
     */
    fun merge(other: NameItem): NameItem {
        return NameItem(
            name = other.name,
            form = if (other.form != "unknown") other.form else this.form,
            rig = if (other.rig != "unknown") other.rig else this.rig,
            manufacturer = other.manufacturer ?: this.manufacturer,
            trueModel = other.trueModel ?: this.trueModel,
            falseName = other.falseName ?: this.falseName
        )
    }

    companion object {
        /**
         * Parse a TSV line into a NameItem
         */
        fun fromTsvLine(line: String): NameItem? {
            val parts = line.split("\t")
            if (parts.isEmpty()) return null

            return NameItem(
                name = parts.getOrNull(0)?.takeIf { it.isNotBlank() } ?: return null,
                form = parts.getOrNull(1)?.takeIf { it.isNotBlank() } ?: "unknown",
                rig = parts.getOrNull(2)?.takeIf { it.isNotBlank() } ?: "unknown",
                manufacturer = parts.getOrNull(3)?.takeIf { it.isNotBlank() },
                trueModel = parts.getOrNull(4)?.takeIf { it.isNotBlank() },
                falseName = parts.getOrNull(5)?.takeIf { it.isNotBlank() }
            )
        }
    }
}
