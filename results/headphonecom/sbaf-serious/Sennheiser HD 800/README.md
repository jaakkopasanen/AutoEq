# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 3.5; 22 3.1; 23 2.9; 25 2.6; 26 2.4; 28 2.1; 30 1.9; 32 1.7; 35 1.5; 37 1.4; 40 1.4; 42 1.4; 45 1.6; 49 1.7; 52 1.7; 56 1.3; 59 1.1; 64 1.0; 68 0.8; 73 0.2; 78 -0.3; 83 -0.6; 89 -0.9; 95 -1.2; 102 -1.5; 109 -2.0; 117 -2.3; 125 -2.7; 134 -3.1; 143 -3.4; 153 -3.5; 164 -3.4; 175 -3.6; 188 -3.7; 201 -3.7; 215 -3.6; 230 -3.6; 246 -3.6; 263 -3.5; 282 -3.3; 301 -3.2; 323 -3.0; 345 -2.8; 369 -2.7; 395 -2.6; 423 -2.4; 452 -2.3; 484 -2.2; 518 -2.1; 554 -1.8; 593 -1.5; 635 -1.3; 679 -1.3; 726 -1.1; 777 -0.8; 832 -0.7; 890 -0.6; 952 -0.1; 1019 0.1; 1090 0.5; 1167 1.2; 1248 1.3; 1336 1.5; 1429 1.4; 1529 1.1; 1636 1.2; 1751 1.4; 1873 1.5; 2004 1.6; 2145 1.4; 2295 1.4; 2455 2.5; 2627 2.6; 2811 2.0; 3008 1.5; 3219 1.2; 3444 1.5; 3685 0.2; 3943 -1.4; 4219 -2.3; 4514 -2.3; 4830 -2.2; 5168 -3.0; 5530 -4.8; 5917 -8.2; 6331 -7.9; 6775 -3.6; 7249 -1.8; 7756 -1.4; 8299 -2.5; 8880 -4.5; 9502 -5.5; 10167 -3.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 -1.3; 14260 -4.2; 15258 -4.5; 16326 -3.3; 17469 -2.3; 18692 -2.1; 20000 -2.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.14 | 2.8 dB  |
| Peaking | 191 Hz   | 0.58 | -4.4 dB |
| Peaking | 6046 Hz  | 4.96 | -9.0 dB |
| Peaking | 15658 Hz | 2.01 | -4.5 dB |
| Peaking | 9332 Hz  | 6.31 | -5.5 dB |
| Peaking | 577 Hz   | 1.31 | -0.6 dB |
| Peaking | 1303 Hz  | 2.52 | 1.4 dB  |
| Peaking | 2746 Hz  | 1.31 | 2.5 dB  |
| Peaking | 4268 Hz  | 3.8  | -2.7 dB |
| Peaking | 11963 Hz | 5.09 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)