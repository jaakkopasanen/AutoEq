# Grado iGi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.3; 22 2.9; 23 2.7; 25 2.4; 26 2.2; 28 2.0; 30 1.7; 32 1.5; 35 1.3; 37 1.1; 40 0.9; 42 0.7; 45 0.5; 49 0.3; 52 0.1; 56 -0.2; 59 -0.4; 64 -0.7; 68 -0.8; 73 -0.9; 78 -1.1; 83 -1.3; 89 -1.4; 95 -1.5; 102 -1.6; 109 -1.6; 117 -1.6; 125 -1.7; 134 -1.7; 143 -1.7; 153 -1.7; 164 -1.7; 175 -1.5; 188 -1.4; 201 -1.3; 215 -1.0; 230 -0.8; 246 -0.6; 263 -0.4; 282 -0.1; 301 0.2; 323 0.4; 345 0.7; 369 0.8; 395 1.1; 423 1.2; 452 1.4; 484 1.5; 518 1.6; 554 1.7; 593 1.9; 635 2.0; 679 1.9; 726 1.9; 777 1.7; 832 1.5; 890 1.1; 952 0.5; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.3; 1336 -1.5; 1429 -1.3; 1529 -1.3; 1636 -2.0; 1751 -1.7; 1873 -0.7; 2004 0.8; 2145 2.6; 2295 4.7; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.8; 6331 1.0; 6775 1.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999997779dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.61 | 3.7 dB  |
| Peaking | 127 Hz  | 0.62 | -2.1 dB |
| Peaking | 576 Hz  | 0.9  | 2.2 dB  |
| Peaking | 1605 Hz | 1.42 | -5.7 dB |
| Peaking | 3121 Hz | 0.8  | 7.9 dB  |
| Peaking | 1952 Hz | 5.45 | -1.0 dB |
| Peaking | 2410 Hz | 3.96 | 1.8 dB  |
| Peaking | 3163 Hz | 3.34 | -1.1 dB |
| Peaking | 5390 Hz | 2.88 | 4.5 dB  |
| Peaking | 6636 Hz | 1.13 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGi/Grado%20iGi.png)