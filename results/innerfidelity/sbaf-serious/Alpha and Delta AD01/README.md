# Alpha and Delta AD01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.0; 22 -8.0; 23 -8.0; 25 -8.0; 26 -8.0; 28 -8.0; 30 -8.0; 32 -7.9; 35 -7.7; 37 -7.6; 40 -7.5; 42 -7.4; 45 -7.2; 49 -7.0; 52 -6.8; 56 -6.6; 59 -6.5; 64 -6.2; 68 -6.1; 73 -5.9; 78 -5.8; 83 -5.7; 89 -5.8; 95 -6.0; 102 -6.1; 109 -6.3; 117 -6.5; 125 -6.7; 134 -6.8; 143 -6.8; 153 -6.7; 164 -6.5; 175 -6.2; 188 -5.9; 201 -5.6; 215 -5.2; 230 -4.8; 246 -4.5; 263 -4.2; 282 -3.7; 301 -3.4; 323 -3.0; 345 -2.6; 369 -2.3; 395 -1.9; 423 -1.5; 452 -1.2; 484 -1.0; 518 -0.7; 554 -0.2; 593 0.2; 635 0.4; 679 0.5; 726 0.7; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.9; 1336 -1.4; 1429 -1.8; 1529 -2.5; 1636 -3.1; 1751 -3.5; 1873 -3.8; 2004 -4.2; 2145 -4.5; 2295 -4.5; 2455 -3.6; 2627 -2.5; 2811 -0.9; 3008 1.5; 3219 3.8; 3444 5.4; 3685 5.2; 3943 3.3; 4219 0.6; 4514 -1.4; 4830 -0.9; 5168 2.4; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.7; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha and Delta AD01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.32 | -7.9 dB |
| Peaking | 165 Hz  | 0.88 | -5.2 dB |
| Peaking | 2151 Hz | 1.85 | -5.1 dB |
| Peaking | 3451 Hz | 4.59 | 7.1 dB  |
| Peaking | 6035 Hz | 4.8  | 6.9 dB  |
| Peaking | 765 Hz  | 2.26 | 1.6 dB  |
| Peaking | 1589 Hz | 4.85 | -0.9 dB |
| Peaking | 4593 Hz | 6.27 | -5.6 dB |
| Peaking | 4876 Hz | 2.27 | 2.4 dB  |
| Peaking | 9420 Hz | 5.1  | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20and%20Delta%20AD01/Alpha%20and%20Delta%20AD01.png)