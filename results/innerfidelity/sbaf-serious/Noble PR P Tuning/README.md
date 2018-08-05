# Noble PR P Tuning

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 3.7; 22 3.6; 23 3.6; 25 3.5; 26 3.4; 28 3.3; 30 3.3; 32 3.2; 35 3.1; 37 3.0; 40 3.0; 42 3.0; 45 2.9; 49 2.8; 52 2.7; 56 2.7; 59 2.7; 64 2.6; 68 2.5; 73 2.3; 78 2.1; 83 1.9; 89 1.5; 95 1.0; 102 0.4; 109 -0.1; 117 -0.6; 125 -1.3; 134 -1.8; 143 -2.0; 153 -2.3; 164 -2.5; 175 -2.6; 188 -2.6; 201 -2.6; 215 -2.5; 230 -2.5; 246 -2.4; 263 -2.3; 282 -2.2; 301 -2.1; 323 -2.0; 345 -1.9; 369 -1.7; 395 -1.6; 423 -1.3; 452 -1.1; 484 -1.0; 518 -0.9; 554 -0.5; 593 -0.1; 635 0.0; 679 0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.2; 952 0.0; 1019 -0.1; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.0; 1529 -1.3; 1636 -1.5; 1751 -1.5; 1873 -1.3; 2004 -1.2; 2145 -1.1; 2295 -1.1; 2455 -0.7; 2627 -0.2; 2811 0.7; 3008 2.5; 3219 3.9; 3444 4.8; 3685 4.4; 3943 2.5; 4219 -0.8; 4514 -3.3; 4830 -5.1; 5168 -6.6; 5530 -8.3; 5917 -8.5; 6331 -7.4; 6775 -6.4; 7249 -6.1; 7756 -6.8; 8299 -7.6; 8880 -6.5; 9502 -3.3; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.6; 17469 -0.3; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR P Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.23 | 3.8 dB  |
| Peaking | 61 Hz    | 2.63 | 2.5 dB  |
| Peaking | 3575 Hz  | 3.66 | 7.8 dB  |
| Peaking | 5684 Hz  | 1.74 | -8.7 dB |
| Peaking | 8379 Hz  | 4.74 | -5.6 dB |
| Peaking | 22 Hz    | 0.26 | 0.3 dB  |
| Peaking | 87 Hz    | 2.49 | 1.7 dB  |
| Peaking | 195 Hz   | 0.77 | -3.0 dB |
| Peaking | 1808 Hz  | 2.64 | -1.5 dB |
| Peaking | 10909 Hz | 4.43 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20P%20Tuning/Noble%20PR%20P%20Tuning.png)