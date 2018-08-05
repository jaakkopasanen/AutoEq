# Shure SE315

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.5; 22 4.4; 23 4.4; 25 4.3; 26 4.3; 28 4.4; 30 4.4; 32 4.3; 35 4.3; 37 4.2; 40 4.2; 42 4.2; 45 4.2; 49 4.2; 52 4.1; 56 4.1; 59 4.1; 64 4.0; 68 3.9; 73 3.9; 78 3.7; 83 3.5; 89 3.2; 95 2.8; 102 2.3; 109 1.8; 117 1.3; 125 0.9; 134 0.4; 143 0.1; 153 -0.1; 164 -0.3; 175 -0.3; 188 -0.2; 201 -0.3; 215 -0.2; 230 -0.2; 246 0.0; 263 0.1; 282 0.2; 301 0.3; 323 0.4; 345 0.8; 369 0.9; 395 1.0; 423 1.1; 452 1.2; 484 1.2; 518 1.2; 554 1.5; 593 1.8; 635 1.9; 679 1.6; 726 1.6; 777 1.6; 832 1.3; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.9; 1336 -2.6; 1429 -3.4; 1529 -4.1; 1636 -4.6; 1751 -4.7; 1873 -4.1; 2004 -3.0; 2145 -1.4; 2295 0.7; 2455 3.1; 2627 5.3; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.71 | 4.5 dB  |
| Peaking | 72 Hz   | 1.69 | 2.9 dB  |
| Peaking | 673 Hz  | 1.4  | 2.0 dB  |
| Peaking | 1753 Hz | 1.53 | -9.1 dB |
| Peaking | 3321 Hz | 0.77 | 8.5 dB  |
| Peaking | 174 Hz  | 2.59 | -1.0 dB |
| Peaking | 2715 Hz | 5.42 | 2.4 dB  |
| Peaking | 3294 Hz | 1.47 | -1.3 dB |
| Peaking | 6259 Hz | 2.06 | 6.1 dB  |
| Peaking | 7362 Hz | 1.47 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE315/Shure%20SE315.png)