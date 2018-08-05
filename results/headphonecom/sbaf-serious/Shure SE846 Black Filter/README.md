# Shure SE846 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.3; 22 -6.4; 23 -6.4; 25 -6.4; 26 -6.3; 28 -6.3; 30 -6.2; 32 -6.2; 35 -6.0; 37 -5.9; 40 -5.8; 42 -5.7; 45 -5.6; 49 -5.4; 52 -5.3; 56 -5.1; 59 -5.0; 64 -4.9; 68 -4.7; 73 -4.6; 78 -4.5; 83 -4.4; 89 -4.4; 95 -4.6; 102 -4.7; 109 -5.0; 117 -5.1; 125 -5.4; 134 -5.6; 143 -5.7; 153 -5.6; 164 -5.5; 175 -5.2; 188 -5.0; 201 -4.7; 215 -4.5; 230 -4.1; 246 -3.9; 263 -3.6; 282 -3.3; 301 -3.0; 323 -2.7; 345 -2.4; 369 -2.2; 395 -1.9; 423 -1.6; 452 -1.5; 484 -1.3; 518 -1.2; 554 -0.8; 593 -0.5; 635 -0.2; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.1; 1636 -1.1; 1751 -1.0; 1873 -0.6; 2004 -0.3; 2145 0.2; 2295 0.9; 2455 2.1; 2627 3.4; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.78 | -5.7 dB |
| Peaking | 36 Hz   | 0.58 | -4.5 dB |
| Peaking | 164 Hz  | 0.7  | -4.9 dB |
| Peaking | 1822 Hz | 1.82 | -3.1 dB |
| Peaking | 3905 Hz | 0.93 | 7.2 dB  |
| Peaking | 791 Hz  | 3.63 | 0.7 dB  |
| Peaking | 2963 Hz | 4.8  | 2.3 dB  |
| Peaking | 3510 Hz | 1.25 | -1.2 dB |
| Peaking | 6260 Hz | 2.44 | 5.1 dB  |
| Peaking | 7427 Hz | 1.55 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Black%20Filter/Shure%20SE846%20Black%20Filter.png)