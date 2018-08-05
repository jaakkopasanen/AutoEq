# Dunu DN2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.4; 22 -4.3; 23 -4.2; 25 -4.1; 26 -4.0; 28 -3.9; 30 -3.8; 32 -3.6; 35 -3.4; 37 -3.2; 40 -3.0; 42 -2.9; 45 -2.6; 49 -2.4; 52 -2.2; 56 -1.9; 59 -1.8; 64 -1.6; 68 -1.4; 73 -1.3; 78 -1.3; 83 -1.3; 89 -1.5; 95 -1.8; 102 -2.1; 109 -2.4; 117 -2.8; 125 -3.2; 134 -3.5; 143 -3.7; 153 -3.8; 164 -3.9; 175 -3.8; 188 -3.8; 201 -3.7; 215 -3.6; 230 -3.4; 246 -3.3; 263 -3.2; 282 -3.0; 301 -2.9; 323 -2.7; 345 -2.6; 369 -2.5; 395 -2.3; 423 -2.1; 452 -1.9; 484 -1.8; 518 -1.6; 554 -1.3; 593 -0.9; 635 -0.8; 679 -0.7; 726 -0.5; 777 -0.1; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.2; 1336 0.2; 1429 0.1; 1529 0.2; 1636 0.3; 1751 0.8; 1873 1.5; 2004 2.2; 2145 2.8; 2295 3.4; 2455 3.9; 2627 4.0; 2811 4.3; 3008 5.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 4.4; 4219 1.3; 4514 -1.5; 4830 -2.4; 5168 -0.3; 5530 2.3; 5917 4.0; 6331 4.1; 6775 3.5; 7249 1.3; 7756 -1.4; 8299 -4.6; 8880 -6.4; 9502 -5.8; 10167 -3.1; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.89 | -4.2 dB |
| Peaking | 202 Hz  | 0.64 | -3.8 dB |
| Peaking | 3096 Hz | 2.04 | 6.3 dB  |
| Peaking | 6471 Hz | 5.08 | 5.1 dB  |
| Peaking | 8957 Hz | 3.83 | -7.5 dB |
| Peaking | 2284 Hz | 3.68 | 1.5 dB  |
| Peaking | 2841 Hz | 4.63 | -1.5 dB |
| Peaking | 3787 Hz | 5.13 | 3.1 dB  |
| Peaking | 4704 Hz | 4.36 | -4.9 dB |
| Peaking | 5681 Hz | 6.65 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000/Dunu%20DN2000.png)