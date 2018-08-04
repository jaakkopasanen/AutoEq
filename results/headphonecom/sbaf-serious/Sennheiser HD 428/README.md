# Sennheiser HD 428

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 4.8; 64 3.5; 68 4.0; 73 5.7; 78 5.4; 83 4.1; 89 2.6; 95 1.7; 102 0.8; 109 0.5; 117 0.1; 125 -0.1; 134 -0.1; 143 -0.1; 153 -0.0; 164 0.4; 175 0.7; 188 1.0; 201 1.3; 215 1.4; 230 2.1; 246 2.2; 263 1.5; 282 1.7; 301 1.8; 323 1.7; 345 1.5; 369 1.6; 395 1.7; 423 1.8; 452 1.8; 484 1.8; 518 1.9; 554 2.2; 593 2.4; 635 2.1; 679 1.3; 726 0.9; 777 0.5; 832 0.1; 890 -0.1; 952 -0.1; 1019 0.1; 1090 1.7; 1167 1.6; 1248 0.1; 1336 -0.6; 1429 -0.8; 1529 -1.1; 1636 -1.8; 1751 -2.1; 1873 -1.8; 2004 -1.2; 2145 -0.0; 2295 1.7; 2455 2.7; 2627 2.5; 2811 2.9; 3008 3.2; 3219 3.2; 3444 3.0; 3685 2.4; 3943 3.6; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.4; 5530 3.4; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 428 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.63 | 6.8 dB  |
| Peaking | 435 Hz   | 1.15 | 2.0 dB  |
| Peaking | 2878 Hz  | 4.11 | 2.0 dB  |
| Peaking | 4875 Hz  | 1.76 | 5.9 dB  |
| Peaking | 24000 Hz | 2.35 | 2.9 dB  |
| Peaking | 77 Hz    | 6.41 | 3.2 dB  |
| Peaking | 119 Hz   | 2.15 | -2.0 dB |
| Peaking | 1736 Hz  | 3.32 | -3.2 dB |
| Peaking | 1055 Hz  | 0.1  | 0.3 dB  |
| Peaking | 8709 Hz  | 3.78 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20428/Sennheiser%20HD%20428.png)