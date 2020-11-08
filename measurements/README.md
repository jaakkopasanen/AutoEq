# Measurements
This folder contains all measurements in AutoEQ and tools to crawl them from the supported databases.

Additional Python packages are required for processing the measurements:
```bash
python -m pip install -U -r measurements/dev-requirements.txt
```

Measurement crawlers require [Google Chrome](https://www.google.com/chrome/) installed and
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home) binary in the measurements folder (or anywhere
in the PATH).

Measurement crawlers also require C++. This should be installed by default on Linux but on Windows you need to install
Microsoft Visual Studio build tools for this. https://visualstudio.microsoft.com/downloads/ ->
"Tools for Visual Studio 2019" -> "Build Tools for Visual Studio 2019".

oratory1990 and Innerfidelity require Ghostscript installed: https://www.ghostscript.com/download/gsdnld.html

Numerical data for Crinacle's measurements is not available in this repository. Crinacle has Patreon and a certain
subscription tier unlocks the raw numerical measurement data. If you are a patreon and have access to the Google Drive
containing the measurement files, you can download the data to `crinacle/raw_data` folder. Download the IEM
"IEM Measurements (TSV)", legacy headphone measurements "Legacy Data (Ears + 711)" and the new GRAS headphone
measurements "FR Data (CSV)" separately. The directory structure should be:
```
measurements
    crinacle
        raw_data
            FR Data (CSV)
                99 Classic L1.txt
                99 Classic L2.txt
                ...
            IEM Measurements (TSV)
                1 Plus 2.2 L.txt
                1 Plus 2.2 R.txt
                ...
            Legacy Data (EARS + 711)
                A990Z R1.txt
                A990Z R2.txt
                ...
```
`update_measurements.py` will then process these files and create AutoEq compatible CSV files in
`crinacle/data` organized by headphone type.

## Updating Measurements and Results
1. Remove measurements that have updates
2. Prune results: `python results/prune_results.py`
3. Crawl new measurements: `python measurements/update_measurements.py --prompt`
4. Run results update: `python results/update_results.py --new_only`
5. Update result indexes: `python results/update_indexes.py`
6. Add files to git: `git add results measurements/*/data measurements/*/name_index.tsv`
7. Commit: `git commit -m "New measurements with pre-computed results."`
8. Push: `git push`
