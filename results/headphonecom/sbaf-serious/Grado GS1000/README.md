# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.3; 37 4.7; 40 4.0; 42 3.6; 45 2.8; 49 1.2; 52 0.1; 56 -1.0; 59 -1.8; 64 -3.0; 68 -3.9; 73 -4.8; 78 -5.6; 83 -6.3; 89 -7.0; 95 -7.4; 102 -7.6; 109 -7.8; 117 -7.6; 125 -7.3; 134 -6.9; 143 -6.6; 153 -6.2; 164 -5.7; 175 -5.2; 188 -4.7; 201 -4.2; 215 -3.7; 230 -3.2; 246 -2.8; 263 -2.3; 282 -2.5; 301 -2.4; 323 -2.1; 345 -1.7; 369 -1.4; 395 -1.1; 423 -0.9; 452 -0.9; 484 -0.8; 518 -0.7; 554 -0.5; 593 -0.3; 635 0.1; 679 0.2; 726 0.2; 777 0.2; 832 0.2; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.4; 1429 -0.8; 1529 -1.3; 1636 -0.8; 1751 -0.7; 1873 -1.3; 2004 -1.3; 2145 -1.4; 2295 -1.2; 2455 -1.1; 2627 -1.1; 2811 -1.3; 3008 -1.3; 3219 -0.9; 3444 -1.3; 3685 -4.9; 3943 -5.4; 4219 -3.4; 4514 -3.8; 4830 -6.0; 5168 -6.9; 5530 -7.5; 5917 -8.2; 6331 -9.8; 6775 -10.4; 7249 -10.1; 7756 -9.4; 8299 -8.4; 8880 -7.6; 9502 -6.9; 10167 -5.0; 10879 -2.4; 11640 -0.7; 12455 -0.2; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.4; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 31 Hz    |  0.6  | 8.5 dB   |
| Peaking | 98 Hz    |  0.65 | -9.9 dB  |
| Peaking | 789 Hz   |  1.16 | 0.8 dB   |
| Peaking | 1691 Hz  |  1.67 | -0.7 dB  |
| Peaking | 6892 Hz  |  1.27 | -10.7 dB |
| Peaking | 3371 Hz  |  5.82 | 1.8 dB   |
| Peaking | 3781 Hz  | 10.1  | -3.9 dB  |
| Peaking | 7092 Hz  |  5.5  | 0.4 dB   |
| Peaking | 9647 Hz  |  2.76 | -3.5 dB  |
| Peaking | 11550 Hz |  1.44 | 3.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)