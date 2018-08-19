# Dunu DN1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.2; 22 -4.2; 23 -4.2; 25 -4.2; 26 -4.1; 28 -4.1; 30 -4.1; 32 -4.1; 35 -4.1; 37 -4.1; 40 -4.1; 42 -4.1; 45 -4.1; 49 -4.2; 52 -4.2; 56 -4.2; 59 -4.3; 64 -4.4; 68 -4.4; 73 -4.5; 78 -4.6; 83 -4.7; 89 -4.8; 95 -4.9; 102 -4.9; 109 -4.8; 117 -4.7; 125 -4.7; 134 -4.7; 143 -4.6; 153 -4.5; 164 -4.3; 175 -4.1; 188 -4.0; 201 -3.8; 215 -3.5; 230 -3.3; 246 -3.1; 263 -2.9; 282 -2.5; 301 -2.3; 323 -2.1; 345 -1.8; 369 -1.6; 395 -1.4; 423 -1.1; 452 -0.8; 484 -0.7; 518 -0.5; 554 -0.2; 593 0.1; 635 0.3; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.0; 1529 -1.2; 1636 -1.3; 1751 -1.1; 1873 -0.7; 2004 -0.3; 2145 0.1; 2295 0.7; 2455 1.7; 2627 2.2; 2811 2.8; 3008 3.9; 3219 5.4; 3444 6.0; 3685 6.0; 3943 5.7; 4219 2.1; 4514 -1.0; 4830 -1.3; 5168 0.8; 5530 1.6; 5917 1.6; 6331 1.8; 6775 1.7; 7249 0.7; 7756 -1.4; 8299 -4.5; 8880 -7.3; 9502 -8.2; 10167 -6.5; 10879 -2.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999844387975dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.19 | -3.9 dB |
| Peaking | 152 Hz   | 0.68 | -2.9 dB |
| Peaking | 3466 Hz  | 3.37 | 6.9 dB  |
| Peaking | 6685 Hz  | 4.1  | 2.9 dB  |
| Peaking | 9307 Hz  | 3.6  | -9.3 dB |
| Peaking | 743 Hz   | 2.26 | 1.0 dB  |
| Peaking | 1604 Hz  | 2.83 | -1.6 dB |
| Peaking | 4425 Hz  | 2.62 | 2.8 dB  |
| Peaking | 4621 Hz  | 6.38 | -6.0 dB |
| Peaking | 11765 Hz | 7.35 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN1000/Dunu%20DN1000.png)