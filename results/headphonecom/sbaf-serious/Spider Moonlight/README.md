# Spider Moonlight

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.4; 22 1.9; 23 1.6; 25 1.2; 26 1.0; 28 0.7; 30 0.4; 32 0.1; 35 -0.3; 37 -0.5; 40 -0.7; 42 -0.9; 45 -1.1; 49 -1.4; 52 -1.6; 56 -1.8; 59 -1.9; 64 -2.2; 68 -2.4; 73 -2.6; 78 -2.7; 83 -3.1; 89 -3.4; 95 -3.4; 102 -3.5; 109 -3.7; 117 -4.2; 125 -4.5; 134 -4.8; 143 -5.1; 153 -5.3; 164 -4.9; 175 -4.7; 188 -5.1; 201 -5.0; 215 -4.5; 230 -3.8; 246 -3.2; 263 -2.3; 282 -1.0; 301 0.3; 323 1.1; 345 1.5; 369 1.5; 395 1.1; 423 0.7; 452 0.1; 484 -0.2; 518 -0.4; 554 -0.5; 593 -0.6; 635 -0.4; 679 0.8; 726 0.7; 777 0.9; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -1.2; 1429 -2.0; 1529 -3.0; 1636 -3.9; 1751 -4.6; 1873 -5.0; 2004 -5.6; 2145 -6.1; 2295 -6.3; 2455 -6.0; 2627 -5.3; 2811 -4.8; 3008 -5.0; 3219 -5.1; 3444 -4.3; 3685 -4.0; 3943 -4.8; 4219 -4.9; 4514 -3.8; 4830 -0.4; 5168 4.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -2.6; 10167 -3.9; 10879 -2.4; 11640 -1.6; 12455 -3.3; 13327 -5.4; 14260 -4.5; 15258 -0.8; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.090907327114607dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider Moonlight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 141 Hz   | 1.05 | -5.5 dB |
| Peaking | 2220 Hz  | 1.8  | -6.0 dB |
| Peaking | 4314 Hz  | 1.76 | -7.8 dB |
| Peaking | 5666 Hz  | 2.32 | 11.3 dB |
| Peaking | 12730 Hz | 1.39 | -4.3 dB |
| Peaking | 23 Hz    | 2.7  | 2.2 dB  |
| Peaking | 222 Hz   | 3.19 | -2.0 dB |
| Peaking | 344 Hz   | 2.95 | 3.0 dB  |
| Peaking | 804 Hz   | 3.19 | 1.3 dB  |
| Peaking | 16112 Hz | 5.13 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Spider%20Moonlight/Spider%20Moonlight.png)