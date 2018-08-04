# Sennheiser HD650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 1.6; 22 0.9; 23 0.6; 25 -0.1; 26 -0.4; 28 -0.9; 30 -1.4; 32 -1.8; 35 -2.3; 37 -2.5; 40 -2.5; 42 -2.3; 45 -2.0; 49 -2.5; 52 -3.1; 56 -3.7; 59 -3.9; 64 -3.9; 68 -3.7; 73 -3.9; 78 -4.2; 83 -4.2; 89 -4.4; 95 -4.4; 102 -4.3; 109 -4.1; 117 -4.0; 125 -4.0; 134 -4.0; 143 -3.9; 153 -3.8; 164 -3.6; 175 -3.5; 188 -3.3; 201 -3.3; 215 -3.0; 230 -2.7; 246 -2.5; 263 -2.4; 282 -2.3; 301 -2.1; 323 -1.9; 345 -1.7; 369 -1.4; 395 -1.3; 423 -1.1; 452 -0.9; 484 -0.9; 518 -0.8; 554 -0.5; 593 -0.0; 635 0.1; 679 -0.0; 726 -0.0; 777 0.4; 832 0.1; 890 -0.1; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.5; 1429 -0.6; 1529 -0.8; 1636 -1.0; 1751 -1.1; 1873 -1.3; 2004 -1.4; 2145 -1.4; 2295 -1.2; 2455 -1.0; 2627 -1.0; 2811 -1.0; 3008 -0.5; 3219 -0.4; 3444 0.4; 3685 1.3; 3943 2.1; 4219 1.1; 4514 -0.2; 4830 0.4; 5168 2.5; 5530 3.3; 5917 2.3; 6331 1.6; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -1.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.11 | 2.3 dB  |
| Peaking | 81 Hz   | 0.51 | -4.0 dB |
| Peaking | 209 Hz  | 0.94 | -1.4 dB |
| Peaking | 2083 Hz | 2.1  | -1.6 dB |
| Peaking | 5653 Hz | 2.97 | 3.0 dB  |
| Peaking | 754 Hz  | 3.08 | 0.6 dB  |
| Peaking | 3283 Hz | 2.36 | -1.5 dB |
| Peaking | 4040 Hz | 2.37 | 3.2 dB  |
| Peaking | 4481 Hz | 5.81 | -3.2 dB |
| Peaking | 9192 Hz | 7.48 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD650/Sennheiser%20HD650.png)