# Sony MDR-V6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.6; 23 5.3; 25 4.6; 26 4.2; 28 3.4; 30 2.7; 32 1.9; 35 0.9; 37 0.4; 40 -0.3; 42 -0.7; 45 -1.2; 49 -1.9; 52 -2.2; 56 -2.2; 59 -1.9; 64 -2.0; 68 -2.3; 73 -2.5; 78 -2.6; 83 -2.5; 89 -2.5; 95 -2.4; 102 -2.0; 109 -1.9; 117 -1.6; 125 -1.4; 134 -1.2; 143 -1.0; 153 -0.8; 164 -0.1; 175 0.9; 188 2.3; 201 2.4; 215 1.9; 230 1.2; 246 1.0; 263 1.5; 282 1.7; 301 1.5; 323 1.3; 345 1.0; 369 0.2; 395 -0.4; 423 -0.6; 452 -0.8; 484 -0.9; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.4; 679 -0.4; 726 -0.4; 777 -0.2; 832 -0.2; 890 -0.3; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -1.1; 1336 -1.3; 1429 -1.9; 1529 -2.7; 1636 -3.4; 1751 -4.0; 1873 -4.1; 2004 -4.2; 2145 -4.3; 2295 -4.1; 2455 -3.8; 2627 -4.3; 2811 -4.9; 3008 -4.9; 3219 -4.3; 3444 -3.7; 3685 -2.4; 3943 -2.2; 4219 -4.7; 4514 -6.3; 4830 -4.2; 5168 -0.8; 5530 1.8; 5917 2.9; 6331 2.0; 6775 -0.6; 7249 -2.5; 7756 -3.4; 8299 -5.0; 8880 -7.3; 9502 -8.7; 10167 -7.5; 10879 -3.6; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.77 | 6.2 dB  |
| Peaking | 70 Hz   | 1.28 | -3.1 dB |
| Peaking | 1863 Hz | 2.28 | -3.2 dB |
| Peaking | 3114 Hz | 1.47 | -4.1 dB |
| Peaking | 9463 Hz | 3.9  | -9.5 dB |
| Peaking | 198 Hz  | 5.59 | 2.9 dB  |
| Peaking | 288 Hz  | 4.31 | 1.9 dB  |
| Peaking | 4625 Hz | 5.34 | -7.1 dB |
| Peaking | 6119 Hz | 1.73 | 7.2 dB  |
| Peaking | 7267 Hz | 2.41 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)