# Shure SE310

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.3; 22 5.3; 23 5.2; 25 5.2; 26 5.2; 28 5.1; 30 5.0; 32 4.9; 35 4.8; 37 4.8; 40 4.6; 42 4.5; 45 4.3; 49 4.1; 52 4.0; 56 3.8; 59 3.7; 64 3.4; 68 3.1; 73 2.8; 78 2.6; 83 2.4; 89 2.1; 95 1.9; 102 1.7; 109 1.6; 117 1.4; 125 1.2; 134 1.0; 143 0.8; 153 0.6; 164 0.5; 175 0.4; 188 0.3; 201 0.2; 215 0.2; 230 0.2; 246 0.1; 263 0.1; 282 0.2; 301 0.2; 323 0.3; 345 0.5; 369 0.6; 395 0.6; 423 0.7; 452 1.0; 484 1.1; 518 1.2; 554 1.3; 593 1.4; 635 1.4; 679 1.5; 726 1.4; 777 1.3; 832 1.2; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.7; 1336 -2.4; 1429 -3.1; 1529 -3.6; 1636 -4.1; 1751 -4.2; 1873 -4.1; 2004 -3.8; 2145 -3.2; 2295 -2.1; 2455 -0.7; 2627 1.2; 2811 3.3; 3008 5.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 4.6; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998308317dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE310 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.65 | 4.2 dB  |
| Peaking | 41 Hz   | 0.54 | 3.5 dB  |
| Peaking | 1905 Hz | 1.8  | -6.2 dB |
| Peaking | 3424 Hz | 1.64 | 7.1 dB  |
| Peaking | 5730 Hz | 3.04 | 5.2 dB  |
| Peaking | 693 Hz  | 1.39 | 1.8 dB  |
| Peaking | 1236 Hz | 4.06 | -0.7 dB |
| Peaking | 1453 Hz | 5.94 | -1.0 dB |
| Peaking | 6594 Hz | 7.89 | 2.1 dB  |
| Peaking | 7838 Hz | 2.29 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE310/Shure%20SE310.png)