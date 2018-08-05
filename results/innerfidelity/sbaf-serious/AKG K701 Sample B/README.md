# AKG K701 sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.7; 32 5.4; 35 4.9; 37 4.6; 40 4.2; 42 4.0; 45 3.7; 49 3.4; 52 3.1; 56 3.0; 59 3.0; 64 3.5; 68 4.0; 73 3.4; 78 2.4; 83 2.4; 89 2.1; 95 1.1; 102 0.4; 109 0.0; 117 -0.4; 125 -0.9; 134 -1.3; 143 -1.6; 153 -1.8; 164 -1.8; 175 -1.9; 188 -2.0; 201 -2.0; 215 -1.9; 230 -1.9; 246 -1.8; 263 -1.8; 282 -1.8; 301 -1.6; 323 -1.3; 345 -1.1; 369 -1.0; 395 -0.9; 423 -0.4; 452 -0.1; 484 0.1; 518 0.2; 554 0.5; 593 0.8; 635 1.1; 679 1.6; 726 2.0; 777 2.3; 832 1.8; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.6; 1336 -0.7; 1429 -0.8; 1529 -1.0; 1636 -1.4; 1751 -2.1; 1873 -2.6; 2004 -3.1; 2145 -3.2; 2295 -3.0; 2455 -2.7; 2627 -2.4; 2811 -1.7; 3008 -0.8; 3219 0.4; 3444 0.9; 3685 0.1; 3943 -0.2; 4219 -1.4; 4514 -2.2; 4830 -1.9; 5168 -1.2; 5530 -1.6; 5917 -3.7; 6331 -4.8; 6775 -3.9; 7249 -3.5; 7756 -3.8; 8299 -4.5; 8880 -4.2; 9502 -2.8; 10167 -1.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.5; 18692 -2.3; 20000 -3.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.11 | 6.5 dB  |
| Peaking | 68 Hz    | 3.73 | 3.1 dB  |
| Peaking | 759 Hz   | 4.38 | 2.6 dB  |
| Peaking | 2097 Hz  | 2.37 | -3.3 dB |
| Peaking | 7358 Hz  | 1.64 | -4.5 dB |
| Peaking | 165 Hz   | 0.33 | 2.4 dB  |
| Peaking | 196 Hz   | 0.66 | -4.6 dB |
| Peaking | 3424 Hz  | 6.89 | 2.2 dB  |
| Peaking | 19791 Hz | 0.18 | -4.7 dB |
| Peaking | 14499 Hz | 0.59 | 4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20B/AKG%20K701%20sample%20B.png)