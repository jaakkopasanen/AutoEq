# Sennheiser HD 419

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.7; 22 -5.0; 23 -5.1; 25 -5.3; 26 -5.4; 28 -5.6; 30 -5.7; 32 -5.8; 35 -6.0; 37 -6.1; 40 -6.2; 42 -6.2; 45 -6.3; 49 -6.3; 52 -6.4; 56 -6.5; 59 -6.5; 64 -6.5; 68 -6.4; 73 -6.6; 78 -6.9; 83 -6.7; 89 -5.7; 95 -4.7; 102 -5.8; 109 -7.5; 117 -8.3; 125 -8.8; 134 -9.0; 143 -9.2; 153 -9.2; 164 -8.8; 175 -9.1; 188 -9.1; 201 -9.1; 215 -9.0; 230 -8.5; 246 -8.0; 263 -7.3; 282 -6.7; 301 -5.8; 323 -4.8; 345 -3.8; 369 -3.1; 395 -2.9; 423 -2.5; 452 -2.0; 484 -2.0; 518 -2.4; 554 -2.7; 593 -2.6; 635 -2.1; 679 -1.2; 726 -0.8; 777 -0.9; 832 -0.6; 890 0.0; 952 0.1; 1019 0.1; 1090 -0.2; 1167 -0.4; 1248 -0.2; 1336 -0.6; 1429 -1.2; 1529 -1.5; 1636 -1.6; 1751 -1.6; 1873 -1.4; 2004 -0.6; 2145 0.6; 2295 1.8; 2455 2.5; 2627 1.9; 2811 2.7; 3008 3.2; 3219 3.3; 3444 3.5; 3685 4.4; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.7; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999017734476dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.64 | -5.2 dB |
| Peaking | 65 Hz   | 1.46 | -3.0 dB |
| Peaking | 128 Hz  | 2.96 | -3.1 dB |
| Peaking | 203 Hz  | 0.89 | -8.3 dB |
| Peaking | 4698 Hz | 1.43 | 6.8 dB  |
| Peaking | 371 Hz  | 5.35 | 0.7 dB  |
| Peaking | 1796 Hz | 2.19 | -4.0 dB |
| Peaking | 2211 Hz | 1.2  | 2.5 dB  |
| Peaking | 6342 Hz | 3.73 | 5.3 dB  |
| Peaking | 6734 Hz | 1.35 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)