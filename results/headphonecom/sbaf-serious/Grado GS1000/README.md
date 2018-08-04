# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.4; 37 4.8; 40 4.1; 42 3.8; 45 3.0; 49 1.5; 52 0.4; 56 -0.7; 59 -1.4; 64 -2.5; 68 -3.3; 73 -4.1; 78 -4.9; 83 -5.5; 89 -6.2; 95 -6.7; 102 -7.1; 109 -7.3; 117 -7.3; 125 -7.3; 134 -7.1; 143 -6.8; 153 -6.5; 164 -6.0; 175 -5.4; 188 -4.9; 201 -4.4; 215 -3.8; 230 -3.3; 246 -2.8; 263 -2.4; 282 -2.5; 301 -2.4; 323 -2.1; 345 -1.7; 369 -1.5; 395 -1.2; 423 -0.9; 452 -0.8; 484 -0.8; 518 -0.8; 554 -0.5; 593 -0.1; 635 0.1; 679 0.1; 726 0.2; 777 0.3; 832 0.3; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.5; 1429 -0.8; 1529 -1.2; 1636 -0.8; 1751 -0.7; 1873 -1.3; 2004 -1.2; 2145 -1.5; 2295 -1.2; 2455 -1.0; 2627 -1.2; 2811 -1.4; 3008 -1.2; 3219 -1.0; 3444 -1.4; 3685 -5.0; 3943 -5.1; 4219 -3.4; 4514 -3.9; 4830 -6.1; 5168 -6.8; 5530 -7.5; 5917 -8.3; 6331 -9.8; 6775 -10.3; 7249 -10.0; 7756 -9.4; 8299 -8.6; 8880 -7.7; 9502 -6.7; 10167 -4.9; 10879 -2.6; 11640 -0.9; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.3; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.65 | 8.0 dB   |
| Peaking | 106 Hz   | 0.66 | -8.9 dB  |
| Peaking | 800 Hz   | 1.01 | 0.8 dB   |
| Peaking | 1668 Hz  | 1.62 | -0.7 dB  |
| Peaking | 6896 Hz  | 1.26 | -10.7 dB |
| Peaking | 7 Hz     | 0.88 | 0.6 dB   |
| Peaking | 3394 Hz  | 5.3  | 1.9 dB   |
| Peaking | 3756 Hz  | 8.96 | -3.9 dB  |
| Peaking | 9641 Hz  | 2.74 | -3.4 dB  |
| Peaking | 11495 Hz | 1.25 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)