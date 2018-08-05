# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.5; 22 0.5; 23 0.4; 25 0.3; 26 0.3; 28 0.2; 30 0.2; 32 0.1; 35 0.1; 37 0.2; 40 0.2; 42 0.2; 45 0.2; 49 0.3; 52 0.3; 56 0.3; 59 0.3; 64 0.3; 68 0.2; 73 0.2; 78 0.1; 83 0.1; 89 0.2; 95 0.3; 102 -0.3; 109 -0.8; 117 -0.9; 125 -0.9; 134 -0.1; 143 -0.2; 153 -1.5; 164 -1.5; 175 -0.8; 188 -2.0; 201 -2.5; 215 -2.7; 230 -2.7; 246 -2.7; 263 -2.5; 282 -2.3; 301 -2.2; 323 -2.1; 345 -1.9; 369 -1.8; 395 -1.6; 423 -1.3; 452 -1.3; 484 -1.4; 518 -1.6; 554 -1.5; 593 -1.4; 635 -1.4; 679 -1.5; 726 -1.4; 777 -1.1; 832 -1.0; 890 -0.8; 952 -0.3; 1019 0.0; 1090 -0.2; 1167 -0.6; 1248 -0.6; 1336 -0.8; 1429 -0.8; 1529 -1.0; 1636 -1.0; 1751 -0.6; 1873 0.3; 2004 1.5; 2145 2.0; 2295 2.9; 2455 4.1; 2627 4.9; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.7; 8299 -6.0; 8880 -8.0; 9502 -7.0; 10167 -3.6; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 240 Hz   | 1.46 | -2.6 dB  |
| Peaking | 642 Hz   | 0.96 | -1.7 dB  |
| Peaking | 1633 Hz  | 2.02 | -3.7 dB  |
| Peaking | 4586 Hz  | 0.5  | 7.5 dB   |
| Peaking | 8929 Hz  | 2.88 | -13.2 dB |
| Peaking | 59 Hz    | 1.29 | 0.4 dB   |
| Peaking | 2926 Hz  | 3.28 | 1.4 dB   |
| Peaking | 4204 Hz  | 0.99 | -1.0 dB  |
| Peaking | 6234 Hz  | 4.35 | 2.0 dB   |
| Peaking | 15301 Hz | 1.84 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)