# Sennheiser EH250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.6; 40 4.8; 42 4.2; 45 3.6; 49 2.9; 52 2.3; 56 1.5; 59 1.0; 64 0.5; 68 0.4; 73 -0.0; 78 -0.5; 83 -0.8; 89 -1.0; 95 -1.2; 102 -1.3; 109 -1.4; 117 -1.4; 125 -1.1; 134 0.2; 143 1.2; 153 1.6; 164 1.9; 175 2.0; 188 2.3; 201 2.7; 215 3.1; 230 3.4; 246 3.6; 263 3.6; 282 3.0; 301 0.9; 323 -0.2; 345 0.3; 369 0.7; 395 1.1; 423 1.2; 452 1.1; 484 0.7; 518 0.2; 554 0.1; 593 0.2; 635 0.2; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.2; 952 0.0; 1019 0.0; 1090 0.2; 1167 0.6; 1248 0.9; 1336 1.5; 1429 2.0; 1529 2.5; 1636 2.7; 1751 2.8; 1873 3.1; 2004 3.4; 2145 3.9; 2295 4.6; 2455 4.6; 2627 5.0; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.8; 3943 1.6; 4219 1.4; 4514 4.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.4; 6775 1.7; 7249 -0.3; 7756 0.0; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.77 | 6.6 dB  |
| Peaking | 93 Hz   | 1.25 | -2.8 dB |
| Peaking | 221 Hz  | 1.62 | 3.7 dB  |
| Peaking | 2804 Hz | 1.26 | 5.7 dB  |
| Peaking | 5521 Hz | 3.51 | 5.7 dB  |
| Peaking | 1072 Hz | 2.85 | -0.9 dB |
| Peaking | 1527 Hz | 2.22 | 0.9 dB  |
| Peaking | 6346 Hz | 8.23 | 3.4 dB  |
| Peaking | 2528 Hz | 7.8  | -0.9 dB |
| Peaking | 7079 Hz | 2.94 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20EH250/Sennheiser%20EH250.png)