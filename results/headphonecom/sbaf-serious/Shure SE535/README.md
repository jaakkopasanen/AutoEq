# Shure SE535

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.3; 22 3.2; 23 3.1; 25 3.1; 26 3.1; 28 3.0; 30 3.0; 32 3.0; 35 3.0; 37 2.9; 40 2.9; 42 2.8; 45 2.8; 49 2.8; 52 2.8; 56 2.8; 59 2.7; 64 2.7; 68 2.5; 73 2.3; 78 2.1; 83 2.0; 89 1.7; 95 1.3; 102 0.7; 109 0.3; 117 -0.3; 125 -0.9; 134 -1.4; 143 -1.7; 153 -1.9; 164 -2.1; 175 -2.2; 188 -2.3; 201 -2.3; 215 -2.3; 230 -2.2; 246 -2.2; 263 -2.2; 282 -2.1; 301 -2.0; 323 -1.9; 345 -1.6; 369 -1.3; 395 -1.3; 423 -1.1; 452 -1.1; 484 -1.1; 518 -0.9; 554 -0.5; 593 -0.3; 635 -0.1; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.1; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.4; 1336 -0.6; 1429 -0.9; 1529 -1.0; 1636 -1.1; 1751 -1.1; 1873 -0.9; 2004 -0.8; 2145 -0.4; 2295 0.6; 2455 1.9; 2627 2.9; 2811 3.9; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.3  | 3.1 dB  |
| Peaking | 82 Hz   | 0.95 | 2.3 dB  |
| Peaking | 170 Hz  | 0.63 | -3.4 dB |
| Peaking | 1864 Hz | 1.88 | -3.0 dB |
| Peaking | 4045 Hz | 1    | 7.1 dB  |
| Peaking | 794 Hz  | 4.53 | 0.6 dB  |
| Peaking | 3159 Hz | 3.82 | 2.0 dB  |
| Peaking | 3775 Hz | 1.47 | -1.4 dB |
| Peaking | 6239 Hz | 2.47 | 4.8 dB  |
| Peaking | 7642 Hz | 1.65 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE535/Shure%20SE535.png)