# AKG K1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.8; 64 4.4; 68 3.2; 73 1.9; 78 0.8; 83 -0.1; 89 -0.8; 95 -1.4; 102 -1.7; 109 -1.7; 117 -1.8; 125 -2.0; 134 -1.5; 143 -1.2; 153 -1.1; 164 -0.9; 175 -0.7; 188 -0.6; 201 -0.5; 215 -0.4; 230 -0.2; 246 -0.1; 263 0.0; 282 0.3; 301 0.3; 323 0.4; 345 0.5; 369 0.5; 395 0.5; 423 0.7; 452 0.8; 484 0.7; 518 0.6; 554 0.8; 593 0.9; 635 0.9; 679 0.8; 726 0.7; 777 0.9; 832 0.8; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.9; 1248 -1.9; 1336 -3.1; 1429 -4.2; 1529 -4.6; 1636 -4.6; 1751 -5.4; 1873 -7.1; 2004 -6.9; 2145 -5.9; 2295 -5.1; 2455 -2.9; 2627 -0.8; 2811 0.8; 3008 2.6; 3219 2.7; 3444 2.1; 3685 0.5; 3943 -1.7; 4219 -2.8; 4514 -2.6; 4830 -2.8; 5168 -2.8; 5530 -3.3; 5917 -5.0; 6331 -5.3; 6775 -4.2; 7249 -4.0; 7756 -4.2; 8299 -4.6; 8880 -4.6; 9502 -3.5; 10167 -1.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.6; 18692 -1.6; 20000 -1.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 71 Hz    | 0.28 | 16.7 dB  |
| Peaking | 105 Hz   | 0.5  | -17.4 dB |
| Peaking | 1945 Hz  | 1.83 | -7.4 dB  |
| Peaking | 3117 Hz  | 3.3  | 5.9 dB   |
| Peaking | 6678 Hz  | 1.13 | -4.9 dB  |
| Peaking | 57 Hz    | 6.15 | 1.1 dB   |
| Peaking | 894 Hz   | 1.28 | 1.0 dB   |
| Peaking | 1395 Hz  | 6.56 | -1.7 dB  |
| Peaking | 9077 Hz  | 4.18 | -2.9 dB  |
| Peaking | 10700 Hz | 1.74 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K1000/AKG%20K1000.png)