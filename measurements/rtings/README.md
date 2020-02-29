# Rtings
This is a process for getting new Rtings measurements and updating pre-computed results

1. Run Rtings pipeline: `python rtings/rtings_crawler.py`
2. Run results update: `python results/update.py --new_only --rtings`
3. Update indexes: `python results/update_indexes.py`
4. Add files to git: `git add results/rtings results/README.md results/INDEX.md rtings/links.json rtings/data rtings/name_index.tsv`
5. Commit: `git commit -m "New Rtings measurements with pre-computed results."`
6. Push: `git push`
