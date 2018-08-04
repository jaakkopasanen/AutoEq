# Koss Pro4S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.7; 22 3.1; 23 2.8; 25 2.3; 26 2.1; 28 1.7; 30 1.3; 32 1.0; 35 0.7; 37 0.5; 40 0.2; 42 0.1; 45 -0.1; 49 -0.3; 52 -0.4; 56 -0.5; 59 -0.5; 64 -0.6; 68 -0.7; 73 -0.8; 78 -0.8; 83 -0.9; 89 -1.0; 95 -1.1; 102 -1.1; 109 -1.1; 117 -0.9; 125 -0.3; 134 0.4; 143 0.4; 153 -0.2; 164 0.5; 175 2.0; 188 2.9; 201 2.7; 215 3.7; 230 4.0; 246 5.4; 263 4.9; 282 3.9; 301 2.5; 323 1.2; 345 0.6; 369 0.8; 395 0.6; 423 0.5; 452 0.4; 484 0.0; 518 -0.2; 554 -0.1; 593 0.1; 635 -0.1; 679 -0.2; 726 -0.3; 777 -0.2; 832 -0.3; 890 -0.2; 952 -0.1; 1019 0.1; 1090 0.1; 1167 -0.2; 1248 -0.5; 1336 -0.8; 1429 -1.1; 1529 -1.2; 1636 -1.4; 1751 -1.6; 1873 -1.8; 2004 -2.0; 2145 -1.8; 2295 -2.4; 2455 -2.9; 2627 -3.2; 2811 -3.2; 3008 -2.5; 3219 -1.5; 3444 -0.6; 3685 0.4; 3943 2.4; 4219 4.1; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.59 | 3.5 dB  |
| Peaking | 89 Hz   |  1.18 | -1.4 dB |
| Peaking | 243 Hz  |  2.36 | 5.3 dB  |
| Peaking | 2784 Hz |  1.19 | -4.3 dB |
| Peaking | 5018 Hz |  1.74 | 8.2 dB  |
| Peaking | 13 Hz   |  0.97 | 0.7 dB  |
| Peaking | 183 Hz  | 13.1  | 1.3 dB  |
| Peaking | 412 Hz  |  1.12 | -0.2 dB |
| Peaking | 6488 Hz |  5.08 | 3.4 dB  |
| Peaking | 7453 Hz |  1.87 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4S/Koss%20Pro4S.png)