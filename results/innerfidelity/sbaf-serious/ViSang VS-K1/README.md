# ViSang VS-K1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.2; 22 3.8; 23 3.5; 25 3.2; 26 3.0; 28 2.7; 30 2.5; 32 2.3; 35 2.1; 37 1.9; 40 1.7; 42 1.6; 45 1.5; 49 1.4; 52 1.3; 56 1.2; 59 1.2; 64 1.1; 68 1.0; 73 0.9; 78 0.7; 83 0.4; 89 0.1; 95 -0.3; 102 -0.8; 109 -1.2; 117 -1.7; 125 -2.1; 134 -2.5; 143 -2.7; 153 -2.8; 164 -2.8; 175 -2.7; 188 -2.6; 201 -2.5; 215 -2.2; 230 -2.0; 246 -1.8; 263 -1.6; 282 -1.3; 301 -1.1; 323 -0.8; 345 -0.5; 369 -0.3; 395 -0.1; 423 0.2; 452 0.4; 484 0.4; 518 0.6; 554 0.9; 593 1.2; 635 1.2; 679 1.2; 726 1.2; 777 1.2; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -0.4; 1248 -0.7; 1336 -1.5; 1429 -1.9; 1529 -0.7; 1636 -1.0; 1751 -2.5; 1873 -2.4; 2004 -1.6; 2145 -0.5; 2295 1.1; 2455 3.2; 2627 5.1; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ViSang VS-K1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.19 | 3.6 dB  |
| Peaking | 166 Hz  | 1.05 | -3.3 dB |
| Peaking | 641 Hz  | 1.88 | 1.5 dB  |
| Peaking | 1836 Hz | 1.61 | -5.7 dB |
| Peaking | 3513 Hz | 0.81 | 7.8 dB  |
| Peaking | 1107 Hz | 5.93 | -0.6 dB |
| Peaking | 2726 Hz | 6.91 | 1.8 dB  |
| Peaking | 3686 Hz | 2.77 | -1.1 dB |
| Peaking | 6239 Hz | 2.29 | 5.5 dB  |
| Peaking | 7397 Hz | 1.48 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ViSang%20VS-K1/ViSang%20VS-K1.png)