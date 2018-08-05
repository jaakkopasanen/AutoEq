# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.4; 37 5.1; 40 4.6; 42 4.4; 45 4.0; 49 3.6; 52 3.4; 56 3.0; 59 2.9; 64 3.0; 68 2.8; 73 2.3; 78 2.5; 83 3.0; 89 2.2; 95 1.3; 102 0.6; 109 0.2; 117 -0.3; 125 -0.9; 134 -1.3; 143 -1.5; 153 -1.9; 164 -2.0; 175 -2.0; 188 -2.1; 201 -2.1; 215 -2.0; 230 -1.9; 246 -2.0; 263 -2.1; 282 -2.1; 301 -2.0; 323 -1.9; 345 -1.7; 369 -1.6; 395 -1.5; 423 -1.3; 452 -1.3; 484 -1.3; 518 -1.2; 554 -0.8; 593 -0.8; 635 -1.0; 679 0.7; 726 0.0; 777 -0.2; 832 -0.4; 890 -0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 -0.2; 1336 -0.1; 1429 -0.0; 1529 0.2; 1636 1.1; 1751 1.2; 1873 1.2; 2004 1.0; 2145 0.6; 2295 1.2; 2455 2.0; 2627 1.0; 2811 0.0; 3008 0.4; 3219 -0.4; 3444 -0.5; 3685 -0.1; 3943 0.1; 4219 -2.4; 4514 -4.0; 4830 -3.2; 5168 -1.4; 5530 -0.5; 5917 -0.1; 6331 -0.1; 6775 0.2; 7249 0.7; 7756 0.3; 8299 -0.5; 8880 -1.4; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -2.2; 18692 -4.8; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.16 | 6.2 dB  |
| Peaking | 186 Hz   | 0.59 | -3.3 dB |
| Peaking | 2143 Hz  | 1.67 | 1.4 dB  |
| Peaking | 4626 Hz  | 5.92 | -4.5 dB |
| Peaking | 19231 Hz | 2.03 | -6.0 dB |
| Peaking | 54 Hz    | 2.68 | -0.7 dB |
| Peaking | 84 Hz    | 6.82 | 1.4 dB  |
| Peaking | 8151 Hz  | 2.24 | 1.0 dB  |
| Peaking | 8764 Hz  | 6.25 | -2.3 dB |
| Peaking | 15937 Hz | 3.27 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)