# Sennheiser HD800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 4.6; 22 4.2; 23 4.0; 25 3.7; 26 3.5; 28 3.2; 30 3.0; 32 2.8; 35 2.5; 37 2.4; 40 2.5; 42 2.6; 45 3.0; 49 3.0; 52 2.5; 56 2.1; 59 2.0; 64 1.7; 68 1.2; 73 0.7; 78 0.4; 83 0.2; 89 -0.2; 95 -0.4; 102 -0.7; 109 -1.1; 117 -1.5; 125 -1.9; 134 -2.3; 143 -2.7; 153 -2.8; 164 -2.7; 175 -2.8; 188 -3.0; 201 -3.0; 215 -3.0; 230 -2.9; 246 -2.9; 263 -2.9; 282 -2.6; 301 -2.4; 323 -2.3; 345 -2.1; 369 -2.0; 395 -2.0; 423 -1.8; 452 -1.6; 484 -1.5; 518 -1.5; 554 -1.2; 593 -0.9; 635 -0.8; 679 -0.8; 726 -0.7; 777 -0.4; 832 -0.4; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.5; 1167 1.0; 1248 1.4; 1336 1.9; 1429 1.9; 1529 1.6; 1636 1.3; 1751 1.6; 1873 1.9; 2004 1.8; 2145 1.9; 2295 2.5; 2455 3.3; 2627 3.1; 2811 3.1; 3008 2.9; 3219 2.3; 3444 2.4; 3685 1.2; 3943 -0.3; 4219 -1.3; 4514 -1.3; 4830 -1.1; 5168 -2.0; 5530 -4.8; 5917 -8.5; 6331 -5.9; 6775 -1.5; 7249 0.5; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.8; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 -0.2; 13327 -3.5; 14260 -5.4; 15258 -5.0; 16326 -2.9; 17469 -0.4; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.16 | 4.0 dB  |
| Peaking | 170 Hz   | 0.49 | -4.5 dB |
| Peaking | 2405 Hz  | 1.07 | 3.1 dB  |
| Peaking | 5899 Hz  | 5.59 | -9.3 dB |
| Peaking | 33058 Hz | 2.92 | -6.1 dB |
| Peaking | 1346 Hz  | 2.79 | 1.9 dB  |
| Peaking | 2328 Hz  | 0.71 | -2.1 dB |
| Peaking | 3081 Hz  | 1.23 | 2.6 dB  |
| Peaking | 4205 Hz  | 5.35 | -2.5 dB |
| Peaking | 7318 Hz  | 8.33 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD800/Sennheiser%20HD800.png)