# KRK Systems KNS 6400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.6; 26 5.5; 28 5.3; 30 5.1; 32 5.0; 35 4.8; 37 4.8; 40 4.9; 42 5.0; 45 5.3; 49 5.7; 52 5.9; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.7; 78 4.4; 83 3.2; 89 2.1; 95 1.5; 102 1.3; 109 0.8; 117 -0.0; 125 -0.6; 134 -0.8; 143 -1.1; 153 -1.2; 164 -1.1; 175 -2.0; 188 -2.3; 201 -2.2; 215 -2.1; 230 -2.1; 246 -1.8; 263 -1.6; 282 -1.6; 301 -2.1; 323 -2.1; 345 -2.1; 369 -2.1; 395 -1.9; 423 -1.4; 452 -1.4; 484 -1.7; 518 -1.9; 554 -2.2; 593 -2.3; 635 -1.5; 679 -0.4; 726 0.1; 777 -0.1; 832 -0.4; 890 -0.2; 952 -0.0; 1019 -0.0; 1090 -0.2; 1167 -0.5; 1248 -0.6; 1336 -0.7; 1429 -0.9; 1529 -1.7; 1636 -1.9; 1751 -3.2; 1873 -3.7; 2004 -3.8; 2145 -3.7; 2295 -3.9; 2455 -4.2; 2627 -4.1; 2811 -3.4; 3008 -2.1; 3219 -2.7; 3444 -1.5; 3685 -0.5; 3943 0.1; 4219 0.9; 4514 2.3; 4830 3.5; 5168 4.5; 5530 4.3; 5917 2.6; 6331 1.7; 6775 1.4; 7249 1.2; 7756 0.3; 8299 -0.1; 8880 -1.4; 9502 -2.5; 10167 -2.0; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.8; 20000 -4.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.43 | 5.8 dB  |
| Peaking | 64 Hz   | 1.45 | 5.3 dB  |
| Peaking | 209 Hz  | 0.51 | -2.6 dB |
| Peaking | 2383 Hz | 1.54 | -4.5 dB |
| Peaking | 5204 Hz | 3.15 | 5.4 dB  |
| Peaking | 575 Hz  | 4.01 | -1.9 dB |
| Peaking | 798 Hz  | 1.16 | 1.0 dB  |
| Peaking | 1807 Hz | 7.96 | -1.2 dB |
| Peaking | 7062 Hz | 5.79 | 0.9 dB  |
| Peaking | 9577 Hz | 5.09 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)