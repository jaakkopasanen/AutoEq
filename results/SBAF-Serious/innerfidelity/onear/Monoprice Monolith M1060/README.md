# Monoprice Monolith M1060
Replace `C:\Program Files\EqualizerAPO\config\config.txt` with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 4.3; 22 4.3; 23 4.3; 25 4.3; 26 4.3; 28 4.4; 30 4.4; 32 4.5; 35 4.5; 37 4.4; 40 4.2; 42 3.9; 45 3.5; 49 3.3; 52 3.3; 56 3.3; 59 3.3; 64 3.3; 68 3.3; 73 3.3; 78 3.2; 83 3.0; 89 2.6; 95 2.3; 102 1.9; 109 1.6; 117 1.3; 125 0.9; 134 0.5; 143 0.3; 153 0.1; 164 0.0; 175 -0.2; 188 -0.3; 201 -0.5; 215 -0.5; 230 -0.4; 246 -0.4; 263 -0.2; 282 0.2; 301 0.1; 323 -0.1; 345 0.2; 369 0.5; 395 0.8; 423 0.9; 452 0.7; 484 0.4; 518 0.1; 554 0.2; 593 -0.1; 635 -0.3; 679 -0.6; 726 -0.5; 777 -0.3; 832 0.2; 890 0.6; 952 0.1; 1019 0.2; 1090 0.1; 1167 -0.3; 1248 -0.5; 1336 -0.5; 1429 -1.1; 1529 -1.6; 1636 -1.2; 1751 0.2; 1873 1.7; 2004 2.7; 2145 3.1; 2295 3.3; 2455 2.7; 2627 2.7; 2811 3.4; 3008 3.7; 3219 3.3; 3444 3.7; 3685 3.0; 3943 2.8; 4219 5.9; 4514 5.9; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 4.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -2.8; 20000 -7.5
```
**OR** if using HeSuVi replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp: -6.0dB` and instead set Global volume in the UI for both channels to **-60**.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/SBAF-Serious/innerfidelity/onear/Monoprice%20Monolith%20M1060/Monoprice%20Monolith%20M1060.png)

# Run 2018-07-27T17:58:28.320106
There results were obtained with parameters:
* `--input_dir="innerfidelity\data\onear\Monoprice Monolith M1060"`
* `--output_dir="results\SBAF-Serious\innerfidelity\onear\Monoprice Monolith M1060"`
* `--compensation="innerfidelity\resources\innerfidelity_compensation_SBAF-Serious-brighter.csv"`
* `--bass_boost=4.0`
* `--tilt=0.0`
* `--max_gain=6.0`
* `--treble_f_lower=6000.0`
* `--treble_f_upper=8000.0`
* `--treble_max_gain=0.0`
* `--treble_gain_k=1.0`