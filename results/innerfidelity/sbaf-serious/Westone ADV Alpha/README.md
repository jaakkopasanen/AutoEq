# Westone ADV Alpha

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.2; 22 -7.2; 23 -7.3; 25 -7.3; 26 -7.3; 28 -7.3; 30 -7.4; 32 -7.4; 35 -7.5; 37 -7.5; 40 -7.6; 42 -7.6; 45 -7.6; 49 -7.7; 52 -7.9; 56 -8.0; 59 -8.0; 64 -8.2; 68 -8.3; 73 -8.5; 78 -8.7; 83 -8.8; 89 -9.0; 95 -9.1; 102 -9.2; 109 -9.2; 117 -9.2; 125 -9.2; 134 -9.2; 143 -9.1; 153 -9.1; 164 -9.0; 175 -8.7; 188 -8.5; 201 -8.4; 215 -8.0; 230 -7.7; 246 -7.4; 263 -7.1; 282 -6.6; 301 -6.2; 323 -5.8; 345 -5.4; 369 -4.9; 395 -4.5; 423 -3.9; 452 -3.4; 484 -3.1; 518 -2.7; 554 -2.1; 593 -1.4; 635 -1.1; 679 -0.9; 726 -0.5; 777 -0.1; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.3; 1429 -0.5; 1529 -0.6; 1636 -0.1; 1751 0.3; 1873 0.8; 2004 1.4; 2145 1.9; 2295 2.6; 2455 3.6; 2627 4.5; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.5; 3943 3.4; 4219 -0.0; 4514 -3.0; 4830 -3.8; 5168 -1.5; 5530 1.4; 5917 3.9; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999437614dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone ADV Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.22 | -6.8 dB |
| Peaking | 137 Hz   | 0.68 | -5.3 dB |
| Peaking | 285 Hz   | 1.06 | -3.2 dB |
| Peaking | 3059 Hz  | 2.43 | 6.8 dB  |
| Peaking | 22791 Hz | 2.3  | 2.6 dB  |
| Peaking | 843 Hz   | 3.02 | 0.9 dB  |
| Peaking | 1495 Hz  | 5.6  | -0.9 dB |
| Peaking | 3736 Hz  | 6.22 | 3.2 dB  |
| Peaking | 4682 Hz  | 4.2  | -6.2 dB |
| Peaking | 6227 Hz  | 4.73 | 6.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20ADV%20Alpha/Westone%20ADV%20Alpha.png)