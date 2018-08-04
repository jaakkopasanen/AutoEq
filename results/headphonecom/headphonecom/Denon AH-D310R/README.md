# Denon AH-D310R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 1.4; 22 0.8; 23 0.5; 25 0.0; 26 -0.2; 28 -0.6; 30 -0.9; 32 -1.2; 35 -1.6; 37 -1.8; 40 -2.1; 42 -2.3; 45 -2.5; 49 -2.7; 52 -2.9; 56 -3.1; 59 -3.2; 64 -3.2; 68 -3.1; 73 -2.7; 78 -2.3; 83 -2.5; 89 -3.0; 95 -3.2; 102 -3.2; 109 -3.2; 117 -3.2; 125 -3.2; 134 -3.2; 143 -3.2; 153 -3.3; 164 -3.8; 175 -4.4; 188 -4.5; 201 -4.2; 215 -4.2; 230 -4.1; 246 -3.8; 263 -3.5; 282 -2.9; 301 -1.7; 323 -1.4; 345 -1.5; 369 -1.0; 395 -0.3; 423 -0.0; 452 0.6; 484 1.2; 518 1.5; 554 1.7; 593 2.5; 635 3.6; 679 4.8; 726 4.9; 777 3.3; 832 1.2; 890 0.1; 952 0.0; 1019 0.0; 1090 0.0; 1167 -0.0; 1248 0.1; 1336 0.6; 1429 3.0; 1529 6.0; 1636 5.7; 1751 5.4; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D310R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.05 | 2.7 dB  |
| Peaking | 61 Hz   | 0.4  | -3.1 dB |
| Peaking | 210 Hz  | 1.48 | -3.5 dB |
| Peaking | 681 Hz  | 4.54 | 4.8 dB  |
| Peaking | 3193 Hz | 0.66 | 6.9 dB  |
| Peaking | 507 Hz  | 3.1  | 1.2 dB  |
| Peaking | 1323 Hz | 1.96 | -5.9 dB |
| Peaking | 1542 Hz | 2.49 | 6.7 dB  |
| Peaking | 6011 Hz | 2    | 7.5 dB  |
| Peaking | 6679 Hz | 1.03 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D310R/Denon%20AH-D310R.png)