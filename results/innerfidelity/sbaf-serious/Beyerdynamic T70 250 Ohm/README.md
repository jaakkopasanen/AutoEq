# Beyerdynamic T70 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.0; 22 4.8; 23 4.7; 25 4.5; 26 4.4; 28 4.2; 30 4.0; 32 3.9; 35 3.7; 37 3.6; 40 3.5; 42 3.4; 45 3.3; 49 3.2; 52 3.1; 56 3.0; 59 3.0; 64 2.9; 68 2.8; 73 2.6; 78 2.2; 83 1.9; 89 1.5; 95 1.1; 102 0.7; 109 0.5; 117 0.2; 125 -0.3; 134 -0.8; 143 -1.0; 153 -1.0; 164 -0.3; 175 -0.5; 188 -0.8; 201 -0.7; 215 -0.6; 230 -0.3; 246 -0.2; 263 -0.2; 282 -0.2; 301 -0.3; 323 -0.5; 345 -0.6; 369 -0.9; 395 -1.0; 423 -1.0; 452 -0.8; 484 -0.5; 518 0.1; 554 0.3; 593 0.3; 635 0.2; 679 0.1; 726 0.0; 777 0.1; 832 0.1; 890 -0.0; 952 0.0; 1019 0.0; 1090 0.0; 1167 0.0; 1248 0.0; 1336 -0.1; 1429 -0.3; 1529 -0.5; 1636 -0.5; 1751 -0.2; 1873 0.3; 2004 1.0; 2145 2.4; 2295 3.8; 2455 4.2; 2627 3.9; 2811 3.3; 3008 3.2; 3219 3.0; 3444 2.9; 3685 3.7; 3943 6.0; 4219 5.6; 4514 3.1; 4830 3.7; 5168 5.6; 5530 6.0; 5917 5.9; 6331 4.8; 6775 1.7; 7249 -2.7; 7756 -5.8; 8299 -8.0; 8880 -8.8; 9502 -7.9; 10167 -5.1; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999254591366dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.61 | 4.6 dB   |
| Peaking | 2520 Hz  | 3.56 | 4.2 dB   |
| Peaking | 3977 Hz  | 4.25 | 4.8 dB   |
| Peaking | 5870 Hz  | 2.78 | 7.8 dB   |
| Peaking | 8654 Hz  | 2.72 | -10.8 dB |
| Peaking | 70 Hz    | 1.37 | 2.0 dB   |
| Peaking | 106 Hz   | 0.32 | -1.0 dB  |
| Peaking | 141 Hz   | 4.22 | -0.9 dB  |
| Peaking | 1621 Hz  | 4.84 | -1.1 dB  |
| Peaking | 11618 Hz | 5.94 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)