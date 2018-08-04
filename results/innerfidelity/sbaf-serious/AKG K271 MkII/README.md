# AKG K271 MkII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.6; 42 5.3; 45 4.7; 49 4.2; 52 3.8; 56 3.5; 59 3.3; 64 3.4; 68 3.7; 73 4.5; 78 5.3; 83 5.9; 89 6.0; 95 6.0; 102 4.8; 109 3.2; 117 2.6; 125 2.2; 134 1.3; 143 0.7; 153 1.0; 164 1.8; 175 1.1; 188 1.0; 201 1.1; 215 0.8; 230 0.2; 246 -0.3; 263 -0.4; 282 -0.6; 301 -0.7; 323 -0.7; 345 -0.7; 369 -0.8; 395 -0.9; 423 -0.9; 452 -0.9; 484 -1.2; 518 -1.5; 554 -1.6; 593 -1.9; 635 -2.6; 679 -2.3; 726 0.1; 777 1.3; 832 0.9; 890 0.7; 952 0.5; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -2.0; 1529 -2.7; 1636 -3.2; 1751 -3.1; 1873 -2.2; 2004 0.0; 2145 1.2; 2295 0.7; 2455 2.1; 2627 2.2; 2811 2.2; 3008 3.0; 3219 3.5; 3444 4.3; 3685 5.0; 3943 4.7; 4219 3.2; 4514 2.8; 4830 4.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.6; 8299 -4.5; 8880 -7.1; 9502 -7.5; 10167 -5.1; 10879 -0.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MkII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.72 | 6.4 dB  |
| Peaking | 90 Hz    | 2.54 | 5.2 dB  |
| Peaking | 5882 Hz  | 2.15 | 6.9 dB  |
| Peaking | 3531 Hz  | 3.15 | 4.1 dB  |
| Peaking | 9123 Hz  | 3.59 | -9.6 dB |
| Peaking | 678 Hz   | 1.69 | -4.5 dB |
| Peaking | 785 Hz   | 2.74 | 4.9 dB  |
| Peaking | 1718 Hz  | 2.52 | -4.8 dB |
| Peaking | 2155 Hz  | 2.07 | 2.6 dB  |
| Peaking | 11278 Hz | 8.39 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K271%20MkII/AKG%20K271%20MkII.png)