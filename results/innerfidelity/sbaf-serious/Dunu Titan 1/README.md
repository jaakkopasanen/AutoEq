# Dunu Titan 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 10 -84; 20 -1.6; 22 -1.7; 23 -1.8; 25 -1.9; 26 -2.0; 28 -2.1; 30 -2.2; 32 -2.3; 35 -2.4; 37 -2.4; 40 -2.5; 42 -2.5; 45 -2.6; 49 -2.8; 52 -2.9; 56 -3.1; 59 -3.3; 64 -3.5; 68 -3.7; 73 -4.0; 78 -4.3; 83 -4.5; 89 -4.7; 95 -5.0; 102 -5.2; 109 -5.2; 117 -5.4; 125 -5.5; 134 -5.7; 143 -5.8; 153 -5.9; 164 -5.9; 175 -5.9; 188 -5.8; 201 -5.8; 215 -5.6; 230 -5.5; 246 -5.4; 263 -5.2; 282 -4.9; 301 -4.7; 323 -4.5; 345 -4.2; 369 -3.2; 395 -3.1; 423 -3.1; 452 -2.8; 484 -2.5; 518 -2.0; 554 -1.4; 593 -0.8; 635 -0.6; 679 -0.5; 726 -0.2; 777 0.1; 832 0.2; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.3; 1429 -1.9; 1529 -2.7; 1636 -3.6; 1751 -4.3; 1873 -4.7; 2004 -4.8; 2145 -4.5; 2295 -4.1; 2455 -3.4; 2627 -2.7; 2811 -2.1; 3008 -1.4; 3219 -0.8; 3444 -0.4; 3685 -0.9; 3943 -1.6; 4219 -3.2; 4514 -4.4; 4830 -4.4; 5168 -3.7; 5530 -3.3; 5917 -2.6; 6331 -1.9; 6775 -1.4; 7249 -0.8; 7756 -0.4; 8299 -0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.3; 12455 -0.7; 13327 -1.5; 14260 -2.5; 15258 -2.3; 16326 -0.5; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.3148766394844996dB` and instead set Global volume in the UI for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 101 Hz   | 0.46 | -4.2 dB |
| Peaking | 238 Hz   | 0.91 | -3.3 dB |
| Peaking | 1992 Hz  | 2.35 | -5.1 dB |
| Peaking | 4936 Hz  | 2.8  | -4.4 dB |
| Peaking | 14475 Hz | 3.57 | -2.8 dB |
| Peaking | 22 Hz    | 1.85 | -0.7 dB |
| Peaking | 816 Hz   | 0.63 | -1.7 dB |
| Peaking | 859 Hz   | 1.09 | 2.9 dB  |
| Peaking | 1581 Hz  | 6.71 | -0.7 dB |
| Peaking | 3490 Hz  | 7.5  | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%201/Dunu%20Titan%201.png)