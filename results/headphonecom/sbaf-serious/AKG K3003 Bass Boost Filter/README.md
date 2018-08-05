# AKG K3003 Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.9; 23 -2.2; 25 -2.6; 26 -2.8; 28 -3.2; 30 -3.5; 32 -3.8; 35 -4.1; 37 -4.3; 40 -4.5; 42 -4.7; 45 -4.9; 49 -5.1; 52 -5.3; 56 -5.4; 59 -5.6; 64 -5.8; 68 -5.8; 73 -6.1; 78 -6.3; 83 -6.5; 89 -6.8; 95 -7.2; 102 -7.7; 109 -8.2; 117 -8.5; 125 -9.1; 134 -9.5; 143 -9.7; 153 -9.9; 164 -9.9; 175 -9.8; 188 -9.7; 201 -9.5; 215 -9.2; 230 -8.9; 246 -8.6; 263 -8.3; 282 -7.9; 301 -7.5; 323 -7.0; 345 -6.4; 369 -6.0; 395 -5.5; 423 -4.8; 452 -4.4; 484 -4.1; 518 -3.6; 554 -2.9; 593 -2.2; 635 -1.7; 679 -1.4; 726 -0.9; 777 -0.4; 832 -0.2; 890 -0.1; 952 -0.1; 1019 -0.0; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.7; 1429 -0.3; 1529 0.0; 1636 -0.7; 1751 -1.4; 1873 -1.7; 2004 -2.0; 2145 -2.2; 2295 -2.2; 2455 -1.7; 2627 -0.9; 2811 0.6; 3008 2.7; 3219 4.2; 3444 5.4; 3685 5.5; 3943 4.4; 4219 1.8; 4514 -0.8; 4830 -2.9; 5168 -4.1; 5530 -2.7; 5917 0.8; 6331 2.9; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.2; 9502 -3.2; 10167 -2.1; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 77 Hz    | 0.31 | -4.4 dB |
| Peaking | 202 Hz   | 0.68 | -6.9 dB |
| Peaking | 3680 Hz  | 2.53 | 12.5 dB |
| Peaking | 4924 Hz  | 0.91 | -8.8 dB |
| Peaking | 6586 Hz  | 3.11 | 8.9 dB  |
| Peaking | 865 Hz   | 2.96 | 1.3 dB  |
| Peaking | 2210 Hz  | 1.24 | 2.1 dB  |
| Peaking | 2199 Hz  | 2.32 | -3.9 dB |
| Peaking | 9691 Hz  | 6.94 | -3.5 dB |
| Peaking | 10809 Hz | 1.68 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)