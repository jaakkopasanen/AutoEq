# Rtings
This is a process for getting new Rtings measurements and updating pre-computed results

1. Copy-paste contents of `rtings/crawl.js` into Chrome (of Firefox) developer console on page:
https://www.rtings.com/headphones/1-2/graph
2. Copy-paste results to a file called `rtings/links_new.json` and optionally reformat the file with some JSON prettifier
3. Run downloader:
`python downloader.py --json_path=rtings/links_new.json --old_json=rtings/links.json --output_dir=rtings/raw_data --file_type=json`
4. Copy-paste contents of `rtings/links_new.json` to `rtings/links.json`
5. Remove file `rtings/links_new.json`
6. Add new headphones to name index `rtings/name_index.tsv`
7. Run Rtings pipeline: `python rtings/rtings_pipeline.py`
8. Run results update: `python results/update.py --new_only --rtings`
9. Update recommendations: `python results/recommendations.py`
10. Update full index: `python results/index.py`
11. Add files to git: `git add results/rtings results/README.md results/INDEX.md rtings/links.json rtings/data`
12. Commit: `git commit -m "New Rtings measurements with pre-computed results."`
13. Push: `git push`
