# Yuin G1A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.3; 56 4.5; 59 3.9; 64 2.9; 68 2.3; 73 1.8; 78 1.5; 83 0.9; 89 0.1; 95 -0.4; 102 -1.0; 109 -1.4; 117 -1.7; 125 -2.1; 134 -2.3; 143 -2.5; 153 -2.8; 164 -2.7; 175 -2.7; 188 -2.6; 201 -2.6; 215 -2.5; 230 -2.3; 246 -2.1; 263 -2.1; 282 -2.0; 301 -1.7; 323 -1.4; 345 -1.2; 369 -0.9; 395 -0.8; 423 -0.5; 452 -0.4; 484 -0.3; 518 0.0; 554 0.1; 593 0.1; 635 0.2; 679 0.4; 726 0.5; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.4; 1167 -0.4; 1248 -0.5; 1336 -1.0; 1429 -0.8; 1529 -1.4; 1636 -2.5; 1751 -3.1; 1873 -3.7; 2004 -4.3; 2145 -4.2; 2295 -4.2; 2455 -3.7; 2627 -2.1; 2811 0.2; 3008 2.4; 3219 5.9; 3444 6.0; 3685 6.0; 3943 3.9; 4219 -0.9; 4514 -5.9; 4830 -8.5; 5168 -4.9; 5530 -1.5; 5917 2.2; 6331 5.2; 6775 2.8; 7249 0.6; 7756 -0.2; 8299 -1.1; 8880 -2.9; 9502 -4.2; 10167 -2.7; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 1.17 | 7.3 dB   |
| Peaking | 2241 Hz | 1.8  | -6.2 dB  |
| Peaking | 3573 Hz | 2.34 | 10.9 dB  |
| Peaking | 4749 Hz | 3.39 | -11.9 dB |
| Peaking | 6281 Hz | 6.65 | 7.2 dB   |
| Peaking | 20 Hz   | 2.73 | 2.6 dB   |
| Peaking | 55 Hz   | 2.07 | 2.7 dB   |
| Peaking | 173 Hz  | 0.77 | -3.1 dB  |
| Peaking | 730 Hz  | 1.41 | 1.0 dB   |
| Peaking | 9475 Hz | 5.73 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G1A/Yuin%20G1A.png)