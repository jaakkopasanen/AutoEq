# AKG K812

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 1.0; 22 0.6; 23 0.5; 25 0.2; 26 0.1; 28 -0.1; 30 -0.3; 32 -0.4; 35 -0.6; 37 -0.7; 40 -0.9; 42 -1.0; 45 -1.1; 49 -1.2; 52 -1.3; 56 -1.4; 59 -1.5; 64 -1.7; 68 -1.9; 73 -2.0; 78 -2.2; 83 -2.5; 89 -2.8; 95 -3.1; 102 -3.3; 109 -3.5; 117 -3.6; 125 -4.0; 134 -4.1; 143 -4.2; 153 -4.4; 164 -4.3; 175 -4.3; 188 -4.4; 201 -4.5; 215 -4.5; 230 -4.4; 246 -4.3; 263 -4.3; 282 -4.1; 301 -4.1; 323 -4.0; 345 -3.9; 369 -3.8; 395 -3.7; 423 -3.4; 452 -3.2; 484 -3.1; 518 -2.9; 554 -2.6; 593 -2.2; 635 -2.0; 679 -1.8; 726 -1.5; 777 -1.0; 832 -0.6; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.7; 1336 0.6; 1429 0.0; 1529 -0.3; 1636 -0.4; 1751 0.3; 1873 0.9; 2004 0.9; 2145 0.7; 2295 0.6; 2455 2.4; 2627 3.2; 2811 0.4; 3008 -1.6; 3219 -2.5; 3444 -2.7; 3685 -2.2; 3943 -0.4; 4219 1.7; 4514 1.9; 4830 -0.5; 5168 -3.7; 5530 -6.4; 5917 -8.8; 6331 -6.3; 6775 -1.0; 7249 -1.2; 7756 -2.1; 8299 -3.3; 8880 -3.8; 9502 -2.9; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -1.1; 18692 -3.2; 20000 -7.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.4663134167153324dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 219 Hz   | 0.39 | -4.6 dB |
| Peaking | 1546 Hz  | 1.3  | 3.2 dB  |
| Peaking | 1567 Hz  | 3.53 | -3.2 dB |
| Peaking | 5931 Hz  | 4.92 | -9.2 dB |
| Peaking | 19924 Hz | 2.15 | -7.3 dB |
| Peaking | 14 Hz    | 1.42 | 1.3 dB  |
| Peaking | 2599 Hz  | 7.59 | 4.1 dB  |
| Peaking | 3344 Hz  | 2.54 | -3.4 dB |
| Peaking | 4357 Hz  | 5.91 | 4.2 dB  |
| Peaking | 8860 Hz  | 5.88 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812/AKG%20K812.png)