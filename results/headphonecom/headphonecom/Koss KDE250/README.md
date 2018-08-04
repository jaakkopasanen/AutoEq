# Koss KDE250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 5.5; 125 5.0; 134 4.6; 143 4.1; 153 3.7; 164 3.4; 175 3.0; 188 2.6; 201 2.3; 215 1.9; 230 1.6; 246 1.1; 263 0.7; 282 0.4; 301 0.3; 323 0.1; 345 -0.1; 369 -0.2; 395 0.0; 423 0.1; 452 0.3; 484 0.7; 518 0.9; 554 1.0; 593 1.2; 635 1.3; 679 1.3; 726 1.3; 777 1.2; 832 1.0; 890 0.8; 952 0.4; 1019 -0.0; 1090 -0.4; 1167 -0.7; 1248 -1.0; 1336 -1.4; 1429 -2.0; 1529 -3.0; 1636 -4.1; 1751 -5.0; 1873 -6.1; 2004 -7.7; 2145 -9.9; 2295 -12.3; 2455 -13.1; 2627 -11.8; 2811 -10.6; 3008 -9.2; 3219 -5.8; 3444 -1.8; 3685 1.7; 3943 4.2; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.8; 6331 3.4; 6775 -0.5; 7249 -4.4; 7756 -6.9; 8299 -7.3; 8880 -5.6; 9502 -3.1; 10167 -1.4; 10879 -1.0; 11640 -1.3; 12455 -0.7; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KDE250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.34 | 6.7 dB   |
| Peaking | 960 Hz   | 1.15 | 2.2 dB   |
| Peaking | 2581 Hz  | 1.42 | -18.5 dB |
| Peaking | 4745 Hz  | 0.98 | 13.5 dB  |
| Peaking | 8043 Hz  | 2.4  | -11.9 dB |
| Peaking | 21 Hz    | 2.46 | 1.3 dB   |
| Peaking | 112 Hz   | 3.28 | 1.2 dB   |
| Peaking | 364 Hz   | 4.67 | -1.0 dB  |
| Peaking | 280 Hz   | 3.17 | -1.0 dB  |
| Peaking | 36092 Hz | 6.04 | -0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Koss%20KDE250/Koss%20KDE250.png)