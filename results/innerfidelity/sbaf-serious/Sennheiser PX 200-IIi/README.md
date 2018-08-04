# Sennheiser PX 200-IIi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.9; 83 5.5; 89 5.1; 95 5.1; 102 5.1; 109 4.5; 117 3.7; 125 3.0; 134 2.3; 143 1.7; 153 1.3; 164 1.0; 175 0.9; 188 0.8; 201 0.6; 215 0.4; 230 0.3; 246 0.1; 263 0.2; 282 0.2; 301 0.0; 323 -0.0; 345 0.0; 369 0.1; 395 0.6; 423 1.0; 452 0.7; 484 0.5; 518 0.4; 554 0.7; 593 1.1; 635 1.5; 679 2.1; 726 2.1; 777 2.2; 832 2.1; 890 1.8; 952 0.9; 1019 0.1; 1090 1.6; 1167 1.6; 1248 2.3; 1336 1.8; 1429 1.0; 1529 0.1; 1636 -0.6; 1751 -1.1; 1873 -1.2; 2004 -1.1; 2145 -1.2; 2295 -0.9; 2455 0.2; 2627 1.3; 2811 1.7; 3008 2.7; 3219 3.4; 3444 4.1; 3685 4.9; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.45 | 6.8 dB  |
| Peaking | 1270 Hz | 4.45 | 2.2 dB  |
| Peaking | 752 Hz  | 3.02 | 2.2 dB  |
| Peaking | 1990 Hz | 2.2  | -2.6 dB |
| Peaking | 4623 Hz | 1.32 | 6.9 dB  |
| Peaking | 19 Hz   | 1.81 | 2.0 dB  |
| Peaking | 90 Hz   | 0.54 | -2.9 dB |
| Peaking | 91 Hz   | 1.15 | 4.1 dB  |
| Peaking | 6356 Hz | 4.08 | 3.9 dB  |
| Peaking | 7499 Hz | 1.66 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200-IIi/Sennheiser%20PX%20200-IIi.png)