# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.2; 23 4.9; 25 4.3; 26 4.0; 28 3.5; 30 3.0; 32 2.6; 35 2.1; 37 1.7; 40 1.1; 42 0.7; 45 0.2; 49 -0.2; 52 -0.5; 56 -0.7; 59 -0.6; 64 0.1; 68 0.4; 73 -0.8; 78 -2.2; 83 -2.9; 89 -3.4; 95 -3.6; 102 -3.8; 109 -4.6; 117 -5.2; 125 -5.6; 134 -5.9; 143 -6.0; 153 -6.0; 164 -5.7; 175 -5.5; 188 -5.4; 201 -5.3; 215 -5.3; 230 -4.5; 246 -3.3; 263 -2.4; 282 -1.8; 301 -1.8; 323 -1.1; 345 -0.1; 369 0.8; 395 1.4; 423 1.8; 452 1.7; 484 1.6; 518 1.4; 554 1.5; 593 1.6; 635 1.4; 679 1.1; 726 1.0; 777 1.0; 832 0.8; 890 0.6; 952 0.4; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.0; 1336 -1.5; 1429 -2.0; 1529 -2.7; 1636 -3.7; 1751 -4.2; 1873 -4.2; 2004 -4.3; 2145 -4.0; 2295 -3.3; 2455 -2.3; 2627 -1.1; 2811 -0.1; 3008 0.7; 3219 0.9; 3444 0.9; 3685 0.6; 3943 0.6; 4219 0.4; 4514 1.1; 4830 -0.3; 5168 -0.4; 5530 1.0; 5917 4.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -4.5; 8880 -5.3; 9502 -2.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.23 | 5.7 dB  |
| Peaking | 146 Hz  | 1.2  | -6.7 dB |
| Peaking | 1894 Hz | 2.7  | -4.9 dB |
| Peaking | 6351 Hz | 4.71 | 6.4 dB  |
| Peaking | 8659 Hz | 6.2  | -6.7 dB |
| Peaking | 20 Hz   | 0.21 | -0.2 dB |
| Peaking | 227 Hz  | 3.51 | -2.2 dB |
| Peaking | 498 Hz  | 1.14 | 2.4 dB  |
| Peaking | 3183 Hz | 2.23 | 3.0 dB  |
| Peaking | 2908 Hz | 0.96 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)