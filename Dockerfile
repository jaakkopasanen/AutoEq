FROM python:3.8-bullseye
COPY . .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install libsndfile1 -y
CMD python autoeq.py --input_dir="measurements/oratory1990/data/onear" --output_dir="my_results/oratory1990/harman_over-ear_2018" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=4.0 --convolution_eq --fs=44100,48000
