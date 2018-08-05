# Beyerdynamic T50p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.6; 45 5.2; 49 4.8; 52 4.5; 56 4.1; 59 3.8; 64 3.5; 68 3.2; 73 3.0; 78 2.9; 83 2.8; 89 2.6; 95 2.2; 102 2.4; 109 2.8; 117 2.7; 125 2.5; 134 2.3; 143 2.4; 153 2.6; 164 3.0; 175 2.3; 188 1.0; 201 -0.3; 215 -1.3; 230 -2.0; 246 -2.4; 263 -2.5; 282 -2.5; 301 -2.8; 323 -3.2; 345 -3.3; 369 -3.2; 395 -3.0; 423 -2.8; 452 -2.7; 484 -2.7; 518 -2.4; 554 -2.1; 593 -1.7; 635 -1.6; 679 -1.2; 726 -0.5; 777 -0.0; 832 -0.0; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.6; 1248 0.8; 1336 0.9; 1429 0.9; 1529 1.0; 1636 1.1; 1751 1.7; 1873 2.5; 2004 3.6; 2145 5.2; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.39 | 6.2 dB  |
| Peaking | 159 Hz  | 1.7  | 4.0 dB  |
| Peaking | 297 Hz  | 0.68 | -4.2 dB |
| Peaking | 2860 Hz | 1.17 | 6.2 dB  |
| Peaking | 5384 Hz | 2.2  | 5.0 dB  |
| Peaking | 1688 Hz | 4.63 | -1.0 dB |
| Peaking | 2233 Hz | 7.86 | 1.5 dB  |
| Peaking | 6319 Hz | 6.82 | 1.5 dB  |
| Peaking | 6643 Hz | 6.05 | 1.5 dB  |
| Peaking | 7703 Hz | 2    | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)