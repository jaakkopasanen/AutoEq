# Phiton PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 4.9; 32 4.3; 35 3.4; 37 2.9; 40 2.4; 42 2.1; 45 1.7; 49 1.2; 52 1.0; 56 0.8; 59 0.5; 64 0.1; 68 -0.0; 73 -0.3; 78 -0.9; 83 -1.3; 89 -1.6; 95 -2.0; 102 -2.3; 109 -2.5; 117 -2.7; 125 -3.1; 134 -3.3; 143 -3.4; 153 -3.3; 164 -2.9; 175 -3.0; 188 -2.8; 201 -2.6; 215 -2.3; 230 -1.8; 246 -1.3; 263 -0.6; 282 0.5; 301 1.5; 323 2.2; 345 2.6; 369 2.8; 395 2.8; 423 2.8; 452 2.8; 484 2.5; 518 2.4; 554 2.6; 593 2.6; 635 2.3; 679 1.8; 726 1.4; 777 1.3; 832 1.4; 890 1.4; 952 0.5; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.3; 1336 -1.9; 1429 -2.2; 1529 -2.5; 1636 -2.7; 1751 -2.5; 1873 -2.0; 2004 -1.0; 2145 0.2; 2295 2.0; 2455 4.3; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.4; 4514 5.3; 4830 6.0; 5168 6.0; 5530 5.8; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiton PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.26 | 7.2 dB  |
| Peaking | 504 Hz  | 0.49 | 12.2 dB |
| Peaking | 624 Hz  | 0.1  | -9.3 dB |
| Peaking | 2936 Hz | 1.65 | 10.1 dB |
| Peaking | 5257 Hz | 1.24 | 9.3 dB  |
| Peaking | 183 Hz  | 2.57 | -0.8 dB |
| Peaking | 920 Hz  | 4.6  | 1.2 dB  |
| Peaking | 1784 Hz | 3.08 | -1.1 dB |
| Peaking | 2502 Hz | 9.19 | 1.6 dB  |
| Peaking | 7880 Hz | 7.81 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiton%20PS500/Phiton%20PS500.png)