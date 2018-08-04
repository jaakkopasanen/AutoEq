# Stax SR-X Mk3 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 5.4; 32 5.1; 35 4.7; 37 4.5; 40 4.3; 42 4.1; 45 4.0; 49 3.9; 52 3.9; 56 3.8; 59 3.8; 64 3.8; 68 3.8; 73 3.7; 78 3.5; 83 3.4; 89 3.1; 95 2.8; 102 2.5; 109 2.2; 117 1.9; 125 1.6; 134 1.3; 143 1.0; 153 0.9; 164 0.8; 175 0.8; 188 0.7; 201 0.7; 215 0.7; 230 0.8; 246 0.8; 263 0.8; 282 0.8; 301 0.8; 323 0.9; 345 0.9; 369 0.9; 395 1.0; 423 1.0; 452 0.9; 484 0.8; 518 0.3; 554 0.9; 593 1.2; 635 1.0; 679 0.7; 726 0.6; 777 0.7; 832 0.5; 890 0.3; 952 0.0; 1019 0.1; 1090 0.1; 1167 0.2; 1248 0.0; 1336 0.4; 1429 0.7; 1529 0.8; 1636 1.1; 1751 1.6; 1873 2.1; 2004 2.0; 2145 1.8; 2295 1.3; 2455 0.5; 2627 -0.3; 2811 -1.1; 3008 -2.0; 3219 -2.3; 3444 -2.5; 3685 -3.3; 3943 -3.8; 4219 -3.8; 4514 -2.4; 4830 -0.4; 5168 0.9; 5530 0.9; 5917 0.1; 6331 -1.1; 6775 -1.9; 7249 -2.3; 7756 -2.3; 8299 -2.7; 8880 -2.6; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -2.8; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-X Mk3 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.08 | 5.1 dB  |
| Peaking | 61 Hz   | 0.57 | 3.1 dB  |
| Peaking | 1957 Hz | 2.65 | 2.4 dB  |
| Peaking | 3768 Hz | 2.89 | -4.0 dB |
| Peaking | 8128 Hz | 3.49 | -2.9 dB |
| Peaking | 154 Hz  | 2.63 | -0.6 dB |
| Peaking | 463 Hz  | 1.06 | 0.8 dB  |
| Peaking | 4297 Hz | 7.76 | -1.7 dB |
| Peaking | 5269 Hz | 3.97 | 2.2 dB  |
| Peaking | 6703 Hz | 6.02 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-X%20Mk3%20Pro/Stax%20SR-X%20Mk3%20Pro.png)