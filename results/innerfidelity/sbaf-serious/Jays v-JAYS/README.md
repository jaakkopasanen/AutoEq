# Jays v-JAYS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 4.9; 42 4.2; 45 3.1; 49 1.9; 52 1.0; 56 0.0; 59 -0.6; 64 -1.5; 68 -1.9; 73 -2.4; 78 -2.8; 83 -2.9; 89 -3.0; 95 -3.0; 102 -2.8; 109 -2.6; 117 -2.4; 125 -2.3; 134 -2.0; 143 -1.7; 153 -1.6; 164 -1.4; 175 -1.0; 188 -0.8; 201 -0.6; 215 -0.3; 230 0.1; 246 0.5; 263 1.0; 282 0.8; 301 0.7; 323 -1.2; 345 -1.8; 369 -1.3; 395 -0.8; 423 -0.3; 452 -0.1; 484 -0.0; 518 0.1; 554 0.3; 593 0.7; 635 0.7; 679 0.6; 726 0.5; 777 0.6; 832 0.3; 890 0.4; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.5; 1336 -2.3; 1429 -3.4; 1529 -4.6; 1636 -5.9; 1751 -7.0; 1873 -7.8; 2004 -8.2; 2145 -8.4; 2295 -8.2; 2455 -7.9; 2627 -8.1; 2811 -8.6; 3008 -9.0; 3219 -8.9; 3444 -9.1; 3685 -11.4; 3943 -12.6; 4219 -11.7; 4514 -9.4; 4830 -6.9; 5168 -4.7; 5530 -4.3; 5917 -0.8; 6331 2.7; 6775 1.6; 7249 -1.2; 7756 -3.3; 8299 -5.2; 8880 -6.3; 9502 -5.7; 10167 -2.5; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.5; 15258 -3.5; 16326 -6.5; 17469 -8.5; 18692 -7.9; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays v-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 1.94 | 7.4 dB   |
| Peaking | 2144 Hz  | 1.61 | -7.7 dB  |
| Peaking | 3951 Hz  | 2.36 | -11.4 dB |
| Peaking | 17008 Hz | 2.59 | -4.9 dB  |
| Peaking | 18650 Hz | 1.67 | -6.7 dB  |
| Peaking | 26 Hz    | 0.07 | 1.9 dB   |
| Peaking | 97 Hz    | 0.79 | -5.1 dB  |
| Peaking | 6510 Hz  | 5.81 | 6.9 dB   |
| Peaking | 9230 Hz  | 2.09 | -8.8 dB  |
| Peaking | 10803 Hz | 1.7  | 5.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20v-JAYS/Jays%20v-JAYS.png)