# Astrotec AM90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.3; 22 3.1; 23 3.1; 25 3.0; 26 3.0; 28 3.0; 30 2.9; 32 2.9; 35 2.7; 37 2.6; 40 2.5; 42 2.4; 45 2.3; 49 2.2; 52 2.1; 56 1.9; 59 1.7; 64 1.4; 68 1.2; 73 0.9; 78 0.6; 83 0.3; 89 -0.0; 95 -0.3; 102 -0.5; 109 -0.6; 117 -0.8; 125 -1.1; 134 -1.3; 143 -1.5; 153 -1.6; 164 -1.8; 175 -1.9; 188 -2.0; 201 -2.0; 215 -2.0; 230 -2.0; 246 -2.1; 263 -2.0; 282 -1.9; 301 -1.9; 323 -1.8; 345 -1.6; 369 -1.6; 395 -1.4; 423 -1.2; 452 -1.0; 484 -0.9; 518 -0.8; 554 -0.5; 593 -0.0; 635 0.1; 679 0.2; 726 0.3; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.6; 1429 0.0; 1529 0.6; 1636 0.8; 1751 0.5; 1873 0.4; 2004 0.3; 2145 0.1; 2295 -0.5; 2455 -1.2; 2627 -2.3; 2811 -3.2; 3008 -0.3; 3219 4.3; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999979483248dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AM90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.66 | 3.1 dB  |
| Peaking | 53 Hz   | 1.37 | 1.2 dB  |
| Peaking | 213 Hz  | 0.7  | -2.3 dB |
| Peaking | 2724 Hz | 4.47 | -6.7 dB |
| Peaking | 4268 Hz | 1.19 | 7.4 dB  |
| Peaking | 1279 Hz | 7.46 | -1.0 dB |
| Peaking | 3385 Hz | 7.67 | 2.9 dB  |
| Peaking | 4255 Hz | 1.47 | -1.3 dB |
| Peaking | 6314 Hz | 2.59 | 5.2 dB  |
| Peaking | 7349 Hz | 1.68 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AM90/Astrotec%20AM90.png)