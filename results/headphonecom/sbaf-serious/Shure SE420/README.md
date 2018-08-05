# Shure SE420

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.5; 22 5.2; 23 5.1; 25 4.8; 26 4.7; 28 4.5; 30 4.3; 32 4.2; 35 4.0; 37 3.9; 40 3.7; 42 3.6; 45 3.5; 49 3.3; 52 3.1; 56 3.0; 59 2.9; 64 2.7; 68 2.6; 73 2.5; 78 2.2; 83 1.9; 89 1.7; 95 1.3; 102 0.7; 109 0.0; 117 -0.5; 125 -1.1; 134 -1.6; 143 -1.9; 153 -2.2; 164 -2.3; 175 -2.4; 188 -2.5; 201 -2.5; 215 -2.5; 230 -2.4; 246 -2.4; 263 -2.4; 282 -2.1; 301 -2.0; 323 -1.9; 345 -1.7; 369 -1.4; 395 -1.3; 423 -1.1; 452 -1.0; 484 -0.9; 518 -0.8; 554 -0.4; 593 -0.0; 635 0.1; 679 0.1; 726 0.2; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -1.9; 1636 -2.2; 1751 -2.3; 1873 -2.3; 2004 -2.5; 2145 -2.7; 2295 -2.5; 2455 -2.0; 2627 -1.3; 2811 -0.1; 3008 1.5; 3219 2.8; 3444 4.0; 3685 4.8; 3943 5.1; 4219 4.6; 4514 4.8; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.37 | 5.3 dB  |
| Peaking | 79 Hz   | 1.12 | 1.9 dB  |
| Peaking | 181 Hz  | 0.77 | -3.3 dB |
| Peaking | 2110 Hz | 1.73 | -4.0 dB |
| Peaking | 4689 Hz | 1.27 | 6.6 dB  |
| Peaking | 793 Hz  | 1.49 | 1.9 dB  |
| Peaking | 3508 Hz | 4.63 | 2.0 dB  |
| Peaking | 783 Hz  | 0.72 | -0.9 dB |
| Peaking | 6168 Hz | 2.91 | 6.1 dB  |
| Peaking | 6508 Hz | 1.18 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE420/Shure%20SE420.png)