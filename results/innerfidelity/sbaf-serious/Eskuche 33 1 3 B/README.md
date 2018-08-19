# Eskuche 33 1 3 B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.2; 35 4.1; 37 3.4; 40 2.5; 42 2.0; 45 1.3; 49 0.7; 52 0.4; 56 0.1; 59 -0.0; 64 -0.2; 68 -0.3; 73 -0.4; 78 -0.6; 83 -0.6; 89 -0.8; 95 -0.9; 102 -0.9; 109 -0.7; 117 -0.6; 125 -0.7; 134 -0.9; 143 -1.1; 153 -1.3; 164 -1.4; 175 -1.4; 188 -1.5; 201 -1.7; 215 -1.8; 230 -1.9; 246 -2.0; 263 -2.1; 282 -2.1; 301 -2.1; 323 -2.0; 345 -1.9; 369 -1.8; 395 -2.0; 423 -2.2; 452 -2.3; 484 -2.7; 518 -2.9; 554 -2.9; 593 -2.6; 635 -2.5; 679 -2.6; 726 -2.5; 777 -2.3; 832 -2.0; 890 -1.5; 952 -0.4; 1019 0.2; 1090 0.8; 1167 1.4; 1248 1.5; 1336 2.3; 1429 3.0; 1529 3.2; 1636 3.5; 1751 3.9; 1873 4.1; 2004 4.2; 2145 4.5; 2295 4.4; 2455 4.2; 2627 4.2; 2811 4.3; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.9; 5530 5.6; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eskuche 33 1 3 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.51 | 6.9 dB  |
| Peaking | 1417 Hz | 0.16 | -4.0 dB |
| Peaking | 1702 Hz | 0.91 | 6.4 dB  |
| Peaking | 3909 Hz | 1.07 | 7.9 dB  |
| Peaking | 6067 Hz | 3.66 | 4.5 dB  |
| Peaking | 36 Hz   | 2.4  | 1.9 dB  |
| Peaking | 40 Hz   | 0.71 | -1.1 dB |
| Peaking | 369 Hz  | 3.77 | 0.8 dB  |
| Peaking | 733 Hz  | 3.58 | -0.7 dB |
| Peaking | 7726 Hz | 8.24 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Eskuche%2033%201%203%20B/Eskuche%2033%201%203%20B.png)