# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.1; 23 -4.1; 25 -4.2; 26 -4.2; 28 -4.3; 30 -4.4; 32 -4.4; 35 -4.4; 37 -4.4; 40 -4.4; 42 -4.4; 45 -4.4; 49 -4.3; 52 -4.2; 56 -4.2; 59 -4.2; 64 -4.2; 68 -4.2; 73 -4.2; 78 -4.2; 83 -4.1; 89 -3.8; 95 -3.5; 102 -3.8; 109 -3.9; 117 -3.8; 125 -3.4; 134 -2.2; 143 -2.1; 153 -3.2; 164 -3.1; 175 -2.4; 188 -3.5; 201 -4.0; 215 -4.1; 230 -4.1; 246 -4.1; 263 -3.9; 282 -3.7; 301 -3.6; 323 -3.5; 345 -3.3; 369 -3.2; 395 -2.8; 423 -2.5; 452 -2.3; 484 -2.1; 518 -2.1; 554 -2.0; 593 -1.9; 635 -1.7; 679 -1.6; 726 -1.4; 777 -1.2; 832 -1.1; 890 -0.8; 952 -0.3; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 0.1; 1336 0.6; 1429 1.3; 1529 1.6; 1636 2.0; 1751 2.5; 1873 3.2; 2004 4.5; 2145 5.0; 2295 5.8; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.8; 8299 -4.5; 8880 -6.1; 9502 -4.4; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.61 | -4.0 dB  |
| Peaking | 70 Hz   | 1.14 | -1.7 dB  |
| Peaking | 314 Hz  | 0.33 | -3.3 dB  |
| Peaking | 3999 Hz | 0.5  | 7.2 dB   |
| Peaking | 8809 Hz | 3.33 | -10.1 dB |
| Peaking | 233 Hz  | 5.26 | -0.9 dB  |
| Peaking | 1265 Hz | 4.96 | -0.8 dB  |
| Peaking | 2371 Hz | 3.36 | 1.8 dB   |
| Peaking | 6117 Hz | 3.29 | 2.3 dB   |
| Peaking | 4984 Hz | 0.55 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Teac%20CT-H02/Teac%20CT-H02.png)