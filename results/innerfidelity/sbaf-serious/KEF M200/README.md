# KEF M200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -9.8; 22 -9.7; 23 -9.7; 25 -9.6; 26 -9.5; 28 -9.3; 30 -9.1; 32 -9.0; 35 -8.8; 37 -8.7; 40 -8.4; 42 -8.3; 45 -8.0; 49 -7.6; 52 -7.4; 56 -7.1; 59 -6.8; 64 -6.5; 68 -6.2; 73 -6.0; 78 -5.8; 83 -5.7; 89 -5.7; 95 -5.8; 102 -6.0; 109 -6.1; 117 -6.2; 125 -6.4; 134 -6.6; 143 -6.3; 153 -6.2; 164 -6.1; 175 -5.6; 188 -5.3; 201 -4.9; 215 -4.5; 230 -4.1; 246 -3.8; 263 -3.4; 282 -2.8; 301 -2.6; 323 -2.1; 345 -1.7; 369 -1.2; 395 -0.9; 423 -0.4; 452 -0.0; 484 0.0; 518 0.4; 554 0.9; 593 1.2; 635 1.3; 679 1.3; 726 1.3; 777 1.3; 832 1.1; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.6; 1336 -2.6; 1429 -3.7; 1529 -4.8; 1636 -5.8; 1751 -6.7; 1873 -7.2; 2004 -7.0; 2145 -6.1; 2295 -4.8; 2455 -2.4; 2627 2.3; 2811 3.0; 3008 3.4; 3219 2.1; 3444 1.7; 3685 1.5; 3943 1.2; 4219 0.8; 4514 1.3; 4830 2.3; 5168 3.8; 5530 4.5; 5917 4.7; 6331 3.3; 6775 1.9; 7249 -0.1; 7756 -2.6; 8299 -4.7; 8880 -4.9; 9502 -2.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.2; 15258 -4.8; 16326 -5.7; 17469 -3.8; 18692 -2.2; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.56 | -8.8 dB |
| Peaking | 38 Hz    | 0.46 | -6.2 dB |
| Peaking | 158 Hz   | 1.1  | -4.8 dB |
| Peaking | 1841 Hz  | 3.16 | -8.2 dB |
| Peaking | 5516 Hz  | 3.64 | 5.2 dB  |
| Peaking | 707 Hz   | 1.83 | 1.9 dB  |
| Peaking | 1516 Hz  | 1.54 | -2.2 dB |
| Peaking | 5502 Hz  | 0.21 | 1.7 dB  |
| Peaking | 8521 Hz  | 3.56 | -7.0 dB |
| Peaking | 16453 Hz | 1.8  | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M200/KEF%20M200.png)