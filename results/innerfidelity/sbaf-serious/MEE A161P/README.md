# MEE A161P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.5; 22 2.4; 23 2.4; 25 2.3; 26 2.3; 28 2.3; 30 2.3; 32 2.3; 35 2.2; 37 2.2; 40 2.1; 42 2.1; 45 2.0; 49 2.0; 52 2.0; 56 2.0; 59 2.0; 64 1.9; 68 1.8; 73 1.7; 78 1.5; 83 1.3; 89 0.9; 95 0.4; 102 -0.2; 109 -0.7; 117 -1.2; 125 -1.9; 134 -2.4; 143 -2.7; 153 -3.0; 164 -3.1; 175 -3.1; 188 -3.1; 201 -3.2; 215 -3.0; 230 -3.0; 246 -2.9; 263 -2.8; 282 -2.7; 301 -2.6; 323 -2.4; 345 -2.2; 369 -2.0; 395 -1.9; 423 -1.6; 452 -1.3; 484 -1.2; 518 -1.0; 554 -0.6; 593 -0.2; 635 0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.5; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.6; 1636 -1.9; 1751 -2.1; 1873 -2.2; 2004 -2.4; 2145 -2.9; 2295 -3.4; 2455 -3.4; 2627 -2.7; 2811 -0.4; 3008 3.1; 3219 5.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.8; 4514 3.7; 4830 1.8; 5168 -0.3; 5530 -3.7; 5917 -3.0; 6331 1.3; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE A161P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 134 Hz  | 0.17 | 4.9 dB   |
| Peaking | 209 Hz  | 0.48 | -8.1 dB  |
| Peaking | 2551 Hz | 1.27 | -11.1 dB |
| Peaking | 3389 Hz | 1.33 | 13.4 dB  |
| Peaking | 5608 Hz | 7.13 | -7.2 dB  |
| Peaking | 13 Hz   | 1.79 | 1.2 dB   |
| Peaking | 2093 Hz | 6.16 | 0.8 dB   |
| Peaking | 6095 Hz | 7.96 | -1.4 dB  |
| Peaking | 6695 Hz | 5.31 | 4.1 dB   |
| Peaking | 7594 Hz | 1.53 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MEE%20A161P/MEE%20A161P.png)