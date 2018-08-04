# Sennheiser HD555

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.1; 22 4.3; 23 3.9; 25 3.2; 26 2.9; 28 2.4; 30 1.9; 32 1.5; 35 0.9; 37 0.6; 40 0.2; 42 -0.0; 45 -0.3; 49 -0.7; 52 -0.8; 56 -0.8; 59 -0.8; 64 -0.8; 68 -0.2; 73 -0.2; 78 -1.2; 83 -1.7; 89 -2.0; 95 -2.2; 102 -2.4; 109 -2.5; 117 -2.6; 125 -2.5; 134 -2.7; 143 -2.7; 153 -2.7; 164 -2.5; 175 -2.7; 188 -2.6; 201 -2.7; 215 -2.8; 230 -2.7; 246 -2.7; 263 -2.6; 282 -2.5; 301 -2.4; 323 -2.3; 345 -2.2; 369 -2.0; 395 -1.8; 423 -1.4; 452 -1.2; 484 -0.9; 518 -0.7; 554 -0.5; 593 0.1; 635 0.1; 679 0.2; 726 0.3; 777 0.2; 832 0.3; 890 0.3; 952 0.0; 1019 0.0; 1090 0.2; 1167 0.6; 1248 1.2; 1336 2.2; 1429 3.3; 1529 4.2; 1636 4.8; 1751 4.3; 1873 3.7; 2004 3.6; 2145 3.6; 2295 3.3; 2455 3.5; 2627 3.8; 2811 3.8; 3008 2.8; 3219 1.6; 3444 1.4; 3685 2.0; 3943 4.4; 4219 6.0; 4514 5.2; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.53 | 5.0 dB  |
| Peaking | 173 Hz  | 0.53 | -3.0 dB |
| Peaking | 1638 Hz | 2.63 | 4.3 dB  |
| Peaking | 2515 Hz | 2.65 | 2.6 dB  |
| Peaking | 5219 Hz | 1.91 | 6.5 dB  |
| Peaking | 654 Hz  | 4.18 | 0.8 dB  |
| Peaking | 3513 Hz | 7.34 | -1.2 dB |
| Peaking | 6436 Hz | 4.09 | 4.8 dB  |
| Peaking | 4142 Hz | 8.51 | 3.0 dB  |
| Peaking | 6702 Hz | 1.55 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD555/Sennheiser%20HD555.png)