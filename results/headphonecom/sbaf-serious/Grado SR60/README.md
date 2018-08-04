# Grado SR60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 4.8; 23 4.3; 25 3.3; 26 2.8; 28 2.0; 30 1.3; 32 0.7; 35 -0.2; 37 -0.7; 40 -1.3; 42 -1.7; 45 -2.2; 49 -2.8; 52 -3.0; 56 -3.4; 59 -3.6; 64 -3.8; 68 -3.7; 73 -3.6; 78 -3.8; 83 -3.9; 89 -3.8; 95 -3.6; 102 -3.4; 109 -3.1; 117 -2.9; 125 -2.6; 134 -2.2; 143 -1.8; 153 -1.6; 164 -1.6; 175 -1.5; 188 -1.2; 201 -0.9; 215 -0.5; 230 -0.9; 246 -1.5; 263 -1.5; 282 -1.2; 301 -1.0; 323 -0.7; 345 -0.5; 369 -0.4; 395 -0.2; 423 0.0; 452 0.1; 484 0.0; 518 0.1; 554 0.3; 593 0.4; 635 0.6; 679 0.4; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.1; 1529 -2.8; 1636 -3.6; 1751 -4.3; 1873 -4.8; 2004 -5.3; 2145 -5.6; 2295 -5.8; 2455 -5.6; 2627 -5.1; 2811 -3.8; 3008 -1.6; 3219 -0.2; 3444 0.8; 3685 1.5; 3943 0.3; 4219 -2.0; 4514 -6.1; 4830 -7.5; 5168 -4.4; 5530 -3.7; 5917 -2.0; 6331 -0.6; 6775 -2.1; 7249 -4.1; 7756 -5.9; 8299 -7.9; 8880 -8.4; 9502 -5.5; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -1.9; 16326 -1.4; 17469 -0.5; 18692 -0.5; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.16 | 6.8 dB  |
| Peaking | 68 Hz    | 0.66 | -4.4 dB |
| Peaking | 2163 Hz  | 1.84 | -6.1 dB |
| Peaking | 8490 Hz  | 3.01 | -8.4 dB |
| Peaking | 21083 Hz | 2.07 | -6.0 dB |
| Peaking | 744 Hz   | 1.91 | 1.0 dB  |
| Peaking | 3707 Hz  | 4.39 | 4.0 dB  |
| Peaking | 4766 Hz  | 5.54 | -7.6 dB |
| Peaking | 10887 Hz | 4.21 | 2.3 dB  |
| Peaking | 15562 Hz | 5.2  | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR60/Grado%20SR60.png)