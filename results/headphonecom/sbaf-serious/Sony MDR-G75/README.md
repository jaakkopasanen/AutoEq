# Sony MDR-G75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.8; 45 5.1; 49 4.0; 52 3.3; 56 2.4; 59 1.8; 64 1.0; 68 0.4; 73 -0.2; 78 -0.8; 83 -1.3; 89 -1.7; 95 -2.2; 102 -2.7; 109 -3.1; 117 -3.6; 125 -3.9; 134 -4.0; 143 -4.3; 153 -4.2; 164 -4.2; 175 -4.0; 188 -3.8; 201 -3.6; 215 -3.3; 230 -2.9; 246 -2.6; 263 -2.4; 282 -2.0; 301 -1.4; 323 -1.0; 345 -0.6; 369 -0.1; 395 0.3; 423 -0.2; 452 -0.1; 484 -0.2; 518 -0.1; 554 0.1; 593 0.4; 635 0.5; 679 0.3; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.9; 1429 -1.5; 1529 -2.3; 1636 -3.2; 1751 -3.7; 1873 -3.1; 2004 -1.7; 2145 -0.2; 2295 1.4; 2455 3.2; 2627 4.7; 2811 5.5; 3008 5.4; 3219 4.6; 3444 2.7; 3685 0.3; 3943 -1.8; 4219 -2.2; 4514 -0.4; 4830 3.2; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -1.5; 9502 -1.2; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-G75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.75 | 7.0 dB  |
| Peaking | 138 Hz   |  0.92 | -5.1 dB |
| Peaking | 3948 Hz  |  0.72 | -9.6 dB |
| Peaking | 2946 Hz  |  2.36 | 12.9 dB |
| Peaking | 5592 Hz  |  1.99 | 12.8 dB |
| Peaking | 1164 Hz  |  0.55 | 1.4 dB  |
| Peaking | 1748 Hz  |  2.67 | -3.7 dB |
| Peaking | 2362 Hz  |  5.43 | 1.3 dB  |
| Peaking | 4202 Hz  | 10.86 | -1.9 dB |
| Peaking | 12752 Hz |  2.59 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-G75/Sony%20MDR-G75.png)