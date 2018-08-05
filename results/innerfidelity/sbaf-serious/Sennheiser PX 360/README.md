# Sennheiser PX 360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.4; 52 5.2; 56 4.8; 59 4.5; 64 4.1; 68 3.8; 73 3.5; 78 3.0; 83 2.6; 89 2.2; 95 1.8; 102 1.4; 109 1.1; 117 0.7; 125 0.6; 134 1.1; 143 1.5; 153 2.1; 164 0.8; 175 2.8; 188 3.2; 201 2.1; 215 1.7; 230 1.0; 246 0.6; 263 0.1; 282 0.6; 301 0.6; 323 0.1; 345 0.1; 369 0.5; 395 1.0; 423 1.5; 452 1.7; 484 1.5; 518 1.6; 554 1.9; 593 2.0; 635 1.8; 679 1.7; 726 1.5; 777 1.6; 832 1.3; 890 0.9; 952 0.5; 1019 -0.2; 1090 -0.9; 1167 -1.9; 1248 -2.8; 1336 -4.0; 1429 -5.2; 1529 -6.5; 1636 -7.6; 1751 -8.4; 1873 -8.7; 2004 -8.0; 2145 -6.8; 2295 -5.1; 2455 -2.9; 2627 -1.2; 2811 -0.2; 3008 1.2; 3219 2.6; 3444 4.1; 3685 5.3; 3943 6.0; 4219 4.7; 4514 3.0; 4830 3.0; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -1.4; 10167 -2.3; 10879 -2.2; 11640 -0.5; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.49 | 6.4 dB   |
| Peaking | 737 Hz   | 0.86 | 2.7 dB   |
| Peaking | 1812 Hz  | 1.51 | -10.1 dB |
| Peaking | 3691 Hz  | 2.24 | 6.7 dB   |
| Peaking | 5870 Hz  | 3.75 | 6.1 dB   |
| Peaking | 114 Hz   | 4.03 | -1.2 dB  |
| Peaking | 187 Hz   | 6.05 | 2.5 dB   |
| Peaking | 331 Hz   | 4.96 | -0.9 dB  |
| Peaking | 9825 Hz  | 0.57 | 0.3 dB   |
| Peaking | 10277 Hz | 3.36 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)