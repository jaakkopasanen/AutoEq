# Stax SR-507 SE1-1049

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 5.9; 22 4.9; 23 4.4; 25 3.7; 26 3.5; 28 3.1; 30 2.8; 32 2.7; 35 2.7; 37 2.9; 40 3.1; 42 3.3; 45 3.5; 49 3.8; 52 4.0; 56 4.2; 59 4.3; 64 4.4; 68 4.4; 73 4.3; 78 4.1; 83 4.0; 89 3.7; 95 3.6; 102 3.1; 109 2.8; 117 2.6; 125 2.2; 134 2.0; 143 1.8; 153 1.7; 164 1.6; 175 1.6; 188 1.5; 201 1.5; 215 1.6; 230 1.7; 246 1.6; 263 1.7; 282 1.8; 301 1.6; 323 1.5; 345 1.6; 369 1.6; 395 1.6; 423 1.7; 452 1.7; 484 1.6; 518 1.6; 554 1.5; 593 1.5; 635 1.4; 679 1.0; 726 1.0; 777 0.9; 832 0.6; 890 0.3; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -1.0; 1248 -1.7; 1336 -2.3; 1429 -2.7; 1529 -3.1; 1636 -3.1; 1751 -3.0; 1873 -2.0; 2004 0.6; 2145 2.4; 2295 4.0; 2455 3.3; 2627 2.1; 2811 1.3; 3008 0.7; 3219 0.1; 3444 1.2; 3685 1.1; 3943 1.8; 4219 1.0; 4514 -1.0; 4830 -0.7; 5168 1.1; 5530 0.7; 5917 -0.6; 6331 1.1; 6775 3.2; 7249 1.3; 7756 0.2; 8299 -2.1; 8880 -4.1; 9502 -4.1; 10167 -2.5; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.5; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-507 SE1-1049 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  0.19 | 3.5 dB  |
| Peaking | 661 Hz  |  0.06 | 1.4 dB  |
| Peaking | 1672 Hz |  1.46 | -5.5 dB |
| Peaking | 2274 Hz |  3.83 | 5.7 dB  |
| Peaking | 9267 Hz |  4.44 | -5.6 dB |
| Peaking | 34 Hz   |  1.11 | -4.0 dB |
| Peaking | 36 Hz   |  0.15 | 2.9 dB  |
| Peaking | 147 Hz  |  0.8  | -2.6 dB |
| Peaking | 4648 Hz | 11.31 | -2.4 dB |
| Peaking | 6830 Hz | 11.48 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-507%20SE1-1049/Stax%20SR-507%20SE1-1049.png)