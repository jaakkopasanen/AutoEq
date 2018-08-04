# Denon AH-D2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.8; 23 -1.2; 25 -1.9; 26 -2.2; 28 -2.6; 30 -2.9; 32 -3.1; 35 -3.1; 37 -2.9; 40 -2.7; 42 -2.7; 45 -2.7; 49 -2.9; 52 -2.9; 56 -2.7; 59 -2.4; 64 -1.9; 68 -2.1; 73 -2.1; 78 -2.1; 83 -2.1; 89 -2.1; 95 -2.1; 102 -2.1; 109 -2.1; 117 -2.1; 125 -1.9; 134 -1.8; 143 -1.8; 153 -1.8; 164 -1.4; 175 -1.5; 188 -1.5; 201 -1.3; 215 -1.2; 230 -1.2; 246 -1.1; 263 -1.0; 282 -0.7; 301 -0.6; 323 -0.6; 345 -0.6; 369 -0.4; 395 -0.3; 423 -0.2; 452 -0.0; 484 0.1; 518 -0.1; 554 -0.5; 593 -0.6; 635 -0.6; 679 -0.6; 726 -0.5; 777 0.7; 832 0.8; 890 0.1; 952 -0.1; 1019 -0.0; 1090 0.2; 1167 0.9; 1248 1.8; 1336 3.0; 1429 4.0; 1529 4.6; 1636 4.8; 1751 4.5; 1873 4.4; 2004 5.0; 2145 5.9; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 5.1; 3444 4.0; 3685 3.2; 3943 3.6; 4219 5.4; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.1; 6331 1.8; 6775 1.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -1.1; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.28 | -2.1 dB |
| Peaking | 96 Hz   | 0.36 | -1.9 dB |
| Peaking | 1018 Hz | 3.26 | -1.7 dB |
| Peaking | 2278 Hz | 0.91 | 6.1 dB  |
| Peaking | 5065 Hz | 3.09 | 5.1 dB  |
| Peaking | 647 Hz  | 4.34 | -1.1 dB |
| Peaking | 1508 Hz | 6.07 | 1.1 dB  |
| Peaking | 1893 Hz | 5.44 | -1.2 dB |
| Peaking | 1280 Hz | 0.2  | 0.2 dB  |
| Peaking | 9661 Hz | 2.8  | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D2000/Denon%20AH-D2000.png)