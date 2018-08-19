# Audeo PFE 121 Green Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.7; 22 -1.7; 23 -1.8; 25 -1.8; 26 -1.9; 28 -1.9; 30 -2.0; 32 -2.1; 35 -2.2; 37 -2.3; 40 -2.4; 42 -2.5; 45 -2.6; 49 -2.8; 52 -2.9; 56 -3.1; 59 -3.2; 64 -3.5; 68 -3.6; 73 -3.9; 78 -4.1; 83 -4.3; 89 -4.6; 95 -4.9; 102 -5.1; 109 -5.1; 117 -5.3; 125 -5.5; 134 -5.6; 143 -5.7; 153 -5.8; 164 -5.8; 175 -5.8; 188 -5.8; 201 -5.7; 215 -5.6; 230 -5.4; 246 -5.3; 263 -5.2; 282 -4.9; 301 -4.7; 323 -4.5; 345 -4.2; 369 -4.0; 395 -3.7; 423 -3.3; 452 -2.9; 484 -2.6; 518 -2.2; 554 -1.7; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.4; 777 -0.1; 832 0.1; 890 0.0; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.3; 1336 0.2; 1429 0.2; 1529 0.1; 1636 0.3; 1751 0.7; 1873 1.4; 2004 2.1; 2145 2.8; 2295 3.6; 2455 4.7; 2627 4.8; 2811 4.5; 3008 4.2; 3219 4.6; 3444 5.8; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.2; 8880 -3.9; 9502 -4.8; 10167 -2.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.4; 15258 -1.9; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999993821055dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Green Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 77 Hz    | 0.3  | -2.4 dB |
| Peaking | 203 Hz   | 0.55 | -4.3 dB |
| Peaking | 3521 Hz  | 0.97 | 5.2 dB  |
| Peaking | 5811 Hz  | 2.01 | 4.2 dB  |
| Peaking | 9217 Hz  | 3.57 | -6.4 dB |
| Peaking | 792 Hz   | 3.04 | 0.8 dB  |
| Peaking | 1644 Hz  | 2.78 | -1.2 dB |
| Peaking | 2621 Hz  | 2.2  | 1.8 dB  |
| Peaking | 3055 Hz  | 4.99 | -2.3 dB |
| Peaking | 14963 Hz | 7.63 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Green%20Filter/Audeo%20PFE%20121%20Green%20Filter.png)