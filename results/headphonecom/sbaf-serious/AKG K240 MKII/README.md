# AKG K240 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.1; 22 5.3; 23 5.0; 25 4.3; 26 3.9; 28 3.4; 30 2.8; 32 2.4; 35 1.7; 37 1.3; 40 0.8; 42 0.6; 45 0.3; 49 -0.1; 52 -0.5; 56 -0.7; 59 -0.5; 64 -0.4; 68 -1.1; 73 -2.2; 78 -2.9; 83 -3.5; 89 -4.0; 95 -4.7; 102 -5.2; 109 -5.6; 117 -6.1; 125 -6.5; 134 -6.8; 143 -6.9; 153 -6.7; 164 -6.4; 175 -6.4; 188 -6.1; 201 -5.9; 215 -5.5; 230 -5.2; 246 -4.8; 263 -4.7; 282 -4.6; 301 -4.5; 323 -4.4; 345 -4.0; 369 -3.8; 395 -3.6; 423 -3.4; 452 -3.3; 484 -3.4; 518 -1.1; 554 -0.2; 593 -0.9; 635 -1.0; 679 -1.1; 726 -0.9; 777 -0.7; 832 -0.5; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.6; 1336 0.2; 1429 -0.4; 1529 -0.9; 1636 -1.5; 1751 -2.3; 1873 -2.9; 2004 -2.9; 2145 -3.9; 2295 -3.8; 2455 -3.4; 2627 -2.1; 2811 -1.3; 3008 -0.3; 3219 1.0; 3444 1.7; 3685 1.7; 3943 0.8; 4219 -0.3; 4514 -1.0; 4830 -0.7; 5168 1.2; 5530 2.1; 5917 1.2; 6331 -0.1; 6775 -1.8; 7249 -2.9; 7756 -5.4; 8299 -8.3; 8880 -9.9; 9502 -8.9; 10167 -5.9; 10879 -2.7; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.25 | 6.8 dB   |
| Peaking | 157 Hz  | 0.48 | -6.9 dB  |
| Peaking | 2180 Hz | 1.82 | -6.0 dB  |
| Peaking | 4165 Hz | 0.23 | 2.5 dB   |
| Peaking | 8915 Hz | 2.53 | -12.6 dB |
| Peaking | 61 Hz   | 6.55 | 1.5 dB   |
| Peaking | 452 Hz  | 8.09 | -1.1 dB  |
| Peaking | 3574 Hz | 4.18 | 2.4 dB   |
| Peaking | 4719 Hz | 2.18 | -3.5 dB  |
| Peaking | 5488 Hz | 4.36 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K240%20MKII/AKG%20K240%20MKII.png)