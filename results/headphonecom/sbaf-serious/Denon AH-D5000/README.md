# Denon AH-D5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 10 -84; 20 -1.5; 22 -2.3; 23 -2.6; 25 -3.2; 26 -3.4; 28 -3.8; 30 -4.0; 32 -4.2; 35 -4.4; 37 -4.6; 40 -4.8; 42 -4.7; 45 -4.5; 49 -4.5; 52 -4.5; 56 -4.5; 59 -4.5; 64 -4.5; 68 -4.5; 73 -4.5; 78 -4.4; 83 -4.4; 89 -4.3; 95 -4.2; 102 -3.9; 109 -3.7; 117 -3.6; 125 -3.6; 134 -3.5; 143 -3.3; 153 -3.2; 164 -3.0; 175 -2.9; 188 -2.6; 201 -2.4; 215 -2.4; 230 -2.2; 246 -2.2; 263 -2.2; 282 -2.1; 301 -2.0; 323 -1.8; 345 -1.4; 369 -1.1; 395 -0.9; 423 -0.5; 452 -0.3; 484 -0.1; 518 0.3; 554 0.9; 593 1.6; 635 1.6; 679 1.0; 726 -0.1; 777 -1.5; 832 -1.9; 890 0.4; 952 1.0; 1019 -0.3; 1090 -1.0; 1167 -1.5; 1248 -1.8; 1336 -2.3; 1429 -2.8; 1529 -3.2; 1636 -3.5; 1751 -3.8; 1873 -3.7; 2004 -3.3; 2145 -2.9; 2295 -2.3; 2455 -1.3; 2627 0.4; 2811 1.3; 3008 1.1; 3219 0.5; 3444 -0.2; 3685 -0.8; 3943 -1.7; 4219 -3.6; 4514 -3.9; 4830 -3.1; 5168 -2.0; 5530 -0.8; 5917 -0.3; 6331 -1.8; 6775 -3.7; 7249 -4.4; 7756 -3.8; 8299 -3.6; 8880 -4.7; 9502 -4.8; 10167 -1.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.9; 14260 -0.1; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.7; 20000 -7.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.2dB` and instead set Global volume in the UI for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.55 | -4.3 dB |
| Peaking | 146 Hz   | 0.71 | -2.2 dB |
| Peaking | 1730 Hz  | 2.32 | -4.0 dB |
| Peaking | 7926 Hz  | 1.63 | -4.4 dB |
| Peaking | 20011 Hz | 4.41 | -7.4 dB |
| Peaking | 607 Hz   | 5.46 | 2.4 dB  |
| Peaking | 2943 Hz  | 5.08 | 2.5 dB  |
| Peaking | 4462 Hz  | 4.21 | -3.4 dB |
| Peaking | 5832 Hz  | 7.1  | 2.2 dB  |
| Peaking | 11158 Hz | 6.48 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)