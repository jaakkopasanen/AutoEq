# Focal Clear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.2; 22 5.9; 23 5.8; 25 5.6; 26 5.5; 28 5.3; 30 5.2; 32 5.0; 35 4.8; 37 4.7; 40 4.6; 42 4.5; 45 4.4; 49 4.2; 52 4.0; 56 3.8; 59 3.7; 64 3.5; 68 3.3; 73 3.1; 78 2.8; 83 2.6; 89 2.3; 95 2.1; 102 1.8; 109 1.6; 117 1.4; 125 1.2; 134 1.0; 143 0.9; 153 0.8; 164 0.8; 175 0.7; 188 0.7; 201 0.7; 215 0.7; 230 0.8; 246 0.9; 263 1.0; 282 1.2; 301 1.3; 323 1.5; 345 1.6; 369 1.8; 395 1.9; 423 1.9; 452 2.0; 484 2.0; 518 2.0; 554 2.0; 593 2.0; 635 1.9; 679 1.8; 726 1.6; 777 1.3; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.3; 1336 -1.5; 1429 -1.2; 1529 -0.8; 1636 -0.0; 1751 0.6; 1873 1.3; 2004 1.9; 2145 2.4; 2295 2.5; 2455 2.3; 2627 1.9; 2811 1.4; 3008 1.1; 3219 1.4; 3444 1.6; 3685 1.9; 3943 4.7; 4219 6.0; 4514 5.7; 4830 5.5; 5168 5.2; 5530 3.9; 5917 1.3; 6331 4.7; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.0; 12455 -0.9; 13327 -0.1; 14260 0.0; 15258 0.0; 16326 -0.4; 17469 -2.8; 18692 -4.7; 20000 -6.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  0.58 | 5.6 dB  |
| Peaking | 58 Hz    |  0.8  | 2.2 dB  |
| Peaking | 472 Hz   |  1.33 | 2.2 dB  |
| Peaking | 2251 Hz  |  4.95 | 2.2 dB  |
| Peaking | 4697 Hz  |  2.1  | 6.1 dB  |
| Peaking | 714 Hz   |  3.65 | 0.8 dB  |
| Peaking | 1299 Hz  |  3.48 | -2.1 dB |
| Peaking | 3570 Hz  | 10.7  | -0.9 dB |
| Peaking | 6564 Hz  | 13.66 | 3.7 dB  |
| Peaking | 19545 Hz |  1.55 | -6.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Clear/Focal%20Clear.png)