# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 4.4; 22 3.7; 23 3.4; 25 2.8; 26 2.5; 28 2.0; 30 1.6; 32 1.2; 35 0.7; 37 0.4; 40 -0.0; 42 -0.3; 45 -0.6; 49 -0.9; 52 -1.2; 56 -1.6; 59 -1.7; 64 -1.3; 68 -0.3; 73 -0.7; 78 -2.0; 83 -2.4; 89 -2.7; 95 -2.8; 102 -2.8; 109 -2.8; 117 -3.1; 125 -3.2; 134 -3.2; 143 -3.2; 153 -3.0; 164 -3.1; 175 -3.1; 188 -3.1; 201 -3.1; 215 -3.0; 230 -3.0; 246 -2.9; 263 -2.9; 282 -2.8; 301 -2.7; 323 -2.6; 345 -2.4; 369 -2.3; 395 -2.1; 423 -1.9; 452 -1.6; 484 -1.2; 518 -0.8; 554 0.7; 593 1.2; 635 0.8; 679 0.9; 726 1.0; 777 1.0; 832 0.7; 890 0.3; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.0; 1248 0.2; 1336 0.9; 1429 1.3; 1529 1.5; 1636 1.5; 1751 0.9; 1873 -0.0; 2004 -0.9; 2145 -1.4; 2295 -1.3; 2455 -1.1; 2627 -0.5; 2811 0.1; 3008 0.6; 3219 1.2; 3444 1.5; 3685 1.9; 3943 1.9; 4219 2.3; 4514 3.2; 4830 4.3; 5168 3.1; 5530 -0.6; 5917 -3.6; 6331 -2.6; 6775 -1.3; 7249 -1.9; 7756 -2.1; 8299 -0.8; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.0dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.21 | 4.6 dB  |
| Peaking | 186 Hz  |  0.34 | -3.4 dB |
| Peaking | 676 Hz  |  1.4  | 2.5 dB  |
| Peaking | 5068 Hz |  2.51 | 9.0 dB  |
| Peaking | 5772 Hz |  2.51 | -8.3 dB |
| Peaking | 15 Hz   |  0.21 | 0.2 dB  |
| Peaking | 1646 Hz |  2.49 | 3.8 dB  |
| Peaking | 2034 Hz |  1.18 | -3.1 dB |
| Peaking | 3208 Hz |  1.98 | 1.7 dB  |
| Peaking | 7706 Hz | 12.44 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/AKG%20K702/AKG%20K702.png)