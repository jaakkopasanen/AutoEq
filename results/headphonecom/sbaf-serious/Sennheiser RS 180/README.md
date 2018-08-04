# Sennheiser RS 180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 10 -84; 20 -0.9; 22 -1.7; 23 -2.0; 25 -2.7; 26 -3.0; 28 -3.5; 30 -4.0; 32 -4.4; 35 -4.9; 37 -5.2; 40 -5.6; 42 -5.8; 45 -6.1; 49 -6.5; 52 -6.6; 56 -6.5; 59 -6.5; 64 -7.1; 68 -7.5; 73 -7.3; 78 -7.1; 83 -7.3; 89 -7.2; 95 -7.3; 102 -7.3; 109 -7.0; 117 -6.7; 125 -6.5; 134 -6.5; 143 -6.4; 153 -6.4; 164 -6.2; 175 -6.1; 188 -6.1; 201 -5.9; 215 -5.5; 230 -5.0; 246 -4.7; 263 -4.7; 282 -4.4; 301 -4.1; 323 -3.8; 345 -3.5; 369 -3.3; 395 -3.1; 423 -2.7; 452 -2.5; 484 -2.4; 518 -2.2; 554 -1.9; 593 -1.6; 635 -1.4; 679 -1.4; 726 -1.5; 777 -0.7; 832 1.0; 890 0.3; 952 0.1; 1019 0.0; 1090 0.3; 1167 0.4; 1248 0.6; 1336 1.0; 1429 0.7; 1529 -0.7; 1636 -2.4; 1751 -3.9; 1873 -4.9; 2004 -5.7; 2145 -6.2; 2295 -5.7; 2455 -4.2; 2627 -2.5; 2811 0.4; 3008 2.2; 3219 -1.8; 3444 -0.6; 3685 2.2; 3943 1.4; 4219 0.5; 4514 -2.1; 4830 -5.5; 5168 -4.8; 5530 -2.6; 5917 -2.3; 6331 -3.1; 6775 1.7; 7249 1.3; 7756 -2.0; 8299 -6.2; 8880 -8.7; 9502 -7.5; 10167 -3.4; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.0dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 95 Hz    |  0.3  | -7.2 dB |
| Peaking | 2051 Hz  |  2.8  | -7.1 dB |
| Peaking | 1261 Hz  |  1.43 | 2.0 dB  |
| Peaking | 9009 Hz  |  4.76 | -9.6 dB |
| Peaking | 24000 Hz |  2.17 | -5.6 dB |
| Peaking | 19 Hz    |  2.04 | 1.5 dB  |
| Peaking | 4175 Hz  |  2.56 | 6.3 dB  |
| Peaking | 4779 Hz  |  2.66 | -8.4 dB |
| Peaking | 7014 Hz  | 10    | 4.8 dB  |
| Peaking | 11154 Hz |  6.71 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20180/Sennheiser%20RS%20180.png)