# AKG K3003

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.8; 23 -3.8; 25 -3.9; 26 -3.9; 28 -3.9; 30 -3.9; 32 -3.9; 35 -3.8; 37 -3.8; 40 -3.9; 42 -3.9; 45 -4.1; 49 -4.3; 52 -4.4; 56 -4.4; 59 -4.5; 64 -4.7; 68 -4.9; 73 -5.1; 78 -5.4; 83 -5.6; 89 -5.8; 95 -6.0; 102 -6.2; 109 -6.4; 117 -6.5; 125 -6.7; 134 -6.8; 143 -6.9; 153 -6.9; 164 -6.9; 175 -6.9; 188 -6.9; 201 -6.8; 215 -6.6; 230 -6.5; 246 -6.3; 263 -6.1; 282 -5.9; 301 -5.6; 323 -5.2; 345 -4.8; 369 -4.4; 395 -4.1; 423 -3.8; 452 -3.4; 484 -3.1; 518 -2.7; 554 -2.3; 593 -1.9; 635 -1.5; 679 -1.2; 726 -0.8; 777 -0.4; 832 -0.2; 890 -0.0; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.0; 1248 0.2; 1336 0.4; 1429 0.6; 1529 1.0; 1636 1.4; 1751 1.8; 1873 2.2; 2004 2.7; 2145 3.3; 2295 4.1; 2455 5.1; 2627 5.9; 2811 6.0; 3008 5.6; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.1; 4830 1.5; 5168 0.3; 5530 -0.3; 5917 -0.9; 6331 0.1; 6775 0.5; 7249 -1.3; 7756 -1.9; 8299 -1.4; 8880 -0.6; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.3; 13327 -6.6; 14260 -15.5; 15258 -20.3; 16326 -18.5; 17469 -12.7; 18692 -6.6; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999964643dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.16 | -3.5 dB  |
| Peaking | 133 Hz   | 0.75 | -3.4 dB  |
| Peaking | 277 Hz   | 0.76 | -3.9 dB  |
| Peaking | 3176 Hz  | 1.22 | 6.9 dB   |
| Peaking | 15837 Hz | 2.3  | -22.7 dB |
| Peaking | 4369 Hz  | 5.38 | 4.1 dB   |
| Peaking | 5080 Hz  | 2.49 | -3.0 dB  |
| Peaking | 7774 Hz  | 6.29 | -1.8 dB  |
| Peaking | 12409 Hz | 2.12 | 6.9 dB   |
| Peaking | 14316 Hz | 3.76 | -8.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/AKG%20K3003/AKG%20K3003.png)