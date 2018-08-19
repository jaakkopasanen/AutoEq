# Focal Spirit One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.4; 22 -4.4; 23 -4.5; 25 -4.5; 26 -4.5; 28 -4.5; 30 -4.6; 32 -4.6; 35 -4.5; 37 -4.5; 40 -4.4; 42 -4.4; 45 -4.3; 49 -4.2; 52 -4.2; 56 -4.3; 59 -4.3; 64 -4.3; 68 -4.1; 73 -3.8; 78 -3.5; 83 -3.5; 89 -4.5; 95 -5.7; 102 -6.4; 109 -6.5; 117 -6.4; 125 -6.2; 134 -6.1; 143 -6.3; 153 -6.1; 164 -5.6; 175 -5.6; 188 -5.2; 201 -4.9; 215 -4.3; 230 -3.7; 246 -3.2; 263 -2.5; 282 -2.0; 301 -1.4; 323 -1.4; 345 -1.3; 369 -1.4; 395 -2.0; 423 -2.2; 452 -2.0; 484 -2.2; 518 -2.2; 554 -2.1; 593 -1.7; 635 -1.9; 679 -1.8; 726 -1.7; 777 -1.3; 832 -1.1; 890 -0.9; 952 -0.5; 1019 -0.0; 1090 -0.5; 1167 -0.4; 1248 -0.2; 1336 -0.3; 1429 -0.5; 1529 -0.6; 1636 -0.6; 1751 -0.3; 1873 0.3; 2004 0.9; 2145 1.5; 2295 2.3; 2455 3.2; 2627 4.1; 2811 4.7; 3008 5.9; 3219 5.4; 3444 6.0; 3685 5.8; 3943 3.1; 4219 1.1; 4514 0.4; 4830 -0.1; 5168 -0.3; 5530 1.6; 5917 5.0; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999973023095dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.52 | -4.4 dB |
| Peaking | 136 Hz  | 0.95 | -5.7 dB |
| Peaking | 1601 Hz | 0.15 | -1.2 dB |
| Peaking | 3107 Hz | 1.92 | 7.3 dB  |
| Peaking | 6308 Hz | 5.79 | 6.5 dB  |
| Peaking | 320 Hz  | 2.95 | 1.6 dB  |
| Peaking | 622 Hz  | 0.5  | -1.0 dB |
| Peaking | 1023 Hz | 1.89 | 1.5 dB  |
| Peaking | 4642 Hz | 1.51 | 2.3 dB  |
| Peaking | 4779 Hz | 3.18 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)