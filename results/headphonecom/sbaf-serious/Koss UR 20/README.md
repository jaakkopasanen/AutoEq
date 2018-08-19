# Koss UR 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.3; 56 4.4; 59 3.8; 64 3.1; 68 3.0; 73 3.2; 78 3.0; 83 2.5; 89 1.9; 95 1.4; 102 0.9; 109 0.5; 117 0.1; 125 -0.1; 134 -0.4; 143 -0.9; 153 -1.2; 164 -1.2; 175 -1.4; 188 -1.8; 201 -1.9; 215 -2.1; 230 -2.1; 246 -2.2; 263 -2.9; 282 -3.6; 301 -4.2; 323 -5.1; 345 -5.9; 369 -6.8; 395 -7.8; 423 -8.7; 452 -9.0; 484 -9.4; 518 -10.1; 554 -10.0; 593 -9.2; 635 -7.2; 679 -4.8; 726 -2.9; 777 -1.1; 832 -1.8; 890 -2.8; 952 -1.4; 1019 0.5; 1090 2.3; 1167 3.9; 1248 5.0; 1336 6.0; 1429 6.0; 1529 6.0; 1636 6.0; 1751 5.8; 1873 3.3; 2004 0.4; 2145 -1.8; 2295 0.3; 2455 1.5; 2627 1.1; 2811 2.7; 3008 5.5; 3219 6.0; 3444 6.0; 3685 1.5; 3943 -0.1; 4219 1.5; 4514 -1.3; 4830 -0.8; 5168 0.8; 5530 -2.3; 5917 -5.1; 6331 -3.4; 6775 -1.9; 7249 -2.7; 7756 -3.6; 8299 -4.2; 8880 -4.0; 9502 -2.7; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.67 | 6.7 dB   |
| Peaking | 488 Hz   | 1.14 | -10.4 dB |
| Peaking | 1396 Hz  | 1.99 | 8.1 dB   |
| Peaking | 3249 Hz  | 5.01 | 7.1 dB   |
| Peaking | 7280 Hz  | 1.37 | -3.8 dB  |
| Peaking | 759 Hz   | 5.38 | 5.2 dB   |
| Peaking | 768 Hz   | 2.31 | -2.6 dB  |
| Peaking | 1733 Hz  | 7.55 | 2.6 dB   |
| Peaking | 2113 Hz  | 8.72 | -3.9 dB  |
| Peaking | 11160 Hz | 4.92 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2020/Koss%20UR%2020.png)