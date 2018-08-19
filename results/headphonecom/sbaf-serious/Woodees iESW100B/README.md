# Woodees iESW100B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 10 -84; 20 -8.5; 22 -8.5; 23 -8.5; 25 -8.5; 26 -8.5; 28 -8.5; 30 -8.5; 32 -8.5; 35 -8.4; 37 -8.4; 40 -8.4; 42 -8.4; 45 -8.4; 49 -8.4; 52 -8.4; 56 -8.4; 59 -8.5; 64 -8.5; 68 -8.6; 73 -8.6; 78 -8.6; 83 -8.6; 89 -8.6; 95 -8.5; 102 -8.4; 109 -8.3; 117 -8.2; 125 -8.0; 134 -7.9; 143 -7.7; 153 -7.5; 164 -7.3; 175 -7.0; 188 -6.6; 201 -6.3; 215 -5.9; 230 -5.5; 246 -5.1; 263 -4.7; 282 -4.2; 301 -3.7; 323 -3.1; 345 -2.6; 369 -2.1; 395 -1.6; 423 -1.1; 452 -0.7; 484 -0.3; 518 0.1; 554 0.6; 593 1.0; 635 1.2; 679 1.5; 726 1.5; 777 1.5; 832 1.2; 890 0.9; 952 0.4; 1019 0.0; 1090 -0.2; 1167 -1.2; 1248 -1.7; 1336 -1.3; 1429 -1.3; 1529 -2.1; 1636 -2.7; 1751 -3.2; 1873 -3.6; 2004 -3.9; 2145 -4.4; 2295 -5.0; 2455 -5.6; 2627 -6.4; 2811 -6.1; 3008 -4.2; 3219 -1.5; 3444 0.9; 3685 2.0; 3943 1.6; 4219 0.1; 4514 -1.6; 4830 -3.0; 5168 -4.3; 5530 -6.4; 5917 -8.9; 6331 -7.0; 6775 -3.7; 7249 -2.0; 7756 -1.7; 8299 -3.5; 8880 -6.2; 9502 -6.8; 10167 -2.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -1.4; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.193212053485652dB` and instead set Global volume in the UI for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW100B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.16 | -9.1 dB |
| Peaking | 1217 Hz  | 0.26 | 4.4 dB  |
| Peaking | 2124 Hz  | 1.09 | -8.8 dB |
| Peaking | 6061 Hz  | 2.55 | -8.5 dB |
| Peaking | 21779 Hz | 1.83 | -3.5 dB |
| Peaking | 1185 Hz  | 6.55 | -1.9 dB |
| Peaking | 2799 Hz  | 6.3  | -3.8 dB |
| Peaking | 3700 Hz  | 4.57 | 4.2 dB  |
| Peaking | 7251 Hz  | 5.99 | 2.5 dB  |
| Peaking | 9272 Hz  | 5.58 | -7.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW100B/Woodees%20iESW100B.png)