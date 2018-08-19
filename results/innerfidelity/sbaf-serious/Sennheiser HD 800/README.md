# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 3.6; 22 3.2; 23 3.1; 25 2.8; 26 2.6; 28 2.4; 30 2.2; 32 2.0; 35 1.8; 37 1.7; 40 1.6; 42 1.6; 45 1.5; 49 1.6; 52 1.8; 56 2.0; 59 1.9; 64 1.4; 68 0.8; 73 0.1; 78 -0.3; 83 -0.7; 89 -1.0; 95 -1.3; 102 -1.6; 109 -1.7; 117 -1.9; 125 -2.2; 134 -2.3; 143 -2.4; 153 -2.6; 164 -2.6; 175 -2.7; 188 -2.8; 201 -2.9; 215 -2.9; 230 -2.8; 246 -2.9; 263 -2.8; 282 -2.6; 301 -2.6; 323 -2.6; 345 -2.4; 369 -2.3; 395 -2.2; 423 -2.0; 452 -1.8; 484 -1.8; 518 -1.7; 554 -1.5; 593 -1.2; 635 -1.1; 679 -1.1; 726 -1.0; 777 -0.5; 832 -0.5; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.9; 1248 1.4; 1336 1.5; 1429 1.5; 1529 1.6; 1636 1.4; 1751 1.2; 1873 1.2; 2004 1.6; 2145 1.6; 2295 1.5; 2455 2.1; 2627 2.6; 2811 2.2; 3008 2.0; 3219 2.2; 3444 2.0; 3685 0.9; 3943 -0.1; 4219 -1.7; 4514 -2.6; 4830 -2.6; 5168 -2.9; 5530 -3.9; 5917 -4.0; 6331 -4.9; 6775 -4.3; 7249 -3.0; 7756 -1.3; 8299 -0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.668584318663928dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.57 | 3.8 dB  |
| Peaking | 58 Hz    | 2.13 | 2.2 dB  |
| Peaking | 214 Hz   | 0.37 | -3.0 dB |
| Peaking | 4025 Hz  | 0.42 | 4.1 dB  |
| Peaking | 5750 Hz  | 1.28 | -8.3 dB |
| Peaking | 1936 Hz  | 1.32 | 1.4 dB  |
| Peaking | 1971 Hz  | 2.38 | -2.0 dB |
| Peaking | 6721 Hz  | 6.81 | -1.3 dB |
| Peaking | 8276 Hz  | 3.81 | 1.2 dB  |
| Peaking | 13291 Hz | 0.82 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)