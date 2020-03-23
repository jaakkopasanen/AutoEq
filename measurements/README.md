# Measurements
This folder contains all measurements in AutoEQ and tools to crawl them from the supported databases.

Measurement crawlers require [Google Chrome](https://www.google.com/chrome/) installed and
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home) binary in the measurements folder (or anywhere
in the PATH).

Measurement crawlers also require C++. This should be installed by default on Linux and on Windows you need to install
Microsoft Visual Studio build tools for this. https://visualstudio.microsoft.com/downloads/ ->
"Tools for Visual Studio 2019" -> "Build Tools for Visual Studio 2019".

oratory1990 and Innerfidelity require Ghostscript installed: https://www.ghostscript.com/download/gsdnld.html

## Updating Measurements
1. Remove measurements that have updates
2. Prune results: `python results/prune_results.py`
3. Run measurements update: `python measurements/update_measurements.py --prompt`
4. Run results update: `python results/update_results.py --new_only`
5. Update result indexes: `python results/update_indexes.py`
6. Add files to git: `git add results measurements/*/data measurements/*/name_index.tsv`
7. Commit: `git commit -m "New measurements with pre-computed results."`
8. Push: `git push`