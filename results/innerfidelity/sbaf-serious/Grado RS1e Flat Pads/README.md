# Grado RS1e Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 4.7; 68 3.5; 73 2.2; 78 1.1; 83 0.1; 89 -0.7; 95 -1.3; 102 -1.7; 109 -1.7; 117 -1.7; 125 -1.7; 134 -1.6; 143 -1.5; 153 -1.3; 164 -1.2; 175 -0.9; 188 -0.7; 201 -0.6; 215 -0.2; 230 0.1; 246 0.1; 263 0.3; 282 0.1; 301 0.0; 323 0.3; 345 0.6; 369 0.6; 395 0.7; 423 0.9; 452 1.0; 484 1.0; 518 1.0; 554 1.2; 593 1.3; 635 1.3; 679 1.1; 726 1.1; 777 1.1; 832 0.8; 890 0.6; 952 0.3; 1019 0.1; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -0.4; 1529 0.9; 1636 1.4; 1751 -3.3; 1873 -6.5; 2004 -5.9; 2145 -3.6; 2295 -1.0; 2455 1.8; 2627 4.0; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.41 | 8.7 dB  |
| Peaking | 104 Hz  | 0.88 | -7.7 dB |
| Peaking | 567 Hz  | 1.79 | 1.1 dB  |
| Peaking | 1983 Hz | 4.26 | -9.7 dB |
| Peaking | 3835 Hz | 0.91 | 7.2 dB  |
| Peaking | 1238 Hz | 5.76 | -1.1 dB |
| Peaking | 2848 Hz | 6.51 | 1.7 dB  |
| Peaking | 3912 Hz | 3.3  | -1.1 dB |
| Peaking | 6274 Hz | 2.51 | 5.1 dB  |
| Peaking | 7397 Hz | 1.53 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Flat%20Pads/Grado%20RS1e%20Flat%20Pads.png)