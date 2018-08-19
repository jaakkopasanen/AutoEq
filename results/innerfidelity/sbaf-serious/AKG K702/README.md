# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 10 -84; 20 2.7; 22 2.1; 23 1.8; 25 1.3; 26 1.0; 28 0.6; 30 0.3; 32 -0.0; 35 -0.4; 37 -0.7; 40 -1.0; 42 -1.1; 45 -1.4; 49 -1.7; 52 -1.9; 56 -2.1; 59 -2.3; 64 -2.6; 68 -2.8; 73 -2.9; 78 -2.7; 83 -2.7; 89 -3.0; 95 -3.3; 102 -3.4; 109 -3.2; 117 -3.7; 125 -4.2; 134 -4.6; 143 -4.8; 153 -5.0; 164 -4.7; 175 -4.7; 188 -4.9; 201 -4.9; 215 -4.7; 230 -4.7; 246 -4.7; 263 -4.6; 282 -4.4; 301 -4.2; 323 -4.0; 345 -3.8; 369 -3.5; 395 -3.3; 423 -2.9; 452 -2.6; 484 -2.3; 518 -1.6; 554 0.1; 593 0.2; 635 0.4; 679 0.8; 726 1.2; 777 1.2; 832 0.8; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -0.7; 1248 -0.5; 1336 -1.0; 1429 -1.6; 1529 -2.4; 1636 -3.1; 1751 -3.9; 1873 -4.2; 2004 -5.3; 2145 -5.6; 2295 -5.3; 2455 -4.6; 2627 -3.3; 2811 -2.2; 3008 -0.9; 3219 0.2; 3444 0.2; 3685 -0.0; 3943 -0.8; 4219 -2.7; 4514 -3.5; 4830 -3.4; 5168 -2.7; 5530 -2.8; 5917 -4.6; 6331 -6.0; 6775 -6.4; 7249 -6.5; 7756 -6.6; 8299 -7.1; 8880 -6.3; 9502 -3.1; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -2.1; 17469 -4.8; 18692 -5.4; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.800444754025543dB` and instead set Global volume in the UI for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 176 Hz   | 0.6  | -5.2 dB |
| Peaking | 2118 Hz  | 2.65 | -5.8 dB |
| Peaking | 6647 Hz  | 2.31 | -5.9 dB |
| Peaking | 8442 Hz  | 5.19 | -5.3 dB |
| Peaking | 18626 Hz | 2    | -6.2 dB |
| Peaking | 21 Hz    | 2.58 | 2.6 dB  |
| Peaking | 741 Hz   | 2.93 | 2.4 dB  |
| Peaking | 3446 Hz  | 3.24 | 5.0 dB  |
| Peaking | 3765 Hz  | 1.66 | -3.3 dB |
| Peaking | 11873 Hz | 1.66 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702/AKG%20K702.png)