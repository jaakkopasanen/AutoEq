# Denon AH-D5000 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.7; 23 -3.2; 25 -3.9; 26 -4.1; 28 -4.6; 30 -4.9; 32 -5.1; 35 -5.3; 37 -5.4; 40 -5.6; 42 -5.6; 45 -5.6; 49 -5.4; 52 -5.2; 56 -5.1; 59 -5.1; 64 -5.1; 68 -5.1; 73 -5.1; 78 -5.1; 83 -5.1; 89 -5.1; 95 -4.9; 102 -4.9; 109 -4.9; 117 -4.8; 125 -4.6; 134 -4.5; 143 -4.2; 153 -4.1; 164 -3.9; 175 -3.8; 188 -3.8; 201 -3.8; 215 -3.7; 230 -3.5; 246 -3.4; 263 -3.2; 282 -3.0; 301 -2.9; 323 -2.8; 345 -2.4; 369 -2.3; 395 -1.9; 423 -1.5; 452 -1.1; 484 -0.6; 518 -0.1; 554 0.6; 593 1.2; 635 1.6; 679 1.3; 726 0.4; 777 -0.9; 832 -2.1; 890 0.3; 952 1.2; 1019 -0.2; 1090 -0.8; 1167 -1.1; 1248 -1.1; 1336 -0.9; 1429 -0.5; 1529 -0.3; 1636 -0.4; 1751 -0.5; 1873 -0.5; 2004 -0.3; 2145 -0.3; 2295 -0.0; 2455 1.0; 2627 3.5; 2811 4.9; 3008 4.3; 3219 3.5; 3444 2.5; 3685 2.0; 3943 1.2; 4219 1.1; 4514 1.9; 4830 2.8; 5168 3.7; 5530 4.5; 5917 3.7; 6331 0.4; 6775 -2.0; 7249 -3.3; 7756 -3.1; 8299 -2.3; 8880 -2.1; 9502 -1.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.34 | -5.5 dB |
| Peaking | 248 Hz  | 1.39 | -1.7 dB |
| Peaking | 2921 Hz | 4.47 | 5.1 dB  |
| Peaking | 5652 Hz | 2.76 | 6.5 dB  |
| Peaking | 7173 Hz | 2.29 | -5.4 dB |
| Peaking | 64 Hz   | 3.7  | 0.5 dB  |
| Peaking | 370 Hz  | 3.9  | -0.6 dB |
| Peaking | 623 Hz  | 4.64 | 2.4 dB  |
| Peaking | 1251 Hz | 4.32 | -1.1 dB |
| Peaking | 2028 Hz | 3.77 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D5000%20(balanced)/Denon%20AH-D5000%20(balanced).png)