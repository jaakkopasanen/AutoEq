# Plugged Crown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.1; 22 0.8; 23 0.6; 25 0.4; 26 0.3; 28 0.1; 30 -0.1; 32 -0.3; 35 -0.6; 37 -0.8; 40 -1.0; 42 -1.1; 45 -1.3; 49 -1.6; 52 -1.7; 56 -2.0; 59 -2.1; 64 -2.4; 68 -2.6; 73 -2.8; 78 -2.9; 83 -2.9; 89 -2.8; 95 -3.1; 102 -3.8; 109 -4.6; 117 -5.2; 125 -5.8; 134 -6.2; 143 -6.3; 153 -6.4; 164 -6.2; 175 -6.5; 188 -7.1; 201 -7.2; 215 -7.1; 230 -6.7; 246 -6.9; 263 -7.1; 282 -7.0; 301 -6.8; 323 -6.4; 345 -5.9; 369 -5.2; 395 -4.4; 423 -3.2; 452 -2.2; 484 -1.8; 518 -0.9; 554 0.6; 593 1.9; 635 2.9; 679 3.3; 726 3.4; 777 2.9; 832 2.0; 890 1.1; 952 0.4; 1019 -0.0; 1090 -0.2; 1167 -0.9; 1248 -1.1; 1336 -1.1; 1429 -1.1; 1529 -1.0; 1636 -1.5; 1751 -2.1; 1873 -2.1; 2004 -1.6; 2145 -0.9; 2295 -0.1; 2455 1.0; 2627 1.7; 2811 2.6; 3008 3.8; 3219 4.6; 3444 5.6; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999892437424dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plugged Crown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 137 Hz  | 1.69 | -1.0 dB |
| Peaking | 269 Hz  | 0.44 | -7.5 dB |
| Peaking | 659 Hz  | 1.55 | 7.5 dB  |
| Peaking | 1861 Hz | 1.84 | -3.0 dB |
| Peaking | 4297 Hz | 1.13 | 7.1 dB  |
| Peaking | 19 Hz   | 1.89 | 1.3 dB  |
| Peaking | 3403 Hz | 3.56 | 1.0 dB  |
| Peaking | 4346 Hz | 3.33 | -1.1 dB |
| Peaking | 6346 Hz | 2.91 | 4.5 dB  |
| Peaking | 7377 Hz | 1.59 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plugged%20Crown/Plugged%20Crown.png)