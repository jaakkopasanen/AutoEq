# AKG K240 Sextett

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.5; 37 5.0; 40 4.1; 42 3.5; 45 2.7; 49 1.8; 52 1.3; 56 0.7; 59 0.7; 64 1.1; 68 1.0; 73 -0.4; 78 -2.3; 83 -3.6; 89 -4.6; 95 -5.3; 102 -5.9; 109 -6.3; 117 -6.7; 125 -6.9; 134 -6.8; 143 -6.9; 153 -6.6; 164 -5.7; 175 -4.7; 188 -5.2; 201 -5.7; 215 -5.5; 230 -5.1; 246 -4.9; 263 -4.5; 282 -4.2; 301 -3.9; 323 -3.6; 345 -3.1; 369 -2.8; 395 -2.7; 423 -2.4; 452 -2.0; 484 -1.5; 518 -1.8; 554 -2.0; 593 -1.8; 635 -1.5; 679 -1.3; 726 -1.1; 777 -0.7; 832 -0.4; 890 -0.2; 952 0.0; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.3; 1636 -2.8; 1751 -3.2; 1873 -3.4; 2004 -3.7; 2145 -3.7; 2295 -2.6; 2455 -2.5; 2627 -1.1; 2811 1.5; 3008 3.3; 3219 2.1; 3444 2.4; 3685 0.8; 3943 -1.1; 4219 -5.2; 4514 -7.2; 4830 -4.2; 5168 -0.2; 5530 1.6; 5917 1.9; 6331 0.6; 6775 -2.0; 7249 -4.1; 7756 -6.2; 8299 -8.6; 8880 -10.2; 9502 -9.8; 10167 -6.6; 10879 -2.0; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Sextett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.6  | 6.5 dB   |
| Peaking | 114 Hz   | 1.27 | -6.1 dB  |
| Peaking | 232 Hz   | 0.75 | -4.0 dB  |
| Peaking | 1918 Hz  | 3.01 | -3.9 dB  |
| Peaking | 8956 Hz  | 3.31 | -11.4 dB |
| Peaking | 2497 Hz  | 3.38 | -3.4 dB  |
| Peaking | 3072 Hz  | 2.35 | 5.3 dB   |
| Peaking | 4485 Hz  | 4.84 | -8.3 dB  |
| Peaking | 5676 Hz  | 5.12 | 4.3 dB   |
| Peaking | 11732 Hz | 6.17 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Sextett/AKG%20K240%20Sextett.png)