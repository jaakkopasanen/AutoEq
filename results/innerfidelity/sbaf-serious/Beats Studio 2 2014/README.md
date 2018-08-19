# Beats Studio 2 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.2; 23 4.7; 25 3.7; 26 3.1; 28 2.2; 30 1.4; 32 1.0; 35 0.6; 37 0.5; 40 0.4; 42 0.4; 45 0.3; 49 0.3; 52 0.3; 56 0.2; 59 0.2; 64 0.1; 68 0.0; 73 -0.0; 78 -0.2; 83 -0.3; 89 -0.5; 95 -0.7; 102 -0.6; 109 -0.4; 117 -0.2; 125 -0.1; 134 0.1; 143 0.3; 153 0.5; 164 0.7; 175 1.0; 188 1.3; 201 1.6; 215 1.9; 230 2.4; 246 2.8; 263 3.2; 282 4.0; 301 4.7; 323 5.5; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.5; 635 3.3; 679 1.0; 726 -0.5; 777 -1.2; 832 -1.5; 890 -0.9; 952 -0.2; 1019 -0.1; 1090 0.2; 1167 0.1; 1248 -0.3; 1336 -0.0; 1429 0.6; 1529 1.0; 1636 1.1; 1751 2.2; 1873 3.0; 2004 3.8; 2145 4.4; 2295 4.8; 2455 5.2; 2627 5.2; 2811 4.5; 3008 3.3; 3219 1.2; 3444 0.9; 3685 1.8; 3943 3.4; 4219 4.7; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -1.5; 10167 -1.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.43 | 5.6 dB  |
| Peaking | 465 Hz  | 0.98 | 7.5 dB  |
| Peaking | 800 Hz  | 2.04 | -4.9 dB |
| Peaking | 2385 Hz | 2.59 | 5.0 dB  |
| Peaking | 5270 Hz | 2.22 | 6.7 dB  |
| Peaking | 105 Hz  | 1.61 | -1.1 dB |
| Peaking | 319 Hz  | 5.99 | 1.1 dB  |
| Peaking | 3395 Hz | 8.36 | -2.2 dB |
| Peaking | 6929 Hz | 0.7  | 1.0 dB  |
| Peaking | 9302 Hz | 2.02 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%202014/Beats%20Studio%202%202014.png)