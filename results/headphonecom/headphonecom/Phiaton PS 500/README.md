# Phiaton PS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.2dB
GraphicEQ: 10 -84; 20 6.6; 22 5.2; 23 4.6; 25 3.5; 26 3.0; 28 2.0; 30 1.2; 32 0.4; 35 -0.5; 37 -0.7; 40 -0.8; 42 -1.0; 45 -1.8; 49 -2.7; 52 -2.7; 56 -2.1; 59 -2.0; 64 -2.6; 68 -3.4; 73 -4.1; 78 -4.5; 83 -4.8; 89 -5.0; 95 -5.2; 102 -5.3; 109 -5.4; 117 -5.5; 125 -5.5; 134 -5.5; 143 -5.5; 153 -5.4; 164 -4.9; 175 -5.2; 188 -5.0; 201 -4.7; 215 -4.6; 230 -4.2; 246 -3.6; 263 -2.8; 282 -1.7; 301 -0.6; 323 0.4; 345 1.0; 369 1.4; 395 1.6; 423 1.6; 452 1.5; 484 1.5; 518 1.5; 554 1.6; 593 1.7; 635 1.6; 679 1.5; 726 1.2; 777 0.9; 832 1.3; 890 1.3; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.1; 1336 0.6; 1429 1.6; 1529 2.2; 1636 2.1; 1751 1.3; 1873 0.8; 2004 1.7; 2145 3.2; 2295 5.2; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.2dB` and instead set Global volume in the UI for both channels to **-72**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.44 | 6.3 dB  |
| Peaking | 100 Hz  | 1.01 | -5.5 dB |
| Peaking | 191 Hz  | 2.38 | -3.7 dB |
| Peaking | 3068 Hz | 1.2  | 6.1 dB  |
| Peaking | 5472 Hz | 2.51 | 4.7 dB  |
| Peaking | 251 Hz  | 3.45 | -2.1 dB |
| Peaking | 455 Hz  | 1.2  | 3.5 dB  |
| Peaking | 1133 Hz | 4.01 | -1.7 dB |
| Peaking | 477 Hz  | 2.91 | -1.7 dB |
| Peaking | 8419 Hz | 3.78 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Phiaton%20PS%20500/Phiaton%20PS%20500.png)