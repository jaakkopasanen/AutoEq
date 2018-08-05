# KRK Systems KNS 8400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 3.2; 22 2.8; 23 2.6; 25 2.3; 26 2.2; 28 2.0; 30 1.9; 32 1.9; 35 2.1; 37 2.2; 40 2.4; 42 2.6; 45 2.8; 49 2.7; 52 2.7; 56 2.7; 59 2.9; 64 3.0; 68 2.8; 73 2.1; 78 1.0; 83 -0.2; 89 -1.5; 95 -2.8; 102 -4.4; 109 -5.3; 117 -6.2; 125 -7.1; 134 -7.3; 143 -7.1; 153 -6.7; 164 -6.3; 175 -7.6; 188 -7.6; 201 -7.1; 215 -6.6; 230 -5.8; 246 -5.0; 263 -4.5; 282 -3.8; 301 -2.9; 323 -2.1; 345 -1.1; 369 -0.1; 395 0.8; 423 1.7; 452 2.1; 484 1.8; 518 1.0; 554 0.1; 593 -0.5; 635 -0.6; 679 -0.1; 726 0.7; 777 0.1; 832 -0.7; 890 -0.4; 952 -0.2; 1019 0.1; 1090 0.0; 1167 -0.1; 1248 -0.4; 1336 -1.2; 1429 -1.8; 1529 -2.8; 1636 -4.0; 1751 -5.1; 1873 -5.6; 2004 -6.0; 2145 -6.6; 2295 -6.9; 2455 -7.0; 2627 -7.1; 2811 -6.7; 3008 -5.0; 3219 -4.9; 3444 -5.3; 3685 -4.8; 3943 -4.6; 4219 -4.1; 4514 -2.6; 4830 -0.6; 5168 0.1; 5530 0.5; 5917 0.2; 6331 -0.4; 6775 -0.4; 7249 0.5; 7756 0.3; 8299 -1.4; 8880 -4.2; 9502 -5.4; 10167 -3.7; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -2.3; 20000 -4.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.54 | 2.6 dB  |
| Peaking | 64 Hz   | 2.11 | 4.0 dB  |
| Peaking | 150 Hz  | 1.05 | -8.5 dB |
| Peaking | 2512 Hz | 1.39 | -7.6 dB |
| Peaking | 9485 Hz | 6.15 | -5.9 dB |
| Peaking | 241 Hz  | 2.76 | -1.8 dB |
| Peaking | 443 Hz  | 3    | 3.5 dB  |
| Peaking | 1112 Hz | 4.13 | 1.4 dB  |
| Peaking | 4142 Hz | 3.38 | -3.5 dB |
| Peaking | 5038 Hz | 1.98 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%208400/KRK%20Systems%20KNS%208400.png)