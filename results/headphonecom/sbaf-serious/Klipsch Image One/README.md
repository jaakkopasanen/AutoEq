# Klipsch Image One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.1dB
GraphicEQ: 10 -84; 20 7.0; 22 6.0; 23 5.5; 25 4.7; 26 4.4; 28 3.7; 30 3.1; 32 2.6; 35 1.9; 37 1.5; 40 1.0; 42 0.6; 45 0.1; 49 -0.4; 52 -0.8; 56 -1.2; 59 -1.5; 64 -1.8; 68 -2.0; 73 -2.2; 78 -2.6; 83 -3.0; 89 -3.3; 95 -3.6; 102 -3.8; 109 -3.9; 117 -4.3; 125 -4.2; 134 -4.4; 143 -4.5; 153 -4.6; 164 -4.7; 175 -4.6; 188 -4.9; 201 -4.7; 215 -4.3; 230 -4.0; 246 -3.7; 263 -3.5; 282 -3.4; 301 -3.3; 323 -3.2; 345 -2.8; 369 -2.5; 395 -2.4; 423 -2.3; 452 -2.2; 484 -1.8; 518 -1.3; 554 -0.6; 593 0.2; 635 1.0; 679 1.5; 726 1.5; 777 1.2; 832 0.6; 890 0.0; 952 -0.5; 1019 0.3; 1090 -0.6; 1167 -1.5; 1248 -1.9; 1336 -2.5; 1429 -2.9; 1529 -3.2; 1636 -3.7; 1751 -4.3; 1873 -4.7; 2004 -5.0; 2145 -5.2; 2295 -5.5; 2455 -5.8; 2627 -6.6; 2811 -6.9; 3008 -6.4; 3219 -5.3; 3444 -3.8; 3685 -1.6; 3943 0.5; 4219 1.3; 4514 1.7; 4830 1.2; 5168 1.3; 5530 -0.2; 5917 1.0; 6331 0.6; 6775 -1.5; 7249 0.4; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.084825809277445dB` and instead set Global volume in the UI for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.12 | 6.9 dB  |
| Peaking | 115 Hz  | 0.73 | -3.7 dB |
| Peaking | 231 Hz  | 1.14 | -2.7 dB |
| Peaking | 2789 Hz | 1.15 | -8.2 dB |
| Peaking | 4286 Hz | 1.93 | 5.4 dB  |
| Peaking | 248 Hz  | 4.83 | 0.7 dB  |
| Peaking | 500 Hz  | 1.35 | -2.3 dB |
| Peaking | 678 Hz  | 1.58 | 3.7 dB  |
| Peaking | 1643 Hz | 1.59 | -1.2 dB |
| Peaking | 2370 Hz | 5.22 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)