# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 5.2; 37 4.9; 40 4.4; 42 4.2; 45 3.9; 49 3.4; 52 3.1; 56 2.6; 59 2.3; 64 2.6; 68 3.5; 73 3.0; 78 1.5; 83 1.0; 89 0.5; 95 0.2; 102 0.1; 109 -0.0; 117 -0.4; 125 -0.8; 134 -1.0; 143 -1.1; 153 -1.1; 164 -1.2; 175 -1.3; 188 -1.4; 201 -1.4; 215 -1.4; 230 -1.4; 246 -1.4; 263 -1.4; 282 -1.3; 301 -1.2; 323 -1.1; 345 -1.0; 369 -0.9; 395 -0.8; 423 -0.7; 452 -0.6; 484 -0.3; 518 -0.2; 554 1.2; 593 1.6; 635 1.0; 679 1.1; 726 1.0; 777 1.0; 832 0.7; 890 0.3; 952 0.1; 1019 0.0; 1090 0.0; 1167 -0.2; 1248 -0.5; 1336 -0.4; 1429 -0.8; 1529 -1.2; 1636 -1.5; 1751 -2.1; 1873 -3.0; 2004 -3.8; 2145 -4.5; 2295 -4.3; 2455 -4.1; 2627 -3.4; 2811 -2.8; 3008 -2.1; 3219 -1.1; 3444 -0.5; 3685 -0.1; 3943 -0.7; 4219 -1.3; 4514 -1.5; 4830 -1.1; 5168 -2.3; 5530 -5.3; 5917 -7.1; 6331 -4.9; 6775 -2.7; 7249 -3.1; 7756 -3.1; 8299 -2.0; 8880 -0.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -2.2; 20000 -8.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.35 | 6.2 dB  |
| Peaking | 206 Hz  | 0.53 | -2.8 dB |
| Peaking | 1116 Hz | 0.22 | 1.7 dB  |
| Peaking | 2197 Hz | 1.56 | -5.8 dB |
| Peaking | 5998 Hz | 3.1  | -6.8 dB |
| Peaking | 623 Hz  | 2.21 | 2.8 dB  |
| Peaking | 626 Hz  | 1.16 | -1.8 dB |
| Peaking | 3612 Hz | 8.07 | 0.9 dB  |
| Peaking | 6631 Hz | 9.96 | 1.5 dB  |
| Peaking | 7743 Hz | 6.66 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K702/AKG%20K702.png)