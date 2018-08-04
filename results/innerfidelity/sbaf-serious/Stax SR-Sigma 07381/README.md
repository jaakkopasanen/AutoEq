# Stax SR-Sigma 07381

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.4; 78 4.5; 83 3.6; 89 2.8; 95 2.2; 102 1.7; 109 1.7; 117 1.6; 125 1.5; 134 1.7; 143 2.0; 153 2.5; 164 2.9; 175 -0.2; 188 -1.9; 201 -0.9; 215 -0.5; 230 -1.1; 246 -1.4; 263 -1.2; 282 -0.9; 301 -0.6; 323 -0.2; 345 0.3; 369 0.6; 395 0.8; 423 1.3; 452 1.7; 484 2.0; 518 2.3; 554 2.7; 593 3.0; 635 2.5; 679 1.2; 726 0.9; 777 0.7; 832 0.1; 890 0.1; 952 0.4; 1019 0.2; 1090 1.3; 1167 0.8; 1248 2.0; 1336 3.3; 1429 3.9; 1529 5.3; 1636 5.8; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.9; 5530 3.9; 5917 2.6; 6331 2.9; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Sigma 07381 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.37 | 6.2 dB  |
| Peaking | 65 Hz   | 3.01 | 2.1 dB  |
| Peaking | 658 Hz  | 0.51 | -7.6 dB |
| Peaking | 549 Hz  | 1.24 | 8.2 dB  |
| Peaking | 2214 Hz | 0.5  | 8.5 dB  |
| Peaking | 165 Hz  | 5.73 | 4.3 dB  |
| Peaking | 183 Hz  | 5.12 | -3.6 dB |
| Peaking | 1065 Hz | 3.88 | -0.7 dB |
| Peaking | 4889 Hz | 3.81 | 2.4 dB  |
| Peaking | 8863 Hz | 1.32 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Sigma%2007381/Stax%20SR-Sigma%2007381.png)