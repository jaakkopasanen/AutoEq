# Shure SE315

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.8; 22 5.7; 23 5.7; 25 5.6; 26 5.6; 28 5.5; 30 5.4; 32 5.4; 35 5.3; 37 5.2; 40 5.1; 42 5.0; 45 4.8; 49 4.7; 52 4.6; 56 4.4; 59 4.2; 64 4.0; 68 3.8; 73 3.5; 78 3.2; 83 3.0; 89 2.7; 95 2.4; 102 2.1; 109 2.0; 117 1.8; 125 1.6; 134 1.4; 143 1.3; 153 1.1; 164 0.9; 175 1.0; 188 0.9; 201 0.8; 215 0.9; 230 0.9; 246 0.9; 263 0.9; 282 1.1; 301 1.1; 323 1.2; 345 1.2; 369 1.4; 395 1.4; 423 1.6; 452 1.7; 484 1.6; 518 1.6; 554 1.9; 593 2.0; 635 2.0; 679 1.8; 726 1.7; 777 1.7; 832 1.3; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.3; 1248 -1.8; 1336 -2.6; 1429 -3.3; 1529 -4.1; 1636 -4.5; 1751 -4.6; 1873 -4.1; 2004 -3.1; 2145 -1.6; 2295 0.4; 2455 2.8; 2627 4.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.1; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999918781dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.38 | 5.7 dB  |
| Peaking | 668 Hz  | 0.85 | 2.4 dB  |
| Peaking | 1804 Hz | 1.29 | -8.7 dB |
| Peaking | 2974 Hz | 1.2  | 9.1 dB  |
| Peaking | 5602 Hz | 2.79 | 4.8 dB  |
| Peaking | 3308 Hz | 4.72 | -1.6 dB |
| Peaking | 3930 Hz | 1.62 | 1.6 dB  |
| Peaking | 6495 Hz | 5.15 | 3.7 dB  |
| Peaking | 6826 Hz | 1.43 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE315/Shure%20SE315.png)