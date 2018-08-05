# Shure SE530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.3; 22 2.2; 23 2.2; 25 2.1; 26 2.1; 28 2.1; 30 2.0; 32 2.0; 35 1.9; 37 1.9; 40 1.8; 42 1.8; 45 1.8; 49 1.7; 52 1.7; 56 1.6; 59 1.5; 64 1.4; 68 1.3; 73 1.2; 78 1.0; 83 0.8; 89 0.4; 95 -0.1; 102 -0.8; 109 -1.3; 117 -1.8; 125 -2.5; 134 -2.9; 143 -3.2; 153 -3.5; 164 -3.7; 175 -3.7; 188 -3.7; 201 -3.8; 215 -3.8; 230 -3.6; 246 -3.6; 263 -3.5; 282 -3.3; 301 -3.3; 323 -3.1; 345 -2.9; 369 -2.8; 395 -2.6; 423 -2.3; 452 -2.0; 484 -1.9; 518 -1.7; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.5; 726 -0.3; 777 0.1; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.0; 1529 -1.3; 1636 -1.6; 1751 -1.7; 1873 -1.8; 2004 -1.8; 2145 -1.6; 2295 -0.8; 2455 0.4; 2627 1.8; 2811 2.9; 3008 4.2; 3219 5.2; 3444 5.9; 3685 5.8; 3943 5.5; 4219 4.6; 4514 4.4; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.33 | 3.0 dB  |
| Peaking | 185 Hz  | 0.63 | -5.5 dB |
| Peaking | 2016 Hz | 2.1  | -3.2 dB |
| Peaking | 3479 Hz | 1.76 | 6.0 dB  |
| Peaking | 5739 Hz | 3.06 | 5.5 dB  |
| Peaking | 3 Hz    | 1.29 | 0.4 dB  |
| Peaking | 137 Hz  | 6.44 | -0.4 dB |
| Peaking | 421 Hz  | 2.59 | -0.5 dB |
| Peaking | 824 Hz  | 2.53 | 0.8 dB  |
| Peaking | 8291 Hz | 4.32 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE530/Shure%20SE530.png)