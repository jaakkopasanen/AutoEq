# Echobox Finder X1 Red Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -10.2; 22 -10.3; 23 -10.3; 25 -10.3; 26 -10.3; 28 -10.2; 30 -10.2; 32 -10.1; 35 -10.0; 37 -9.9; 40 -9.8; 42 -9.7; 45 -9.6; 49 -9.4; 52 -9.3; 56 -9.2; 59 -9.1; 64 -9.0; 68 -8.9; 73 -8.8; 78 -8.8; 83 -8.7; 89 -8.6; 95 -8.6; 102 -8.4; 109 -8.2; 117 -7.9; 125 -7.8; 134 -7.6; 143 -7.3; 153 -7.1; 164 -6.9; 175 -6.5; 188 -6.1; 201 -5.9; 215 -5.5; 230 -5.1; 246 -4.8; 263 -4.4; 282 -4.0; 301 -3.6; 323 -3.2; 345 -2.8; 369 -2.4; 395 -2.1; 423 -1.6; 452 -1.2; 484 -1.0; 518 -0.7; 554 -0.3; 593 0.2; 635 0.4; 679 0.5; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.4; 1636 -2.8; 1751 -3.0; 1873 -3.1; 2004 -3.1; 2145 -3.2; 2295 -3.4; 2455 -3.3; 2627 -3.6; 2811 -4.1; 3008 -4.8; 3219 -5.7; 3444 -6.2; 3685 -6.4; 3943 -6.4; 4219 -7.3; 4514 -8.0; 4830 -8.2; 5168 -8.3; 5530 -9.6; 5917 -10.7; 6331 -12.0; 6775 -10.4; 7249 -8.2; 7756 -6.1; 8299 -4.7; 8880 -4.1; 9502 -4.9; 10167 -7.0; 10879 -8.2; 11640 -6.5; 12455 -3.3; 13327 -2.1; 14260 -3.8; 15258 -4.8; 16326 -2.4; 17469 -0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9225735650765596dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Red Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.47 | -8.7 dB |
| Peaking | 109 Hz   | 0.39 | -6.8 dB |
| Peaking | 697 Hz   | 1.49 | 2.2 dB  |
| Peaking | 5618 Hz  | 0.69 | -9.5 dB |
| Peaking | 11066 Hz | 5.41 | -4.7 dB |
| Peaking | 1693 Hz  | 3.66 | -1.3 dB |
| Peaking | 5233 Hz  | 2.11 | 1.4 dB  |
| Peaking | 6390 Hz  | 4.58 | -3.8 dB |
| Peaking | 8444 Hz  | 4.36 | 2.7 dB  |
| Peaking | 15301 Hz | 5.21 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Red%20Filter/Echobox%20Finder%20X1%20Red%20Filter.png)