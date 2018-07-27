# Monoprice Monolith M1060
Replace `C:\Program Files\EqualizerAPO\config\config.txt` with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.6; 49 5.2; 52 5.1; 56 5.0; 59 5.0; 64 5.3; 68 5.6; 73 6.0; 78 6.0; 83 5.9; 89 5.2; 95 4.3; 102 3.5; 109 2.9; 117 2.3; 125 1.6; 134 1.0; 143 0.5; 153 0.2; 164 -0.1; 175 -0.4; 188 -0.5; 201 -0.8; 215 -0.9; 230 -0.9; 246 -0.9; 263 -0.8; 282 -0.4; 301 -0.5; 323 -0.6; 345 -0.3; 369 -0.0; 395 0.3; 423 0.4; 452 0.4; 484 0.3; 518 0.0; 554 -0.1; 593 -0.3; 635 -0.2; 679 -0.0; 726 0.4; 777 0.7; 832 1.0; 890 1.1; 952 0.2; 1019 0.3; 1090 0.6; 1167 0.9; 1248 1.4; 1336 2.0; 1429 1.8; 1529 1.4; 1636 1.4; 1751 2.0; 1873 2.9; 2004 3.7; 2145 4.1; 2295 4.2; 2455 3.7; 2627 3.8; 2811 4.7; 3008 5.0; 3219 4.5; 3444 4.6; 3685 3.4; 3943 2.8; 4219 5.9; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.8; 5917 3.5; 6331 2.0; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.9; 17469 -3.4; 18692 -5.2; 20000 -6.2
```
**OR** if using HeSuVi replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp: -6.1dB` and instead set Global volume in the UI for both channels to **-61**.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/Sonoma%20Model%20One/innerfidelity/onear/Monoprice%20Monolith%20M1060/Monoprice%20Monolith%20M1060.png)

# Run 2018-07-27T18:00:15.361347
There results were obtained with parameters:
* `--input_dir="innerfidelity\data\onear\Monoprice Monolith M1060"`
* `--output_dir="results\Sonoma Model One\innerfidelity\onear\Monoprice Monolith M1060"`
* `--compensation="innerfidelity\data\onear\Sonoma Model One\Sonoma Model One.csv"`
* `--bass_boost=4.0`
* `--tilt=0.0`
* `--max_gain=6.0`
* `--treble_f_lower=6000.0`
* `--treble_f_upper=8000.0`
* `--treble_max_gain=0.0`
* `--treble_gain_k=1.0`