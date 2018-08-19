# JAYS j-Jays

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.6; 22 -4.7; 23 -4.8; 25 -4.8; 26 -4.9; 28 -4.9; 30 -4.9; 32 -4.9; 35 -5.0; 37 -5.0; 40 -5.1; 42 -5.2; 45 -5.2; 49 -5.2; 52 -5.3; 56 -5.5; 59 -5.7; 64 -5.9; 68 -6.0; 73 -6.1; 78 -6.3; 83 -6.5; 89 -6.6; 95 -6.7; 102 -6.7; 109 -6.8; 117 -6.8; 125 -6.9; 134 -7.0; 143 -7.1; 153 -7.0; 164 -6.9; 175 -6.8; 188 -6.6; 201 -6.3; 215 -6.0; 230 -5.6; 246 -5.3; 263 -5.5; 282 -5.4; 301 -5.0; 323 -4.4; 345 -3.8; 369 -3.3; 395 -2.8; 423 -2.4; 452 -2.1; 484 -1.7; 518 -1.2; 554 -0.8; 593 -0.4; 635 -0.0; 679 0.2; 726 0.5; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.8; 1248 -1.0; 1336 -1.3; 1429 -2.2; 1529 -3.5; 1636 -4.1; 1751 -4.1; 1873 -3.7; 2004 -2.9; 2145 -2.0; 2295 -0.6; 2455 1.0; 2627 2.6; 2811 4.4; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.5; 4219 2.4; 4514 -1.5; 4830 -4.2; 5168 -1.1; 5530 4.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999028094dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS j-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.23 | -4.6 dB |
| Peaking | 152 Hz   | 0.72 | -4.3 dB |
| Peaking | 292 Hz   | 1.93 | -2.0 dB |
| Peaking | 3379 Hz  | 3.41 | 7.2 dB  |
| Peaking | 22543 Hz | 2.33 | 3.6 dB  |
| Peaking | 799 Hz   | 1.92 | 1.5 dB  |
| Peaking | 1759 Hz  | 2.21 | -4.8 dB |
| Peaking | 2804 Hz  | 5.1  | 2.7 dB  |
| Peaking | 4879 Hz  | 7.71 | -7.3 dB |
| Peaking | 6015 Hz  | 3.92 | 6.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20j-Jays/JAYS%20j-Jays.png)