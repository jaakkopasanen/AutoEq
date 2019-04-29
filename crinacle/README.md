# crinacle
This is a process for getting new crinacle measurements and updating pre-computed results

1. Download new files or the full folder from crinacle's Google Drive and save to `crinacle/raw_data`.
2. Run crinacle pipeline: `python crinacle/pipeline.py`
3. Run averaging script: `python average --input_dir="crinacle/data/inear" --output_dir="crinacle/data/inear"`
4. Run results update: `python results/update.py --new_only --crinacle`
5. Update recommendations: `python results/recommendations.py`
6. Update full index: `python results/index.py`
7. Add files to git: `git add results/crinacle results/README.md results/INDEX.md`
8. Commit: `git commit -m "New crinacle pre-computed results."`
9. Push: `git push`
