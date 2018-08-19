# Klipsch X10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.9; 22 -1.0; 23 -1.0; 25 -1.0; 26 -1.0; 28 -1.1; 30 -1.1; 32 -1.1; 35 -1.2; 37 -1.3; 40 -1.3; 42 -1.4; 45 -1.5; 49 -1.7; 52 -1.8; 56 -2.0; 59 -2.1; 64 -2.4; 68 -2.6; 73 -2.9; 78 -3.1; 83 -3.2; 89 -3.5; 95 -3.8; 102 -4.0; 109 -4.0; 117 -4.2; 125 -4.3; 134 -4.5; 143 -4.5; 153 -4.7; 164 -4.6; 175 -4.6; 188 -4.6; 201 -4.5; 215 -4.4; 230 -4.3; 246 -4.2; 263 -4.0; 282 -3.8; 301 -3.7; 323 -3.4; 345 -3.2; 369 -3.0; 395 -2.7; 423 -2.4; 452 -2.1; 484 -2.0; 518 -1.7; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.5; 726 -0.3; 777 0.1; 832 0.2; 890 0.1; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.7; 1529 -0.8; 1636 -1.0; 1751 -0.8; 1873 -0.6; 2004 -0.3; 2145 -0.2; 2295 0.0; 2455 0.3; 2627 0.0; 2811 -0.3; 3008 0.2; 3219 1.9; 3444 4.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.8; 8299 -3.8; 8880 -4.0; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999752452863dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.18 | -0.7 dB |
| Peaking | 114 Hz  | 0.77 | -2.5 dB |
| Peaking | 243 Hz  | 0.71 | -3.2 dB |
| Peaking | 5093 Hz | 1.4  | 7.2 dB  |
| Peaking | 8557 Hz | 4.75 | -6.6 dB |
| Peaking | 809 Hz  | 2.58 | 1.0 dB  |
| Peaking | 3363 Hz | 0.99 | -2.7 dB |
| Peaking | 3705 Hz | 3.69 | 5.2 dB  |
| Peaking | 6381 Hz | 6.1  | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X10/Klipsch%20X10.png)