# Sony MDR-V6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.3dB
GraphicEQ: 10 -84; 20 6.7; 22 5.6; 23 5.1; 25 4.1; 26 3.7; 28 2.9; 30 2.1; 32 1.4; 35 0.3; 37 -0.2; 40 -0.9; 42 -1.3; 45 -1.8; 49 -2.4; 52 -2.8; 56 -2.7; 59 -2.5; 64 -2.6; 68 -2.9; 73 -3.2; 78 -3.3; 83 -3.3; 89 -3.3; 95 -3.3; 102 -3.0; 109 -3.0; 117 -2.9; 125 -2.7; 134 -2.5; 143 -2.3; 153 -2.1; 164 -1.4; 175 -0.5; 188 1.0; 201 1.1; 215 0.5; 230 -0.2; 246 -0.4; 263 0.1; 282 0.3; 301 0.1; 323 -0.0; 345 -0.4; 369 -1.1; 395 -1.6; 423 -1.8; 452 -1.8; 484 -1.7; 518 -1.6; 554 -1.3; 593 -1.0; 635 -0.7; 679 -0.4; 726 -0.4; 777 -0.3; 832 -0.3; 890 -0.3; 952 -0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.4; 1336 0.1; 1429 0.2; 1529 -0.0; 1636 -0.4; 1751 -0.9; 1873 -1.2; 2004 -1.3; 2145 -1.3; 2295 -1.0; 2455 -0.8; 2627 -1.3; 2811 -1.9; 3008 -2.3; 3219 -2.0; 3444 -1.6; 3685 -0.4; 3943 0.2; 4219 -1.1; 4514 -1.5; 4830 1.3; 5168 4.6; 5530 6.0; 5917 5.9; 6331 4.2; 6775 0.8; 7249 -1.5; 7756 -2.4; 8299 -3.6; 8880 -5.4; 9502 -6.1; 10167 -4.0; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.3dB` and instead set Global volume in the UI for both channels to **-73**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.01 | 7.4 dB  |
| Peaking | 54 Hz    | 0.84 | -3.5 dB |
| Peaking | 108 Hz   | 1.69 | -2.2 dB |
| Peaking | 5765 Hz  | 5.05 | 7.6 dB  |
| Peaking | 9104 Hz  | 3.22 | -6.5 dB |
| Peaking | 190 Hz   | 2.87 | 2.4 dB  |
| Peaking | 463 Hz   | 2.48 | -1.9 dB |
| Peaking | 159 Hz   | 3.6  | -1.8 dB |
| Peaking | 2947 Hz  | 1.8  | -2.1 dB |
| Peaking | 11560 Hz | 3.85 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-V6/Sony%20MDR-V6.png)