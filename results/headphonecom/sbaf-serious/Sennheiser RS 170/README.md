# Sennheiser RS 170

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 10 -84; 20 6.7; 22 5.6; 23 5.2; 25 4.3; 26 3.9; 28 3.1; 30 2.5; 32 1.9; 35 1.2; 37 0.7; 40 0.0; 42 -0.3; 45 -0.9; 49 -1.4; 52 -1.8; 56 -2.3; 59 -2.5; 64 -2.8; 68 -3.2; 73 -3.7; 78 -4.0; 83 -3.8; 89 -3.8; 95 -3.4; 102 -3.3; 109 -3.7; 117 -4.4; 125 -5.2; 134 -5.7; 143 -5.9; 153 -6.0; 164 -5.8; 175 -5.6; 188 -6.0; 201 -5.8; 215 -5.1; 230 -4.3; 246 -3.9; 263 -3.5; 282 -3.3; 301 -2.7; 323 -2.0; 345 -1.7; 369 -1.3; 395 -1.5; 423 -1.7; 452 -1.8; 484 -1.7; 518 -1.1; 554 -0.6; 593 -0.1; 635 0.4; 679 0.6; 726 0.8; 777 1.5; 832 2.6; 890 1.7; 952 0.4; 1019 -0.1; 1090 0.9; 1167 -0.1; 1248 -1.3; 1336 -2.2; 1429 -3.2; 1529 -4.3; 1636 -5.5; 1751 -4.2; 1873 -1.3; 2004 -3.2; 2145 -4.0; 2295 -4.4; 2455 -4.4; 2627 -4.1; 2811 -4.2; 3008 -3.8; 3219 -3.6; 3444 -3.4; 3685 -3.0; 3943 -1.7; 4219 0.3; 4514 4.6; 4830 6.0; 5168 2.4; 5530 2.0; 5917 2.2; 6331 0.3; 6775 -1.1; 7249 1.2; 7756 0.3; 8299 -1.1; 8880 -3.7; 9502 -5.0; 10167 -3.7; 10879 -0.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.770350994758656dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 170 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.9  | 6.2 dB  |
| Peaking | 148 Hz  | 0.74 | -6.0 dB |
| Peaking | 1608 Hz | 6.85 | -4.0 dB |
| Peaking | 4140 Hz | 0.87 | -9.4 dB |
| Peaking | 4731 Hz | 2.2  | 14.1 dB |
| Peaking | 65 Hz   | 3.23 | -1.4 dB |
| Peaking | 825 Hz  | 3.08 | 3.1 dB  |
| Peaking | 2334 Hz | 4.56 | -1.6 dB |
| Peaking | 9051 Hz | 1.43 | 3.7 dB  |
| Peaking | 9468 Hz | 3.76 | -8.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20170/Sennheiser%20RS%20170.png)