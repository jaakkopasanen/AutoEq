# HiFiMAN HE1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 3.8; 22 3.5; 23 3.4; 25 3.3; 26 3.2; 28 3.1; 30 3.0; 32 2.9; 35 2.7; 37 2.5; 40 2.3; 42 2.2; 45 2.1; 49 2.0; 52 1.9; 56 1.7; 59 1.5; 64 1.4; 68 1.3; 73 1.2; 78 1.0; 83 0.8; 89 0.6; 95 0.4; 102 0.2; 109 -0.0; 117 -0.2; 125 -0.4; 134 -0.5; 143 -0.5; 153 -0.8; 164 -0.9; 175 -1.2; 188 -1.5; 201 -0.7; 215 0.2; 230 -0.2; 246 -0.7; 263 -1.1; 282 -1.3; 301 -1.7; 323 -2.3; 345 -2.3; 369 -1.1; 395 1.5; 423 1.3; 452 0.3; 484 0.1; 518 -0.5; 554 -1.2; 593 1.0; 635 1.2; 679 0.1; 726 -0.7; 777 0.4; 832 0.1; 890 -0.2; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 0.5; 1248 2.4; 1336 1.9; 1429 2.3; 1529 2.4; 1636 2.5; 1751 2.7; 1873 3.2; 2004 4.3; 2145 3.1; 2295 4.0; 2455 4.1; 2627 4.2; 2811 3.4; 3008 2.3; 3219 1.1; 3444 1.4; 3685 2.0; 3943 1.8; 4219 2.7; 4514 -1.7; 4830 -3.9; 5168 -3.8; 5530 -1.2; 5917 0.6; 6331 -2.7; 6775 -5.0; 7249 -4.3; 7756 -3.8; 8299 -3.7; 8880 -3.2; 9502 -1.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.6; 20000 -4.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.43813194480295dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.24 | 3.7 dB  |
| Peaking | 202 Hz  | 0.62 | -1.3 dB |
| Peaking | 2335 Hz | 1.01 | 4.0 dB  |
| Peaking | 4928 Hz | 8.11 | -5.1 dB |
| Peaking | 7409 Hz | 2.7  | -5.2 dB |
| Peaking | 341 Hz  | 5.17 | -2.3 dB |
| Peaking | 404 Hz  | 6.64 | 2.9 dB  |
| Peaking | 1074 Hz | 7.95 | -1.4 dB |
| Peaking | 3264 Hz | 5.33 | -3.1 dB |
| Peaking | 3521 Hz | 2.36 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE1000/HiFiMAN%20HE1000.png)