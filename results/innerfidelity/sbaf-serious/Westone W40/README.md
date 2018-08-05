# Westone W40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.3; 22 3.7; 23 3.4; 25 2.9; 26 2.7; 28 2.3; 30 1.9; 32 1.6; 35 1.3; 37 1.0; 40 0.7; 42 0.6; 45 0.4; 49 0.1; 52 -0.0; 56 -0.2; 59 -0.4; 64 -0.6; 68 -0.8; 73 -1.0; 78 -1.3; 83 -1.6; 89 -2.1; 95 -2.6; 102 -3.3; 109 -3.8; 117 -4.3; 125 -5.0; 134 -5.5; 143 -5.8; 153 -6.0; 164 -6.2; 175 -6.3; 188 -6.3; 201 -6.2; 215 -6.2; 230 -6.0; 246 -6.0; 263 -5.9; 282 -5.7; 301 -5.5; 323 -5.3; 345 -5.1; 369 -4.9; 395 -4.7; 423 -4.2; 452 -3.9; 484 -3.7; 518 -3.3; 554 -2.8; 593 -2.2; 635 -1.8; 679 -1.5; 726 -1.1; 777 -0.6; 832 -0.3; 890 -0.1; 952 0.0; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.3; 1429 -0.4; 1529 -0.4; 1636 -0.3; 1751 0.3; 1873 0.9; 2004 1.8; 2145 2.7; 2295 3.5; 2455 4.5; 2627 5.2; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.8; 9502 -4.0; 10167 -3.4; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.74 | 5.6 dB  |
| Peaking | 146 Hz  | 1.37 | -2.9 dB |
| Peaking | 271 Hz  | 0.61 | -5.3 dB |
| Peaking | 4407 Hz | 0.73 | 7.1 dB  |
| Peaking | 9372 Hz | 2.63 | -6.5 dB |
| Peaking | 880 Hz  | 2.59 | 0.9 dB  |
| Peaking | 1637 Hz | 2.22 | -1.9 dB |
| Peaking | 2784 Hz | 1.95 | 2.6 dB  |
| Peaking | 3853 Hz | 0.96 | -1.4 dB |
| Peaking | 6035 Hz | 5.27 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W40/Westone%20W40.png)