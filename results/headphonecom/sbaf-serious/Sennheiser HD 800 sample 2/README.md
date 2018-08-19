# Sennheiser HD 800 sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 10 -84; 20 2.3; 22 2.0; 23 1.8; 25 1.5; 26 1.3; 28 1.1; 30 0.9; 32 0.7; 35 0.4; 37 0.3; 40 0.1; 42 0.0; 45 -0.0; 49 0.2; 52 0.5; 56 0.1; 59 -0.4; 64 -0.2; 68 -0.1; 73 -1.0; 78 -1.7; 83 -2.1; 89 -2.4; 95 -2.7; 102 -2.9; 109 -3.2; 117 -3.3; 125 -3.5; 134 -3.7; 143 -3.8; 153 -4.0; 164 -3.9; 175 -4.1; 188 -4.2; 201 -4.2; 215 -4.2; 230 -4.2; 246 -4.2; 263 -4.1; 282 -4.1; 301 -4.0; 323 -3.6; 345 -3.5; 369 -3.4; 395 -3.3; 423 -3.0; 452 -2.9; 484 -2.8; 518 -2.5; 554 -2.4; 593 -2.2; 635 -1.9; 679 -1.7; 726 -1.4; 777 -1.2; 832 -1.1; 890 -0.8; 952 -0.1; 1019 0.1; 1090 0.6; 1167 1.3; 1248 1.2; 1336 1.2; 1429 0.8; 1529 0.6; 1636 1.0; 1751 1.2; 1873 1.0; 2004 1.3; 2145 0.9; 2295 0.4; 2455 1.5; 2627 2.1; 2811 1.1; 3008 -0.1; 3219 0.1; 3444 0.8; 3685 -0.6; 3943 -2.8; 4219 -3.3; 4514 -3.1; 4830 -3.2; 5168 -4.1; 5530 -4.9; 5917 -7.9; 6331 -9.8; 6775 -5.8; 7249 -4.2; 7756 -4.5; 8299 -6.0; 8880 -8.2; 9502 -9.4; 10167 -6.7; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 -0.2; 14260 -2.9; 15258 -3.7; 16326 -3.6; 17469 -4.4; 18692 -5.3; 20000 -5.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.417885359608485dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.22 | 2.0 dB  |
| Peaking | 201 Hz   | 0.35 | -4.7 dB |
| Peaking | 2533 Hz  | 0.49 | 2.9 dB  |
| Peaking | 6640 Hz  | 0.88 | -8.2 dB |
| Peaking | 19099 Hz | 1.2  | -5.8 dB |
| Peaking | 6248 Hz  | 9.32 | -5.5 dB |
| Peaking | 7286 Hz  | 2.84 | 4.0 dB  |
| Peaking | 9598 Hz  | 3.21 | -9.3 dB |
| Peaking | 11218 Hz | 1.82 | 6.2 dB  |
| Peaking | 15089 Hz | 3.04 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20sample%202/Sennheiser%20HD%20800%20sample%202.png)