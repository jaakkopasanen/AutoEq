# AKG Y50BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.5; 26 5.3; 28 4.9; 30 4.4; 32 4.0; 35 3.5; 37 3.2; 40 2.8; 42 2.6; 45 2.3; 49 2.1; 52 1.9; 56 1.8; 59 1.7; 64 1.5; 68 1.4; 73 1.2; 78 1.1; 83 1.0; 89 0.8; 95 0.7; 102 0.7; 109 0.8; 117 0.9; 125 1.3; 134 1.8; 143 2.6; 153 3.5; 164 4.7; 175 5.7; 188 5.9; 201 5.3; 215 4.1; 230 3.0; 246 2.2; 263 1.4; 282 0.6; 301 -0.3; 323 -1.0; 345 -1.3; 369 -1.2; 395 -0.8; 423 -0.4; 452 -0.1; 484 0.0; 518 0.0; 554 -0.0; 593 -0.1; 635 -0.3; 679 -0.5; 726 -0.9; 777 -1.2; 832 -1.6; 890 -1.9; 952 -1.5; 1019 -0.1; 1090 -1.3; 1167 -2.3; 1248 -3.0; 1336 -3.1; 1429 -3.0; 1529 -2.8; 1636 -2.2; 1751 -1.4; 1873 -0.5; 2004 0.4; 2145 1.3; 2295 2.5; 2455 3.9; 2627 4.9; 2811 5.0; 3008 3.2; 3219 0.3; 3444 0.0; 3685 2.1; 3943 2.4; 4219 1.2; 4514 0.2; 4830 -0.9; 5168 -1.8; 5530 -2.6; 5917 -2.2; 6331 -1.4; 6775 -0.2; 7249 1.1; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.3; 13327 -2.5; 14260 -4.1; 15258 -5.0; 16326 -5.2; 17469 -4.8; 18692 -4.0; 20000 -3.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.75 | 6.0 dB  |
| Peaking | 184 Hz   | 2.81 | 6.2 dB  |
| Peaking | 1413 Hz  | 1.2  | -3.2 dB |
| Peaking | 2610 Hz  | 2.89 | 6.1 dB  |
| Peaking | 16974 Hz | 1.16 | -5.7 dB |
| Peaking | 314 Hz   | 1.4  | 1.6 dB  |
| Peaking | 337 Hz   | 2.67 | -3.3 dB |
| Peaking | 3946 Hz  | 9.48 | 2.4 dB  |
| Peaking | 5639 Hz  | 3.35 | -3.3 dB |
| Peaking | 7873 Hz  | 1.18 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20Y50BT/AKG%20Y50BT.png)