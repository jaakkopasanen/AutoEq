# Shure SE315

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.4; 22 4.3; 23 4.3; 25 4.2; 26 4.2; 28 4.2; 30 4.2; 32 4.1; 35 4.0; 37 3.9; 40 3.8; 42 3.7; 45 3.6; 49 3.4; 52 3.3; 56 3.1; 59 3.0; 64 2.7; 68 2.5; 73 2.3; 78 2.1; 83 1.9; 89 1.7; 95 1.5; 102 1.3; 109 1.1; 117 0.9; 125 0.9; 134 0.7; 143 0.5; 153 0.4; 164 0.2; 175 0.2; 188 0.3; 201 0.2; 215 0.2; 230 0.1; 246 0.3; 263 0.3; 282 0.4; 301 0.4; 323 0.6; 345 0.9; 369 1.0; 395 1.1; 423 1.1; 452 1.2; 484 1.3; 518 1.4; 554 1.5; 593 1.7; 635 1.8; 679 1.7; 726 1.7; 777 1.6; 832 1.3; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.9; 1336 -2.6; 1429 -3.4; 1529 -4.1; 1636 -4.6; 1751 -4.7; 1873 -4.1; 2004 -3.0; 2145 -1.4; 2295 0.8; 2455 3.0; 2627 5.3; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999938477dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.65 | 4.1 dB  |
| Peaking | 57 Hz   | 1.02 | 1.7 dB  |
| Peaking | 664 Hz  | 1.15 | 2.0 dB  |
| Peaking | 1751 Hz | 1.49 | -9.2 dB |
| Peaking | 3308 Hz | 0.77 | 8.6 dB  |
| Peaking | 2146 Hz | 5.91 | -0.8 dB |
| Peaking | 2646 Hz | 5.31 | 1.8 dB  |
| Peaking | 3583 Hz | 2.95 | -1.2 dB |
| Peaking | 6269 Hz | 2.24 | 5.4 dB  |
| Peaking | 7406 Hz | 1.47 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE315/Shure%20SE315.png)