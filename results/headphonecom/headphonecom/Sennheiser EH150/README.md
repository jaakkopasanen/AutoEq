# Sennheiser EH150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 5.9; 452 4.9; 484 3.4; 518 2.1; 554 1.1; 593 0.7; 635 0.3; 679 0.5; 726 0.4; 777 0.1; 832 -0.0; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.2; 1167 0.5; 1248 0.8; 1336 1.4; 1429 2.2; 1529 2.8; 1636 3.2; 1751 3.8; 1873 4.3; 2004 5.0; 2145 5.7; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 5.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.21 | 6.3 dB  |
| Peaking | 321 Hz  | 1.42 | 4.1 dB  |
| Peaking | 2252 Hz | 1.99 | 4.8 dB  |
| Peaking | 3644 Hz | 1.7  | 4.8 dB  |
| Peaking | 5693 Hz | 2.89 | 5.1 dB  |
| Peaking | 15 Hz   | 1.9  | 1.1 dB  |
| Peaking | 426 Hz  | 5.17 | 2.5 dB  |
| Peaking | 734 Hz  | 0.98 | -1.6 dB |
| Peaking | 1576 Hz | 3.5  | 1.2 dB  |
| Peaking | 8313 Hz | 4.24 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20EH150/Sennheiser%20EH150.png)