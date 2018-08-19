# Alpha and Delta AD01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -8.1; 22 -8.1; 23 -8.1; 25 -8.1; 26 -8.1; 28 -8.1; 30 -8.1; 32 -8.1; 35 -8.0; 37 -8.0; 40 -7.9; 42 -7.9; 45 -7.8; 49 -7.7; 52 -7.6; 56 -7.6; 59 -7.6; 64 -7.5; 68 -7.5; 73 -7.4; 78 -7.4; 83 -7.4; 89 -7.4; 95 -7.4; 102 -7.2; 109 -7.0; 117 -6.8; 125 -6.7; 134 -6.6; 143 -6.4; 153 -6.2; 164 -6.0; 175 -5.7; 188 -5.4; 201 -5.2; 215 -4.8; 230 -4.5; 246 -4.2; 263 -3.9; 282 -3.5; 301 -3.2; 323 -2.9; 345 -2.5; 369 -2.2; 395 -1.9; 423 -1.4; 452 -1.1; 484 -1.0; 518 -0.7; 554 -0.2; 593 0.2; 635 0.4; 679 0.5; 726 0.7; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.9; 1336 -1.4; 1429 -1.8; 1529 -2.5; 1636 -3.1; 1751 -3.5; 1873 -3.8; 2004 -4.2; 2145 -4.5; 2295 -4.5; 2455 -3.6; 2627 -2.5; 2811 -0.9; 3008 1.5; 3219 3.8; 3444 5.4; 3685 5.2; 3943 3.3; 4219 0.6; 4514 -1.4; 4830 -0.9; 5168 2.4; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.7; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.052587415132024dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha and Delta AD01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 42 Hz   |  0.19 | -8.2 dB |
| Peaking | 2150 Hz |  1.99 | -5.1 dB |
| Peaking | 3454 Hz |  4.71 | 7.0 dB  |
| Peaking | 6070 Hz |  4.33 | 6.8 dB  |
| Peaking | 9335 Hz |  3.91 | -1.8 dB |
| Peaking | 205 Hz  |  1.25 | -0.7 dB |
| Peaking | 721 Hz  |  1.38 | 1.8 dB  |
| Peaking | 1564 Hz |  4.35 | -1.1 dB |
| Peaking | 4607 Hz | 10.92 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20and%20Delta%20AD01/Alpha%20and%20Delta%20AD01.png)