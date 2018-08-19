# NarMoo R1M Gunmetal Port

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -10.3; 22 -10.0; 23 -9.9; 25 -9.7; 26 -9.6; 28 -9.4; 30 -9.2; 32 -9.0; 35 -8.8; 37 -8.6; 40 -8.4; 42 -8.3; 45 -8.2; 49 -8.0; 52 -7.9; 56 -7.9; 59 -7.8; 64 -7.8; 68 -7.8; 73 -7.8; 78 -7.8; 83 -7.9; 89 -8.0; 95 -8.0; 102 -8.0; 109 -8.0; 117 -7.9; 125 -7.9; 134 -8.0; 143 -7.9; 153 -7.8; 164 -7.8; 175 -7.6; 188 -7.5; 201 -7.4; 215 -7.1; 230 -6.9; 246 -6.6; 263 -6.4; 282 -6.1; 301 -5.8; 323 -5.5; 345 -5.1; 369 -4.7; 395 -4.4; 423 -3.8; 452 -3.6; 484 -3.3; 518 -2.9; 554 -2.3; 593 -1.7; 635 -1.3; 679 -1.2; 726 -0.8; 777 -0.4; 832 -0.4; 890 -0.4; 952 -0.1; 1019 -0.0; 1090 0.0; 1167 0.0; 1248 0.0; 1336 -0.2; 1429 -0.4; 1529 -0.7; 1636 -0.8; 1751 -0.9; 1873 -0.7; 2004 -0.5; 2145 -0.4; 2295 -0.3; 2455 0.1; 2627 -0.1; 2811 -0.4; 3008 -0.6; 3219 -0.7; 3444 -0.9; 3685 -1.3; 3943 -2.2; 4219 -4.3; 4514 -6.3; 4830 -7.8; 5168 -7.6; 5530 -5.3; 5917 -1.8; 6331 0.9; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -0.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.0; 17469 -3.3; 18692 -2.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6471813487744313dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Gunmetal Port ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.12 | -9.5 dB |
| Peaking | 200 Hz   | 0.59 | -5.8 dB |
| Peaking | 5033 Hz  | 3.04 | -9.4 dB |
| Peaking | 6594 Hz  | 2.88 | 4.0 dB  |
| Peaking | 17798 Hz | 3.32 | -3.8 dB |
| Peaking | 15 Hz    | 1.45 | -0.8 dB |
| Peaking | 455 Hz   | 1.17 | -1.6 dB |
| Peaking | 698 Hz   | 0.54 | 1.4 dB  |
| Peaking | 1701 Hz  | 2.51 | -1.1 dB |
| Peaking | 2526 Hz  | 4.06 | 0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Gunmetal%20Port/NarMoo%20R1M%20Gunmetal%20Port.png)