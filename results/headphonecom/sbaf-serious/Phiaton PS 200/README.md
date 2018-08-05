# Phiaton PS 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.6; 22 1.6; 23 1.6; 25 1.6; 26 1.6; 28 1.6; 30 1.6; 32 1.5; 35 1.5; 37 1.5; 40 1.5; 42 1.5; 45 1.5; 49 1.4; 52 1.4; 56 1.4; 59 1.4; 64 1.3; 68 1.2; 73 1.1; 78 1.0; 83 0.8; 89 0.5; 95 0.1; 102 -0.4; 109 -0.9; 117 -1.4; 125 -2.0; 134 -2.5; 143 -2.7; 153 -2.9; 164 -3.0; 175 -3.1; 188 -3.2; 201 -3.2; 215 -3.0; 230 -2.9; 246 -2.9; 263 -2.9; 282 -2.6; 301 -2.4; 323 -2.3; 345 -1.9; 369 -1.8; 395 -1.6; 423 -1.3; 452 -1.1; 484 -1.0; 518 -0.8; 554 -0.6; 593 -0.2; 635 0.1; 679 0.1; 726 0.2; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -1.0; 1429 -1.3; 1529 -1.6; 1636 -1.8; 1751 -1.8; 1873 -1.5; 2004 -1.2; 2145 -0.8; 2295 -0.0; 2455 1.2; 2627 2.6; 2811 4.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.3; 4514 3.6; 4830 3.2; 5168 3.2; 5530 2.7; 5917 1.7; 6331 0.4; 6775 -0.8; 7249 -1.9; 7756 -3.0; 8299 -4.2; 8880 -5.8; 9502 -7.3; 10167 -7.0; 10879 -3.8; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 158 Hz   | 0.18 | 4.3 dB  |
| Peaking | 207 Hz   | 0.49 | -7.6 dB |
| Peaking | 2025 Hz  | 1.09 | -5.5 dB |
| Peaking | 3293 Hz  | 1.13 | 8.8 dB  |
| Peaking | 9363 Hz  | 2.6  | -8.3 dB |
| Peaking | 89 Hz    | 3.24 | 0.5 dB  |
| Peaking | 135 Hz   | 4.61 | -0.7 dB |
| Peaking | 7296 Hz  | 6.6  | -1.1 dB |
| Peaking | 12109 Hz | 6    | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)