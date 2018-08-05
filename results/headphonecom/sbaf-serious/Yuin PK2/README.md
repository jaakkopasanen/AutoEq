# Yuin PK2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.3; 95 4.5; 102 3.7; 109 3.3; 117 2.8; 125 2.3; 134 1.9; 143 1.6; 153 1.4; 164 1.2; 175 1.2; 188 1.0; 201 1.0; 215 1.1; 230 1.0; 246 1.0; 263 1.0; 282 1.1; 301 1.2; 323 1.3; 345 1.5; 369 1.6; 395 1.2; 423 1.1; 452 1.3; 484 1.6; 518 1.6; 554 1.6; 593 1.7; 635 1.5; 679 1.2; 726 1.0; 777 1.0; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.3; 1529 -3.2; 1636 -4.1; 1751 -4.9; 1873 -5.4; 2004 -5.7; 2145 -5.8; 2295 -5.5; 2455 -4.6; 2627 -3.7; 2811 -2.5; 3008 -0.9; 3219 0.1; 3444 0.9; 3685 0.8; 3943 -0.1; 4219 -2.1; 4514 -3.9; 4830 -4.5; 5168 -4.5; 5530 -4.7; 5917 -4.6; 6331 -3.1; 6775 -1.1; 7249 -0.1; 7756 -0.9; 8299 -2.7; 8880 -3.7; 9502 -2.9; 10167 -0.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.44 | 6.7 dB   |
| Peaking | 2566 Hz | 0.37 | 8.1 dB   |
| Peaking | 2033 Hz | 1.01 | -13.6 dB |
| Peaking | 5288 Hz | 2.06 | -8.5 dB  |
| Peaking | 9013 Hz | 3.75 | -4.9 dB  |
| Peaking | 15 Hz   | 1.03 | 2.1 dB   |
| Peaking | 41 Hz   | 1.33 | -1.2 dB  |
| Peaking | 80 Hz   | 3.03 | 1.6 dB   |
| Peaking | 147 Hz  | 1.97 | -1.0 dB  |
| Peaking | 3513 Hz | 7.65 | 1.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)