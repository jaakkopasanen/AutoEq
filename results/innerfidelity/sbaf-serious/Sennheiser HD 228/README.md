# Sennheiser HD 228

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.2; 22 4.5; 23 4.2; 25 3.5; 26 3.2; 28 2.6; 30 2.0; 32 1.5; 35 0.9; 37 0.6; 40 0.1; 42 -0.2; 45 -0.6; 49 -1.1; 52 -1.5; 56 -1.9; 59 -2.3; 64 -2.8; 68 -3.1; 73 -3.6; 78 -4.0; 83 -4.3; 89 -4.6; 95 -5.0; 102 -5.1; 109 -5.0; 117 -4.7; 125 -4.7; 134 -5.3; 143 -6.2; 153 -6.8; 164 -6.6; 175 -6.8; 188 -6.9; 201 -6.6; 215 -6.3; 230 -6.0; 246 -6.2; 263 -5.5; 282 -4.1; 301 -3.3; 323 -3.5; 345 -3.3; 369 -2.7; 395 -2.0; 423 -1.3; 452 -1.1; 484 -0.7; 518 -0.2; 554 0.3; 593 0.7; 635 0.8; 679 0.7; 726 0.7; 777 0.7; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.5; 1248 0.9; 1336 1.2; 1429 1.7; 1529 1.3; 1636 0.0; 1751 0.6; 1873 1.1; 2004 1.4; 2145 1.8; 2295 2.6; 2455 3.3; 2627 3.7; 2811 4.1; 3008 5.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 3.1; 4830 -1.6; 5168 -2.8; 5530 -0.6; 5917 1.9; 6331 2.2; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -2.9; 18692 -4.3; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999996093441dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.02 | 5.5 dB  |
| Peaking | 91 Hz    | 0.84 | -3.8 dB |
| Peaking | 203 Hz   | 1.22 | -5.9 dB |
| Peaking | 3344 Hz  | 1.81 | 6.6 dB  |
| Peaking | 18598 Hz | 2.57 | -4.9 dB |
| Peaking | 656 Hz   | 2.59 | 1.4 dB  |
| Peaking | 4283 Hz  | 6.64 | 4.0 dB  |
| Peaking | 5028 Hz  | 4.91 | -6.2 dB |
| Peaking | 6686 Hz  | 3.18 | 3.7 dB  |
| Peaking | 7688 Hz  | 3.2  | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)