# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 2.0; 22 1.2; 23 0.9; 25 0.3; 26 -0.0; 28 -0.5; 30 -1.0; 32 -1.4; 35 -1.9; 37 -2.3; 40 -2.9; 42 -3.3; 45 -3.7; 49 -4.2; 52 -4.5; 56 -4.6; 59 -4.5; 64 -3.8; 68 -3.5; 73 -4.5; 78 -5.8; 83 -6.4; 89 -6.6; 95 -6.5; 102 -6.3; 109 -6.6; 117 -6.8; 125 -6.8; 134 -6.7; 143 -6.6; 153 -6.4; 164 -6.0; 175 -5.7; 188 -5.5; 201 -5.4; 215 -5.3; 230 -4.5; 246 -3.3; 263 -2.4; 282 -1.9; 301 -1.8; 323 -1.1; 345 -0.1; 369 0.8; 395 1.4; 423 1.8; 452 1.7; 484 1.6; 518 1.4; 554 1.5; 593 1.6; 635 1.4; 679 1.1; 726 1.0; 777 1.0; 832 0.8; 890 0.6; 952 0.4; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.0; 1336 -1.5; 1429 -2.0; 1529 -2.7; 1636 -3.7; 1751 -4.2; 1873 -4.2; 2004 -4.3; 2145 -4.0; 2295 -3.3; 2455 -2.3; 2627 -1.1; 2811 -0.1; 3008 0.7; 3219 0.9; 3444 0.9; 3685 0.6; 3943 0.6; 4219 0.4; 4514 1.1; 4830 -0.3; 5168 -0.4; 5530 1.0; 5917 4.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -4.5; 8880 -5.3; 9502 -2.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 91 Hz   | 0.87 | -6.1 dB |
| Peaking | 175 Hz  | 1.83 | -3.9 dB |
| Peaking | 1882 Hz | 2.7  | -4.9 dB |
| Peaking | 6322 Hz | 4.69 | 6.4 dB  |
| Peaking | 8620 Hz | 6.17 | -6.6 dB |
| Peaking | 16 Hz   | 1.66 | 3.2 dB  |
| Peaking | 45 Hz   | 3.01 | -1.9 dB |
| Peaking | 233 Hz  | 3.71 | -1.6 dB |
| Peaking | 488 Hz  | 1.35 | 2.5 dB  |
| Peaking | 3284 Hz | 5.32 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)