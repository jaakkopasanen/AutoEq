# Sony MDR-V500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 5.9; 109 5.4; 117 4.7; 125 4.1; 134 3.5; 143 3.2; 153 3.6; 164 3.5; 175 3.0; 188 2.9; 201 2.7; 215 3.3; 230 3.8; 246 3.5; 263 3.3; 282 2.8; 301 2.1; 323 2.1; 345 2.0; 369 2.0; 395 1.9; 423 1.8; 452 1.7; 484 1.5; 518 1.2; 554 1.1; 593 1.2; 635 1.4; 679 1.1; 726 0.6; 777 0.7; 832 1.2; 890 0.6; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 0.1; 1248 -0.7; 1336 -1.8; 1429 -2.4; 1529 -2.7; 1636 -2.7; 1751 -2.9; 1873 -2.9; 2004 -2.9; 2145 -2.9; 2295 -3.0; 2455 -3.1; 2627 -3.1; 2811 -3.4; 3008 -4.3; 3219 -4.4; 3444 -4.0; 3685 -3.6; 3943 -3.4; 4219 -3.0; 4514 -2.1; 4830 -1.1; 5168 0.3; 5530 1.4; 5917 0.5; 6331 -1.1; 6775 -0.2; 7249 1.1; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -2.1; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.27 | 5.5 dB  |
| Peaking | 204 Hz   | 0.2  | 1.8 dB  |
| Peaking | 3567 Hz  | 0.58 | -6.4 dB |
| Peaking | 5668 Hz  | 0.96 | 4.9 dB  |
| Peaking | 10357 Hz | 8.47 | -2.1 dB |
| Peaking | 38 Hz    | 2.42 | -0.3 dB |
| Peaking | 1244 Hz  | 2.17 | 1.5 dB  |
| Peaking | 1421 Hz  | 2.9  | -2.0 dB |
| Peaking | 2645 Hz  | 2.94 | 1.5 dB  |
| Peaking | 3088 Hz  | 2.91 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V500/Sony%20MDR-V500.png)