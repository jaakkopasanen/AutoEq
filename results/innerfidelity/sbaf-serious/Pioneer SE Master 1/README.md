# Pioneer SE Master 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 3.2; 22 2.4; 23 2.1; 25 1.5; 26 1.3; 28 0.9; 30 0.5; 32 0.3; 35 0.1; 37 0.0; 40 -0.3; 42 -0.6; 45 -1.1; 49 -1.8; 52 -2.3; 56 -2.9; 59 -3.2; 64 -3.7; 68 -4.1; 73 -4.5; 78 -4.9; 83 -5.2; 89 -5.7; 95 -6.0; 102 -6.3; 109 -6.5; 117 -6.6; 125 -6.9; 134 -6.9; 143 -7.0; 153 -7.1; 164 -6.9; 175 -6.9; 188 -6.9; 201 -6.8; 215 -6.5; 230 -6.3; 246 -6.0; 263 -5.8; 282 -5.4; 301 -5.1; 323 -4.8; 345 -4.5; 369 -4.2; 395 -3.9; 423 -3.5; 452 -3.1; 484 -3.0; 518 -2.6; 554 -2.0; 593 -1.4; 635 -1.3; 679 -1.3; 726 -1.0; 777 -0.6; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.1; 1090 0.6; 1167 1.3; 1248 2.0; 1336 2.3; 1429 2.1; 1529 1.7; 1636 1.5; 1751 1.1; 1873 0.3; 2004 -0.8; 2145 -1.7; 2295 -2.3; 2455 -2.3; 2627 -2.4; 2811 -2.9; 3008 -2.6; 3219 -1.6; 3444 0.2; 3685 0.7; 3943 0.8; 4219 -0.7; 4514 -2.1; 4830 -3.4; 5168 -4.1; 5530 -5.9; 5917 -11.1; 6331 -10.7; 6775 -5.5; 7249 -3.6; 7756 -2.8; 8299 -2.1; 8880 -1.5; 9502 -0.6; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -2.1; 17469 -6.9; 18692 -10.5; 20000 -11.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2508448048906673dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE Master 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.68 | 4.2 dB   |
| Peaking | 121 Hz   | 0.6  | -6.4 dB  |
| Peaking | 278 Hz   | 1.02 | -3.0 dB  |
| Peaking | 2692 Hz  | 4.65 | -2.9 dB  |
| Peaking | 6110 Hz  | 4.37 | -12.2 dB |
| Peaking | 486 Hz   | 4.02 | -0.7 dB  |
| Peaking | 1402 Hz  | 2.26 | 2.8 dB   |
| Peaking | 2217 Hz  | 5.18 | -1.8 dB  |
| Peaking | 3806 Hz  | 8.1  | 2.1 dB   |
| Peaking | 19234 Hz | 1.87 | -12.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE%20Master%201/Pioneer%20SE%20Master%201.png)