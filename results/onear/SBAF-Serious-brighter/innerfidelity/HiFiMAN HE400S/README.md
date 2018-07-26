# HiFiMAN HE400S
### EqualizerAPO GraphicEQ
If you are using [HeSuVi](https://sourceforge.net/projects/hesuvi/), replace contents of HeSuVi's eq file `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` with this line and set global volume for both channels from HeSuVi UI to **-60**.
```
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.6; 52 5.4; 56 5.1; 59 4.9; 64 4.4; 68 4.1; 73 3.8; 78 3.5; 83 3.3; 89 2.8; 95 2.4; 102 2.1; 109 1.7; 117 1.2; 125 0.8; 134 0.5; 143 0.3; 153 0.2; 164 0.1; 175 0.1; 188 0.1; 201 0.1; 215 0.2; 230 0.3; 246 0.4; 263 0.3; 282 0.3; 301 0.2; 323 0.1; 345 -0.0; 369 0.0; 395 -0.2; 423 0.3; 452 0.5; 484 0.9; 518 1.2; 554 1.1; 593 1.1; 635 1.0; 679 1.0; 726 0.8; 777 0.6; 832 0.3; 890 0.1; 952 -0.1; 1019 -0.1; 1090 -0.1; 1167 0.7; 1248 0.5; 1336 0.1; 1429 -0.1; 1529 0.1; 1636 0.3; 1751 0.7; 1873 1.3; 2004 1.7; 2145 1.7; 2295 2.4; 2455 2.7; 2627 3.0; 2811 2.4; 3008 2.3; 3219 2.5; 3444 2.6; 3685 2.6; 3943 2.4; 4219 0.7; 4514 -0.1; 4830 2.1; 5168 5.4; 5530 6.0; 5917 4.2; 6331 1.9; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```
If you are not using HeSuVi, copy this to the end of EqualizerAPO configuration file `C:\Program Files\EqualizerAPO\config\config.txt`.
```
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.6; 52 5.4; 56 5.1; 59 4.9; 64 4.4; 68 4.1; 73 3.8; 78 3.5; 83 3.3; 89 2.8; 95 2.4; 102 2.1; 109 1.7; 117 1.2; 125 0.8; 134 0.5; 143 0.3; 153 0.2; 164 0.1; 175 0.1; 188 0.1; 201 0.1; 215 0.2; 230 0.3; 246 0.4; 263 0.3; 282 0.3; 301 0.2; 323 0.1; 345 -0.0; 369 0.0; 395 -0.2; 423 0.3; 452 0.5; 484 0.9; 518 1.2; 554 1.1; 593 1.1; 635 1.0; 679 1.0; 726 0.8; 777 0.6; 832 0.3; 890 0.1; 952 -0.1; 1019 -0.1; 1090 -0.1; 1167 0.7; 1248 0.5; 1336 0.1; 1429 -0.1; 1529 0.1; 1636 0.3; 1751 0.7; 1873 1.3; 2004 1.7; 2145 1.7; 2295 2.4; 2455 2.7; 2627 3.0; 2811 2.4; 3008 2.3; 3219 2.5; 3444 2.6; 3685 2.6; 3943 2.4; 4219 0.7; 4514 -0.1; 4830 2.1; 5168 5.4; 5530 6.0; 5917 4.2; 6331 1.9; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
Copy: L=-6.0dB*l, R=-6.0dB*R
```
EqualizerAPO Peace GUI does not work with GraphicEQ so you have to disable parametric equalization configured by Peace if you are already using it.
![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/onear/SBAF-Serious-brighter/innerfidelity/HiFiMAN%20HE400S/HiFiMAN%20HE400S.png)

# Run 2018-07-26T11:40:17.908130
There results were obtained with parameters:
* `--input_dir="innerfidelity\data\onear\HiFiMAN HE400S"`
* `--output_dir="results\onear\SBAF-Serious-brighter\innerfidelity\HiFiMAN HE400S"`
* `--compensation="innerfidelity\resources\innerfidelity_compensation_SBAF-Serious-brighter.csv"`
* `--bass_boost=4.0`
* `--tilt=0.0`
* `--max_gain=6.0`
* `--treble_f_lower=6000.0`
* `--treble_f_upper=8000.0`
* `--treble_max_gain=0.0`
* `--treble_gain_k=1.0`