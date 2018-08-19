# ViSang VS-K1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.2; 22 3.7; 23 3.5; 25 3.1; 26 2.9; 28 2.6; 30 2.3; 32 2.1; 35 1.8; 37 1.6; 40 1.3; 42 1.2; 45 0.9; 49 0.7; 52 0.5; 56 0.2; 59 0.1; 64 -0.2; 68 -0.4; 73 -0.7; 78 -0.9; 83 -1.2; 89 -1.5; 95 -1.7; 102 -1.9; 109 -1.9; 117 -2.0; 125 -2.1; 134 -2.3; 143 -2.3; 153 -2.3; 164 -2.3; 175 -2.2; 188 -2.1; 201 -2.0; 215 -1.9; 230 -1.7; 246 -1.6; 263 -1.4; 282 -1.1; 301 -0.9; 323 -0.7; 345 -0.4; 369 -0.3; 395 -0.1; 423 0.3; 452 0.4; 484 0.5; 518 0.6; 554 0.9; 593 1.2; 635 1.2; 679 1.2; 726 1.2; 777 1.3; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -0.4; 1248 -0.7; 1336 -1.5; 1429 -1.9; 1529 -0.7; 1636 -1.0; 1751 -2.5; 1873 -2.4; 2004 -1.6; 2145 -0.5; 2295 1.1; 2455 3.2; 2627 5.1; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999918779dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ViSang VS-K1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.53 | 4.7 dB  |
| Peaking | 138 Hz  | 0.64 | -2.6 dB |
| Peaking | 619 Hz  | 1.59 | 1.5 dB  |
| Peaking | 1836 Hz | 1.59 | -5.7 dB |
| Peaking | 3509 Hz | 0.81 | 7.8 dB  |
| Peaking | 1099 Hz | 6.86 | -0.6 dB |
| Peaking | 2720 Hz | 7    | 1.8 dB  |
| Peaking | 3693 Hz | 2.83 | -1.1 dB |
| Peaking | 6263 Hz | 2.25 | 5.8 dB  |
| Peaking | 7336 Hz | 1.47 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ViSang%20VS-K1/ViSang%20VS-K1.png)