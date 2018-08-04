# Denon AH-D2000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.2; 22 1.4; 23 1.1; 25 0.5; 26 0.3; 28 -0.1; 30 -0.4; 32 -0.5; 35 -0.6; 37 -0.6; 40 -0.7; 42 -0.6; 45 -0.5; 49 -0.2; 52 -0.1; 56 -0.1; 59 -0.1; 64 0.0; 68 0.1; 73 0.1; 78 -0.0; 83 -0.2; 89 -0.4; 95 -0.8; 102 -1.0; 109 -1.3; 117 -1.6; 125 -2.0; 134 -2.3; 143 -2.5; 153 -2.5; 164 -2.3; 175 -2.4; 188 -2.4; 201 -2.5; 215 -2.3; 230 -2.2; 246 -2.1; 263 -2.0; 282 -1.9; 301 -1.7; 323 -1.7; 345 -1.5; 369 -1.3; 395 -1.1; 423 -0.9; 452 -0.8; 484 -1.0; 518 -1.2; 554 -1.3; 593 -1.2; 635 -1.4; 679 -0.4; 726 1.4; 777 0.8; 832 -0.0; 890 -0.3; 952 -0.2; 1019 0.0; 1090 0.3; 1167 0.7; 1248 1.0; 1336 1.1; 1429 1.0; 1529 0.8; 1636 0.6; 1751 0.9; 1873 1.1; 2004 1.4; 2145 1.5; 2295 1.5; 2455 1.7; 2627 1.6; 2811 3.2; 3008 5.4; 3219 4.7; 3444 2.6; 3685 1.4; 3943 1.2; 4219 1.3; 4514 2.2; 4830 3.2; 5168 2.6; 5530 2.9; 5917 1.9; 6331 1.2; 6775 0.7; 7249 0.2; 7756 0.2; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -1.4; 10879 -1.3; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 203 Hz   | 0.74 | -2.5 dB |
| Peaking | 10583 Hz | 4.81 | -1.6 dB |
| Peaking | 1825 Hz  | 1.02 | 1.0 dB  |
| Peaking | 3074 Hz  | 5.6  | 5.0 dB  |
| Peaking | 5187 Hz  | 3    | 2.9 dB  |
| Peaking | 36 Hz    | 0.9  | -3.4 dB |
| Peaking | 20 Hz    | 0.16 | 3.1 dB  |
| Peaking | 126 Hz   | 1.35 | -1.6 dB |
| Peaking | 667 Hz   | 2.63 | -1.9 dB |
| Peaking | 731 Hz   | 6.86 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000%20B2012/Denon%20AH-D2000%20B2012.png)