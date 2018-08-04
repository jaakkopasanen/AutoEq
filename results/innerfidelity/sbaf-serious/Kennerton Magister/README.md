# Kennerton Magister

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.7; 23 5.6; 25 5.2; 26 5.0; 28 4.7; 30 4.4; 32 4.1; 35 3.8; 37 3.7; 40 3.6; 42 3.6; 45 3.6; 49 3.6; 52 3.5; 56 3.3; 59 3.0; 64 2.9; 68 3.1; 73 3.2; 78 3.1; 83 2.6; 89 1.7; 95 1.4; 102 0.6; 109 -0.3; 117 -1.0; 125 -1.7; 134 -2.1; 143 -2.2; 153 -2.2; 164 -1.5; 175 -2.0; 188 -2.4; 201 -2.2; 215 -2.0; 230 -1.5; 246 -1.0; 263 -0.3; 282 0.9; 301 2.0; 323 3.1; 345 3.7; 369 3.9; 395 3.3; 423 2.8; 452 2.4; 484 1.7; 518 1.3; 554 1.2; 593 1.0; 635 0.6; 679 0.4; 726 0.5; 777 0.6; 832 0.6; 890 0.4; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -1.0; 1336 -1.7; 1429 -2.4; 1529 -3.2; 1636 -3.8; 1751 -4.2; 1873 -4.8; 2004 -4.3; 2145 -3.9; 2295 -3.8; 2455 -2.9; 2627 -2.2; 2811 -1.8; 3008 -0.8; 3219 -0.7; 3444 -0.1; 3685 -0.1; 3943 -0.2; 4219 0.3; 4514 0.9; 4830 2.2; 5168 5.2; 5530 6.0; 5917 5.9; 6331 4.9; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Magister ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.04 | 5.6 dB  |
| Peaking | 65 Hz   | 2.6  | 2.7 dB  |
| Peaking | 381 Hz  | 3.13 | 4.2 dB  |
| Peaking | 1944 Hz | 1.79 | -4.9 dB |
| Peaking | 5728 Hz | 3.39 | 7.0 dB  |
| Peaking | 46 Hz   | 2.23 | 2.4 dB  |
| Peaking | 87 Hz   | 2.18 | 3.4 dB  |
| Peaking | 249 Hz  | 0.23 | -3.8 dB |
| Peaking | 311 Hz  | 3.63 | 2.8 dB  |
| Peaking | 591 Hz  | 0.65 | 3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Kennerton%20Magister/Kennerton%20Magister.png)