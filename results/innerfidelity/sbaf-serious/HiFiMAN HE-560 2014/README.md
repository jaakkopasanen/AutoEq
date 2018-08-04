# HiFiMAN HE-560 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 2.0; 22 2.0; 23 2.1; 25 2.1; 26 2.1; 28 2.2; 30 2.2; 32 2.2; 35 2.3; 37 2.3; 40 2.3; 42 2.4; 45 2.5; 49 2.5; 52 2.5; 56 2.4; 59 2.4; 64 2.4; 68 2.3; 73 2.1; 78 2.0; 83 1.9; 89 1.7; 95 1.4; 102 0.9; 109 0.6; 117 0.2; 125 -0.2; 134 -0.6; 143 -0.8; 153 -1.0; 164 -1.1; 175 -1.1; 188 -1.3; 201 -1.5; 215 -1.4; 230 -1.5; 246 -1.6; 263 -1.5; 282 -1.2; 301 -1.2; 323 -1.4; 345 -1.6; 369 -1.8; 395 -2.0; 423 -2.2; 452 -1.7; 484 -1.1; 518 0.2; 554 1.7; 593 1.6; 635 0.7; 679 0.3; 726 0.0; 777 -0.4; 832 -0.7; 890 -0.3; 952 -0.0; 1019 0.1; 1090 -0.1; 1167 -0.5; 1248 -0.4; 1336 -0.8; 1429 -0.0; 1529 0.2; 1636 0.9; 1751 2.2; 1873 2.5; 2004 2.8; 2145 2.8; 2295 1.9; 2455 1.8; 2627 1.2; 2811 0.7; 3008 -0.6; 3219 -1.6; 3444 -1.6; 3685 -2.5; 3943 -2.5; 4219 -4.0; 4514 -4.7; 4830 -3.3; 5168 0.5; 5530 0.5; 5917 -0.5; 6331 -2.4; 6775 -2.0; 7249 -1.3; 7756 -1.4; 8299 -2.8; 8880 -3.9; 9502 -1.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-560 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.12 | 2.4 dB  |
| Peaking | 65 Hz   | 2.21 | 2.1 dB  |
| Peaking | 2067 Hz | 3.26 | 3.3 dB  |
| Peaking | 4291 Hz | 3.55 | -4.6 dB |
| Peaking | 8694 Hz | 4.58 | -3.7 dB |
| Peaking | 363 Hz  | 0.67 | -2.1 dB |
| Peaking | 580 Hz  | 4.35 | 3.3 dB  |
| Peaking | 4731 Hz | 8.75 | -3.0 dB |
| Peaking | 5215 Hz | 4.08 | 3.0 dB  |
| Peaking | 6439 Hz | 7.12 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-560%202014/HiFiMAN%20HE-560%202014.png)