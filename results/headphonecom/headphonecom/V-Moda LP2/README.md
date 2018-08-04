# V-Moda LP2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.7; 22 -7.2; 23 -7.4; 25 -7.8; 26 -8.0; 28 -8.2; 30 -8.5; 32 -8.6; 35 -8.8; 37 -8.9; 40 -9.1; 42 -9.1; 45 -9.2; 49 -9.2; 52 -9.2; 56 -9.2; 59 -9.2; 64 -9.2; 68 -9.1; 73 -8.8; 78 -8.4; 83 -8.1; 89 -8.3; 95 -9.1; 102 -9.5; 109 -9.6; 117 -9.5; 125 -9.2; 134 -9.1; 143 -9.1; 153 -8.9; 164 -8.3; 175 -8.3; 188 -8.2; 201 -7.7; 215 -7.0; 230 -6.3; 246 -5.2; 263 -4.5; 282 -3.8; 301 -2.4; 323 -0.8; 345 0.5; 369 1.3; 395 2.1; 423 2.9; 452 3.6; 484 4.2; 518 4.6; 554 4.7; 593 4.3; 635 3.4; 679 2.3; 726 1.4; 777 0.6; 832 0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.3; 1248 0.8; 1336 1.1; 1429 1.9; 1529 2.5; 1636 2.9; 1751 3.3; 1873 3.8; 2004 4.1; 2145 4.2; 2295 3.0; 2455 2.3; 2627 2.1; 2811 1.2; 3008 0.4; 3219 1.1; 3444 2.5; 3685 3.8; 3943 5.7; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 6 Hz    | 1.51 | -6.2 dB |
| Peaking | 38 Hz   | 0.39 | -8.1 dB |
| Peaking | 171 Hz  | 0.67 | -7.0 dB |
| Peaking | 475 Hz  | 1.28 | 6.8 dB  |
| Peaking | 4806 Hz | 1.33 | 6.5 dB  |
| Peaking | 950 Hz  | 2.45 | -1.7 dB |
| Peaking | 1938 Hz | 1.85 | 3.5 dB  |
| Peaking | 3040 Hz | 4.69 | -2.9 dB |
| Peaking | 6396 Hz | 3.91 | 3.8 dB  |
| Peaking | 7433 Hz | 1.67 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/V-Moda%20LP2/V-Moda%20LP2.png)