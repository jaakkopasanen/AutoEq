# Etymotic ER4SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.8; 59 5.6; 64 5.2; 68 5.0; 73 4.7; 78 4.4; 83 4.0; 89 3.7; 95 3.4; 102 3.1; 109 3.0; 117 2.8; 125 2.5; 134 2.3; 143 2.1; 153 1.9; 164 1.7; 175 1.6; 188 1.5; 201 1.4; 215 1.3; 230 1.3; 246 1.3; 263 1.3; 282 1.3; 301 1.3; 323 1.3; 345 1.3; 369 1.4; 395 1.4; 423 1.6; 452 1.6; 484 1.6; 518 1.6; 554 1.8; 593 1.9; 635 1.8; 679 1.6; 726 1.5; 777 1.5; 832 1.2; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.7; 1336 -2.3; 1429 -3.0; 1529 -3.7; 1636 -4.2; 1751 -4.6; 1873 -4.8; 2004 -4.9; 2145 -4.9; 2295 -4.8; 2455 -4.1; 2627 -3.2; 2811 -1.9; 3008 -0.1; 3219 1.6; 3444 2.9; 3685 3.1; 3943 2.8; 4219 1.5; 4514 0.9; 4830 1.5; 5168 3.1; 5530 4.6; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.38 | 6.3 dB  |
| Peaking | 838 Hz   | 0.64 | 3.8 dB  |
| Peaking | 2205 Hz  | 0.58 | -7.9 dB |
| Peaking | 3498 Hz  | 2.08 | 8.0 dB  |
| Peaking | 6002 Hz  | 3.03 | 7.5 dB  |
| Peaking | 40 Hz    | 1.45 | -0.4 dB |
| Peaking | 54 Hz    | 2.32 | 0.5 dB  |
| Peaking | 12624 Hz | 2.65 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4SR/Etymotic%20ER4SR.png)