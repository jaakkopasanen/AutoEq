# HiFiMAN HE1000 PreProduction

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 3.6; 22 3.3; 23 3.1; 25 2.9; 26 2.8; 28 2.7; 30 2.6; 32 2.5; 35 2.5; 37 2.4; 40 2.3; 42 2.3; 45 2.3; 49 2.1; 52 2.1; 56 1.9; 59 1.7; 64 1.5; 68 1.5; 73 1.4; 78 1.2; 83 1.0; 89 0.8; 95 0.5; 102 0.3; 109 0.2; 117 0.0; 125 -0.2; 134 -0.3; 143 -0.5; 153 -0.8; 164 -1.0; 175 -1.2; 188 -0.9; 201 -0.4; 215 -0.6; 230 -0.2; 246 -0.5; 263 -0.9; 282 -1.3; 301 -1.8; 323 -1.7; 345 -1.3; 369 -0.2; 395 -0.3; 423 0.3; 452 0.4; 484 -0.6; 518 -1.1; 554 0.5; 593 0.1; 635 -0.3; 679 0.1; 726 -0.3; 777 0.2; 832 -0.1; 890 -0.3; 952 -0.4; 1019 0.5; 1090 1.2; 1167 0.6; 1248 1.9; 1336 2.5; 1429 2.1; 1529 2.2; 1636 1.3; 1751 3.0; 1873 2.5; 2004 3.4; 2145 3.5; 2295 3.2; 2455 3.6; 2627 3.5; 2811 3.0; 3008 1.5; 3219 0.6; 3444 1.6; 3685 1.8; 3943 1.0; 4219 -1.6; 4514 -2.3; 4830 -2.3; 5168 -2.1; 5530 -0.5; 5917 0.0; 6331 -3.1; 6775 -4.6; 7249 -3.6; 7756 -2.8; 8299 -2.8; 8880 -2.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -2.3; 20000 -6.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.8822228467666022dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE1000 PreProduction ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.7  | 3.1 dB  |
| Peaking | 1343 Hz  | 5.01 | 1.5 dB  |
| Peaking | 2332 Hz  | 1.52 | 3.7 dB  |
| Peaking | 4654 Hz  | 6.03 | -2.9 dB |
| Peaking | 7122 Hz  | 2.95 | -4.4 dB |
| Peaking | 67 Hz    | 2    | 0.7 dB  |
| Peaking | 166 Hz   | 2.41 | -1.2 dB |
| Peaking | 310 Hz   | 4.36 | -1.9 dB |
| Peaking | 913 Hz   | 7.05 | -0.8 dB |
| Peaking | 19687 Hz | 3.12 | -6.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE1000%20PreProduction/HiFiMAN%20HE1000%20PreProduction.png)