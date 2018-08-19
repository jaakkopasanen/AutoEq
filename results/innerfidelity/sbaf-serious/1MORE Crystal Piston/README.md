# 1MORE Crystal Piston

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -6.1; 22 -6.6; 23 -6.8; 25 -7.2; 26 -7.3; 28 -7.6; 30 -7.8; 32 -7.9; 35 -8.3; 37 -8.5; 40 -8.6; 42 -8.7; 45 -8.8; 49 -9.0; 52 -9.1; 56 -9.3; 59 -9.4; 64 -9.5; 68 -9.6; 73 -9.8; 78 -9.9; 83 -9.9; 89 -10.1; 95 -10.1; 102 -10.2; 109 -10.1; 117 -9.9; 125 -9.9; 134 -9.8; 143 -9.7; 153 -9.6; 164 -9.4; 175 -9.1; 188 -8.9; 201 -8.5; 215 -8.2; 230 -7.8; 246 -7.5; 263 -7.1; 282 -6.6; 301 -6.2; 323 -5.8; 345 -5.3; 369 -4.8; 395 -4.4; 423 -3.8; 452 -3.3; 484 -3.0; 518 -2.5; 554 -2.0; 593 -1.3; 635 -0.9; 679 -0.6; 726 -0.2; 777 0.2; 832 0.3; 890 0.2; 952 0.3; 1019 0.1; 1090 0.1; 1167 0.2; 1248 0.5; 1336 0.4; 1429 0.1; 1529 -0.3; 1636 -1.0; 1751 -2.0; 1873 -2.7; 2004 -2.8; 2145 -2.6; 2295 -2.3; 2455 -1.8; 2627 -1.6; 2811 -1.6; 3008 -1.2; 3219 -1.0; 3444 -0.8; 3685 -1.4; 3943 -2.2; 4219 -3.9; 4514 -5.6; 4830 -6.7; 5168 -7.3; 5530 -8.0; 5917 -7.5; 6331 -6.0; 6775 -4.5; 7249 -3.7; 7756 -4.0; 8299 -4.9; 8880 -5.3; 9502 -3.9; 10167 -0.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.623903954884589dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Crystal Piston ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.33 | -7.9 dB |
| Peaking | 143 Hz   | 0.72 | -5.2 dB |
| Peaking | 291 Hz   | 1.27 | -2.8 dB |
| Peaking | 5460 Hz  | 1.89 | -8.0 dB |
| Peaking | 8785 Hz  | 5.26 | -4.3 dB |
| Peaking | 467 Hz   | 2.27 | -1.0 dB |
| Peaking | 1048 Hz  | 0.71 | 1.4 dB  |
| Peaking | 2001 Hz  | 2.33 | -3.1 dB |
| Peaking | 3542 Hz  | 5.9  | 1.3 dB  |
| Peaking | 11085 Hz | 4.93 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Crystal%20Piston/1MORE%20Crystal%20Piston.png)