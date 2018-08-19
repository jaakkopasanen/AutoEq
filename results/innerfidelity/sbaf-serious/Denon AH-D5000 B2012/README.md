# Denon AH-D5000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 10 -84; 20 0.9; 22 -0.0; 23 -0.4; 25 -1.0; 26 -1.2; 28 -1.6; 30 -1.8; 32 -2.0; 35 -2.2; 37 -2.2; 40 -2.3; 42 -2.3; 45 -2.3; 49 -2.3; 52 -2.3; 56 -2.4; 59 -2.5; 64 -2.6; 68 -2.4; 73 -2.2; 78 -2.3; 83 -2.6; 89 -2.9; 95 -3.1; 102 -3.3; 109 -3.4; 117 -3.5; 125 -3.6; 134 -3.7; 143 -3.9; 153 -3.9; 164 -3.8; 175 -3.8; 188 -3.8; 201 -3.7; 215 -3.7; 230 -3.5; 246 -3.4; 263 -3.3; 282 -3.0; 301 -2.9; 323 -2.7; 345 -2.5; 369 -2.4; 395 -2.2; 423 -1.9; 452 -1.6; 484 -1.5; 518 -1.2; 554 -0.7; 593 -0.1; 635 0.4; 679 0.6; 726 0.3; 777 -0.5; 832 -1.7; 890 -0.3; 952 0.5; 1019 -0.2; 1090 -0.6; 1167 -0.9; 1248 -1.3; 1336 -1.7; 1429 -2.4; 1529 -3.3; 1636 -3.7; 1751 -4.1; 1873 -4.2; 2004 -4.1; 2145 -3.8; 2295 -2.0; 2455 1.1; 2627 0.5; 2811 1.0; 3008 1.4; 3219 0.3; 3444 0.5; 3685 0.8; 3943 1.6; 4219 1.6; 4514 0.6; 4830 -0.7; 5168 -1.1; 5530 -1.3; 5917 -2.0; 6331 -2.1; 6775 -3.0; 7249 -2.5; 7756 -0.5; 8299 0.0; 8880 -0.4; 9502 -3.1; 10167 -4.3; 10879 -3.1; 11640 -2.0; 12455 -2.5; 13327 -3.3; 14260 -2.1; 15258 -0.1; 16326 0.0; 17469 -0.2; 18692 -3.5; 20000 -8.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.8507303564988744dB` and instead set Global volume in the UI for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 1.03 | -1.8 dB |
| Peaking | 172 Hz   | 0.6  | -3.9 dB |
| Peaking | 1788 Hz  | 3.12 | -4.7 dB |
| Peaking | 10856 Hz | 1.35 | -3.1 dB |
| Peaking | 19856 Hz | 3.12 | -8.3 dB |
| Peaking | 662 Hz   | 6.07 | 1.5 dB  |
| Peaking | 2874 Hz  | 5.13 | 1.9 dB  |
| Peaking | 4061 Hz  | 5.83 | 2.2 dB  |
| Peaking | 6393 Hz  | 4.21 | -2.0 dB |
| Peaking | 16492 Hz | 4.04 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20B2012/Denon%20AH-D5000%20B2012.png)