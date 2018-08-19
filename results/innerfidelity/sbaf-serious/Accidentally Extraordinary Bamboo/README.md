# Accidentally Extraordinary Bamboo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.6; 22 4.0; 23 3.6; 25 3.0; 26 2.8; 28 2.2; 30 1.8; 32 1.3; 35 0.7; 37 0.4; 40 -0.1; 42 -0.4; 45 -0.8; 49 -1.4; 52 -1.8; 56 -2.2; 59 -2.6; 64 -3.1; 68 -3.5; 73 -4.0; 78 -4.5; 83 -4.9; 89 -5.4; 95 -5.8; 102 -6.2; 109 -6.5; 117 -6.8; 125 -7.1; 134 -7.4; 143 -7.6; 153 -7.8; 164 -8.0; 175 -8.1; 188 -8.1; 201 -8.2; 215 -8.1; 230 -7.9; 246 -7.8; 263 -7.7; 282 -7.3; 301 -7.0; 323 -6.6; 345 -6.1; 369 -5.6; 395 -5.1; 423 -4.4; 452 -3.8; 484 -3.4; 518 -2.8; 554 -2.2; 593 -1.5; 635 -1.1; 679 -0.2; 726 0.7; 777 0.7; 832 0.9; 890 0.8; 952 0.4; 1019 -0.0; 1090 -0.5; 1167 -1.0; 1248 -1.7; 1336 -2.7; 1429 -3.9; 1529 -5.2; 1636 -6.3; 1751 -7.4; 1873 -7.9; 2004 -7.8; 2145 -7.3; 2295 -6.3; 2455 -4.5; 2627 -2.4; 2811 -0.4; 3008 2.1; 3219 4.2; 3444 5.8; 3685 6.0; 3943 5.8; 4219 4.5; 4514 3.3; 4830 2.8; 5168 2.5; 5530 1.3; 5917 -1.2; 6331 -5.6; 6775 -7.3; 7249 -4.9; 7756 -1.8; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999918362886dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary Bamboo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.37 | 4.7 dB  |
| Peaking | 174 Hz  | 0.58 | -8.7 dB |
| Peaking | 2035 Hz | 2.02 | -9.9 dB |
| Peaking | 3719 Hz | 1.64 | 7.8 dB  |
| Peaking | 6756 Hz | 5.15 | -9.1 dB |
| Peaking | 171 Hz  | 1.04 | 3.1 dB  |
| Peaking | 228 Hz  | 0.45 | -2.7 dB |
| Peaking | 800 Hz  | 1.44 | 3.6 dB  |
| Peaking | 840 Hz  | 1.95 | -0.2 dB |
| Peaking | 1546 Hz | 4.48 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%20Bamboo/Accidentally%20Extraordinary%20Bamboo.png)