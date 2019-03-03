# Rtings
This is a process for getting new Reference Audio Analyzer measurements and updating pre-computed results

1. Copy-paste contents of `referenceaudioanalyzer/crawl.js` into Chrome (of Firefox) developer console on page:
https://reference-audio-analyzer.pro/en/catalog-reports.php?sp_1=1&tp=1 
2. Copy-paste results to a file called `referenceaudioanalyzer/links.json` and optionally reformat the file with some JSON prettifier
3. Check which are new: `python referenceaudioanalyzer/check_new.py`
4. Run downloader: `python downloader.py --json_path=referenceaudioanalyzer/links_new.json --output_dir=referenceaudioanalyzer/images --file_type=png`
5. Remove files `referenceaudioanalyzer/links.json` and `referenceaudioanalyzer/links_new.json`
6. Run pipeline: `python referenceaudioanalyzer/referenceaudioanalyzer_pipeline.py`
7. Run results update: `python results/update.py --new_only --referenceaudioanalyzer`
8. Update recommendations: `python results/recommendations.py`
9. Update full index: `python results/index.py`
10. Add files to git: `git add results/referenceaudioanalyzer results/README.md results/INDEX.md referenceaudioanalyzer/names.txt referenceaudioanalyzer/data`
11. Commit: `git commit -m "New Reference Audio Analyzer measurements with pre-computed results."`
12. Push: `git push`
