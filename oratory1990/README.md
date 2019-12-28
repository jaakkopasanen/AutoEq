# oratory1990
This is a process for getting new oratory1990 measurements and updating pre-computed results

1. Copy-paste contents of `oratory1990/crawl.js` into Chrome (of Firefox) developer console on page:
https://old.reddit.com/r/oratory1990/wiki/index/list_of_presets
2. Copy-paste results to a file called `oratory1990/links_new.json` and optionally reformat the file with some JSON prettifier
3. Run downloader: `python downloader.py --json_path=oratory1990/links_new.json --old_json=oratory1990/links.json --output_dir=oratory1990/pdf --file_type=pdf`
4. Copy-paste contents of `oratory1990/links_new.json` to `oratory1990/links.json`
5. Remove file `oratory1990/links_new.json`
6. Run oratory1990 PDF parser: `python oratory1990/oratory1990_pdf_parser.py`. This needs GhostScript installed!
7. Manually move new headphone folders from `oratory1990/new_data` into `oratory1990/onear`, `oratory1990/inear` or
`oratory1990/earbud` folders in `rtings/data` depending on the headphone type
8. Run results update: `python results/update.py --new_only --oratory1990`
9. Update indexes: `python results/update_indexes.py`
10. Add files to git: `git add results/oratory1990 results/README.md results/INDEX.md oratory1990/links.json oratory1990/data`
11. Commit: `git commit -m "New oratory1990 measurements with pre-computed results."`
12. Push: `git push`
