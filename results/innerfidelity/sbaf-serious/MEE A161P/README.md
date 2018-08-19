# MEE A161P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.5; 22 2.4; 23 2.3; 25 2.2; 26 2.2; 28 2.1; 30 2.1; 32 2.0; 35 1.9; 37 1.8; 40 1.7; 42 1.6; 45 1.5; 49 1.3; 52 1.2; 56 1.0; 59 0.9; 64 0.6; 68 0.4; 73 0.1; 78 -0.1; 83 -0.4; 89 -0.7; 95 -1.0; 102 -1.3; 109 -1.4; 117 -1.6; 125 -1.9; 134 -2.1; 143 -2.3; 153 -2.5; 164 -2.5; 175 -2.5; 188 -2.7; 201 -2.8; 215 -2.6; 230 -2.7; 246 -2.7; 263 -2.6; 282 -2.5; 301 -2.4; 323 -2.3; 345 -2.1; 369 -2.0; 395 -1.8; 423 -1.5; 452 -1.3; 484 -1.2; 518 -1.0; 554 -0.6; 593 -0.2; 635 0.1; 679 0.1; 726 0.3; 777 0.6; 832 0.5; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.6; 1636 -1.9; 1751 -2.1; 1873 -2.2; 2004 -2.4; 2145 -2.9; 2295 -3.4; 2455 -3.4; 2627 -2.7; 2811 -0.4; 3008 3.1; 3219 5.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.8; 4514 3.7; 4830 1.8; 5168 -0.3; 5530 -3.7; 5917 -3.0; 6331 1.3; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999991048581dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE A161P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.49 | 2.4 dB   |
| Peaking | 197 Hz  | 0.69 | -3.1 dB  |
| Peaking | 2531 Hz | 1.51 | -10.8 dB |
| Peaking | 3355 Hz | 1.3  | 12.3 dB  |
| Peaking | 5610 Hz | 6.86 | -7.3 dB  |
| Peaking | 784 Hz  | 2.73 | 1.1 dB   |
| Peaking | 1577 Hz | 6.18 | -0.7 dB  |
| Peaking | 6133 Hz | 5.65 | -1.3 dB  |
| Peaking | 6724 Hz | 6.06 | 4.0 dB   |
| Peaking | 7993 Hz | 1.64 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MEE%20A161P/MEE%20A161P.png)