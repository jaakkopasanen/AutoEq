# KEF M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.9; 22 -8.9; 23 -8.9; 25 -8.9; 26 -8.9; 28 -8.9; 30 -8.9; 32 -8.9; 35 -8.8; 37 -8.7; 40 -8.6; 42 -8.6; 45 -8.6; 49 -8.7; 52 -8.6; 56 -8.5; 59 -8.4; 64 -8.4; 68 -8.4; 73 -8.4; 78 -8.3; 83 -8.1; 89 -7.8; 95 -7.4; 102 -7.4; 109 -7.4; 117 -7.0; 125 -7.4; 134 -7.7; 143 -7.8; 153 -7.8; 164 -7.5; 175 -7.6; 188 -7.3; 201 -7.2; 215 -7.2; 230 -7.2; 246 -6.9; 263 -6.5; 282 -5.8; 301 -5.0; 323 -3.8; 345 -2.8; 369 -2.3; 395 -2.2; 423 -2.0; 452 -2.2; 484 -2.6; 518 -3.1; 554 -3.2; 593 -3.1; 635 -3.1; 679 -2.9; 726 -2.5; 777 -1.8; 832 -1.3; 890 -0.9; 952 -0.3; 1019 0.2; 1090 0.7; 1167 1.2; 1248 1.3; 1336 1.2; 1429 1.1; 1529 1.2; 1636 1.1; 1751 1.4; 1873 1.5; 2004 1.4; 2145 1.4; 2295 1.4; 2455 1.3; 2627 1.0; 2811 0.7; 3008 0.8; 3219 0.3; 3444 0.3; 3685 1.0; 3943 2.0; 4219 3.3; 4514 4.2; 4830 5.3; 5168 5.4; 5530 5.8; 5917 5.9; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.19 | -8.9 dB |
| Peaking | 211 Hz  | 1.21 | -4.0 dB |
| Peaking | 654 Hz  | 2.2  | -2.7 dB |
| Peaking | 1445 Hz | 1    | 1.7 dB  |
| Peaking | 5451 Hz | 2.34 | 6.4 dB  |
| Peaking | 276 Hz  | 5.26 | -0.9 dB |
| Peaking | 366 Hz  | 4.59 | 1.1 dB  |
| Peaking | 3387 Hz | 9.06 | -1.1 dB |
| Peaking | 6632 Hz | 6.32 | 2.2 dB  |
| Peaking | 7776 Hz | 2.52 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KEF%20M500/KEF%20M500.png)