# Stax SR-Sigma 07381

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.7; 73 4.7; 78 3.7; 83 2.8; 89 2.1; 95 1.5; 102 1.2; 109 1.3; 117 1.4; 125 1.5; 134 1.8; 143 2.2; 153 2.8; 164 3.1; 175 0.0; 188 -1.7; 201 -0.7; 215 -0.3; 230 -0.9; 246 -1.3; 263 -1.1; 282 -0.8; 301 -0.6; 323 -0.2; 345 0.3; 369 0.7; 395 0.8; 423 1.3; 452 1.7; 484 2.0; 518 2.3; 554 2.7; 593 3.0; 635 2.5; 679 1.3; 726 0.9; 777 0.7; 832 0.1; 890 0.1; 952 0.4; 1019 0.2; 1090 1.3; 1167 0.8; 1248 2.0; 1336 3.3; 1429 3.9; 1529 5.3; 1636 5.8; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.9; 5530 3.9; 5917 2.6; 6331 2.9; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Sigma 07381 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.42 | 6.2 dB  |
| Peaking | 62 Hz   | 3.15 | 2.4 dB  |
| Peaking | 558 Hz  | 1.31 | 7.8 dB  |
| Peaking | 697 Hz  | 0.57 | -7.4 dB |
| Peaking | 2226 Hz | 0.5  | 8.3 dB  |
| Peaking | 163 Hz  | 5.18 | 5.1 dB  |
| Peaking | 178 Hz  | 4    | -3.7 dB |
| Peaking | 1612 Hz | 4.05 | 1.7 dB  |
| Peaking | 4848 Hz | 1.36 | 5.1 dB  |
| Peaking | 5190 Hz | 0.56 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Sigma%2007381/Stax%20SR-Sigma%2007381.png)