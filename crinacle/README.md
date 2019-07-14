# crinacle
This is a process for getting new crinacle measurements and updating pre-computed results

1. Download new files or the full folder from crinacle's Google Drive and save to `crinacle/raw_data`.
2. Add new models to name index `names_index.tsv`
3. Run crinacle pipeline: `python crinacle/pipeline.py`
4. Run averaging script: `python average.py --input_dir="crinacle/data/inear" --output_dir="crinacle/data/inear"`
5. Run results update: `python results/update.py --new_only --crinacle`
6. Update recommendations: `python results/recommendations.py`
7. Update full index: `python results/index.py`
8. Add files to git: `git add results/crinacle results/README.md results/INDEX.md`
9. Commit: `git commit -m "New crinacle pre-computed results."`
10. Push: `git push`
