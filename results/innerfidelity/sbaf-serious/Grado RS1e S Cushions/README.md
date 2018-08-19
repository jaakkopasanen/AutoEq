# Grado RS1e S Cushions

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 5.0; 37 4.4; 40 3.7; 42 3.3; 45 2.7; 49 1.9; 52 1.4; 56 0.8; 59 0.4; 64 -0.3; 68 -0.7; 73 -1.2; 78 -1.7; 83 -2.1; 89 -2.5; 95 -2.9; 102 -3.2; 109 -3.4; 117 -3.5; 125 -3.7; 134 -3.8; 143 -3.9; 153 -4.0; 164 -4.0; 175 -3.9; 188 -3.8; 201 -3.6; 215 -3.4; 230 -3.1; 246 -3.0; 263 -2.9; 282 -2.9; 301 -2.8; 323 -2.5; 345 -2.3; 369 -2.0; 395 -1.8; 423 -1.4; 452 -1.2; 484 -1.1; 518 -1.0; 554 -0.7; 593 -0.4; 635 -0.2; 679 -0.2; 726 -0.1; 777 0.1; 832 0.1; 890 0.0; 952 0.1; 1019 0.1; 1090 0.2; 1167 0.1; 1248 0.3; 1336 0.3; 1429 0.7; 1529 1.1; 1636 0.6; 1751 -4.4; 1873 -6.9; 2004 -6.4; 2145 -4.5; 2295 -2.5; 2455 -0.0; 2627 2.1; 2811 3.8; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e S Cushions ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.55 | 7.9 dB   |
| Peaking | 131 Hz   | 0.32 | -5.5 dB  |
| Peaking | 690 Hz   | 0.21 | 1.3 dB   |
| Peaking | 1987 Hz  | 3.64 | -10.1 dB |
| Peaking | 4051 Hz  | 1    | 6.6 dB   |
| Peaking | 1613 Hz  | 7.39 | 3.7 dB   |
| Peaking | 1779 Hz  | 4.63 | -2.1 dB  |
| Peaking | 6218 Hz  | 3.22 | 5.0 dB   |
| Peaking | 7319 Hz  | 1.4  | -3.2 dB  |
| Peaking | 24000 Hz | 1.42 | 0.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20S%20Cushions/Grado%20RS1e%20S%20Cushions.png)