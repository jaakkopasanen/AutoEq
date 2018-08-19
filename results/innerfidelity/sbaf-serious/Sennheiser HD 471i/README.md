# Sennheiser HD 471i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.1; 22 0.7; 23 0.5; 25 0.2; 26 0.1; 28 -0.0; 30 -0.2; 32 -0.3; 35 -0.4; 37 -0.4; 40 -0.5; 42 -0.4; 45 -0.4; 49 -0.4; 52 -0.3; 56 -0.1; 59 -0.0; 64 0.2; 68 0.3; 73 0.5; 78 0.6; 83 0.8; 89 0.9; 95 0.9; 102 1.4; 109 2.0; 117 2.6; 125 1.9; 134 -0.5; 143 -1.7; 153 -1.7; 164 -0.9; 175 -1.9; 188 -2.6; 201 -2.3; 215 -2.4; 230 -2.5; 246 -2.5; 263 -2.3; 282 -2.0; 301 -1.7; 323 -1.3; 345 -0.8; 369 -0.3; 395 -0.3; 423 -0.3; 452 -0.5; 484 -0.4; 518 -0.5; 554 -0.4; 593 -0.4; 635 -0.5; 679 -0.6; 726 -0.7; 777 -0.3; 832 -0.1; 890 -0.1; 952 -0.0; 1019 0.1; 1090 0.2; 1167 -0.2; 1248 -0.2; 1336 -0.3; 1429 -0.7; 1529 -1.1; 1636 -1.1; 1751 -0.9; 1873 -0.4; 2004 0.6; 2145 2.1; 2295 2.9; 2455 3.1; 2627 4.1; 2811 4.5; 3008 5.0; 3219 5.3; 3444 5.3; 3685 5.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999017734476dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 471i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 114 Hz  | 3.13 | 3.5 dB  |
| Peaking | 204 Hz  | 1.06 | -2.8 dB |
| Peaking | 1638 Hz | 2.88 | -2.6 dB |
| Peaking | 4110 Hz | 0.96 | 6.7 dB  |
| Peaking | 81 Hz   | 4.58 | 0.6 dB  |
| Peaking | 2777 Hz | 2.9  | 1.1 dB  |
| Peaking | 3765 Hz | 2.23 | -0.9 dB |
| Peaking | 6266 Hz | 2.71 | 4.8 dB  |
| Peaking | 7419 Hz | 1.52 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20471i/Sennheiser%20HD%20471i.png)