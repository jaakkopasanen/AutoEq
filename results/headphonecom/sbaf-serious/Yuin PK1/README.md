# Yuin PK1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.8; 78 5.2; 83 4.7; 89 4.2; 95 3.8; 102 3.5; 109 3.4; 117 3.3; 125 3.1; 134 3.0; 143 2.9; 153 2.8; 164 2.7; 175 2.7; 188 2.6; 201 2.6; 215 2.7; 230 2.5; 246 2.6; 263 2.6; 282 2.5; 301 2.6; 323 2.6; 345 2.6; 369 2.5; 395 2.3; 423 2.2; 452 2.0; 484 1.7; 518 1.5; 554 1.6; 593 1.6; 635 1.4; 679 1.1; 726 1.0; 777 0.9; 832 0.7; 890 0.4; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -3.2; 1751 -3.6; 1873 -4.0; 2004 -4.3; 2145 -4.3; 2295 -3.8; 2455 -3.0; 2627 -2.0; 2811 -0.7; 3008 0.7; 3219 1.7; 3444 2.3; 3685 2.2; 3943 1.3; 4219 -0.7; 4514 -2.3; 4830 -2.7; 5168 -2.7; 5530 -2.8; 5917 -3.4; 6331 -3.7; 6775 -2.8; 7249 -2.1; 7756 -2.0; 8299 -2.3; 8880 -2.0; 9502 -1.2; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.2; 15258 -0.5; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.37 | 6.4 dB  |
| Peaking | 375 Hz   | 0.6  | 2.0 dB  |
| Peaking | 2050 Hz  | 1.54 | -4.9 dB |
| Peaking | 3494 Hz  | 2.4  | 5.4 dB  |
| Peaking | 5484 Hz  | 1.12 | -3.9 dB |
| Peaking | 42 Hz    | 1.94 | -0.4 dB |
| Peaking | 68 Hz    | 3    | 1.0 dB  |
| Peaking | 103 Hz   | 2.46 | -0.5 dB |
| Peaking | 8836 Hz  | 5.06 | -1.1 dB |
| Peaking | 10719 Hz | 2.23 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)