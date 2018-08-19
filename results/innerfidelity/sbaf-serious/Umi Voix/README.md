# Umi Voix

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.6; 23 -3.7; 25 -3.7; 26 -3.7; 28 -3.8; 30 -3.8; 32 -3.9; 35 -4.0; 37 -4.0; 40 -4.0; 42 -4.0; 45 -4.1; 49 -4.2; 52 -4.2; 56 -4.3; 59 -4.3; 64 -4.4; 68 -4.6; 73 -4.7; 78 -4.8; 83 -5.0; 89 -5.1; 95 -5.2; 102 -5.3; 109 -5.2; 117 -5.2; 125 -5.3; 134 -5.2; 143 -5.1; 153 -5.0; 164 -4.9; 175 -4.7; 188 -4.3; 201 -4.2; 215 -3.7; 230 -3.5; 246 -3.1; 263 -2.7; 282 -2.1; 301 -1.6; 323 -1.0; 345 -0.4; 369 0.2; 395 0.8; 423 1.4; 452 2.3; 484 2.4; 518 2.6; 554 2.9; 593 3.4; 635 3.2; 679 2.9; 726 2.6; 777 2.4; 832 1.8; 890 1.2; 952 0.6; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.7; 1336 -2.2; 1429 -2.6; 1529 -2.7; 1636 -2.4; 1751 -1.6; 1873 -0.5; 2004 1.0; 2145 2.6; 2295 4.1; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.5; 4219 2.9; 4514 3.3; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999994907dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Umi Voix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.5  | -3.9 dB |
| Peaking | 108 Hz  | 1.26 | -3.8 dB |
| Peaking | 189 Hz  | 2.15 | -3.1 dB |
| Peaking | 3044 Hz | 2.14 | 6.6 dB  |
| Peaking | 5598 Hz | 2.66 | 6.0 dB  |
| Peaking | 280 Hz  | 2.19 | -1.6 dB |
| Peaking | 604 Hz  | 1.09 | 3.9 dB  |
| Peaking | 1480 Hz | 1.57 | -4.2 dB |
| Peaking | 2371 Hz | 4.48 | 3.1 dB  |
| Peaking | 8256 Hz | 4.75 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Umi%20Voix/Umi%20Voix.png)