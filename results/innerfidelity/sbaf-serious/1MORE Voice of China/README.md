# 1MORE Voice of China

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 1.4; 22 0.7; 23 0.4; 25 -0.1; 26 -0.3; 28 -0.7; 30 -1.1; 32 -1.4; 35 -1.9; 37 -2.1; 40 -2.4; 42 -2.5; 45 -2.8; 49 -3.1; 52 -3.2; 56 -3.4; 59 -3.5; 64 -3.7; 68 -3.8; 73 -3.9; 78 -4.2; 83 -4.5; 89 -4.9; 95 -5.2; 102 -5.7; 109 -6.1; 117 -6.6; 125 -7.0; 134 -7.4; 143 -7.6; 153 -7.6; 164 -7.6; 175 -7.5; 188 -7.3; 201 -7.1; 215 -6.8; 230 -6.4; 246 -6.2; 263 -5.9; 282 -5.4; 301 -5.0; 323 -4.7; 345 -4.2; 369 -3.8; 395 -3.4; 423 -2.9; 452 -2.5; 484 -2.2; 518 -1.8; 554 -1.3; 593 -0.7; 635 -0.4; 679 -0.3; 726 -0.0; 777 0.4; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.4; 1336 -0.9; 1429 -0.9; 1529 -1.4; 1636 -1.8; 1751 -2.1; 1873 -2.2; 2004 -2.2; 2145 -2.5; 2295 -3.0; 2455 -3.4; 2627 -3.6; 2811 -3.9; 3008 -3.2; 3219 -2.6; 3444 -1.7; 3685 -1.7; 3943 -2.4; 4219 -4.5; 4514 -6.4; 4830 -7.6; 5168 -7.0; 5530 -4.1; 5917 -0.4; 6331 1.9; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.3; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Voice of China ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 52 Hz   |  1.28 | -1.6 dB |
| Peaking | 166 Hz  |  0.68 | -7.8 dB |
| Peaking | 2514 Hz |  1.95 | -3.4 dB |
| Peaking | 4926 Hz |  3.41 | -8.3 dB |
| Peaking | 6551 Hz |  4.28 | 4.8 dB  |
| Peaking | 355 Hz  |  2.21 | -0.8 dB |
| Peaking | 803 Hz  |  1.7  | 1.4 dB  |
| Peaking | 1660 Hz |  4.16 | -1.0 dB |
| Peaking | 3690 Hz | 10.23 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Voice%20of%20China/1MORE%20Voice%20of%20China.png)