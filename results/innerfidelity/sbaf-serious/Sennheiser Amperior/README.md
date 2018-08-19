# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 4.2; 22 3.5; 23 3.2; 25 2.7; 26 2.4; 28 2.0; 30 1.5; 32 1.1; 35 0.6; 37 0.3; 40 -0.1; 42 -0.3; 45 -0.6; 49 -1.0; 52 -1.2; 56 -1.5; 59 -1.7; 64 -1.9; 68 -2.0; 73 -2.2; 78 -2.8; 83 -3.4; 89 -3.7; 95 -3.9; 102 -4.3; 109 -4.6; 117 -4.8; 125 -5.1; 134 -5.2; 143 -5.2; 153 -5.2; 164 -4.7; 175 -4.6; 188 -4.4; 201 -4.0; 215 -3.4; 230 -2.7; 246 -1.9; 263 -1.4; 282 -0.7; 301 -0.2; 323 0.3; 345 0.9; 369 1.3; 395 1.7; 423 2.0; 452 1.9; 484 1.7; 518 1.4; 554 1.5; 593 1.5; 635 1.3; 679 1.1; 726 0.9; 777 0.9; 832 0.6; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.7; 1529 -2.2; 1636 -2.8; 1751 -3.1; 1873 -3.3; 2004 -3.3; 2145 -3.0; 2295 -1.9; 2455 -0.5; 2627 0.6; 2811 1.4; 3008 2.2; 3219 2.3; 3444 2.3; 3685 2.2; 3943 2.4; 4219 2.6; 4514 3.3; 4830 3.3; 5168 4.4; 5530 4.5; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.3; 8299 -4.7; 8880 -5.7; 9502 -3.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.958492719114095dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.96 | 4.1 dB   |
| Peaking | 129 Hz  | 1.13 | -5.7 dB  |
| Peaking | 1887 Hz | 2.6  | -4.4 dB  |
| Peaking | 6576 Hz | 0.97 | 7.7 dB   |
| Peaking | 8566 Hz | 2.59 | -11.3 dB |
| Peaking | 76 Hz   | 0.98 | -2.2 dB  |
| Peaking | 210 Hz  | 1.13 | -5.2 dB  |
| Peaking | 272 Hz  | 0.32 | 4.8 dB   |
| Peaking | 1058 Hz | 0.51 | -1.7 dB  |
| Peaking | 2988 Hz | 4.87 | 1.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)