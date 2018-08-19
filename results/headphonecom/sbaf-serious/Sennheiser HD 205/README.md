# Sennheiser HD 205

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.6; 26 5.4; 28 5.2; 30 4.9; 32 4.6; 35 4.2; 37 3.9; 40 3.6; 42 3.5; 45 3.5; 49 3.1; 52 2.6; 56 2.1; 59 1.9; 64 1.9; 68 1.9; 73 1.8; 78 1.1; 83 0.7; 89 0.3; 95 -0.1; 102 -0.4; 109 -0.5; 117 -0.6; 125 -0.8; 134 -0.6; 143 0.0; 153 0.7; 164 0.3; 175 -0.1; 188 -0.1; 201 0.1; 215 0.8; 230 1.0; 246 0.7; 263 0.7; 282 0.9; 301 1.2; 323 1.6; 345 2.2; 369 3.0; 395 3.9; 423 4.3; 452 3.8; 484 2.6; 518 1.3; 554 0.5; 593 0.7; 635 1.8; 679 3.6; 726 4.5; 777 3.8; 832 2.5; 890 1.3; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.0; 1248 -1.3; 1336 -1.6; 1429 -1.9; 1529 -2.2; 1636 -2.3; 1751 -2.2; 1873 -1.7; 2004 -1.3; 2145 -0.6; 2295 0.2; 2455 1.2; 2627 2.5; 2811 3.4; 3008 3.5; 3219 4.0; 3444 5.2; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 2.4; 5168 -0.0; 5530 2.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.8  | 5.8 dB  |
| Peaking | 412 Hz   | 3.34 | 4.4 dB  |
| Peaking | 737 Hz   | 5.72 | 4.6 dB  |
| Peaking | 4011 Hz  | 1.85 | 6.4 dB  |
| Peaking | 24000 Hz | 2.45 | 2.8 dB  |
| Peaking | 115 Hz   | 3.58 | -1.3 dB |
| Peaking | 1672 Hz  | 1.79 | -3.1 dB |
| Peaking | 2799 Hz  | 3.94 | 1.8 dB  |
| Peaking | 5181 Hz  | 9.04 | -4.7 dB |
| Peaking | 6148 Hz  | 5.22 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205/Sennheiser%20HD%20205.png)