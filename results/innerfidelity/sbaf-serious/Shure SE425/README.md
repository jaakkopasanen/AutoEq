# Shure SE425

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.8; 30 5.6; 32 5.5; 35 5.3; 37 5.1; 40 4.9; 42 4.8; 45 4.7; 49 4.5; 52 4.4; 56 4.2; 59 4.1; 64 3.9; 68 3.7; 73 3.5; 78 3.2; 83 2.9; 89 2.4; 95 1.9; 102 1.2; 109 0.6; 117 0.1; 125 -0.6; 134 -1.2; 143 -1.5; 153 -1.8; 164 -2.0; 175 -2.1; 188 -2.1; 201 -2.1; 215 -2.1; 230 -2.1; 246 -2.0; 263 -2.0; 282 -1.9; 301 -1.8; 323 -1.7; 345 -1.6; 369 -1.5; 395 -1.3; 423 -1.1; 452 -0.9; 484 -0.9; 518 -0.7; 554 -0.4; 593 -0.0; 635 0.1; 679 0.1; 726 0.3; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.1; 1529 -1.5; 1636 -1.7; 1751 -2.0; 1873 -2.0; 2004 -2.0; 2145 -2.1; 2295 -2.1; 2455 -1.3; 2627 -0.5; 2811 0.4; 3008 1.7; 3219 2.6; 3444 3.3; 3685 3.5; 3943 3.6; 4219 3.1; 4514 3.0; 4830 3.9; 5168 5.5; 5530 6.0; 5917 5.9; 6331 4.8; 6775 2.8; 7249 0.7; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.06 | 6.3 dB  |
| Peaking | 61 Hz   | 2.1  | 3.3 dB  |
| Peaking | 2261 Hz | 1.21 | -3.3 dB |
| Peaking | 5653 Hz | 3.34 | 6.1 dB  |
| Peaking | 3463 Hz | 1.84 | 4.5 dB  |
| Peaking | 89 Hz   | 1.93 | 2.2 dB  |
| Peaking | 194 Hz  | 0.59 | -2.6 dB |
| Peaking | 788 Hz  | 1.7  | 1.1 dB  |
| Peaking | 8235 Hz | 4.44 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE425/Shure%20SE425.png)