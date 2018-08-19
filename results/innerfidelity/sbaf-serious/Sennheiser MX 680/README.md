# Sennheiser MX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 5.9; 201 5.4; 215 5.1; 230 4.9; 246 4.4; 263 4.2; 282 4.0; 301 3.7; 323 3.5; 345 3.4; 369 3.3; 395 3.5; 423 3.2; 452 3.3; 484 3.1; 518 2.9; 554 2.9; 593 2.6; 635 2.1; 679 1.8; 726 1.5; 777 1.4; 832 1.1; 890 0.7; 952 0.3; 1019 0.3; 1090 -0.3; 1167 -0.7; 1248 -1.5; 1336 -2.6; 1429 -3.7; 1529 -5.1; 1636 -6.5; 1751 -8.0; 1873 -9.3; 2004 -10.3; 2145 -11.0; 2295 -11.2; 2455 -10.8; 2627 -10.4; 2811 -9.1; 3008 -6.7; 3219 -4.6; 3444 -2.6; 3685 -2.0; 3943 -2.2; 4219 -3.6; 4514 -4.7; 4830 -5.4; 5168 -6.1; 5530 -7.7; 5917 -9.8; 6331 -10.3; 6775 -8.4; 7249 -6.6; 7756 -5.6; 8299 -5.7; 8880 -6.0; 9502 -5.1; 10167 -2.7; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -1.7; 15258 -2.0; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.1  | 5.7 dB   |
| Peaking | 347 Hz   | 0.26 | 2.3 dB   |
| Peaking | 2168 Hz  | 1.6  | -12.3 dB |
| Peaking | 6478 Hz  | 1.82 | -9.2 dB  |
| Peaking | 14863 Hz | 7.57 | -2.1 dB  |
| Peaking | 2753 Hz  | 6.93 | -2.7 dB  |
| Peaking | 3651 Hz  | 5.06 | 2.7 dB   |
| Peaking | 5867 Hz  | 3.31 | -2.1 dB  |
| Peaking | 8800 Hz  | 1.24 | 4.2 dB   |
| Peaking | 9094 Hz  | 3.28 | -7.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20680/Sennheiser%20MX%20680.png)