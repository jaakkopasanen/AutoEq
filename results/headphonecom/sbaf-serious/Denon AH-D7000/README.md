# Denon AH-D7000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 5.3; 22 4.1; 23 3.5; 25 2.5; 26 2.1; 28 1.4; 30 0.8; 32 0.3; 35 -0.0; 37 -0.2; 40 -0.4; 42 -0.6; 45 -0.8; 49 -0.7; 52 -0.4; 56 -0.0; 59 0.0; 64 -0.1; 68 -0.1; 73 0.1; 78 0.1; 83 0.1; 89 0.2; 95 0.2; 102 0.2; 109 -0.0; 117 -0.1; 125 -0.3; 134 -0.4; 143 -0.4; 153 -0.3; 164 0.1; 175 0.2; 188 0.2; 201 0.5; 215 0.7; 230 1.0; 246 1.2; 263 1.4; 282 1.7; 301 2.0; 323 2.4; 345 2.7; 369 3.0; 395 3.1; 423 3.1; 452 2.6; 484 1.9; 518 1.5; 554 1.1; 593 0.7; 635 0.2; 679 -0.1; 726 -0.4; 777 -0.6; 832 -0.9; 890 1.0; 952 0.6; 1019 -0.0; 1090 0.2; 1167 0.6; 1248 1.0; 1336 1.4; 1429 1.6; 1529 1.7; 1636 1.9; 1751 2.1; 1873 2.3; 2004 2.2; 2145 2.3; 2295 2.8; 2455 3.1; 2627 3.1; 2811 3.1; 3008 2.7; 3219 1.5; 3444 0.3; 3685 0.1; 3943 0.7; 4219 0.8; 4514 -1.0; 4830 -0.6; 5168 1.2; 5530 2.1; 5917 1.3; 6331 -0.7; 6775 -1.0; 7249 -1.1; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.79 | 4.3 dB  |
| Peaking | 377 Hz  | 2.02 | 3.3 dB  |
| Peaking | 2443 Hz | 1.28 | 3.3 dB  |
| Peaking | 5535 Hz | 5    | 5.2 dB  |
| Peaking | 5424 Hz | 1.79 | -3.3 dB |
| Peaking | 19 Hz   | 1.28 | 1.2 dB  |
| Peaking | 41 Hz   | 1.93 | -1.2 dB |
| Peaking | 468 Hz  | 4.34 | 0.4 dB  |
| Peaking | 766 Hz  | 4.13 | -1.3 dB |
| Peaking | 1450 Hz | 4.97 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)