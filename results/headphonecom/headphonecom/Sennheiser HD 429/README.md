# Sennheiser HD 429

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.7; 22 -5.9; 23 -6.0; 25 -6.1; 26 -6.2; 28 -6.2; 30 -6.3; 32 -6.4; 35 -6.5; 37 -6.5; 40 -6.5; 42 -6.5; 45 -6.5; 49 -6.3; 52 -6.3; 56 -6.2; 59 -6.0; 64 -5.8; 68 -5.6; 73 -5.3; 78 -4.8; 83 -4.3; 89 -3.3; 95 -2.0; 102 -2.1; 109 -3.6; 117 -4.2; 125 -4.4; 134 -4.5; 143 -4.5; 153 -3.9; 164 -3.5; 175 -4.1; 188 -3.9; 201 -3.7; 215 -3.9; 230 -3.6; 246 -3.2; 263 -2.4; 282 -1.6; 301 -1.1; 323 -0.9; 345 -0.6; 369 -0.6; 395 -0.8; 423 -0.8; 452 -0.8; 484 -1.0; 518 -1.1; 554 -1.1; 593 -1.0; 635 -0.8; 679 -0.9; 726 -0.9; 777 -0.8; 832 -0.6; 890 -0.4; 952 -0.1; 1019 -0.1; 1090 -0.3; 1167 -0.7; 1248 -0.3; 1336 0.9; 1429 1.1; 1529 1.5; 1636 1.8; 1751 2.3; 1873 3.0; 2004 3.7; 2145 4.9; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.67 | -6.0 dB |
| Peaking | 59 Hz   | 1.57 | -3.2 dB |
| Peaking | 170 Hz  | 1.09 | -3.7 dB |
| Peaking | 1042 Hz | 0.88 | -1.7 dB |
| Peaking | 3380 Hz | 0.7  | 7.0 dB  |
| Peaking | 9 Hz    | 1.36 | -0.7 dB |
| Peaking | 2356 Hz | 4.42 | 1.8 dB  |
| Peaking | 3173 Hz | 1.13 | -1.0 dB |
| Peaking | 6196 Hz | 2.1  | 5.5 dB  |
| Peaking | 7501 Hz | 1.46 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)