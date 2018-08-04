# AKG K240 MK II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 10 -84; 20 2.1; 22 1.3; 23 0.9; 25 0.3; 26 -0.1; 28 -0.6; 30 -1.2; 32 -1.6; 35 -2.3; 37 -2.7; 40 -3.2; 42 -3.4; 45 -3.7; 49 -4.1; 52 -4.4; 56 -4.7; 59 -4.5; 64 -4.3; 68 -5.0; 73 -6.0; 78 -6.6; 83 -7.0; 89 -7.2; 95 -7.5; 102 -7.7; 109 -7.6; 117 -7.7; 125 -7.6; 134 -7.6; 143 -7.5; 153 -7.1; 164 -6.6; 175 -6.5; 188 -6.2; 201 -5.9; 215 -5.6; 230 -5.2; 246 -4.8; 263 -4.7; 282 -4.6; 301 -4.5; 323 -4.4; 345 -4.0; 369 -3.8; 395 -3.6; 423 -3.4; 452 -3.3; 484 -3.4; 518 -1.1; 554 -0.2; 593 -0.9; 635 -1.0; 679 -1.1; 726 -0.9; 777 -0.7; 832 -0.5; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.6; 1336 0.2; 1429 -0.4; 1529 -0.9; 1636 -1.5; 1751 -2.3; 1873 -2.9; 2004 -2.9; 2145 -3.9; 2295 -3.8; 2455 -3.4; 2627 -2.1; 2811 -1.3; 3008 -0.3; 3219 1.0; 3444 1.7; 3685 1.7; 3943 0.8; 4219 -0.3; 4514 -1.0; 4830 -0.7; 5168 1.2; 5530 2.1; 5917 1.2; 6331 -0.1; 6775 -1.8; 7249 -2.9; 7756 -5.4; 8299 -8.3; 8880 -9.9; 9502 -8.9; 10167 -5.9; 10879 -2.7; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.7dB` and instead set Global volume in the UI for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MK II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.37 | 4.3 dB   |
| Peaking | 36 Hz    | 1.23 | -2.9 dB  |
| Peaking | 108 Hz   | 0.42 | -8.7 dB  |
| Peaking | 2181 Hz  | 3.8  | -4.2 dB  |
| Peaking | 8965 Hz  | 3.66 | -11.0 dB |
| Peaking | 486 Hz   | 3.23 | -2.5 dB  |
| Peaking | 1121 Hz  | 3.56 | 1.3 dB   |
| Peaking | 541 Hz   | 5.5  | 3.4 dB   |
| Peaking | 3548 Hz  | 5.48 | 2.5 dB   |
| Peaking | 21369 Hz | 1.74 | 1.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K240%20MK%20II/AKG%20K240%20MK%20II.png)