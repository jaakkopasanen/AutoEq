# Sennheiser CX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 2.5; 22 2.1; 23 1.9; 25 1.6; 26 1.4; 28 1.2; 30 0.9; 32 0.7; 35 0.5; 37 0.3; 40 0.1; 42 0.0; 45 -0.1; 49 -0.3; 52 -0.5; 56 -0.6; 59 -0.7; 64 -1.0; 68 -1.1; 73 -1.3; 78 -1.5; 83 -1.9; 89 -2.2; 95 -2.7; 102 -3.4; 109 -3.8; 117 -4.6; 125 -5.2; 134 -5.8; 143 -6.3; 153 -6.5; 164 -6.8; 175 -7.0; 188 -7.0; 201 -7.1; 215 -7.0; 230 -7.0; 246 -7.0; 263 -6.7; 282 -6.6; 301 -6.3; 323 -5.9; 345 -5.4; 369 -5.1; 395 -4.7; 423 -4.1; 452 -3.8; 484 -3.4; 518 -3.0; 554 -2.2; 593 -1.8; 635 -1.2; 679 -0.4; 726 0.2; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.7; 1429 -2.2; 1529 -2.9; 1636 -3.4; 1751 -3.8; 1873 -4.0; 2004 -4.3; 2145 -4.5; 2295 -4.4; 2455 -4.1; 2627 -3.5; 2811 -2.3; 3008 -0.5; 3219 1.1; 3444 2.5; 3685 3.0; 3943 2.2; 4219 -0.3; 4514 -2.9; 4830 -5.3; 5168 -6.3; 5530 -3.6; 5917 0.3; 6331 3.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -1.3; 10167 -0.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 211 Hz  | 0.75 | -7.7 dB |
| Peaking | 2205 Hz | 1.72 | -5.1 dB |
| Peaking | 3694 Hz | 3    | 5.6 dB  |
| Peaking | 5087 Hz | 3.3  | -7.8 dB |
| Peaking | 6506 Hz | 4.84 | 6.0 dB  |
| Peaking | 12 Hz   | 0.59 | 3.4 dB  |
| Peaking | 130 Hz  | 4.83 | -0.9 dB |
| Peaking | 452 Hz  | 1.89 | -1.2 dB |
| Peaking | 803 Hz  | 1.85 | 2.1 dB  |
| Peaking | 1561 Hz | 4.35 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20680/Sennheiser%20CX%20680.png)