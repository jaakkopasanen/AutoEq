# Venture Electronics Monk Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.4; 89 4.5; 95 3.6; 102 2.6; 109 2.0; 117 1.2; 125 0.3; 134 -0.5; 143 -1.1; 153 -1.7; 164 -2.1; 175 -2.2; 188 -2.4; 201 -2.2; 215 -2.1; 230 -2.3; 246 -2.2; 263 -2.1; 282 -1.9; 301 -1.6; 323 -1.4; 345 -0.8; 369 -1.0; 395 -2.6; 423 -1.1; 452 -0.4; 484 -0.3; 518 -0.2; 554 0.0; 593 0.2; 635 0.3; 679 0.3; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.7; 1336 -1.4; 1429 -2.4; 1529 -3.6; 1636 -4.6; 1751 -5.7; 1873 -6.5; 2004 -7.4; 2145 -7.9; 2295 -8.2; 2455 -7.5; 2627 -6.9; 2811 -5.7; 3008 -3.8; 3219 -1.9; 3444 -0.1; 3685 -0.1; 3943 -0.6; 4219 -2.1; 4514 -3.5; 4830 -4.4; 5168 -3.5; 5530 -1.7; 5917 -1.5; 6331 0.5; 6775 -3.4; 7249 -5.0; 7756 -5.9; 8299 -5.3; 8880 -3.0; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -1.5; 14260 -5.8; 15258 -6.9; 16326 -3.7; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.75 | 7.3 dB  |
| Peaking | 2208 Hz  | 1.85 | -8.6 dB |
| Peaking | 7758 Hz  | 4.12 | -6.2 dB |
| Peaking | 24000 Hz | 1.61 | -4.4 dB |
| Peaking | 15102 Hz | 3.36 | -7.3 dB |
| Peaking | 21 Hz    | 2.96 | 1.9 dB  |
| Peaking | 81 Hz    | 2.45 | 3.3 dB  |
| Peaking | 191 Hz   | 1.02 | -3.2 dB |
| Peaking | 4472 Hz  | 1.67 | 3.6 dB  |
| Peaking | 4768 Hz  | 3.86 | -7.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Monk%20Plus/Venture%20Electronics%20Monk%20Plus.png)