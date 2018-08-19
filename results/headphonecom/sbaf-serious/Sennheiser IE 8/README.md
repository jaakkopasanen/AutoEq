# Sennheiser IE 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.6; 23 -2.9; 25 -3.5; 26 -3.7; 28 -4.1; 30 -4.5; 32 -4.9; 35 -5.4; 37 -5.7; 40 -6.1; 42 -6.4; 45 -6.8; 49 -7.2; 52 -7.5; 56 -7.9; 59 -8.2; 64 -8.6; 68 -8.9; 73 -9.3; 78 -9.5; 83 -9.7; 89 -10.1; 95 -10.4; 102 -10.4; 109 -10.5; 117 -10.7; 125 -10.8; 134 -10.9; 143 -11.0; 153 -11.0; 164 -10.9; 175 -10.8; 188 -10.6; 201 -10.4; 215 -10.1; 230 -9.9; 246 -9.6; 263 -9.2; 282 -8.8; 301 -8.3; 323 -7.8; 345 -7.1; 369 -6.5; 395 -6.0; 423 -5.6; 452 -5.2; 484 -4.7; 518 -4.1; 554 -3.4; 593 -2.8; 635 -2.1; 679 -1.6; 726 -1.2; 777 -0.8; 832 -0.5; 890 -0.3; 952 -0.3; 1019 0.0; 1090 -0.0; 1167 -0.4; 1248 -0.8; 1336 -1.5; 1429 -2.3; 1529 -3.1; 1636 -3.5; 1751 -3.7; 1873 -3.7; 2004 -3.5; 2145 -3.4; 2295 -2.9; 2455 -2.4; 2627 -1.7; 2811 -0.9; 3008 -0.1; 3219 0.8; 3444 1.5; 3685 1.0; 3943 -0.3; 4219 -1.3; 4514 -0.7; 4830 1.6; 5168 3.4; 5530 3.8; 5917 2.5; 6331 1.3; 6775 1.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -0.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.3; 15258 -1.2; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.950345603398736dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.45 | -7.9 dB |
| Peaking | 182 Hz  | 0.86 | -5.5 dB |
| Peaking | 338 Hz  | 1.28 | -3.3 dB |
| Peaking | 1914 Hz | 2.36 | -4.0 dB |
| Peaking | 5495 Hz | 4.48 | 4.1 dB  |
| Peaking | 507 Hz  | 3.84 | -0.9 dB |
| Peaking | 987 Hz  | 1.65 | 1.2 dB  |
| Peaking | 1493 Hz | 4.65 | -1.3 dB |
| Peaking | 3442 Hz | 6.27 | 2.1 dB  |
| Peaking | 4263 Hz | 8.42 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20IE%208/Sennheiser%20IE%208.png)