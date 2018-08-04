# Denon AH-D1100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -11.3; 22 -11.8; 23 -12.0; 25 -12.4; 26 -12.6; 28 -12.9; 30 -13.2; 32 -13.5; 35 -13.8; 37 -14.0; 40 -14.2; 42 -14.4; 45 -14.5; 49 -14.7; 52 -14.8; 56 -14.9; 59 -15.0; 64 -15.1; 68 -15.1; 73 -15.1; 78 -15.1; 83 -15.0; 89 -14.8; 95 -14.5; 102 -14.0; 109 -13.7; 117 -13.7; 125 -14.3; 134 -15.1; 143 -15.2; 153 -14.3; 164 -13.4; 175 -13.0; 188 -13.8; 201 -13.6; 215 -13.3; 230 -12.5; 246 -11.5; 263 -10.4; 282 -9.1; 301 -7.5; 323 -5.8; 345 -4.0; 369 -2.2; 395 -0.3; 423 1.3; 452 2.4; 484 2.6; 518 2.2; 554 1.7; 593 1.0; 635 0.4; 679 -0.1; 726 -0.4; 777 -0.6; 832 -0.7; 890 -0.4; 952 -0.2; 1019 0.2; 1090 0.5; 1167 0.8; 1248 1.2; 1336 1.7; 1429 2.0; 1529 1.8; 1636 1.4; 1751 0.6; 1873 -0.2; 2004 -0.2; 2145 0.5; 2295 1.8; 2455 3.4; 2627 4.9; 2811 6.0; 3008 6.0; 3219 5.1; 3444 3.1; 3685 5.8; 3943 6.0; 4219 6.0; 4514 5.0; 4830 4.9; 5168 6.0; 5530 5.4; 5917 5.9; 6331 5.4; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -0.7; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.52 | -11.7 dB |
| Peaking | 76 Hz   | 0.94 | -8.6 dB  |
| Peaking | 147 Hz  | 1.68 | -8.4 dB  |
| Peaking | 231 Hz  | 2.43 | -8.8 dB  |
| Peaking | 4066 Hz | 0.96 | 6.2 dB   |
| Peaking | 462 Hz  | 2.2  | 7.8 dB   |
| Peaking | 414 Hz  | 1.07 | -3.6 dB  |
| Peaking | 1380 Hz | 6.1  | 1.4 dB   |
| Peaking | 6196 Hz | 3.05 | 4.9 dB   |
| Peaking | 7243 Hz | 1.19 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D1100/Denon%20AH-D1100.png)