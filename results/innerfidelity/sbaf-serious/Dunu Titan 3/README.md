# Dunu Titan 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.3; 23 -1.3; 25 -1.3; 26 -1.3; 28 -1.4; 30 -1.4; 32 -1.4; 35 -1.4; 37 -1.4; 40 -1.4; 42 -1.4; 45 -1.4; 49 -1.4; 52 -1.3; 56 -1.1; 59 -1.1; 64 -1.3; 68 -1.3; 73 -1.3; 78 -1.4; 83 -1.5; 89 -1.8; 95 -2.2; 102 -2.6; 109 -2.9; 117 -3.4; 125 -3.8; 134 -4.1; 143 -4.2; 153 -4.3; 164 -4.2; 175 -4.1; 188 -3.9; 201 -3.7; 215 -3.4; 230 -3.1; 246 -2.9; 263 -2.6; 282 -2.2; 301 -2.0; 323 -1.8; 345 -1.5; 369 -1.2; 395 -0.9; 423 -0.1; 452 0.2; 484 0.0; 518 0.2; 554 0.5; 593 0.8; 635 1.0; 679 0.9; 726 1.0; 777 1.0; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.3; 1529 -2.9; 1636 -3.5; 1751 -3.9; 1873 -4.2; 2004 -4.5; 2145 -4.8; 2295 -5.1; 2455 -4.7; 2627 -4.1; 2811 -2.9; 3008 -1.0; 3219 0.9; 3444 2.1; 3685 2.2; 3943 1.2; 4219 -1.4; 4514 -4.1; 4830 -7.4; 5168 -8.9; 5530 -5.1; 5917 -0.1; 6331 2.9; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.5dB` and instead set Global volume in the UI for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 155 Hz  | 0.96 | -4.4 dB  |
| Peaking | 2233 Hz | 1.65 | -5.7 dB  |
| Peaking | 3614 Hz | 3.05 | 5.4 dB   |
| Peaking | 5098 Hz | 3.71 | -10.6 dB |
| Peaking | 6455 Hz | 4.23 | 6.2 dB   |
| Peaking | 40 Hz   | 2.14 | -0.8 dB  |
| Peaking | 25 Hz   | 1.29 | -1.2 dB  |
| Peaking | 301 Hz  | 2.06 | -0.8 dB  |
| Peaking | 699 Hz  | 1.1  | 1.6 dB   |
| Peaking | 1521 Hz | 3.31 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%203/Dunu%20Titan%203.png)