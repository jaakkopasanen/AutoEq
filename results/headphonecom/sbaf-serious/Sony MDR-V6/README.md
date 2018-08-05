# Sony MDR-V6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 4.9; 37 4.4; 40 3.7; 42 3.3; 45 2.7; 49 2.1; 52 1.8; 56 1.8; 59 2.0; 64 1.9; 68 1.5; 73 1.2; 78 1.0; 83 0.9; 89 0.7; 95 0.5; 102 0.4; 109 0.2; 117 -0.0; 125 -0.2; 134 -0.4; 143 -0.4; 153 -0.4; 164 0.1; 175 1.0; 188 2.4; 201 2.5; 215 1.9; 230 1.2; 246 1.0; 263 1.5; 282 1.7; 301 1.5; 323 1.3; 345 1.0; 369 0.2; 395 -0.4; 423 -0.6; 452 -0.8; 484 -0.9; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.4; 679 -0.4; 726 -0.4; 777 -0.2; 832 -0.2; 890 -0.3; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -1.1; 1336 -1.3; 1429 -1.9; 1529 -2.7; 1636 -3.4; 1751 -4.0; 1873 -4.1; 2004 -4.2; 2145 -4.3; 2295 -4.1; 2455 -3.8; 2627 -4.3; 2811 -4.9; 3008 -4.9; 3219 -4.3; 3444 -3.7; 3685 -2.4; 3943 -2.2; 4219 -4.7; 4514 -6.3; 4830 -4.2; 5168 -0.8; 5530 1.8; 5917 2.9; 6331 2.0; 6775 -0.6; 7249 -2.5; 7756 -3.4; 8299 -5.0; 8880 -7.3; 9502 -8.7; 10167 -7.5; 10879 -3.6; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.81 | 6.3 dB  |
| Peaking | 2446 Hz  | 1.07 | -4.7 dB |
| Peaking | 4536 Hz  | 6.17 | -5.4 dB |
| Peaking | 5840 Hz  | 4.59 | 5.2 dB  |
| Peaking | 9371 Hz  | 3.24 | -9.2 dB |
| Peaking | 156 Hz   | 1.82 | -1.5 dB |
| Peaking | 292 Hz   | 4.28 | 1.7 dB  |
| Peaking | 195 Hz   | 3.69 | 3.3 dB  |
| Peaking | 1710 Hz  | 8.34 | -1.1 dB |
| Peaking | 11990 Hz | 6.09 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)