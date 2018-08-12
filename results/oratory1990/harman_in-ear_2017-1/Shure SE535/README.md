# Shure SE535

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.1; 22 4.0; 23 4.0; 25 3.9; 26 3.8; 28 3.7; 30 3.7; 32 3.6; 35 3.5; 37 3.4; 40 3.2; 42 3.2; 45 3.0; 49 2.9; 52 2.7; 56 2.5; 59 2.4; 64 2.1; 68 1.8; 73 1.5; 78 1.2; 83 0.9; 89 0.6; 95 0.3; 102 -0.1; 109 -0.4; 117 -0.7; 125 -1.0; 134 -1.2; 143 -1.4; 153 -1.6; 164 -1.8; 175 -2.0; 188 -2.1; 201 -2.2; 215 -2.3; 230 -2.4; 246 -2.4; 263 -2.4; 282 -2.4; 301 -2.4; 323 -2.3; 345 -2.2; 369 -2.1; 395 -2.0; 423 -1.9; 452 -1.8; 484 -1.7; 518 -1.5; 554 -1.3; 593 -1.1; 635 -0.9; 679 -0.7; 726 -0.5; 777 -0.2; 832 -0.0; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 0.1; 1336 0.4; 1429 0.8; 1529 1.3; 1636 1.8; 1751 2.2; 1873 2.7; 2004 3.2; 2145 4.0; 2295 5.0; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -1.6; 15258 -1.3; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.44 | 4.2 dB  |
| Peaking | 67 Hz   | 0.82 | 2.3 dB  |
| Peaking | 189 Hz  | 0.24 | -2.8 dB |
| Peaking | 4707 Hz | 0.53 | 8.4 dB  |
| Peaking | 8765 Hz | 0.81 | -4.8 dB |
| Peaking | 1356 Hz | 2.95 | -1.0 dB |
| Peaking | 2547 Hz | 3.33 | 1.7 dB  |
| Peaking | 5157 Hz | 1.04 | -1.1 dB |
| Peaking | 5980 Hz | 4.05 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE535/Shure%20SE535.png)