package com.autoeq.mobile.crawlers

import com.autoeq.mobile.indexing.NameIndex
import java.io.File

/**
 * Base interface for measurement crawlers.
 * Crawlers are used for sources that don't have a name_index.tsv file
 * and need to programmatically generate the index.
 */
interface BaseCrawler {
    /**
     * The path to the measurements directory for this source
     */
    val measurementsPath: File

    /**
     * The name of this source (e.g., "Headphone.com Legacy", "Innerfidelity")
     */
    val sourceName: String

    /**
     * Read and generate the name index for this source
     */
    fun readNameIndex(): NameIndex

    /**
     * Get the cached name index (reads if not already cached)
     */
    fun getNameIndex(): NameIndex
}

/**
 * Abstract base implementation with caching
 */
abstract class AbstractCrawler(
    override val measurementsPath: File,
    override val sourceName: String
) : BaseCrawler {
    protected var cachedNameIndex: NameIndex? = null

    override fun getNameIndex(): NameIndex {
        if (cachedNameIndex == null) {
            cachedNameIndex = readNameIndex()
        }
        return cachedNameIndex!!
    }

    /**
     * Clear the cached name index
     */
    fun clearCache() {
        cachedNameIndex = null
    }
}
