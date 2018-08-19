# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.1; 22 2.4; 23 1.8; 25 0.7; 26 0.3; 28 -0.3; 30 -0.7; 32 -0.9; 35 -0.9; 37 -0.9; 40 -0.7; 42 -0.6; 45 -0.5; 49 -0.3; 52 -0.2; 56 -0.2; 59 -0.3; 64 -0.4; 68 -0.6; 73 -1.0; 78 -1.4; 83 -1.7; 89 -2.2; 95 -2.5; 102 -2.9; 109 -2.8; 117 -2.9; 125 -3.0; 134 -2.9; 143 -2.9; 153 -2.8; 164 -2.9; 175 -2.8; 188 -2.9; 201 -2.9; 215 -2.8; 230 -2.7; 246 -2.6; 263 -2.6; 282 -2.3; 301 -2.3; 323 -2.2; 345 -2.2; 369 -2.2; 395 -2.2; 423 -2.1; 452 -2.2; 484 -2.1; 518 -2.0; 554 -1.6; 593 -1.1; 635 -1.1; 679 -1.3; 726 -1.1; 777 -0.6; 832 -0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -2.0; 1336 -3.1; 1429 -4.2; 1529 -5.4; 1636 -6.0; 1751 -5.6; 1873 -4.6; 2004 -3.7; 2145 -2.9; 2295 -2.3; 2455 -1.6; 2627 -1.1; 2811 -0.3; 3008 1.1; 3219 2.1; 3444 2.4; 3685 1.4; 3943 -0.5; 4219 -2.5; 4514 -1.8; 4830 1.4; 5168 5.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.4; 7249 -2.2; 7756 -2.3; 8299 -0.6; 8880 0.0; 9502 -0.3; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.090907327114607dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 155 Hz  |  0.71 | -3.1 dB |
| Peaking | 425 Hz  |  1.75 | -1.4 dB |
| Peaking | 1691 Hz |  2.34 | -6.1 dB |
| Peaking | 3304 Hz |  7.61 | 3.2 dB  |
| Peaking | 5762 Hz |  5.14 | 7.3 dB  |
| Peaking | 61 Hz   |  4.01 | 0.7 dB  |
| Peaking | 961 Hz  |  4.88 | 1.3 dB  |
| Peaking | 4324 Hz | 10.14 | -3.7 dB |
| Peaking | 6601 Hz |  6.07 | 3.9 dB  |
| Peaking | 7343 Hz |  5.25 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)