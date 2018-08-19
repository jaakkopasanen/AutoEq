# Grado PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.2; 32 4.5; 35 3.6; 37 3.0; 40 2.2; 42 1.7; 45 1.0; 49 0.0; 52 -0.6; 56 -1.4; 59 -1.9; 64 -2.6; 68 -3.1; 73 -3.6; 78 -3.9; 83 -4.0; 89 -4.3; 95 -4.6; 102 -4.7; 109 -4.6; 117 -4.5; 125 -4.4; 134 -4.2; 143 -4.0; 153 -3.8; 164 -3.5; 175 -3.2; 188 -3.0; 201 -2.8; 215 -2.5; 230 -2.3; 246 -2.0; 263 -1.7; 282 -1.4; 301 -1.1; 323 -0.7; 345 -0.5; 369 -0.2; 395 0.1; 423 0.2; 452 0.3; 484 0.5; 518 0.7; 554 0.8; 593 1.0; 635 1.1; 679 0.9; 726 0.9; 777 0.9; 832 0.7; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.3; 1167 -0.6; 1248 -1.2; 1336 -1.9; 1429 -2.7; 1529 -3.5; 1636 -3.8; 1751 -2.9; 1873 -2.8; 2004 -4.3; 2145 -5.2; 2295 -1.6; 2455 0.5; 2627 2.3; 2811 4.5; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.9; 3943 3.9; 4219 4.3; 4514 4.4; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -2.5; 9502 -4.1; 10167 -1.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.95 | 6.9 dB  |
| Peaking | 100 Hz  | 0.75 | -5.4 dB |
| Peaking | 2056 Hz | 1.85 | -7.1 dB |
| Peaking | 3086 Hz | 1.72 | 8.0 dB  |
| Peaking | 5572 Hz | 2.98 | 5.8 dB  |
| Peaking | 225 Hz  | 1.76 | -0.8 dB |
| Peaking | 627 Hz  | 0.91 | 1.4 dB  |
| Peaking | 1474 Hz | 5.48 | -1.9 dB |
| Peaking | 6516 Hz | 9.76 | 2.0 dB  |
| Peaking | 9386 Hz | 5.67 | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS500/Grado%20PS500.png)