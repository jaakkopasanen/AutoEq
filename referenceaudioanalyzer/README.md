# Rtings
This is a process for getting new Reference Audio Analyzer measurements and updating pre-computed results

1. Copy-paste contents of `referenceaudioanalyzer/crawl.js` into Chrome (of Firefox) developer console on page:
https://reference-audio-analyzer.pro/en/catalog-reports.php?sp_1=1&tp=1
2. Copy-paste results to a file called `referenceaudioanalyzer/links_new.json` and optionally reformat the file with some JSON prettifier
3. Run downloader: `python downloader.py --json_path=referenceaudioanalyzer/links_new.json --old_json=referenceaudioanalyzer/links.json --output_dir=referenceaudioanalyzer/images --file_type=png`
4. Copy-paste contents of `referenceaudioanalyzer/links_new.json` to `referenceaudioanalyzer/links.json`
5. Remove file `referenceaudioanalyzer/links_new.json`
6. Run Rtings pipeline: `python referenceaudioanalyzer/rtings_pipeline.py`
7. Manually move new headphone folders from `referenceaudioanalyzer/new_data` into `referenceaudioanalyzer/onear`,
`referenceaudioanalyzer/near` or `referenceaudioanalyzer/earbud`
folders in `rtings/data` depending on the heaphone type
8. Run results update: `python results/update.py --new_only --referenceaudioanalyzer`
9. Update recommendations: `python results/recommendations.py`
10. Update full index: `python results/index.py`
11. Add files to git: `git add results/referenceaudioanalyzer results/README.md results/INDEX.md referenceaudioanalyzer/links.json referenceaudioanalyzer/data`
12. Commit: `git commit -m "New Reference Audio Analyzer measurements with pre-computed results."`
12. Push: `git push`
