# Measurements
This folder contains all measurements in AutoEQ and tools to crawl them from the supported databases.

1. Remove measurements that have updates
2. Prune results: `python results/prune.py`
3. Run measurements update: `python measurements/update_measurements.py`
4. Run results update: `python results/update_results.py --new_only`
5. Update result indexes: `python results/update_indexes.py`
6. Add files to git: `git add results measurements/*/data measurements/*/name_index.tsv`
7. Commit: `git commit -m "New measurements with pre-computed results."`
8. Push: `git push`