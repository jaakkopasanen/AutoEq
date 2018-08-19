# Sleek SA1- Normal Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.4; 23 -5.4; 25 -5.5; 26 -5.5; 28 -5.6; 30 -5.6; 32 -5.6; 35 -5.7; 37 -5.7; 40 -5.8; 42 -5.8; 45 -5.9; 49 -6.1; 52 -6.2; 56 -6.4; 59 -6.6; 64 -6.8; 68 -7.0; 73 -7.2; 78 -7.5; 83 -7.7; 89 -7.9; 95 -7.9; 102 -8.1; 109 -8.2; 117 -8.2; 125 -8.4; 134 -8.5; 143 -8.6; 153 -8.6; 164 -8.6; 175 -8.5; 188 -8.4; 201 -8.3; 215 -8.1; 230 -7.9; 246 -7.7; 263 -7.5; 282 -7.2; 301 -6.8; 323 -6.4; 345 -5.9; 369 -5.5; 395 -5.1; 423 -4.6; 452 -4.3; 484 -4.0; 518 -3.5; 554 -2.9; 593 -2.4; 635 -1.9; 679 -1.4; 726 -1.0; 777 -0.6; 832 -0.4; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.2; 1336 0.2; 1429 0.3; 1529 0.3; 1636 0.4; 1751 0.8; 1873 1.3; 2004 1.8; 2145 2.4; 2295 2.9; 2455 3.5; 2627 4.0; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 4.8; 4219 2.6; 4514 0.6; 4830 -1.0; 5168 -2.6; 5530 -3.6; 5917 -1.1; 6331 2.1; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678133dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA1- Normal Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.2  | -5.0 dB |
| Peaking | 131 Hz  | 0.65 | -4.4 dB |
| Peaking | 282 Hz  | 0.79 | -4.5 dB |
| Peaking | 3394 Hz | 1.25 | 6.6 dB  |
| Peaking | 5167 Hz | 4.17 | -6.3 dB |
| Peaking | 512 Hz  | 2.29 | -1.0 dB |
| Peaking | 1300 Hz | 0.55 | 1.5 dB  |
| Peaking | 1584 Hz | 1.25 | -1.8 dB |
| Peaking | 6533 Hz | 1.79 | -2.2 dB |
| Peaking | 6655 Hz | 5.72 | 5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA1-%20Normal%20Filter/Sleek%20SA1-%20Normal%20Filter.png)