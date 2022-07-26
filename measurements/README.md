# Measurements
This folder contains all measurements in AutoEQ and tools to crawl them from the supported databases.

## Installing Dependencies
Additional Python packages are required for processing the measurements:
```bash
python -m pip install -U -r measurements/dev-requirements.txt
```

Measurement crawlers require [Google Chrome](https://www.google.com/chrome/) installed and
[ChromeDriver](https://sites.google.com/chromium.org/driver/) binary in the measurements folder (or anywhere
in the PATH).

Measurement crawlers also require C++. This should be installed by default on Linux but on Windows you need to install
Microsoft Visual Studio build tools for this. https://visualstudio.microsoft.com/downloads/ ->
"Tools for Visual Studio 2019" -> "Build Tools for Visual Studio 2019".

oratory1990 crawler requires Ghostscript installed: https://www.ghostscript.com/download/gsdnld.html

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
Sometimes the Zip files don't contain all of the measurement files. This is a bug in Google Drive.

Crawler Jupyter Notebook requires IPyWidgets and the extension
```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```

Finally install IPython kernel
```bash
python -m ipykernel install --user --name="autoeq"
```

## Crawling Measurement Data
Crawlers are intended to be ran in a Jupyter Notebook (or Lab). The notebook has graphical user interface for prompting
the headphone names and forms from the user. Run
```bash
jupyter lab measurements/crawl.ipynb
```
Make sure to select the IPython kernel you just installed. Run (Shift+Enter) the first two code blocks to import
dependencies and then run the crawler blocks which you need.

**Alternatively** you can run the individual crawlers but this will only process the measurements which have already
been added to the respective name index. This would be most useful for processing the raw measurement data after you've
become Crinacle's patreon.
```bash
python -m measurements.crinacle.crinacle_crawler
python -m measurements.oratory1990.oratory1990_crawler
python -m measurements.referenceaudioanalyzer.reference_audio_analyzer_crawler
python -m measurements.rtings.rtings_crawler
```
If you just downloaded the Crinacle's raw data and run the crawler like this, you need to create averaged measurements
too.
```bash
python -m measurements.average --input_dir="measurements/crinacle/data/onear/GRAS 43AG-7"
python -m measurements.average --input_dir="measurements/crinacle/data/onear/Ears-711"
python -m measurements.average --input_dir="measurements/crinacle/data/inear"
```

## Updating Measurements and Results
1. Remove measurements that have updates
2. Check obsolete results: `python results/prune_results.py --dry-run --crinacle --oratory1990 --referenceaudioanalyzer --rtings`
3. Prune results: `python results/prune_results.py --crinacle --oratory1990 --referenceaudioanalyzer --rtings`
4. Crawl new measurements: `jupyter lab measurements/crawl.ipynb`
5. Run results update: `python results/update_results.py --new_only`
6. Update result indexes: `python results/update_indexes.py`
7. Add files to git: `git add results measurements/*/data/**/*.csv measurements/*/name_index.tsv`
8. Commit: `git commit -m "New measurements with pre-computed results."`
9. Push: `git push`
