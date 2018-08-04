# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 4.9; 22 4.2; 23 3.9; 25 3.3; 26 3.0; 28 2.6; 30 2.1; 32 1.8; 35 1.3; 37 1.0; 40 0.6; 42 0.3; 45 0.0; 49 -0.3; 52 -0.6; 56 -1.0; 59 -1.2; 64 -0.8; 68 0.3; 73 -0.1; 78 -1.3; 83 -1.7; 89 -1.9; 95 -1.9; 102 -1.8; 109 -1.7; 117 -1.8; 125 -2.0; 134 -1.9; 143 -1.9; 153 -1.7; 164 -1.7; 175 -1.7; 188 -1.7; 201 -1.7; 215 -1.6; 230 -1.6; 246 -1.5; 263 -1.5; 282 -1.4; 301 -1.3; 323 -1.2; 345 -1.0; 369 -0.9; 395 -0.8; 423 -0.7; 452 -0.6; 484 -0.4; 518 -0.3; 554 1.2; 593 1.7; 635 1.1; 679 1.0; 726 1.0; 777 1.1; 832 0.8; 890 0.3; 952 0.1; 1019 0.0; 1090 0.0; 1167 -0.2; 1248 -0.5; 1336 -0.4; 1429 -0.8; 1529 -1.2; 1636 -1.5; 1751 -2.1; 1873 -2.9; 2004 -3.8; 2145 -4.5; 2295 -4.3; 2455 -4.1; 2627 -3.5; 2811 -2.9; 3008 -2.0; 3219 -1.2; 3444 -0.6; 3685 -0.2; 3943 -0.4; 4219 -1.3; 4514 -1.6; 4830 -1.2; 5168 -2.3; 5530 -5.3; 5917 -7.1; 6331 -4.9; 6775 -2.6; 7249 -2.9; 7756 -3.1; 8299 -2.2; 8880 -0.6; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -2.1; 20000 -8.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.12 | 4.9 dB  |
| Peaking | 181 Hz  | 0.41 | -2.3 dB |
| Peaking | 1264 Hz | 0.26 | 1.7 dB  |
| Peaking | 2192 Hz | 1.54 | -5.8 dB |
| Peaking | 5989 Hz | 3.16 | -6.8 dB |
| Peaking | 595 Hz  | 7.67 | 1.5 dB  |
| Peaking | 1124 Hz | 3.28 | -0.6 dB |
| Peaking | 7622 Hz | 2.42 | 1.8 dB  |
| Peaking | 7741 Hz | 4.99 | -3.8 dB |
| Peaking | 3660 Hz | 8.35 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K702/AKG%20K702.png)