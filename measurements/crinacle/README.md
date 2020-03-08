# crinacle
This is a process for getting new crinacle measurements and updating pre-computed results

1. Download new files or the full folder from crinacle's Google Drive and save to `crinacle/raw_data`.
2. Run Crawler: `python measurements/crinacle/crinacle_crawler.py`
3. Run results update: `python results/update.py --new_only --crinacle`
4. Update indexes: `python results/update_indexes.py`
5. Add files to git: `git add results/crinacle results/README.md results/INDEX.md`
6. Commit: `git commit -m "New crinacle pre-computed results."`
7. Push: `git push`
