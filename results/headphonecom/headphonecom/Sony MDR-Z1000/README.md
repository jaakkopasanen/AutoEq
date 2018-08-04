# Sony MDR-Z1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.6; 45 5.0; 49 4.1; 52 3.5; 56 2.8; 59 2.3; 64 1.5; 68 1.0; 73 0.5; 78 0.1; 83 -0.3; 89 -0.5; 95 -0.5; 102 -0.7; 109 -1.0; 117 -1.4; 125 -1.9; 134 -2.2; 143 -2.3; 153 -2.2; 164 -1.7; 175 -1.3; 188 -1.2; 201 -0.9; 215 -0.7; 230 -0.3; 246 0.1; 263 0.9; 282 1.1; 301 0.3; 323 -0.5; 345 -0.9; 369 -1.2; 395 -1.5; 423 -1.5; 452 -1.4; 484 -1.4; 518 -1.1; 554 -0.8; 593 -0.5; 635 -0.2; 679 0.1; 726 0.1; 777 -0.1; 832 0.0; 890 0.0; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.1; 1336 0.1; 1429 -0.0; 1529 -0.3; 1636 -0.8; 1751 -1.2; 1873 -1.2; 2004 -0.9; 2145 0.2; 2295 1.6; 2455 2.5; 2627 3.4; 2811 4.5; 3008 5.3; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -3.8; 9502 -4.3; 10167 -0.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.78 | 6.7 dB  |
| Peaking | 126 Hz  | 1.33 | -2.7 dB |
| Peaking | 452 Hz  | 2.74 | -1.6 dB |
| Peaking | 4602 Hz | 1.04 | 7.1 dB  |
| Peaking | 9145 Hz | 4.3  | -6.5 dB |
| Peaking | 273 Hz  | 7.64 | 1.8 dB  |
| Peaking | 1896 Hz | 2.72 | -2.9 dB |
| Peaking | 3131 Hz | 1.75 | 3.5 dB  |
| Peaking | 4210 Hz | 1.04 | -2.2 dB |
| Peaking | 6111 Hz | 4.85 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)