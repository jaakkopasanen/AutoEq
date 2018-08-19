# Bose QuietComfort 20 Aware mod

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.8; 22 3.1; 23 2.4; 25 1.3; 26 0.8; 28 0.1; 30 -0.3; 32 -0.5; 35 -0.6; 37 -0.5; 40 -0.4; 42 -0.3; 45 -0.1; 49 0.1; 52 0.2; 56 0.2; 59 0.2; 64 0.0; 68 -0.2; 73 -0.5; 78 -0.9; 83 -1.3; 89 -1.7; 95 -2.1; 102 -2.3; 109 -2.4; 117 -2.4; 125 -2.5; 134 -2.4; 143 -2.4; 153 -2.4; 164 -2.4; 175 -2.4; 188 -2.4; 201 -2.4; 215 -2.4; 230 -2.3; 246 -2.2; 263 -2.1; 282 -1.9; 301 -1.8; 323 -1.8; 345 -1.6; 369 -1.6; 395 -1.7; 423 -1.6; 452 -1.6; 484 -1.7; 518 -1.5; 554 -1.1; 593 -0.7; 635 -0.7; 679 -0.9; 726 -0.7; 777 -0.2; 832 0.2; 890 0.4; 952 0.3; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -2.2; 1336 -3.2; 1429 -4.4; 1529 -5.5; 1636 -6.1; 1751 -5.8; 1873 -4.8; 2004 -3.7; 2145 -2.9; 2295 -2.3; 2455 -1.5; 2627 -1.1; 2811 -0.3; 3008 1.2; 3219 2.2; 3444 2.5; 3685 1.6; 3943 -0.1; 4219 -2.0; 4514 -1.1; 4830 2.0; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.8; 7249 -1.5; 7756 -3.7; 8299 -2.6; 8880 -1.0; 9502 -0.9; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.094765865819561dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Aware mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 181 Hz  |  0.61 | -2.6 dB |
| Peaking | 1691 Hz |  2.36 | -6.3 dB |
| Peaking | 3304 Hz |  7.32 | 3.0 dB  |
| Peaking | 5992 Hz |  3.23 | 7.7 dB  |
| Peaking | 7824 Hz |  4.63 | -5.5 dB |
| Peaking | 18 Hz   |  2.85 | 4.3 dB  |
| Peaking | 475 Hz  |  3.44 | -0.7 dB |
| Peaking | 918 Hz  |  4.17 | 1.5 dB  |
| Peaking | 4357 Hz |  7.79 | -3.6 dB |
| Peaking | 5172 Hz | 10.54 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Aware%20mod/Bose%20QuietComfort%2020%20Aware%20mod.png)