# KRK KNS 8400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -11.7; 22 -11.5; 23 -11.5; 25 -11.3; 26 -11.2; 28 -11.0; 30 -10.8; 32 -10.5; 35 -10.0; 37 -9.7; 40 -9.1; 42 -8.7; 45 -8.1; 49 -7.2; 52 -6.4; 56 -5.4; 59 -4.8; 64 -4.4; 68 -4.5; 73 -5.4; 78 -6.7; 83 -8.0; 89 -9.4; 95 -10.4; 102 -11.7; 109 -12.4; 117 -12.5; 125 -11.1; 134 -9.6; 143 -11.1; 153 -10.7; 164 -9.0; 175 -10.2; 188 -9.7; 201 -8.5; 215 -7.4; 230 -6.1; 246 -4.9; 263 -3.7; 282 -2.9; 301 -2.0; 323 -0.9; 345 0.2; 369 1.1; 395 2.0; 423 2.8; 452 3.0; 484 2.7; 518 2.0; 554 1.1; 593 0.5; 635 0.3; 679 0.1; 726 0.7; 777 1.4; 832 -0.3; 890 -0.4; 952 -0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.9; 1336 -1.7; 1429 -2.2; 1529 -3.0; 1636 -3.8; 1751 -4.0; 1873 -4.7; 2004 -4.5; 2145 -5.2; 2295 -5.3; 2455 -5.3; 2627 -5.4; 2811 -5.0; 3008 -3.4; 3219 -3.6; 3444 -4.1; 3685 -3.5; 3943 -4.1; 4219 -4.5; 4514 -3.3; 4830 -1.2; 5168 -0.4; 5530 -1.1; 5917 -1.7; 6331 -3.5; 6775 -2.9; 7249 -0.4; 7756 -0.8; 8299 -4.1; 8880 -6.7; 9502 -4.9; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.3; 14260 -1.6; 15258 -1.8; 16326 -2.2; 17469 -3.7; 18692 -7.0; 20000 -12.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.1  | -10.5 dB |
| Peaking | 37 Hz   | 1.96 | -4.5 dB  |
| Peaking | 127 Hz  | 1.09 | -12.1 dB |
| Peaking | 2603 Hz | 1.07 | -5.5 dB  |
| Peaking | 8954 Hz | 6.06 | -7.0 dB  |
| Peaking | 102 Hz  | 4.54 | -1.7 dB  |
| Peaking | 132 Hz  | 7.07 | 3.3 dB   |
| Peaking | 202 Hz  | 2.77 | -3.1 dB  |
| Peaking | 432 Hz  | 2.2  | 4.6 dB   |
| Peaking | 775 Hz  | 6.21 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20KNS%208400/KRK%20KNS%208400.png)