# Polk Ultrafocus 8000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.2; 22 -3.1; 23 -3.0; 25 -2.9; 26 -2.8; 28 -2.6; 30 -2.4; 32 -2.1; 35 -1.7; 37 -1.4; 40 -1.1; 42 -0.9; 45 -0.6; 49 -0.3; 52 -0.1; 56 0.2; 59 0.5; 64 0.9; 68 1.0; 73 1.2; 78 1.2; 83 1.1; 89 1.1; 95 1.1; 102 1.2; 109 1.4; 117 1.5; 125 1.5; 134 1.6; 143 1.6; 153 1.8; 164 2.1; 175 2.0; 188 1.9; 201 1.9; 215 2.0; 230 2.0; 246 2.0; 263 1.8; 282 1.8; 301 1.7; 323 1.6; 345 1.7; 369 1.8; 395 1.6; 423 1.5; 452 1.4; 484 1.2; 518 1.4; 554 1.6; 593 1.9; 635 1.9; 679 1.6; 726 1.6; 777 1.7; 832 1.7; 890 0.9; 952 0.5; 1019 -0.0; 1090 0.2; 1167 0.4; 1248 0.8; 1336 1.1; 1429 1.4; 1529 1.7; 1636 2.1; 1751 2.4; 1873 3.1; 2004 3.3; 2145 3.7; 2295 4.4; 2455 5.6; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 3.2; 4830 2.6; 5168 4.1; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999991164dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Ultrafocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  1.05 | -3.3 dB |
| Peaking | 174 Hz  |  0.42 | 2.0 dB  |
| Peaking | 638 Hz  |  2.69 | 1.0 dB  |
| Peaking | 3101 Hz |  1.19 | 6.5 dB  |
| Peaking | 5994 Hz |  4.6  | 5.0 dB  |
| Peaking | 1101 Hz |  3.31 | -1.4 dB |
| Peaking | 1357 Hz |  0.54 | 0.4 dB  |
| Peaking | 3124 Hz |  6.09 | -0.9 dB |
| Peaking | 4062 Hz | 11.5  | 1.6 dB  |
| Peaking | 8499 Hz |  3.01 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Ultrafocus%208000/Polk%20Ultrafocus%208000.png)