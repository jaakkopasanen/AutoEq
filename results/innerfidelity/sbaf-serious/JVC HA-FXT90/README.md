# JVC HA-FXT90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 10 -84; 20 1.9; 22 1.4; 23 1.1; 25 0.6; 26 0.4; 28 -0.1; 30 -0.6; 32 -1.1; 35 -1.6; 37 -1.9; 40 -2.3; 42 -2.6; 45 -2.9; 49 -3.4; 52 -3.7; 56 -4.1; 59 -4.4; 64 -4.8; 68 -5.1; 73 -5.5; 78 -5.8; 83 -6.1; 89 -6.5; 95 -6.8; 102 -7.0; 109 -7.0; 117 -7.2; 125 -7.3; 134 -7.4; 143 -7.5; 153 -7.4; 164 -7.4; 175 -7.2; 188 -7.1; 201 -7.0; 215 -6.7; 230 -6.4; 246 -6.2; 263 -5.8; 282 -5.5; 301 -5.1; 323 -4.9; 345 -4.5; 369 -4.1; 395 -3.8; 423 -3.2; 452 -2.8; 484 -2.4; 518 -2.1; 554 -1.6; 593 -1.0; 635 -0.6; 679 -0.5; 726 -0.1; 777 0.2; 832 0.2; 890 0.0; 952 0.2; 1019 -0.0; 1090 -0.4; 1167 -0.7; 1248 -0.7; 1336 -1.2; 1429 -1.3; 1529 -0.4; 1636 -0.1; 1751 -0.7; 1873 -1.1; 2004 -1.5; 2145 -1.8; 2295 -2.0; 2455 -2.0; 2627 -2.1; 2811 -1.8; 3008 -0.8; 3219 0.3; 3444 1.1; 3685 0.9; 3943 -0.2; 4219 -2.5; 4514 -4.7; 4830 -6.1; 5168 -6.5; 5530 -5.5; 5917 -3.3; 6331 -1.9; 6775 -1.8; 7249 -3.3; 7756 -5.4; 8299 -6.4; 8880 -4.6; 9502 -0.7; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.9597026241316586dB` and instead set Global volume in the UI for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FXT90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 111 Hz   | 0.62 | -6.5 dB |
| Peaking | 252 Hz   | 0.97 | -3.5 dB |
| Peaking | 2280 Hz  | 4.24 | -1.5 dB |
| Peaking | 6048 Hz  | 1.16 | -4.6 dB |
| Peaking | 24000 Hz | 2.12 | -3.9 dB |
| Peaking | 19 Hz    | 2.23 | 2.1 dB  |
| Peaking | 3671 Hz  | 4.92 | 3.4 dB  |
| Peaking | 4976 Hz  | 2.6  | -5.8 dB |
| Peaking | 7051 Hz  | 1.23 | 6.6 dB  |
| Peaking | 8212 Hz  | 3.67 | -9.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA-FXT90/JVC%20HA-FXT90.png)