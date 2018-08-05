# Brainwavz S0

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 10 -84; 20 -6.6; 22 -6.8; 23 -6.9; 25 -7.0; 26 -7.1; 28 -7.2; 30 -7.2; 32 -7.3; 35 -7.4; 37 -7.4; 40 -7.4; 42 -7.5; 45 -7.5; 49 -7.5; 52 -7.5; 56 -7.5; 59 -7.5; 64 -7.5; 68 -7.5; 73 -7.6; 78 -7.7; 83 -7.9; 89 -8.1; 95 -8.5; 102 -8.9; 109 -9.2; 117 -9.7; 125 -10.1; 134 -10.4; 143 -10.5; 153 -10.5; 164 -10.5; 175 -10.2; 188 -10.1; 201 -9.8; 215 -9.5; 230 -9.1; 246 -8.8; 263 -8.5; 282 -8.1; 301 -7.6; 323 -7.2; 345 -6.7; 369 -6.2; 395 -5.7; 423 -5.2; 452 -4.7; 484 -4.3; 518 -3.8; 554 -3.2; 593 -2.6; 635 -2.1; 679 -1.9; 726 -1.4; 777 -0.9; 832 -0.5; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.3; 1167 0.2; 1248 0.5; 1336 0.7; 1429 1.0; 1529 0.6; 1636 -1.0; 1751 -2.4; 1873 -2.7; 2004 -2.4; 2145 -2.0; 2295 -1.6; 2455 -0.9; 2627 -0.4; 2811 0.2; 3008 1.0; 3219 1.3; 3444 1.5; 3685 0.8; 3943 -0.1; 4219 -2.5; 4514 -4.9; 4830 -7.0; 5168 -8.5; 5530 -6.6; 5917 -2.0; 6331 1.4; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.8dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 8 Hz    | 1.6  | -6.2 dB |
| Peaking | 32 Hz   | 0.34 | -6.5 dB |
| Peaking | 161 Hz  | 0.78 | -8.0 dB |
| Peaking | 336 Hz  | 1.14 | -3.4 dB |
| Peaking | 5085 Hz | 5.8  | -9.5 dB |
| Peaking | 1511 Hz | 1.8  | 4.2 dB  |
| Peaking | 1811 Hz | 2.03 | -5.3 dB |
| Peaking | 3509 Hz | 2.39 | 4.0 dB  |
| Peaking | 4287 Hz | 1.53 | -2.6 dB |
| Peaking | 6702 Hz | 6.06 | 4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S0/Brainwavz%20S0.png)