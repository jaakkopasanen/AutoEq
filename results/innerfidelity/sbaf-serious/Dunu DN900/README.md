# Dunu DN900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.6; 22 -2.4; 23 -2.3; 25 -2.1; 26 -2.0; 28 -1.8; 30 -1.6; 32 -1.4; 35 -1.1; 37 -1.0; 40 -0.7; 42 -0.6; 45 -0.4; 49 -0.1; 52 0.1; 56 0.3; 59 0.5; 64 0.6; 68 0.7; 73 0.8; 78 0.8; 83 0.7; 89 0.5; 95 0.2; 102 -0.2; 109 -0.6; 117 -1.0; 125 -1.5; 134 -1.9; 143 -2.1; 153 -2.3; 164 -2.3; 175 -2.3; 188 -2.2; 201 -2.3; 215 -2.1; 230 -2.1; 246 -2.0; 263 -1.9; 282 -1.8; 301 -1.7; 323 -1.6; 345 -1.5; 369 -1.4; 395 -1.2; 423 -1.0; 452 -0.9; 484 -0.9; 518 -0.8; 554 -0.6; 593 -0.2; 635 -0.2; 679 -0.2; 726 -0.1; 777 0.0; 832 -0.1; 890 -0.2; 952 -0.1; 1019 -0.0; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.1; 1429 -1.5; 1529 -1.8; 1636 -1.9; 1751 -1.7; 1873 -1.3; 2004 -0.5; 2145 0.4; 2295 1.6; 2455 3.2; 2627 4.6; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.83 | -2.6 dB |
| Peaking | 80 Hz   | 1.01 | 3.0 dB  |
| Peaking | 155 Hz  | 0.57 | -3.1 dB |
| Peaking | 1735 Hz | 1.9  | -4.3 dB |
| Peaking | 3744 Hz | 0.86 | 7.2 dB  |
| Peaking | 2268 Hz | 5.61 | -0.8 dB |
| Peaking | 2797 Hz | 3.58 | 1.5 dB  |
| Peaking | 3751 Hz | 2.89 | -1.2 dB |
| Peaking | 6205 Hz | 2.45 | 5.1 dB  |
| Peaking | 7480 Hz | 1.51 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN900/Dunu%20DN900.png)