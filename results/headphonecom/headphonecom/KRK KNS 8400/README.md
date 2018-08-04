# KRK KNS 8400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 -12.2; 22 -12.1; 23 -12.0; 25 -11.8; 26 -11.7; 28 -11.5; 30 -11.3; 32 -11.1; 35 -10.6; 37 -10.2; 40 -9.7; 42 -9.3; 45 -8.7; 49 -7.8; 52 -7.0; 56 -6.0; 59 -5.4; 64 -4.9; 68 -5.1; 73 -6.0; 78 -7.3; 83 -8.7; 89 -10.2; 95 -11.3; 102 -12.7; 109 -13.6; 117 -13.7; 125 -12.3; 134 -10.9; 143 -12.4; 153 -12.0; 164 -10.4; 175 -11.5; 188 -11.0; 201 -9.8; 215 -8.7; 230 -7.5; 246 -6.3; 263 -5.0; 282 -4.3; 301 -3.4; 323 -2.2; 345 -1.2; 369 -0.2; 395 0.8; 423 1.6; 452 2.0; 484 1.9; 518 1.5; 554 0.6; 593 -0.0; 635 -0.0; 679 0.0; 726 0.7; 777 1.2; 832 -0.4; 890 -0.4; 952 -0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.3; 1336 -0.4; 1429 -0.1; 1529 -0.3; 1636 -0.8; 1751 -0.9; 1873 -1.7; 2004 -1.6; 2145 -2.1; 2295 -2.3; 2455 -2.4; 2627 -2.4; 2811 -2.1; 3008 -0.9; 3219 -1.3; 3444 -2.0; 3685 -1.4; 3943 -1.7; 4219 -0.8; 4514 1.5; 4830 4.3; 5168 5.0; 5530 3.6; 5917 1.8; 6331 -1.3; 6775 -1.5; 7249 0.6; 7756 0.1; 8299 -2.6; 8880 -4.8; 9502 -2.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -4.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 22 Hz   |  1.16 | -10.9 dB |
| Peaking | 36 Hz   |  1.93 | -4.9 dB  |
| Peaking | 129 Hz  |  0.99 | -13.3 dB |
| Peaking | 5131 Hz |  2.92 | 10.1 dB  |
| Peaking | 4910 Hz |  0.78 | -4.8 dB  |
| Peaking | 105 Hz  |  2.33 | -6.7 dB  |
| Peaking | 127 Hz  |  1.12 | 7.8 dB   |
| Peaking | 189 Hz  |  1.45 | -6.3 dB  |
| Peaking | 450 Hz  |  1.96 | 3.8 dB   |
| Peaking | 8889 Hz | 12.14 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/KRK%20KNS%208400/KRK%20KNS%208400.png)