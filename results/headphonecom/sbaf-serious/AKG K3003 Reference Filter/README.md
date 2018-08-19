# AKG K3003 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.2; 22 2.7; 23 2.4; 25 2.0; 26 1.8; 28 1.4; 30 1.1; 32 0.8; 35 0.4; 37 0.2; 40 -0.2; 42 -0.4; 45 -0.7; 49 -1.0; 52 -1.3; 56 -1.6; 59 -1.8; 64 -2.2; 68 -2.4; 73 -2.8; 78 -3.1; 83 -3.3; 89 -3.6; 95 -3.8; 102 -4.0; 109 -4.1; 117 -4.3; 125 -4.5; 134 -4.6; 143 -4.7; 153 -4.9; 164 -4.8; 175 -4.9; 188 -4.8; 201 -4.7; 215 -4.6; 230 -4.5; 246 -4.4; 263 -4.2; 282 -3.9; 301 -3.7; 323 -3.3; 345 -3.0; 369 -2.6; 395 -2.3; 423 -2.0; 452 -1.8; 484 -1.6; 518 -1.2; 554 -0.9; 593 -0.5; 635 -0.2; 679 -0.0; 726 0.3; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -0.9; 1336 -1.0; 1429 -1.1; 1529 -1.6; 1636 -2.1; 1751 -2.4; 1873 -2.4; 2004 -2.3; 2145 -2.0; 2295 -1.5; 2455 -0.7; 2627 0.6; 2811 1.8; 3008 3.1; 3219 4.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.8; 4514 -0.8; 4830 -3.1; 5168 -2.5; 5530 -0.2; 5917 2.9; 6331 4.8; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -2.8; 8880 -6.8; 9502 -8.9; 10167 -7.0; 10879 -1.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999973023095dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.14 | 3.3 dB   |
| Peaking | 158 Hz  | 0.52 | -5.0 dB  |
| Peaking | 3600 Hz | 4.61 | 7.3 dB   |
| Peaking | 6533 Hz | 6.56 | 5.9 dB   |
| Peaking | 9466 Hz | 4.58 | -10.0 dB |
| Peaking | 804 Hz  | 1.86 | 1.6 dB   |
| Peaking | 2067 Hz | 1.16 | -2.9 dB  |
| Peaking | 2869 Hz | 4.4  | 2.3 dB   |
| Peaking | 4633 Hz | 1.75 | 3.9 dB   |
| Peaking | 4878 Hz | 4.78 | -8.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)