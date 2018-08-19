# Sennheiser RS 160

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.9; 23 -1.0; 25 -1.2; 26 -1.2; 28 -1.3; 30 -1.4; 32 -1.4; 35 -1.5; 37 -1.6; 40 -1.6; 42 -1.6; 45 -1.6; 49 -1.6; 52 -1.6; 56 -1.5; 59 -1.5; 64 -1.6; 68 -1.5; 73 -1.5; 78 -1.4; 83 -1.2; 89 -1.0; 95 -1.1; 102 -1.8; 109 -2.7; 117 -3.0; 125 -2.3; 134 -2.6; 143 -3.2; 153 -3.1; 164 -2.4; 175 -1.8; 188 -2.0; 201 -2.1; 215 -1.7; 230 -1.4; 246 -1.1; 263 -0.7; 282 -0.3; 301 0.0; 323 0.0; 345 -0.2; 369 -0.4; 395 -0.6; 423 -0.7; 452 -0.5; 484 0.0; 518 0.4; 554 1.0; 593 1.4; 635 1.6; 679 1.5; 726 1.6; 777 1.8; 832 1.7; 890 1.8; 952 0.9; 1019 -0.3; 1090 -0.8; 1167 -0.7; 1248 -0.8; 1336 -1.5; 1429 -2.3; 1529 -2.8; 1636 -3.7; 1751 -3.6; 1873 0.1; 2004 -1.7; 2145 -2.9; 2295 -3.2; 2455 -2.7; 2627 -1.6; 2811 -2.2; 3008 -1.8; 3219 -1.0; 3444 -0.2; 3685 0.7; 3943 1.4; 4219 0.6; 4514 0.4; 4830 2.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.9; 8880 -5.5; 9502 -6.4; 10167 -4.6; 10879 -1.6; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.098269946750708dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 0.99 | -2.8 dB |
| Peaking | 1612 Hz | 5.26 | -3.4 dB |
| Peaking | 2474 Hz | 2.37 | -3.0 dB |
| Peaking | 5858 Hz | 2.48 | 7.2 dB  |
| Peaking | 9338 Hz | 3.93 | -7.8 dB |
| Peaking | 38 Hz   | 1.07 | -0.7 dB |
| Peaking | 45 Hz   | 0.38 | -0.7 dB |
| Peaking | 92 Hz   | 3.63 | 1.5 dB  |
| Peaking | 824 Hz  | 1.59 | 2.9 dB  |
| Peaking | 1102 Hz | 2.08 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20160/Sennheiser%20RS%20160.png)