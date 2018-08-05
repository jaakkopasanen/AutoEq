# Denon AH-D5000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 10 -84; 20 0.9; 22 0.0; 23 -0.4; 25 -1.0; 26 -1.2; 28 -1.6; 30 -1.8; 32 -2.0; 35 -2.1; 37 -2.2; 40 -2.2; 42 -2.2; 45 -2.2; 49 -2.1; 52 -2.0; 56 -2.0; 59 -2.1; 64 -2.0; 68 -1.8; 73 -1.5; 78 -1.5; 83 -1.8; 89 -2.1; 95 -2.4; 102 -2.8; 109 -3.0; 117 -3.3; 125 -3.6; 134 -3.8; 143 -4.1; 153 -4.1; 164 -4.0; 175 -4.0; 188 -4.0; 201 -3.9; 215 -3.8; 230 -3.6; 246 -3.5; 263 -3.3; 282 -3.1; 301 -2.9; 323 -2.7; 345 -2.5; 369 -2.4; 395 -2.2; 423 -1.9; 452 -1.6; 484 -1.5; 518 -1.2; 554 -0.7; 593 -0.1; 635 0.4; 679 0.6; 726 0.3; 777 -0.5; 832 -1.7; 890 -0.3; 952 0.5; 1019 -0.2; 1090 -0.6; 1167 -0.9; 1248 -1.3; 1336 -1.7; 1429 -2.4; 1529 -3.3; 1636 -3.7; 1751 -4.1; 1873 -4.2; 2004 -4.1; 2145 -3.8; 2295 -2.0; 2455 1.1; 2627 0.5; 2811 1.0; 3008 1.4; 3219 0.3; 3444 0.5; 3685 0.8; 3943 1.6; 4219 1.6; 4514 0.6; 4830 -0.7; 5168 -1.1; 5530 -1.3; 5917 -2.0; 6331 -2.1; 6775 -3.0; 7249 -2.5; 7756 -0.5; 8299 0.0; 8880 -0.4; 9502 -3.1; 10167 -4.3; 10879 -3.1; 11640 -2.0; 12455 -2.5; 13327 -3.3; 14260 -2.1; 15258 -0.1; 16326 0.0; 17469 -0.2; 18692 -3.5; 20000 -8.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.3dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.36 | -2.0 dB |
| Peaking | 181 Hz   | 0.69 | -4.2 dB |
| Peaking | 1788 Hz  | 3.1  | -4.7 dB |
| Peaking | 19731 Hz | 3.12 | -8.3 dB |
| Peaking | 36934 Hz | 1.35 | -3.1 dB |
| Peaking | 664 Hz   | 6.36 | 1.5 dB  |
| Peaking | 2857 Hz  | 5.14 | 2.0 dB  |
| Peaking | 4091 Hz  | 5.89 | 2.2 dB  |
| Peaking | 6422 Hz  | 4.1  | -2.1 dB |
| Peaking | 16609 Hz | 3.31 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20B2012/Denon%20AH-D5000%20B2012.png)