# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.5; 23 -3.6; 25 -3.7; 26 -3.7; 28 -3.8; 30 -3.8; 32 -3.9; 35 -3.9; 37 -3.8; 40 -3.8; 42 -3.8; 45 -3.8; 49 -3.7; 52 -3.6; 56 -3.6; 59 -3.6; 64 -3.6; 68 -3.6; 73 -3.6; 78 -3.5; 83 -3.3; 89 -2.9; 95 -2.6; 102 -2.8; 109 -2.8; 117 -2.5; 125 -2.1; 134 -0.9; 143 -0.8; 153 -1.9; 164 -1.7; 175 -1.0; 188 -2.2; 201 -2.6; 215 -2.7; 230 -2.7; 246 -2.7; 263 -2.6; 282 -2.3; 301 -2.2; 323 -2.1; 345 -1.9; 369 -1.8; 395 -1.6; 423 -1.3; 452 -1.3; 484 -1.4; 518 -1.6; 554 -1.5; 593 -1.4; 635 -1.4; 679 -1.5; 726 -1.4; 777 -1.1; 832 -1.0; 890 -0.8; 952 -0.3; 1019 0.0; 1090 -0.2; 1167 -0.6; 1248 -0.6; 1336 -0.8; 1429 -0.8; 1529 -1.0; 1636 -1.0; 1751 -0.6; 1873 0.3; 2004 1.5; 2145 2.0; 2295 2.9; 2455 4.1; 2627 4.9; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.7; 8299 -6.0; 8880 -8.0; 9502 -7.0; 10167 -3.6; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 37 Hz   | 0.42 | -4.0 dB  |
| Peaking | 401 Hz  | 0.43 | -1.9 dB  |
| Peaking | 1637 Hz | 2.06 | -3.5 dB  |
| Peaking | 4573 Hz | 0.5  | 7.5 dB   |
| Peaking | 8929 Hz | 2.89 | -13.2 dB |
| Peaking | 142 Hz  | 8.89 | 1.6 dB   |
| Peaking | 230 Hz  | 4.61 | -0.9 dB  |
| Peaking | 2896 Hz | 3.4  | 1.4 dB   |
| Peaking | 5059 Hz | 0.83 | -1.2 dB  |
| Peaking | 6234 Hz | 3.37 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)