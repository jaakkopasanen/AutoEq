# Beyerdynamic T5p sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.0; 22 -0.9; 23 -0.9; 25 -0.8; 26 -0.7; 28 -0.5; 30 -0.3; 32 -0.0; 35 0.3; 37 0.4; 40 0.8; 42 1.0; 45 1.2; 49 1.3; 52 1.5; 56 1.9; 59 2.3; 64 3.1; 68 3.6; 73 3.9; 78 3.3; 83 2.1; 89 0.6; 95 -0.8; 102 -1.7; 109 -2.1; 117 -2.3; 125 -2.2; 134 -2.0; 143 -1.7; 153 -1.1; 164 -0.2; 175 -1.0; 188 -0.9; 201 -0.5; 215 -0.1; 230 0.4; 246 0.7; 263 1.1; 282 1.4; 301 1.7; 323 1.9; 345 2.1; 369 2.2; 395 2.2; 423 2.4; 452 2.5; 484 2.3; 518 2.4; 554 2.8; 593 3.6; 635 5.2; 679 5.0; 726 2.1; 777 2.0; 832 2.0; 890 1.4; 952 1.2; 1019 -0.0; 1090 0.0; 1167 0.5; 1248 0.1; 1336 -1.7; 1429 -2.0; 1529 -0.8; 1636 -0.7; 1751 -1.1; 1873 0.1; 2004 -0.4; 2145 -1.9; 2295 -2.1; 2455 -0.6; 2627 0.8; 2811 1.1; 3008 1.9; 3219 2.9; 3444 3.7; 3685 4.1; 3943 4.2; 4219 3.3; 4514 4.6; 4830 6.0; 5168 6.0; 5530 3.5; 5917 0.0; 6331 -0.0; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 1.76 | 6.2 dB  |
| Peaking | 105 Hz  | 1.27 | -4.4 dB |
| Peaking | 377 Hz  | 1.44 | 2.4 dB  |
| Peaking | 645 Hz  | 4.35 | 4.8 dB  |
| Peaking | 4604 Hz | 2.22 | 5.6 dB  |
| Peaking | 20 Hz   | 1.73 | -1.1 dB |
| Peaking | 2258 Hz | 6.41 | -2.8 dB |
| Peaking | 1391 Hz | 6.79 | -2.4 dB |
| Peaking | 3391 Hz | 4.45 | 2.2 dB  |
| Peaking | 6147 Hz | 0.57 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sample%201/Beyerdynamic%20T5p%20sample%201.png)