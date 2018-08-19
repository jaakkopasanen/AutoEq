# Klipsch Image S2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -6.4; 22 -6.5; 23 -6.6; 25 -6.7; 26 -6.7; 28 -6.8; 30 -6.9; 32 -7.0; 35 -7.0; 37 -7.0; 40 -7.0; 42 -7.0; 45 -7.1; 49 -7.1; 52 -7.1; 56 -7.1; 59 -7.2; 64 -7.2; 68 -7.2; 73 -7.2; 78 -7.2; 83 -7.2; 89 -7.1; 95 -7.1; 102 -6.9; 109 -6.8; 117 -6.6; 125 -6.5; 134 -6.3; 143 -6.2; 153 -6.0; 164 -5.8; 175 -5.5; 188 -5.2; 201 -4.9; 215 -4.5; 230 -4.2; 246 -3.8; 263 -3.5; 282 -3.1; 301 -2.7; 323 -2.3; 345 -1.8; 369 -1.4; 395 -1.0; 423 -0.7; 452 -0.3; 484 -0.0; 518 0.3; 554 0.6; 593 0.8; 635 1.1; 679 1.3; 726 1.4; 777 1.3; 832 1.2; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.8; 1167 -1.5; 1248 -2.3; 1336 -3.0; 1429 -3.0; 1529 -2.7; 1636 -2.8; 1751 -3.4; 1873 -4.1; 2004 -4.8; 2145 -5.7; 2295 -6.2; 2455 -6.3; 2627 -5.3; 2811 -3.3; 3008 -0.6; 3219 1.9; 3444 3.7; 3685 4.3; 3943 3.5; 4219 1.7; 4514 -0.3; 4830 -2.1; 5168 -4.5; 5530 -7.7; 5917 -5.0; 6331 0.3; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.3; 14260 -2.4; 15258 -2.2; 16326 -0.1; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.445995223321511dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.34 | -7.1 dB |
| Peaking | 151 Hz   | 0.94 | -3.4 dB |
| Peaking | 2406 Hz  | 1.68 | -8.0 dB |
| Peaking | 3545 Hz  | 2.42 | 7.3 dB  |
| Peaking | 5513 Hz  | 6.85 | -8.7 dB |
| Peaking | 735 Hz   | 1.7  | 2.3 dB  |
| Peaking | 1336 Hz  | 4.1  | -2.0 dB |
| Peaking | 6062 Hz  | 2.79 | -2.2 dB |
| Peaking | 6715 Hz  | 5.53 | 5.5 dB  |
| Peaking | 14760 Hz | 5.29 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S2/Klipsch%20Image%20S2.png)