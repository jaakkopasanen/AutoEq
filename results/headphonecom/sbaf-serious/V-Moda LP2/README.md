# V-Moda LP2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.2; 22 -2.7; 23 -2.9; 25 -3.3; 26 -3.4; 28 -3.7; 30 -3.9; 32 -4.1; 35 -4.3; 37 -4.3; 40 -4.5; 42 -4.5; 45 -4.6; 49 -4.7; 52 -4.7; 56 -4.7; 59 -4.7; 64 -4.8; 68 -4.7; 73 -4.5; 78 -4.1; 83 -3.9; 89 -4.3; 95 -5.4; 102 -6.1; 109 -6.5; 117 -6.6; 125 -6.7; 134 -7.0; 143 -7.2; 153 -7.2; 164 -6.7; 175 -6.8; 188 -6.7; 201 -6.2; 215 -5.6; 230 -4.8; 246 -3.8; 263 -3.1; 282 -2.4; 301 -1.0; 323 0.5; 345 1.9; 369 2.7; 395 3.3; 423 4.1; 452 4.6; 484 5.0; 518 5.1; 554 5.2; 593 4.7; 635 3.7; 679 2.4; 726 1.4; 777 0.8; 832 0.3; 890 -0.1; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 0.1; 1248 0.2; 1336 -0.3; 1429 -0.2; 1529 -0.2; 1636 -0.1; 1751 0.3; 1873 0.9; 2004 1.1; 2145 1.2; 2295 -0.0; 2455 -0.7; 2627 -0.9; 2811 -1.8; 3008 -2.1; 3219 -1.2; 3444 0.4; 3685 1.8; 3943 3.6; 4219 4.3; 4514 5.4; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -1.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 0.6  | -1.8 dB |
| Peaking | 40 Hz   | 0.8  | -3.6 dB |
| Peaking | 161 Hz  | 0.76 | -7.4 dB |
| Peaking | 466 Hz  | 1.51 | 7.2 dB  |
| Peaking | 5317 Hz | 2.37 | 7.1 dB  |
| Peaking | 606 Hz  | 5.38 | 1.9 dB  |
| Peaking | 909 Hz  | 1.09 | -1.1 dB |
| Peaking | 2996 Hz | 2.79 | -6.0 dB |
| Peaking | 3204 Hz | 1.16 | 3.2 dB  |
| Peaking | 9364 Hz | 2.06 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20LP2/V-Moda%20LP2.png)