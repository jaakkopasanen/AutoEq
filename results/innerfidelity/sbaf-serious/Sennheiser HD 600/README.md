# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.3; 40 4.6; 42 4.2; 45 3.7; 49 3.2; 52 2.9; 56 2.5; 59 2.3; 64 1.8; 68 1.6; 73 1.4; 78 0.9; 83 0.3; 89 -0.4; 95 -0.9; 102 -1.5; 109 -1.9; 117 -2.3; 125 -2.8; 134 -3.1; 143 -3.3; 153 -3.4; 164 -3.3; 175 -3.2; 188 -3.3; 201 -3.2; 215 -3.1; 230 -2.9; 246 -2.7; 263 -2.6; 282 -2.3; 301 -2.2; 323 -2.0; 345 -1.8; 369 -1.7; 395 -1.6; 423 -1.3; 452 -1.2; 484 -1.2; 518 -1.1; 554 -0.7; 593 -0.5; 635 -0.5; 679 -0.6; 726 -0.6; 777 -0.4; 832 -0.5; 890 -0.7; 952 -0.5; 1019 0.0; 1090 -0.4; 1167 -0.7; 1248 -1.0; 1336 -1.2; 1429 -1.5; 1529 -1.9; 1636 -2.1; 1751 -2.5; 1873 -1.8; 2004 -1.4; 2145 -1.6; 2295 -1.2; 2455 -0.8; 2627 -0.9; 2811 -1.3; 3008 -1.1; 3219 -1.5; 3444 -1.7; 3685 -1.4; 3943 -0.7; 4219 -0.9; 4514 -1.9; 4830 -1.3; 5168 1.3; 5530 4.1; 5917 3.6; 6331 3.9; 6775 3.7; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -0.9; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.4  | 6.4 dB  |
| Peaking | 156 Hz  | 0.62 | -4.3 dB |
| Peaking | 1689 Hz | 2.74 | -1.9 dB |
| Peaking | 5187 Hz | 1.01 | -4.3 dB |
| Peaking | 6016 Hz | 2.35 | 8.5 dB  |
| Peaking | 9401 Hz | 1.31 | 0.7 dB  |
| Peaking | 8773 Hz | 3.34 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)