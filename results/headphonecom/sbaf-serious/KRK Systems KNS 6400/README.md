# KRK Systems KNS 6400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 5.1; 22 4.9; 23 4.8; 25 4.5; 26 4.4; 28 4.2; 30 4.1; 32 3.9; 35 3.8; 37 3.8; 40 3.7; 42 3.7; 45 4.0; 49 5.0; 52 5.5; 56 5.8; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.0; 83 3.6; 89 2.4; 95 1.6; 102 0.8; 109 0.2; 117 -0.6; 125 -1.4; 134 -2.0; 143 -2.5; 153 -2.2; 164 -1.7; 175 -2.9; 188 -4.0; 201 -4.5; 215 -4.8; 230 -4.4; 246 -3.5; 263 -3.7; 282 -3.9; 301 -4.0; 323 -4.1; 345 -3.9; 369 -3.4; 395 -2.7; 423 -1.9; 452 -1.3; 484 -1.1; 518 -1.2; 554 -1.5; 593 -1.9; 635 -1.9; 679 -1.4; 726 0.3; 777 0.3; 832 -0.9; 890 -0.4; 952 -0.1; 1019 0.0; 1090 -0.3; 1167 -0.7; 1248 -0.9; 1336 -0.8; 1429 -0.8; 1529 -1.0; 1636 -0.9; 1751 -2.1; 1873 -3.0; 2004 -3.6; 2145 -3.6; 2295 -3.5; 2455 -3.9; 2627 -3.7; 2811 -2.8; 3008 -0.7; 3219 -1.1; 3444 -0.0; 3685 2.4; 3943 1.4; 4219 0.8; 4514 0.7; 4830 2.5; 5168 3.1; 5530 3.0; 5917 0.0; 6331 -1.7; 6775 -1.9; 7249 0.3; 7756 0.3; 8299 0.0; 8880 -1.4; 9502 -2.9; 10167 -1.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.7; 20000 -7.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.74 | 4.8 dB  |
| Peaking | 67 Hz   | 1.23 | 7.4 dB  |
| Peaking | 120 Hz  | 0.63 | -2.4 dB |
| Peaking | 259 Hz  | 0.95 | -3.7 dB |
| Peaking | 2234 Hz | 2.69 | -4.3 dB |
| Peaking | 2681 Hz | 6.74 | -2.2 dB |
| Peaking | 5368 Hz | 6.11 | 2.5 dB  |
| Peaking | 5357 Hz | 0.97 | 2.1 dB  |
| Peaking | 9538 Hz | 5.74 | -3.6 dB |
| Peaking | 6399 Hz | 4.77 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)