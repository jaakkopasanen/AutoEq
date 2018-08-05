# NarMoo B2M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.4; 22 -7.3; 23 -7.3; 25 -7.2; 26 -7.2; 28 -7.0; 30 -6.9; 32 -6.7; 35 -6.5; 37 -6.4; 40 -6.1; 42 -6.0; 45 -5.8; 49 -5.5; 52 -5.2; 56 -5.0; 59 -4.8; 64 -4.5; 68 -4.3; 73 -4.1; 78 -4.0; 83 -3.9; 89 -4.0; 95 -4.1; 102 -4.4; 109 -4.6; 117 -4.8; 125 -5.1; 134 -5.3; 143 -5.3; 153 -5.3; 164 -5.2; 175 -4.9; 188 -4.7; 201 -4.5; 215 -4.3; 230 -4.0; 246 -3.8; 263 -3.6; 282 -3.2; 301 -3.0; 323 -2.8; 345 -2.5; 369 -2.3; 395 -2.1; 423 -1.8; 452 -1.5; 484 -1.4; 518 -1.2; 554 -0.9; 593 -0.5; 635 -0.3; 679 -0.3; 726 -0.1; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.8; 1529 -1.1; 1636 -1.5; 1751 -0.5; 1873 0.2; 2004 0.4; 2145 0.4; 2295 0.5; 2455 0.9; 2627 1.5; 2811 2.3; 3008 4.0; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 3.3; 4830 2.3; 5168 3.9; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo B2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.8  | -6.1 dB |
| Peaking | 39 Hz   | 0.88 | -3.5 dB |
| Peaking | 163 Hz  | 0.64 | -4.8 dB |
| Peaking | 3610 Hz | 2.64 | 6.5 dB  |
| Peaking | 5957 Hz | 3.92 | 5.9 dB  |
| Peaking | 812 Hz  | 3.02 | 0.8 dB  |
| Peaking | 1655 Hz | 3.45 | -2.0 dB |
| Peaking | 1833 Hz | 6.46 | 1.1 dB  |
| Peaking | 6682 Hz | 8.73 | 1.6 dB  |
| Peaking | 7804 Hz | 2.69 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20B2M/NarMoo%20B2M.png)