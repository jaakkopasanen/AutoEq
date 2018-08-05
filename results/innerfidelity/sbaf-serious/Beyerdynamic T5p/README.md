# Beyerdynamic T5p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.6; 22 0.5; 23 0.4; 25 0.3; 26 0.3; 28 0.3; 30 0.4; 32 0.5; 35 0.6; 37 0.6; 40 0.8; 42 0.9; 45 1.0; 49 1.1; 52 1.2; 56 1.5; 59 1.8; 64 2.2; 68 2.6; 73 2.9; 78 2.7; 83 2.2; 89 1.2; 95 0.1; 102 -1.2; 109 -2.0; 117 -2.5; 125 -3.1; 134 -3.2; 143 -3.0; 153 -2.5; 164 -1.4; 175 -1.9; 188 -2.2; 201 -1.9; 215 -1.4; 230 -1.0; 246 -0.6; 263 -0.2; 282 0.3; 301 0.6; 323 0.8; 345 1.0; 369 1.2; 395 1.2; 423 1.3; 452 1.3; 484 1.1; 518 1.0; 554 1.3; 593 2.4; 635 4.6; 679 3.6; 726 1.7; 777 1.7; 832 1.3; 890 0.4; 952 0.4; 1019 0.1; 1090 0.0; 1167 -0.5; 1248 -1.4; 1336 -2.0; 1429 -1.9; 1529 -2.1; 1636 -2.2; 1751 -2.7; 1873 -1.6; 2004 -1.5; 2145 -3.0; 2295 -2.7; 2455 -1.0; 2627 0.6; 2811 0.8; 3008 1.6; 3219 2.4; 3444 3.4; 3685 3.9; 3943 4.7; 4219 2.9; 4514 4.2; 4830 6.0; 5168 6.0; 5530 2.8; 5917 0.1; 6331 0.0; 6775 2.2; 7249 1.3; 7756 0.1; 8299 -1.8; 8880 -1.9; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 78 Hz   |  1.36 | 4.6 dB  |
| Peaking | 123 Hz  |  1.29 | -4.8 dB |
| Peaking | 646 Hz  |  1.66 | 3.5 dB  |
| Peaking | 1816 Hz |  1.09 | -3.2 dB |
| Peaking | 4206 Hz |  1.58 | 5.5 dB  |
| Peaking | 345 Hz  |  1.89 | 2.8 dB  |
| Peaking | 347 Hz  |  1.12 | -1.8 dB |
| Peaking | 5121 Hz |  9.45 | 3.2 dB  |
| Peaking | 6007 Hz | 10.28 | -2.6 dB |
| Peaking | 8589 Hz |  7.61 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)