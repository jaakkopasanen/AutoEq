# Stax SR-Gamma Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.8; 64 4.7; 68 4.1; 73 3.8; 78 3.4; 83 2.8; 89 2.1; 95 1.2; 102 0.6; 109 0.2; 117 -0.5; 125 -1.1; 134 -1.4; 143 -1.4; 153 -1.4; 164 -1.4; 175 -1.4; 188 -1.4; 201 -1.4; 215 -1.2; 230 -0.9; 246 -0.7; 263 -0.4; 282 0.0; 301 0.2; 323 0.4; 345 0.6; 369 0.6; 395 0.6; 423 0.7; 452 0.7; 484 0.6; 518 0.6; 554 0.7; 593 0.8; 635 0.9; 679 0.8; 726 0.6; 777 0.7; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.9; 1336 -1.4; 1429 -1.8; 1529 -2.2; 1636 -2.5; 1751 -2.6; 1873 -2.3; 2004 -1.5; 2145 -0.7; 2295 0.6; 2455 2.3; 2627 3.3; 2811 3.6; 3008 4.0; 3219 3.9; 3444 3.8; 3685 3.9; 3943 4.2; 4219 3.1; 4514 2.2; 4830 1.6; 5168 0.6; 5530 -0.5; 5917 -1.6; 6331 -2.1; 6775 -1.3; 7249 -0.4; 7756 -0.9; 8299 -2.8; 8880 -4.8; 9502 -4.6; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.5; 20000 -4.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Gamma Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.85 | 7.1 dB  |
| Peaking | 1803 Hz | 1.28 | -8.4 dB |
| Peaking | 2683 Hz | 0.59 | 7.3 dB  |
| Peaking | 6004 Hz | 2.57 | -4.3 dB |
| Peaking | 9108 Hz | 4.47 | -6.2 dB |
| Peaking | 35 Hz   | 1.3  | -6.0 dB |
| Peaking | 42 Hz   | 0.36 | 5.2 dB  |
| Peaking | 138 Hz  | 0.76 | -4.4 dB |
| Peaking | 384 Hz  | 1    | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Gamma%20Pro/Stax%20SR-Gamma%20Pro.png)