# crinacle
This is a process for getting new crinacle measurements and updating pre-computed results

1. Download new files or the full folder from crinacle's Google Drive and save to `crinacle/raw_data`.
2. Download phone book: `python crinacle/download_phone_book.py`
3. Generate new instances of name index: `python crinacle/names.py`
4. Add new models to name index `names_index.tsv`
5. Run crinacle pipeline: `python crinacle/pipeline.py`
6. Run averaging script: `python average.py --input_dir="crinacle/data/inear" --output_dir="crinacle/data/inear"`
7. Run results update: `python results/update.py --new_only --crinacle`
8. Update indexes: `python results/update_indexes.py`
9. Add files to git: `git add results/crinacle results/README.md results/INDEX.md`
10. Commit: `git commit -m "New crinacle pre-computed results."`
11. Push: `git push`
