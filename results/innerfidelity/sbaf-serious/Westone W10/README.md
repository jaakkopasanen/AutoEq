# Westone W10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.7; 26 5.6; 28 5.3; 30 5.0; 32 4.8; 35 4.6; 37 4.4; 40 4.2; 42 4.0; 45 3.8; 49 3.7; 52 3.6; 56 3.4; 59 3.3; 64 3.2; 68 3.0; 73 2.8; 78 2.6; 83 2.3; 89 1.8; 95 1.3; 102 0.7; 109 0.2; 117 -0.4; 125 -1.1; 134 -1.6; 143 -1.9; 153 -2.2; 164 -2.4; 175 -2.4; 188 -2.4; 201 -2.5; 215 -2.5; 230 -2.4; 246 -2.4; 263 -2.4; 282 -2.2; 301 -2.1; 323 -2.0; 345 -1.9; 369 -1.9; 395 -1.9; 423 -1.6; 452 -1.4; 484 -1.3; 518 -1.2; 554 -0.8; 593 -0.4; 635 -0.2; 679 -0.3; 726 -0.2; 777 0.1; 832 0.1; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 0.0; 1248 0.0; 1336 -0.0; 1429 -0.1; 1529 -0.0; 1636 0.2; 1751 0.6; 1873 1.3; 2004 2.1; 2145 2.9; 2295 3.7; 2455 4.6; 2627 5.2; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.33 | 6.2 dB  |
| Peaking | 80 Hz   | 1.04 | 3.5 dB  |
| Peaking | 143 Hz  | 0.41 | -3.9 dB |
| Peaking | 3949 Hz | 0.95 | 7.0 dB  |
| Peaking | 1608 Hz | 2.54 | -1.5 dB |
| Peaking | 2674 Hz | 2.12 | 1.7 dB  |
| Peaking | 3846 Hz | 2.6  | -1.4 dB |
| Peaking | 6231 Hz | 2.54 | 5.1 dB  |
| Peaking | 7459 Hz | 1.55 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W10/Westone%20W10.png)