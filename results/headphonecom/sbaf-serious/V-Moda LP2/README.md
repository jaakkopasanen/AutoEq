# V-Moda LP2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.2; 22 -2.7; 23 -2.9; 25 -3.3; 26 -3.5; 28 -3.7; 30 -3.9; 32 -4.1; 35 -4.3; 37 -4.4; 40 -4.6; 42 -4.7; 45 -4.8; 49 -4.9; 52 -4.9; 56 -5.0; 59 -5.1; 64 -5.3; 68 -5.3; 73 -5.2; 78 -4.9; 83 -4.7; 89 -5.1; 95 -6.1; 102 -6.6; 109 -6.9; 117 -6.9; 125 -6.7; 134 -6.9; 143 -7.0; 153 -7.0; 164 -6.5; 175 -6.6; 188 -6.5; 201 -6.0; 215 -5.4; 230 -4.7; 246 -3.7; 263 -3.0; 282 -2.4; 301 -1.0; 323 0.6; 345 1.9; 369 2.7; 395 3.4; 423 4.0; 452 4.6; 484 5.0; 518 5.3; 554 5.2; 593 4.6; 635 3.7; 679 2.5; 726 1.5; 777 0.7; 832 0.3; 890 -0.1; 952 -0.0; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 0.1; 1336 -0.2; 1429 -0.2; 1529 -0.2; 1636 -0.1; 1751 0.3; 1873 0.8; 2004 1.1; 2145 1.2; 2295 -0.0; 2455 -0.8; 2627 -0.9; 2811 -1.7; 3008 -2.2; 3219 -1.2; 3444 0.5; 3685 1.8; 3943 3.3; 4219 4.4; 4514 5.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.5; 10167 -1.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099810366727418dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.64 | -3.6 dB |
| Peaking | 158 Hz  | 0.64 | -7.0 dB |
| Peaking | 462 Hz  | 1.46 | 7.4 dB  |
| Peaking | 5314 Hz | 2.38 | 7.1 dB  |
| Peaking | 603 Hz  | 4.68 | 1.8 dB  |
| Peaking | 892 Hz  | 1.12 | -1.1 dB |
| Peaking | 2987 Hz | 2.92 | -5.7 dB |
| Peaking | 3236 Hz | 1.15 | 2.8 dB  |
| Peaking | 9487 Hz | 2.23 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20LP2/V-Moda%20LP2.png)