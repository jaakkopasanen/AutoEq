# Dunu DN2000J

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 1.6; 22 1.0; 23 0.8; 25 0.3; 26 0.2; 28 -0.2; 30 -0.5; 32 -0.7; 35 -1.0; 37 -1.2; 40 -1.3; 42 -1.4; 45 -1.6; 49 -1.7; 52 -1.8; 56 -1.9; 59 -2.0; 64 -2.1; 68 -2.2; 73 -2.3; 78 -2.5; 83 -2.8; 89 -3.1; 95 -3.4; 102 -3.9; 109 -4.3; 117 -4.7; 125 -5.2; 134 -5.5; 143 -5.7; 153 -5.8; 164 -5.8; 175 -5.6; 188 -5.4; 201 -5.3; 215 -5.0; 230 -4.7; 246 -4.5; 263 -4.3; 282 -3.9; 301 -3.6; 323 -3.3; 345 -3.0; 369 -2.8; 395 -2.5; 423 -2.0; 452 -1.7; 484 -1.6; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.3; 1336 -0.7; 1429 -1.3; 1529 -2.0; 1636 -2.2; 1751 -2.2; 1873 -2.1; 2004 -1.9; 2145 -1.8; 2295 -1.5; 2455 -1.0; 2627 -0.8; 2811 -0.9; 3008 -0.3; 3219 0.4; 3444 1.8; 3685 2.9; 3943 2.6; 4219 -0.1; 4514 -3.9; 4830 -6.2; 5168 -6.2; 5530 -8.3; 5917 -9.4; 6331 -8.7; 6775 -6.7; 7249 -6.4; 7756 -6.9; 8299 -7.2; 8880 -6.7; 9502 -4.9; 10167 -1.9; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -1.5; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000J ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 164 Hz   | 0.67 | -5.8 dB |
| Peaking | 1811 Hz  | 2.76 | -2.1 dB |
| Peaking | 3794 Hz  | 4.26 | 6.1 dB  |
| Peaking | 8520 Hz  | 3.83 | -5.2 dB |
| Peaking | 5773 Hz  | 1.86 | -9.2 dB |
| Peaking | 16 Hz    | 1.18 | 2.5 dB  |
| Peaking | 39 Hz    | 1.64 | -1.0 dB |
| Peaking | 811 Hz   | 2.56 | 1.0 dB  |
| Peaking | 11064 Hz | 3.15 | 2.8 dB  |
| Peaking | 10273 Hz | 1.68 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000J/Dunu%20DN2000J.png)