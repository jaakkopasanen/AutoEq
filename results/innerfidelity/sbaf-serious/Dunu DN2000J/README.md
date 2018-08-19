# Dunu DN2000J

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 1.5; 22 1.0; 23 0.7; 25 0.2; 26 0.0; 28 -0.3; 30 -0.7; 32 -0.9; 35 -1.3; 37 -1.5; 40 -1.8; 42 -1.9; 45 -2.2; 49 -2.5; 52 -2.6; 56 -2.9; 59 -3.1; 64 -3.4; 68 -3.6; 73 -3.9; 78 -4.2; 83 -4.4; 89 -4.6; 95 -4.8; 102 -5.0; 109 -5.0; 117 -5.1; 125 -5.2; 134 -5.3; 143 -5.3; 153 -5.3; 164 -5.2; 175 -5.1; 188 -5.0; 201 -4.9; 215 -4.6; 230 -4.4; 246 -4.2; 263 -4.0; 282 -3.7; 301 -3.5; 323 -3.2; 345 -2.9; 369 -2.7; 395 -2.4; 423 -2.0; 452 -1.7; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.3; 1336 -0.7; 1429 -1.3; 1529 -2.0; 1636 -2.2; 1751 -2.2; 1873 -2.1; 2004 -1.9; 2145 -1.8; 2295 -1.5; 2455 -1.0; 2627 -0.8; 2811 -0.9; 3008 -0.3; 3219 0.4; 3444 1.8; 3685 2.9; 3943 2.6; 4219 -0.1; 4514 -3.9; 4830 -6.2; 5168 -6.2; 5530 -8.3; 5917 -9.4; 6331 -8.7; 6775 -6.7; 7249 -6.4; 7756 -6.9; 8299 -7.2; 8880 -6.7; 9502 -4.9; 10167 -1.9; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -1.5; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1360153354417317dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000J ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 107 Hz   | 0.61 | -4.5 dB |
| Peaking | 240 Hz   | 0.92 | -2.4 dB |
| Peaking | 5803 Hz  | 3.39 | -8.5 dB |
| Peaking | 8586 Hz  | 2.06 | -7.2 dB |
| Peaking | 10853 Hz | 2.82 | 2.9 dB  |
| Peaking | 20 Hz    | 2.2  | 1.8 dB  |
| Peaking | 894 Hz   | 1.6  | 1.1 dB  |
| Peaking | 1810 Hz  | 1.54 | -2.2 dB |
| Peaking | 3821 Hz  | 3.85 | 5.1 dB  |
| Peaking | 4693 Hz  | 6.98 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000J/Dunu%20DN2000J.png)