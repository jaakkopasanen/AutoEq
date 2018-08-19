# Fostex TH610

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 -1.9; 22 -2.1; 23 -2.2; 25 -2.3; 26 -2.4; 28 -2.5; 30 -2.5; 32 -2.6; 35 -2.7; 37 -2.7; 40 -2.7; 42 -2.8; 45 -2.9; 49 -3.0; 52 -3.0; 56 -3.1; 59 -3.2; 64 -3.2; 68 -3.3; 73 -3.3; 78 -3.4; 83 -3.6; 89 -3.9; 95 -4.2; 102 -4.5; 109 -4.6; 117 -4.7; 125 -4.9; 134 -5.1; 143 -5.2; 153 -5.3; 164 -4.8; 175 -4.9; 188 -5.0; 201 -4.9; 215 -4.7; 230 -4.5; 246 -4.4; 263 -4.2; 282 -3.8; 301 -3.5; 323 -3.1; 345 -2.7; 369 -2.3; 395 -1.9; 423 -1.3; 452 -0.9; 484 -0.8; 518 -0.6; 554 -0.2; 593 0.2; 635 0.2; 679 0.2; 726 0.2; 777 0.4; 832 0.4; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 0.0; 1248 -0.0; 1336 -0.2; 1429 -0.5; 1529 -0.8; 1636 -0.8; 1751 -0.6; 1873 -0.1; 2004 0.6; 2145 2.2; 2295 3.7; 2455 4.5; 2627 3.0; 2811 1.4; 3008 0.7; 3219 0.6; 3444 0.7; 3685 0.4; 3943 0.2; 4219 -0.4; 4514 -0.2; 4830 1.1; 5168 2.8; 5530 3.0; 5917 1.8; 6331 0.9; 6775 0.7; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -3.0; 10167 -3.1; 10879 -1.2; 11640 -0.0; 12455 0.0; 13327 -0.1; 14260 -0.6; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -5.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.641943052032007dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH610 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.32 | -2.6 dB |
| Peaking | 182 Hz   | 0.82 | -4.1 dB |
| Peaking | 2432 Hz  | 4.6  | 5.1 dB  |
| Peaking | 5734 Hz  | 1.88 | 4.4 dB  |
| Peaking | 6894 Hz  | 0.58 | -2.1 dB |
| Peaking | 714 Hz   | 1.83 | 1.0 dB  |
| Peaking | 1635 Hz  | 4.51 | -1.1 dB |
| Peaking | 8549 Hz  | 3.7  | 2.3 dB  |
| Peaking | 9828 Hz  | 3.43 | -4.1 dB |
| Peaking | 11566 Hz | 2.59 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH610/Fostex%20TH610.png)