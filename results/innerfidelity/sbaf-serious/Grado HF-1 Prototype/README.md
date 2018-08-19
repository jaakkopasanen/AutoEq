# Grado HF-1 Prototype

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.8; 45 5.2; 49 4.1; 52 3.3; 56 2.3; 59 1.8; 64 1.2; 68 0.6; 73 -0.3; 78 -1.0; 83 -1.5; 89 -1.9; 95 -2.2; 102 -2.4; 109 -2.4; 117 -2.4; 125 -2.3; 134 -2.2; 143 -2.1; 153 -1.8; 164 -1.6; 175 -1.3; 188 -1.0; 201 -1.0; 215 -0.9; 230 -0.7; 246 -0.5; 263 -0.3; 282 -0.0; 301 0.4; 323 0.2; 345 0.3; 369 0.5; 395 0.5; 423 0.4; 452 0.4; 484 0.4; 518 0.5; 554 0.6; 593 0.7; 635 0.8; 679 0.6; 726 0.6; 777 0.7; 832 0.5; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.9; 1336 -1.6; 1429 -2.4; 1529 -3.3; 1636 -3.8; 1751 -4.2; 1873 -4.7; 2004 -5.2; 2145 -5.5; 2295 -4.8; 2455 -3.9; 2627 -3.3; 2811 -2.9; 3008 -1.9; 3219 -1.1; 3444 -0.8; 3685 -1.3; 3943 -1.4; 4219 -4.8; 4514 -8.1; 4830 -8.6; 5168 -5.7; 5530 -3.4; 5917 -3.3; 6331 -3.9; 6775 -5.5; 7249 -6.9; 7756 -7.4; 8299 -9.2; 8880 -11.2; 9502 -10.6; 10167 -6.6; 10879 -1.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.1; 18692 -1.9; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Prototype ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.19 | 11.2 dB  |
| Peaking | 106 Hz   | 0.49 | -13.0 dB |
| Peaking | 2012 Hz  | 1.92 | -5.5 dB  |
| Peaking | 4709 Hz  | 5.38 | -8.3 dB  |
| Peaking | 8760 Hz  | 2.64 | -11.5 dB |
| Peaking | 3622 Hz  | 6.11 | 1.3 dB   |
| Peaking | 9819 Hz  | 6.46 | -3.4 dB  |
| Peaking | 11441 Hz | 2.84 | 3.1 dB   |
| Peaking | 18465 Hz | 4.07 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Prototype/Grado%20HF-1%20Prototype.png)