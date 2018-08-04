# V-Moda M-80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.1; 22 2.6; 23 2.4; 25 2.0; 26 1.8; 28 1.5; 30 1.2; 32 1.0; 35 0.7; 37 0.6; 40 0.3; 42 0.2; 45 0.0; 49 -0.1; 52 -0.3; 56 -0.4; 59 -0.5; 64 -0.7; 68 -0.8; 73 -1.0; 78 -1.1; 83 -1.2; 89 -1.4; 95 -1.9; 102 -2.3; 109 -2.4; 117 -2.5; 125 -2.7; 134 -3.0; 143 -3.2; 153 -3.4; 164 -3.3; 175 -3.1; 188 -3.0; 201 -2.7; 215 -3.2; 230 -4.5; 246 -4.2; 263 -3.6; 282 -3.0; 301 -2.4; 323 -1.7; 345 -0.9; 369 -0.3; 395 0.0; 423 0.4; 452 0.7; 484 1.1; 518 1.6; 554 2.4; 593 3.0; 635 3.2; 679 3.0; 726 2.7; 777 2.5; 832 1.9; 890 1.3; 952 0.6; 1019 -0.2; 1090 -0.8; 1167 -1.4; 1248 -2.0; 1336 -2.3; 1429 -2.5; 1529 -2.6; 1636 -2.4; 1751 -1.9; 1873 -1.1; 2004 -0.3; 2145 0.3; 2295 0.5; 2455 0.7; 2627 0.4; 2811 -0.4; 3008 -1.0; 3219 -1.7; 3444 -1.5; 3685 -0.1; 3943 1.6; 4219 2.5; 4514 1.4; 4830 2.2; 5168 5.7; 5530 6.0; 5917 5.8; 6331 3.5; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.23 | 3.0 dB  |
| Peaking | 143 Hz  | 0.93 | -3.0 dB |
| Peaking | 250 Hz  | 3.07 | -3.1 dB |
| Peaking | 632 Hz  | 2.64 | 3.8 dB  |
| Peaking | 5595 Hz | 3.85 | 6.7 dB  |
| Peaking | 837 Hz  | 3.34 | 1.6 dB  |
| Peaking | 1501 Hz | 1.56 | -3.3 dB |
| Peaking | 4048 Hz | 6.97 | 2.3 dB  |
| Peaking | 3289 Hz | 3.17 | -2.6 dB |
| Peaking | 2336 Hz | 2.03 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20M-80/V-Moda%20M-80.png)