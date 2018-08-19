# Sennheiser HD 555

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.4; 37 5.1; 40 4.7; 42 4.4; 45 4.1; 49 3.6; 52 3.4; 56 3.4; 59 3.3; 64 3.1; 68 3.7; 73 3.4; 78 2.3; 83 1.7; 89 1.2; 95 0.9; 102 0.5; 109 0.2; 117 0.1; 125 -0.1; 134 -0.4; 143 -0.7; 153 -0.7; 164 -0.7; 175 -0.9; 188 -1.0; 201 -1.1; 215 -1.2; 230 -1.2; 246 -1.2; 263 -1.2; 282 -1.1; 301 -1.0; 323 -0.9; 345 -0.8; 369 -0.6; 395 -0.5; 423 -0.2; 452 -0.2; 484 -0.1; 518 -0.0; 554 -0.0; 593 0.5; 635 0.4; 679 0.4; 726 0.4; 777 0.2; 832 0.4; 890 0.3; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.5; 1336 0.9; 1429 1.2; 1529 1.5; 1636 1.8; 1751 1.3; 1873 0.7; 2004 0.7; 2145 0.6; 2295 0.3; 2455 0.4; 2627 0.8; 2811 0.9; 3008 0.1; 3219 -0.7; 3444 -0.6; 3685 -0.0; 3943 1.8; 4219 3.4; 4514 0.6; 4830 -0.1; 5168 2.2; 5530 5.2; 5917 5.9; 6331 4.3; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.7; 18692 -3.6; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.22 | 6.3 dB  |
| Peaking | 164 Hz   | 0.55 | -2.2 dB |
| Peaking | 626 Hz   | 1.85 | 0.7 dB  |
| Peaking | 1600 Hz  | 2.86 | 1.7 dB  |
| Peaking | 5922 Hz  | 4.1  | 6.2 dB  |
| Peaking | 71 Hz    | 7.15 | 0.9 dB  |
| Peaking | 3481 Hz  | 6.03 | -1.5 dB |
| Peaking | 4203 Hz  | 6.18 | 3.5 dB  |
| Peaking | 4682 Hz  | 8.24 | -2.8 dB |
| Peaking | 19113 Hz | 2.16 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20555/Sennheiser%20HD%20555.png)