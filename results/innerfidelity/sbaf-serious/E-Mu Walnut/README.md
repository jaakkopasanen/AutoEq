# E-Mu Walnut

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.0; 22 -0.3; 23 -0.5; 25 -0.8; 26 -0.9; 28 -1.1; 30 -1.2; 32 -1.3; 35 -1.5; 37 -1.6; 40 -1.6; 42 -1.7; 45 -1.7; 49 -1.9; 52 -1.9; 56 -1.9; 59 -1.8; 64 -1.8; 68 -1.9; 73 -1.8; 78 -1.9; 83 -2.0; 89 -2.0; 95 -2.2; 102 -2.4; 109 -2.5; 117 -2.7; 125 -2.9; 134 -3.1; 143 -3.2; 153 -3.2; 164 -3.0; 175 -2.8; 188 -2.6; 201 -2.5; 215 -2.1; 230 -1.9; 246 -1.7; 263 -1.4; 282 -1.0; 301 -0.6; 323 -0.4; 345 -0.1; 369 0.1; 395 0.3; 423 0.7; 452 0.7; 484 0.6; 518 0.5; 554 0.5; 593 0.6; 635 0.3; 679 0.0; 726 -0.1; 777 -0.0; 832 -0.2; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.5; 1167 0.9; 1248 1.0; 1336 0.9; 1429 0.8; 1529 0.6; 1636 0.6; 1751 0.8; 1873 1.5; 2004 2.3; 2145 3.2; 2295 4.0; 2455 4.8; 2627 4.0; 2811 3.1; 3008 2.9; 3219 2.7; 3444 3.2; 3685 4.7; 3943 5.4; 4219 2.4; 4514 1.1; 4830 3.5; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -0.7; 10167 -0.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Walnut ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.66 | -1.7 dB |
| Peaking | 153 Hz  | 1.32 | -2.9 dB |
| Peaking | 3795 Hz | 5.94 | 4.1 dB  |
| Peaking | 2445 Hz | 2.55 | 4.4 dB  |
| Peaking | 5763 Hz | 3.31 | 6.6 dB  |
| Peaking | 242 Hz  | 3.52 | -0.6 dB |
| Peaking | 448 Hz  | 2.39 | 1.0 dB  |
| Peaking | 6650 Hz | 9.49 | 2.0 dB  |
| Peaking | 1231 Hz | 7.63 | 0.8 dB  |
| Peaking | 8691 Hz | 1.61 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Walnut/E-Mu%20Walnut.png)