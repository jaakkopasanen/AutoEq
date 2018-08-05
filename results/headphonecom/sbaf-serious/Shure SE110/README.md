# Shure SE110

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.9; 28 5.8; 30 5.8; 32 5.7; 35 5.7; 37 5.6; 40 5.6; 42 5.5; 45 5.4; 49 5.3; 52 5.3; 56 5.2; 59 5.1; 64 4.9; 68 4.9; 73 4.8; 78 4.6; 83 4.3; 89 3.9; 95 3.5; 102 3.0; 109 2.6; 117 2.0; 125 1.2; 134 0.7; 143 0.4; 153 0.1; 164 -0.1; 175 -0.1; 188 -0.2; 201 -0.2; 215 -0.2; 230 -0.1; 246 -0.3; 263 -0.4; 282 -0.2; 301 -0.2; 323 -0.0; 345 0.1; 369 0.2; 395 0.3; 423 0.5; 452 0.5; 484 0.5; 518 0.6; 554 0.6; 593 0.9; 635 1.0; 679 0.8; 726 0.8; 777 0.9; 832 0.8; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -2.0; 1429 -3.1; 1529 -4.1; 1636 -4.7; 1751 -5.0; 1873 -4.6; 2004 -3.6; 2145 -2.1; 2295 -1.4; 2455 -0.4; 2627 1.1; 2811 3.1; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.8; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE110 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.68 | 6.0 dB  |
| Peaking | 73 Hz   | 1.6  | 3.3 dB  |
| Peaking | 773 Hz  | 1.54 | 1.3 dB  |
| Peaking | 1808 Hz | 1.65 | -7.1 dB |
| Peaking | 3963 Hz | 0.99 | 7.6 dB  |
| Peaking | 191 Hz  | 1.93 | -0.9 dB |
| Peaking | 3130 Hz | 5.89 | 2.5 dB  |
| Peaking | 3793 Hz | 1.43 | -1.2 dB |
| Peaking | 6272 Hz | 2.45 | 5.4 dB  |
| Peaking | 7378 Hz | 1.58 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE110/Shure%20SE110.png)