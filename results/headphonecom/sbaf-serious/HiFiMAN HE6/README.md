# HiFiMAN HE6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 4.2; 22 3.2; 23 2.8; 25 2.1; 26 1.8; 28 1.5; 30 1.3; 32 1.2; 35 1.3; 37 1.3; 40 1.5; 42 1.5; 45 1.6; 49 1.7; 52 1.7; 56 1.5; 59 1.5; 64 1.5; 68 1.4; 73 1.3; 78 1.0; 83 0.8; 89 0.8; 95 0.7; 102 0.7; 109 0.7; 117 0.5; 125 0.3; 134 0.2; 143 0.0; 153 -0.1; 164 -0.1; 175 -0.0; 188 -0.1; 201 -0.1; 215 -0.1; 230 -0.1; 246 -0.1; 263 -0.1; 282 0.1; 301 0.3; 323 0.2; 345 0.4; 369 0.5; 395 0.4; 423 0.4; 452 0.3; 484 0.3; 518 0.3; 554 0.2; 593 0.2; 635 0.4; 679 0.6; 726 0.7; 777 0.5; 832 0.1; 890 -0.2; 952 0.1; 1019 0.0; 1090 0.2; 1167 1.2; 1248 0.8; 1336 1.0; 1429 0.9; 1529 0.6; 1636 1.0; 1751 2.6; 1873 3.2; 2004 3.3; 2145 2.4; 2295 1.6; 2455 2.5; 2627 2.6; 2811 0.9; 3008 -0.3; 3219 -0.3; 3444 -0.1; 3685 -0.6; 3943 -0.6; 4219 -2.4; 4514 -3.2; 4830 -1.2; 5168 2.2; 5530 5.1; 5917 -3.0; 6331 -4.5; 6775 -5.0; 7249 -4.3; 7756 -3.6; 8299 -4.0; 8880 -4.8; 9502 -3.8; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 -1.4; 13327 -4.5; 14260 -6.2; 15258 -5.6; 16326 -3.3; 17469 -0.6; 18692 -0.2; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.789398639508402dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -3.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 2036 Hz  | 1.94 | 3.1 dB  |
| Peaking | 4378 Hz  | 9.99 | -3.3 dB |
| Peaking | 7682 Hz  | 2.39 | -4.8 dB |
| Peaking | 14703 Hz | 2.8  | -6.7 dB |
| Peaking | 18 Hz    | 1.68 | 4.5 dB  |
| Peaking | 56 Hz    | 1.11 | 1.5 dB  |
| Peaking | 5501 Hz  | 9.69 | 9.2 dB  |
| Peaking | 6088 Hz  | 4.9  | -4.1 dB |
| Peaking | 17964 Hz | 3.3  | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)