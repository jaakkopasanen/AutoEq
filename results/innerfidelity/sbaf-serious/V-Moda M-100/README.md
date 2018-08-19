# V-Moda M-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.7; 23 -3.8; 25 -3.9; 26 -3.9; 28 -4.0; 30 -4.1; 32 -4.1; 35 -4.2; 37 -4.3; 40 -4.3; 42 -4.4; 45 -4.4; 49 -4.5; 52 -4.6; 56 -4.8; 59 -4.8; 64 -4.9; 68 -5.0; 73 -4.9; 78 -5.1; 83 -5.3; 89 -5.2; 95 -5.0; 102 -4.9; 109 -5.3; 117 -5.8; 125 -6.2; 134 -6.4; 143 -6.3; 153 -5.9; 164 -5.0; 175 -4.8; 188 -4.6; 201 -3.9; 215 -3.0; 230 -2.1; 246 -1.1; 263 -0.2; 282 0.6; 301 0.7; 323 1.6; 345 2.8; 369 3.6; 395 4.2; 423 4.5; 452 4.5; 484 4.1; 518 3.6; 554 3.5; 593 3.2; 635 2.7; 679 2.1; 726 1.6; 777 1.3; 832 0.8; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.4; 1429 -0.7; 1529 -0.8; 1636 -0.9; 1751 -0.8; 1873 -0.6; 2004 -0.5; 2145 -0.7; 2295 -0.3; 2455 0.0; 2627 0.2; 2811 0.2; 3008 1.0; 3219 1.1; 3444 0.9; 3685 1.0; 3943 1.3; 4219 2.0; 4514 3.3; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.8; 9502 -4.2; 10167 -4.1; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099566618642662dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.69 | -2.9 dB |
| Peaking | 64 Hz   | 0.7  | -3.3 dB |
| Peaking | 150 Hz  | 1.11 | -5.2 dB |
| Peaking | 431 Hz  | 1.45 | 5.5 dB  |
| Peaking | 5465 Hz | 2.86 | 7.1 dB  |
| Peaking | 620 Hz  | 6.47 | 0.9 dB  |
| Peaking | 744 Hz  | 5.91 | 0.3 dB  |
| Peaking | 1611 Hz | 1.28 | -1.2 dB |
| Peaking | 7834 Hz | 0.71 | 0.9 dB  |
| Peaking | 9705 Hz | 4.01 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20M-100/V-Moda%20M-100.png)