# Sennheiser PX 100-IIi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.4; 42 5.1; 45 4.5; 49 3.9; 52 3.4; 56 2.9; 59 2.6; 64 2.0; 68 1.7; 73 1.2; 78 0.9; 83 0.4; 89 -0.1; 95 -0.5; 102 -1.0; 109 -1.2; 117 -1.5; 125 -1.9; 134 -2.4; 143 -2.7; 153 -2.8; 164 -3.0; 175 -3.0; 188 -3.0; 201 -2.9; 215 -2.8; 230 -2.7; 246 -2.5; 263 -2.5; 282 -2.3; 301 -2.1; 323 -1.9; 345 -1.7; 369 -1.5; 395 -1.3; 423 -0.9; 452 -0.7; 484 -0.7; 518 -0.6; 554 -0.3; 593 -0.1; 635 -0.0; 679 0.0; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -2.9; 1751 -3.4; 1873 -3.2; 2004 -2.5; 2145 -1.2; 2295 0.7; 2455 2.7; 2627 3.8; 2811 4.5; 3008 4.8; 3219 4.0; 3444 1.9; 3685 3.1; 3943 3.9; 4219 0.7; 4514 -1.7; 4830 0.4; 5168 3.6; 5530 5.6; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.61 | 6.5 dB  |
| Peaking | 170 Hz  | 0.77 | -3.6 dB |
| Peaking | 1829 Hz | 2.62 | -4.5 dB |
| Peaking | 2853 Hz | 2.46 | 5.5 dB  |
| Peaking | 5989 Hz | 4.31 | 6.6 dB  |
| Peaking | 784 Hz  | 2.54 | 0.8 dB  |
| Peaking | 3931 Hz | 9.4  | 3.7 dB  |
| Peaking | 4526 Hz | 4.97 | -4.0 dB |
| Peaking | 5224 Hz | 6.61 | 2.4 dB  |
| Peaking | 8275 Hz | 4.87 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20100-IIi/Sennheiser%20PX%20100-IIi.png)