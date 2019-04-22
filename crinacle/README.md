# crinacle
This is a process for getting new crinacle measurements and updating pre-computed results

1. Download new files or the full folder from crinacle's Google Drive.
2. Run crinacle pipeline: `python crinacle/pipeline.py`
3. Run results update: `python results/update.py --new_only --crinacle`
4. Update recommendations: `python results/recommendations.py`
5. Update full index: `python results/index.py`
6. Add files to git: `git add results/crinacle results/README.md results/INDEX.md`
7. Commit: `git commit -m "New crinacle pre-computed results."`
8. Push: `git push`
