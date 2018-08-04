# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -10.5; 22 -10.4; 23 -10.4; 25 -10.3; 26 -10.3; 28 -10.2; 30 -10.1; 32 -10.0; 35 -9.8; 37 -9.7; 40 -9.6; 42 -9.4; 45 -9.3; 49 -9.0; 52 -8.9; 56 -8.6; 59 -8.4; 64 -8.1; 68 -7.8; 73 -7.4; 78 -7.1; 83 -6.7; 89 -6.1; 95 -5.6; 102 -5.1; 109 -4.8; 117 -5.0; 125 -6.2; 134 -7.1; 143 -7.1; 153 -6.3; 164 -5.1; 175 -4.7; 188 -5.8; 201 -5.9; 215 -5.6; 230 -5.3; 246 -4.8; 263 -4.4; 282 -3.8; 301 -3.2; 323 -2.4; 345 -1.9; 369 -2.2; 395 -1.8; 423 -1.4; 452 -1.3; 484 -1.3; 518 -1.1; 554 -0.7; 593 -0.3; 635 -0.1; 679 -0.1; 726 -0.1; 777 -0.4; 832 -0.8; 890 -0.8; 952 -0.5; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.7; 1336 -2.7; 1429 -3.4; 1529 -3.8; 1636 -3.7; 1751 -3.3; 1873 -2.1; 2004 -1.7; 2145 -1.0; 2295 -0.1; 2455 0.9; 2627 1.7; 2811 2.6; 3008 2.9; 3219 2.7; 3444 2.3; 3685 1.7; 3943 1.0; 4219 -1.0; 4514 -2.6; 4830 -2.7; 5168 -0.2; 5530 2.0; 5917 2.6; 6331 3.3; 6775 2.8; 7249 1.3; 7756 0.2; 8299 -1.1; 8880 -1.8; 9502 -1.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 1.34 | -10.2 dB |
| Peaking | 23 Hz   | 0.76 | -6.9 dB  |
| Peaking | 53 Hz   | 0.72 | -6.0 dB  |
| Peaking | 186 Hz  | 0.92 | -4.8 dB  |
| Peaking | 1561 Hz | 3.72 | -4.3 dB  |
| Peaking | 107 Hz  | 7.6  | 0.8 dB   |
| Peaking | 3121 Hz | 3.07 | 3.3 dB   |
| Peaking | 4704 Hz | 4.94 | -4.7 dB  |
| Peaking | 6189 Hz | 2.32 | 3.9 dB   |
| Peaking | 8696 Hz | 3.86 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)