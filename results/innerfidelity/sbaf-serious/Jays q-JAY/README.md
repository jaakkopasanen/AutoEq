# Jays q-JAY

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.4; 22 3.4; 23 3.4; 25 3.4; 26 3.3; 28 3.2; 30 3.1; 32 3.1; 35 3.0; 37 3.0; 40 2.9; 42 2.8; 45 2.7; 49 2.6; 52 2.4; 56 2.2; 59 2.0; 64 1.8; 68 1.6; 73 1.3; 78 1.0; 83 0.7; 89 0.4; 95 0.2; 102 -0.0; 109 -0.2; 117 -0.4; 125 -0.6; 134 -0.9; 143 -1.1; 153 -1.2; 164 -1.3; 175 -1.3; 188 -1.4; 201 -1.6; 215 -1.6; 230 -1.5; 246 -1.5; 263 -1.6; 282 -1.4; 301 -1.4; 323 -1.3; 345 -1.2; 369 -1.1; 395 -1.0; 423 -0.7; 452 -0.6; 484 -0.6; 518 -0.4; 554 -0.2; 593 0.2; 635 0.3; 679 0.3; 726 0.4; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.7; 1429 -0.9; 1529 -1.1; 1636 -1.2; 1751 -0.9; 1873 -0.6; 2004 -0.2; 2145 0.2; 2295 0.9; 2455 1.9; 2627 2.8; 2811 4.1; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 4.0; 4514 3.2; 4830 4.0; 5168 5.4; 5530 5.9; 5917 5.9; 6331 4.8; 6775 3.6; 7249 1.3; 7756 0.3; 8299 -0.7; 8880 -2.0; 9502 -3.6; 10167 -5.0; 10879 -4.7; 11640 -2.1; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715981dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays q-JAY ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.34 | 3.5 dB  |
| Peaking | 49 Hz    | 2.15 | 2.2 dB  |
| Peaking | 3386 Hz  | 2.64 | 6.3 dB  |
| Peaking | 5771 Hz  | 2.59 | 5.9 dB  |
| Peaking | 10194 Hz | 3.15 | -5.9 dB |
| Peaking | 70 Hz    | 2.04 | 0.9 dB  |
| Peaking | 216 Hz   | 0.92 | -1.7 dB |
| Peaking | 1673 Hz  | 2.71 | -1.7 dB |
| Peaking | 2877 Hz  | 7.94 | 1.2 dB  |
| Peaking | 12599 Hz | 7.16 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20q-JAY/Jays%20q-JAY.png)