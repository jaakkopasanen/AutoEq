# Grado SR125i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.6; 35 4.8; 37 4.2; 40 3.5; 42 3.0; 45 2.4; 49 1.6; 52 1.1; 56 0.6; 59 0.2; 64 -0.3; 68 -0.7; 73 -1.1; 78 -1.4; 83 -1.7; 89 -2.0; 95 -2.2; 102 -2.3; 109 -2.3; 117 -2.3; 125 -2.5; 134 -2.4; 143 -2.4; 153 -2.3; 164 -2.2; 175 -2.0; 188 -1.9; 201 -1.7; 215 -1.4; 230 -1.2; 246 -1.0; 263 -0.8; 282 -0.4; 301 -0.1; 323 -0.5; 345 -0.7; 369 -0.7; 395 -0.8; 423 -0.5; 452 -0.4; 484 -0.3; 518 -0.3; 554 -0.1; 593 0.3; 635 0.3; 679 0.2; 726 0.2; 777 0.4; 832 0.3; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.0; 1167 -0.1; 1248 -0.5; 1336 -1.1; 1429 -1.9; 1529 -2.9; 1636 -3.4; 1751 -4.0; 1873 -6.8; 2004 -9.9; 2145 -9.8; 2295 -8.0; 2455 -5.9; 2627 -4.5; 2811 -2.7; 3008 -1.8; 3219 -0.4; 3444 -1.1; 3685 -1.8; 3943 -1.6; 4219 -0.2; 4514 0.1; 4830 -0.1; 5168 -0.7; 5530 -0.6; 5917 1.7; 6331 1.5; 6775 -0.9; 7249 -3.0; 7756 -3.7; 8299 -4.1; 8880 -4.3; 9502 -3.0; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.84 | 6.7 dB   |
| Peaking | 108 Hz   | 0.74 | -3.1 dB  |
| Peaking | 2109 Hz  | 3.1  | -10.5 dB |
| Peaking | 8469 Hz  | 3.98 | -4.9 dB  |
| Peaking | 24000 Hz | 2.15 | -2.6 dB  |
| Peaking | 878 Hz   | 0.93 | 1.8 dB   |
| Peaking | 950 Hz   | 0.55 | -1.1 dB  |
| Peaking | 6201 Hz  | 7.28 | 3.1 dB   |
| Peaking | 7261 Hz  | 7.33 | -1.9 dB  |
| Peaking | 10758 Hz | 6.06 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)