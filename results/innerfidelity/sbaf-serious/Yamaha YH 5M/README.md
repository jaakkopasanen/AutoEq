# Yamaha YH 5M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.8; 78 5.6; 83 5.2; 89 4.8; 95 4.5; 102 4.2; 109 4.0; 117 3.8; 125 3.6; 134 3.1; 143 2.8; 153 2.7; 164 2.5; 175 2.3; 188 2.0; 201 1.9; 215 1.9; 230 1.8; 246 1.7; 263 1.5; 282 1.4; 301 1.4; 323 1.3; 345 1.1; 369 1.0; 395 0.9; 423 0.7; 452 0.7; 484 0.3; 518 0.0; 554 -0.1; 593 -0.1; 635 -0.4; 679 -0.9; 726 -1.2; 777 -1.4; 832 -1.5; 890 -0.9; 952 -0.2; 1019 0.1; 1090 1.5; 1167 3.1; 1248 4.6; 1336 5.8; 1429 6.0; 1529 6.0; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.9; 4830 4.8; 5168 3.8; 5530 4.4; 5917 4.5; 6331 2.0; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH 5M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.28 | 6.3 dB  |
| Peaking | 871 Hz  | 1.69 | -3.3 dB |
| Peaking | 1394 Hz | 1.86 | 4.7 dB  |
| Peaking | 2363 Hz | 1.05 | 4.4 dB  |
| Peaking | 4291 Hz | 1.33 | 4.2 dB  |
| Peaking | 71 Hz   | 4.55 | 0.6 dB  |
| Peaking | 6605 Hz | 2.56 | 2.4 dB  |
| Peaking | 7617 Hz | 1.58 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH%205M/Yamaha%20YH%205M.png)