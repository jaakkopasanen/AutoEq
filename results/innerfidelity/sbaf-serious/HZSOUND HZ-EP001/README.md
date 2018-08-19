# HZSOUND HZ-EP001

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.5; 22 -2.6; 23 -2.6; 25 -2.6; 26 -2.6; 28 -2.6; 30 -2.6; 32 -2.6; 35 -2.6; 37 -2.5; 40 -2.5; 42 -2.5; 45 -2.5; 49 -2.6; 52 -2.5; 56 -2.5; 59 -2.6; 64 -2.7; 68 -2.8; 73 -2.9; 78 -3.0; 83 -3.2; 89 -3.4; 95 -3.5; 102 -3.6; 109 -3.7; 117 -3.7; 125 -3.8; 134 -3.9; 143 -4.0; 153 -4.1; 164 -4.1; 175 -4.1; 188 -4.1; 201 -4.1; 215 -4.0; 230 -3.9; 246 -3.9; 263 -3.9; 282 -3.7; 301 -3.7; 323 -3.6; 345 -3.6; 369 -3.9; 395 -3.9; 423 -1.1; 452 -1.2; 484 -1.7; 518 -1.7; 554 -1.4; 593 -1.0; 635 -0.8; 679 -0.7; 726 -0.3; 777 -0.1; 832 0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.3; 1336 0.1; 1429 0.1; 1529 -0.0; 1636 0.0; 1751 0.4; 1873 0.8; 2004 1.2; 2145 1.5; 2295 2.0; 2455 2.9; 2627 3.0; 2811 3.2; 3008 3.2; 3219 3.4; 3444 2.8; 3685 1.2; 3943 0.7; 4219 0.1; 4514 2.4; 4830 3.2; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09602509597788dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ-EP001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.13 | -2.4 dB |
| Peaking | 196 Hz  | 0.71 | -3.1 dB |
| Peaking | 360 Hz  | 4.03 | -1.9 dB |
| Peaking | 2774 Hz | 2.31 | 3.3 dB  |
| Peaking | 5760 Hz | 3.25 | 6.6 dB  |
| Peaking | 270 Hz  | 6.58 | -0.3 dB |
| Peaking | 1612 Hz | 7.66 | -0.4 dB |
| Peaking | 4121 Hz | 6.02 | -3.1 dB |
| Peaking | 4353 Hz | 1.82 | 1.4 dB  |
| Peaking | 8278 Hz | 3.62 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ-EP001/HZSOUND%20HZ-EP001.png)