# FLC Technologies FLC8 CCY Voca

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.9; 32 5.7; 35 5.6; 37 5.5; 40 5.3; 42 5.2; 45 5.0; 49 4.7; 52 4.6; 56 4.3; 59 4.1; 64 3.8; 68 3.5; 73 3.2; 78 2.8; 83 2.5; 89 2.1; 95 1.7; 102 1.5; 109 1.3; 117 1.1; 125 0.8; 134 0.4; 143 0.3; 153 0.1; 164 -0.1; 175 -0.2; 188 -0.3; 201 -0.4; 215 -0.5; 230 -0.4; 246 -0.5; 263 -0.5; 282 -0.4; 301 -0.3; 323 -0.3; 345 -0.2; 369 -0.0; 395 0.0; 423 0.3; 452 0.4; 484 0.4; 518 0.5; 554 0.8; 593 1.1; 635 1.2; 679 1.1; 726 1.1; 777 1.2; 832 1.3; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.5; 1248 -2.3; 1336 -3.5; 1429 -4.8; 1529 -6.2; 1636 -7.0; 1751 -6.7; 1873 -5.6; 2004 -3.9; 2145 -2.7; 2295 -1.9; 2455 -1.0; 2627 -0.7; 2811 -0.5; 3008 -0.5; 3219 2.5; 3444 5.8; 3685 6.0; 3943 6.0; 4219 5.4; 4514 5.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.6; 10167 -2.4; 10879 -2.3; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 CCY Voca ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.78 | 5.9 dB  |
| Peaking | 57 Hz   | 1.31 | 2.6 dB  |
| Peaking | 1722 Hz | 2.24 | -8.1 dB |
| Peaking | 4991 Hz | 1.04 | 7.3 dB  |
| Peaking | 9574 Hz | 1.7  | -3.9 dB |
| Peaking | 226 Hz  | 1.56 | -0.8 dB |
| Peaking | 741 Hz  | 1.81 | 1.8 dB  |
| Peaking | 3008 Hz | 3.96 | -4.4 dB |
| Peaking | 3474 Hz | 3.98 | 4.6 dB  |
| Peaking | 4545 Hz | 5.82 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20CCY%20Voca/FLC%20Technologies%20FLC8%20CCY%20Voca.png)