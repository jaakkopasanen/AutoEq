# HiFiMAN HE1000 PreProduction

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 3.6; 22 3.3; 23 3.2; 25 2.9; 26 2.8; 28 2.7; 30 2.6; 32 2.6; 35 2.5; 37 2.5; 40 2.5; 42 2.4; 45 2.4; 49 2.4; 52 2.3; 56 2.2; 59 2.1; 64 2.0; 68 2.1; 73 2.1; 78 2.0; 83 1.8; 89 1.5; 95 1.2; 102 0.9; 109 0.6; 117 0.2; 125 -0.2; 134 -0.4; 143 -0.7; 153 -1.0; 164 -1.2; 175 -1.4; 188 -1.1; 201 -0.6; 215 -0.7; 230 -0.3; 246 -0.6; 263 -1.0; 282 -1.3; 301 -1.8; 323 -1.7; 345 -1.3; 369 -0.2; 395 -0.3; 423 0.2; 452 0.4; 484 -0.6; 518 -1.1; 554 0.5; 593 0.1; 635 -0.3; 679 0.1; 726 -0.3; 777 0.2; 832 -0.1; 890 -0.3; 952 -0.4; 1019 0.5; 1090 1.2; 1167 0.6; 1248 1.9; 1336 2.5; 1429 2.1; 1529 2.2; 1636 1.3; 1751 3.0; 1873 2.5; 2004 3.4; 2145 3.5; 2295 3.2; 2455 3.6; 2627 3.5; 2811 3.0; 3008 1.5; 3219 0.6; 3444 1.6; 3685 1.8; 3943 1.0; 4219 -1.6; 4514 -2.3; 4830 -2.3; 5168 -2.1; 5530 -0.5; 5917 0.0; 6331 -3.1; 6775 -4.6; 7249 -3.6; 7756 -2.8; 8299 -2.8; 8880 -2.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -2.3; 20000 -6.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE1000 PreProduction ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.89 | 3.1 dB  |
| Peaking | 67 Hz   | 2.19 | 1.8 dB  |
| Peaking | 1352 Hz | 4.44 | 1.7 dB  |
| Peaking | 2313 Hz | 1.84 | 3.9 dB  |
| Peaking | 7064 Hz | 2.12 | -4.1 dB |
| Peaking | 911 Hz  | 5.51 | -0.7 dB |
| Peaking | 170 Hz  | 3.18 | -1.6 dB |
| Peaking | 308 Hz  | 4.12 | -2.0 dB |
| Peaking | 4628 Hz | 4.14 | -5.1 dB |
| Peaking | 4710 Hz | 1.84 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE1000%20PreProduction/HiFiMAN%20HE1000%20PreProduction.png)