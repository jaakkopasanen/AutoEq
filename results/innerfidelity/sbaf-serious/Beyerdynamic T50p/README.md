# Beyerdynamic T50p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.7; 49 5.2; 52 4.8; 56 4.3; 59 3.9; 64 3.4; 68 3.0; 73 2.6; 78 2.4; 83 2.2; 89 1.9; 95 1.5; 102 1.6; 109 2.0; 117 1.6; 125 1.8; 134 1.7; 143 1.4; 153 1.8; 164 2.1; 175 1.6; 188 0.2; 201 -1.1; 215 -2.0; 230 -2.4; 246 -2.6; 263 -2.5; 282 -2.4; 301 -2.6; 323 -2.6; 345 -2.6; 369 -2.6; 395 -2.6; 423 -2.4; 452 -2.4; 484 -2.4; 518 -2.2; 554 -1.9; 593 -1.5; 635 -1.4; 679 -1.4; 726 -0.8; 777 0.2; 832 0.3; 890 0.1; 952 -0.0; 1019 0.1; 1090 0.3; 1167 0.5; 1248 0.7; 1336 0.8; 1429 0.5; 1529 0.3; 1636 0.2; 1751 0.4; 1873 1.0; 2004 1.8; 2145 3.1; 2295 4.7; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 30 Hz   | 0.47 | 6.4 dB  |
| Peaking | 163 Hz  | 2.12 | 3.7 dB  |
| Peaking | 263 Hz  | 0.62 | -3.8 dB |
| Peaking | 5373 Hz | 2.15 | 5.3 dB  |
| Peaking | 3014 Hz | 1.44 | 6.1 dB  |
| Peaking | 1744 Hz | 2.61 | -3.2 dB |
| Peaking | 1775 Hz | 1.21 | 2.0 dB  |
| Peaking | 6758 Hz | 4.9  | 1.0 dB  |
| Peaking | 6391 Hz | 5.8  | 2.5 dB  |
| Peaking | 7385 Hz | 1.82 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)