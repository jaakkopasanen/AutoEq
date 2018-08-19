# Etymotic ER4PT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.7; 59 5.5; 64 5.2; 68 4.9; 73 4.6; 78 4.3; 83 4.0; 89 3.6; 95 3.3; 102 3.0; 109 2.9; 117 2.7; 125 2.4; 134 2.1; 143 1.9; 153 1.7; 164 1.6; 175 1.5; 188 1.5; 201 1.3; 215 1.3; 230 1.3; 246 1.2; 263 1.1; 282 1.2; 301 1.2; 323 1.2; 345 1.2; 369 1.3; 395 1.3; 423 1.4; 452 1.4; 484 1.3; 518 1.3; 554 1.5; 593 1.7; 635 1.7; 679 1.6; 726 1.5; 777 1.5; 832 1.3; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.7; 1167 -1.1; 1248 -1.7; 1336 -2.3; 1429 -3.0; 1529 -3.6; 1636 -4.1; 1751 -4.4; 1873 -4.4; 2004 -4.4; 2145 -4.4; 2295 -4.1; 2455 -3.2; 2627 -2.4; 2811 -1.3; 3008 0.3; 3219 1.4; 3444 2.3; 3685 2.3; 3943 1.6; 4219 0.2; 4514 -0.3; 4830 0.7; 5168 2.8; 5530 4.6; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.6; 8880 -2.1; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4PT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.38 | 6.3 dB  |
| Peaking | 849 Hz   |  0.67 | 5.1 dB  |
| Peaking | 2209 Hz  |  0.43 | -8.1 dB |
| Peaking | 3410 Hz  |  1.93 | 7.9 dB  |
| Peaking | 5983 Hz  |  2.96 | 8.9 dB  |
| Peaking | 6720 Hz  | 11.36 | 0.9 dB  |
| Peaking | 8603 Hz  |  6.83 | -2.4 dB |
| Peaking | 10625 Hz |  1.89 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4PT/Etymotic%20ER4PT.png)