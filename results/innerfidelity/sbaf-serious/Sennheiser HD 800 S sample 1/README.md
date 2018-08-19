# Sennheiser HD 800 S sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 4.8; 22 4.2; 23 3.9; 25 3.4; 26 3.2; 28 2.9; 30 2.5; 32 2.2; 35 1.9; 37 1.7; 40 1.5; 42 1.3; 45 1.2; 49 1.1; 52 1.0; 56 0.7; 59 0.6; 64 0.6; 68 0.5; 73 0.2; 78 -0.2; 83 -0.7; 89 -1.1; 95 -1.6; 102 -2.0; 109 -2.2; 117 -2.4; 125 -2.7; 134 -2.9; 143 -3.0; 153 -3.2; 164 -3.1; 175 -3.2; 188 -3.4; 201 -3.4; 215 -3.4; 230 -3.4; 246 -3.4; 263 -3.4; 282 -3.2; 301 -3.2; 323 -3.1; 345 -2.9; 369 -2.8; 395 -2.7; 423 -2.5; 452 -2.3; 484 -2.3; 518 -2.2; 554 -1.9; 593 -1.6; 635 -1.5; 679 -1.5; 726 -1.2; 777 -0.8; 832 -0.7; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.6; 1248 1.0; 1336 1.5; 1429 1.8; 1529 2.1; 1636 2.0; 1751 1.8; 1873 1.7; 2004 2.0; 2145 2.0; 2295 1.8; 2455 2.1; 2627 2.3; 2811 2.0; 3008 1.9; 3219 1.7; 3444 1.9; 3685 1.3; 3943 0.8; 4219 0.1; 4514 0.1; 4830 0.1; 5168 -0.7; 5530 -1.5; 5917 -1.2; 6331 -3.8; 6775 -4.5; 7249 -3.4; 7756 -2.4; 8299 -1.5; 8880 -0.9; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.3; 15258 -0.1; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.888814143119096dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.01 | 2.2 dB  |
| Peaking | 22 Hz   | 0.24 | 2.9 dB  |
| Peaking | 204 Hz  | 0.37 | -4.0 dB |
| Peaking | 2098 Hz | 0.7  | 2.5 dB  |
| Peaking | 6769 Hz | 3.05 | -4.9 dB |
| Peaking | 29 Hz   | 0.66 | -0.6 dB |
| Peaking | 72 Hz   | 2.65 | 0.8 dB  |
| Peaking | 108 Hz  | 2.35 | -0.4 dB |
| Peaking | 1480 Hz | 8.03 | 0.5 dB  |
| Peaking | 4276 Hz | 9.08 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sample%201/Sennheiser%20HD%20800%20S%20sample%201.png)