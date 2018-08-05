# Sony MDR-AS50G

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.1; 23 -1.3; 25 -1.7; 26 -1.8; 28 -2.1; 30 -2.4; 32 -2.6; 35 -2.8; 37 -2.9; 40 -3.1; 42 -3.2; 45 -3.3; 49 -3.5; 52 -3.6; 56 -3.6; 59 -3.6; 64 -3.7; 68 -3.8; 73 -3.9; 78 -4.0; 83 -4.2; 89 -4.5; 95 -4.7; 102 -5.2; 109 -5.5; 117 -5.9; 125 -6.4; 134 -6.7; 143 -6.8; 153 -6.8; 164 -6.8; 175 -6.6; 188 -6.4; 201 -6.1; 215 -5.8; 230 -5.5; 246 -5.2; 263 -5.0; 282 -4.7; 301 -4.3; 323 -3.9; 345 -3.4; 369 -3.0; 395 -2.8; 423 -2.4; 452 -2.1; 484 -1.9; 518 -1.6; 554 -1.1; 593 -0.6; 635 -0.4; 679 -0.4; 726 -0.3; 777 0.0; 832 0.1; 890 0.1; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.5; 1429 -2.2; 1529 -3.2; 1636 -3.9; 1751 -4.3; 1873 -4.2; 2004 -4.1; 2145 -3.8; 2295 -3.2; 2455 -2.0; 2627 -0.6; 2811 1.7; 3008 4.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.4; 4514 -0.1; 4830 -2.6; 5168 -3.6; 5530 -2.6; 5917 -1.1; 6331 -0.4; 6775 -1.1; 7249 -3.7; 7756 -6.5; 8299 -6.7; 8880 -3.4; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -1.3; 14260 -5.2; 15258 -3.4; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS50G ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.75 | -2.4 dB |
| Peaking | 166 Hz   | 0.7  | -6.6 dB |
| Peaking | 1976 Hz  | 1.94 | -5.2 dB |
| Peaking | 3399 Hz  | 3.19 | 8.2 dB  |
| Peaking | 8023 Hz  | 4.05 | -7.3 dB |
| Peaking | 860 Hz   | 2.45 | 1.1 dB  |
| Peaking | 4030 Hz  | 9.39 | 3.5 dB  |
| Peaking | 5048 Hz  | 4.83 | -4.5 dB |
| Peaking | 12959 Hz | 0.83 | 1.7 dB  |
| Peaking | 14472 Hz | 3.79 | -7.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS50G/Sony%20MDR-AS50G.png)