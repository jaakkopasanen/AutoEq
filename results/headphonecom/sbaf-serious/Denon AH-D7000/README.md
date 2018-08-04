# Denon AH-D7000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 1.3; 22 0.1; 23 -0.5; 25 -1.5; 26 -1.9; 28 -2.6; 30 -3.2; 32 -3.7; 35 -4.0; 37 -4.2; 40 -4.4; 42 -4.6; 45 -4.7; 49 -4.7; 52 -4.4; 56 -4.0; 59 -3.9; 64 -4.0; 68 -3.9; 73 -3.7; 78 -3.5; 83 -3.3; 89 -3.0; 95 -2.6; 102 -2.3; 109 -2.0; 117 -1.7; 125 -1.4; 134 -1.2; 143 -1.0; 153 -0.7; 164 -0.2; 175 0.1; 188 0.1; 201 0.4; 215 0.7; 230 1.0; 246 1.2; 263 1.4; 282 1.7; 301 2.0; 323 2.4; 345 2.7; 369 3.0; 395 3.1; 423 3.1; 452 2.6; 484 1.9; 518 1.5; 554 1.1; 593 0.7; 635 0.2; 679 -0.1; 726 -0.4; 777 -0.6; 832 -0.9; 890 1.0; 952 0.6; 1019 -0.0; 1090 0.2; 1167 0.6; 1248 1.0; 1336 1.4; 1429 1.6; 1529 1.7; 1636 1.9; 1751 2.1; 1873 2.3; 2004 2.2; 2145 2.3; 2295 2.8; 2455 3.1; 2627 3.1; 2811 3.1; 3008 2.7; 3219 1.5; 3444 0.3; 3685 0.1; 3943 0.7; 4219 0.8; 4514 -1.0; 4830 -0.6; 5168 1.2; 5530 2.1; 5917 1.3; 6331 -0.7; 6775 -1.0; 7249 -1.1; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.96 | 3.5 dB  |
| Peaking | 46 Hz    | 0.6  | -4.9 dB |
| Peaking | 360 Hz   | 1.54 | 3.3 dB  |
| Peaking | 2343 Hz  | 1.55 | 3.1 dB  |
| Peaking | 21741 Hz | 2.03 | -0.3 dB |
| Peaking | 763 Hz   | 4.68 | -1.3 dB |
| Peaking | 1451 Hz  | 4.56 | 0.8 dB  |
| Peaking | 4680 Hz  | 8.21 | -2.3 dB |
| Peaking | 5620 Hz  | 4.53 | 2.7 dB  |
| Peaking | 6600 Hz  | 4.11 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)