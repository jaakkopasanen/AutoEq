# Audeze LCD-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.7; 42 5.5; 45 5.2; 49 4.9; 52 4.7; 56 4.5; 59 4.4; 64 4.4; 68 4.3; 73 4.2; 78 4.0; 83 3.3; 89 2.8; 95 2.4; 102 2.1; 109 2.0; 117 1.8; 125 1.6; 134 1.5; 143 1.4; 153 1.2; 164 1.2; 175 1.1; 188 1.0; 201 0.8; 215 0.8; 230 0.8; 246 0.9; 263 0.9; 282 1.0; 301 1.1; 323 1.2; 345 1.3; 369 1.1; 395 0.9; 423 0.8; 452 0.7; 484 0.6; 518 0.5; 554 0.7; 593 0.9; 635 0.9; 679 0.5; 726 0.5; 777 0.8; 832 0.9; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -1.3; 1336 -1.4; 1429 -1.3; 1529 -1.8; 1636 -2.3; 1751 -2.4; 1873 -2.0; 2004 -2.2; 2145 -2.5; 2295 -2.2; 2455 -1.6; 2627 -1.8; 2811 -1.6; 3008 -1.4; 3219 -1.7; 3444 -1.8; 3685 -2.5; 3943 -3.5; 4219 -5.4; 4514 -6.2; 4830 -6.1; 5168 -4.7; 5530 -3.6; 5917 -2.9; 6331 -0.8; 6775 0.8; 7249 1.2; 7756 -0.1; 8299 -2.5; 8880 -4.0; 9502 -4.0; 10167 -3.3; 10879 -2.4; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.7; 18692 -0.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.4  | 6.2 dB  |
| Peaking | 780 Hz   | 0.51 | 1.2 dB  |
| Peaking | 1725 Hz  | 1.04 | -2.8 dB |
| Peaking | 4667 Hz  | 2.67 | -6.2 dB |
| Peaking | 21590 Hz | 1.69 | -2.6 dB |
| Peaking | 73 Hz    | 3.02 | 1.5 dB  |
| Peaking | 81 Hz    | 1.3  | -0.8 dB |
| Peaking | 7197 Hz  | 4.72 | 3.4 dB  |
| Peaking | 9259 Hz  | 2.9  | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-1/Audeze%20LCD-1.png)