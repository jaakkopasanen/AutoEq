# Noontec Zoro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.2; 22 -0.2; 23 -0.4; 25 -0.7; 26 -0.8; 28 -1.0; 30 -1.2; 32 -1.4; 35 -1.6; 37 -1.7; 40 -1.9; 42 -2.0; 45 -2.1; 49 -2.2; 52 -2.3; 56 -2.4; 59 -2.5; 64 -2.7; 68 -3.0; 73 -3.2; 78 -3.4; 83 -3.6; 89 -3.7; 95 -3.9; 102 -4.2; 109 -4.2; 117 -4.4; 125 -4.5; 134 -4.6; 143 -4.6; 153 -4.7; 164 -4.8; 175 -4.6; 188 -4.7; 201 -4.8; 215 -4.7; 230 -4.7; 246 -4.6; 263 -4.4; 282 -4.0; 301 -3.9; 323 -3.9; 345 -3.8; 369 -3.8; 395 -3.6; 423 -3.3; 452 -3.3; 484 -3.3; 518 -3.1; 554 -2.8; 593 -2.4; 635 -2.1; 679 -1.9; 726 -1.4; 777 -0.9; 832 -0.5; 890 -0.2; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.1; 1336 -0.6; 1429 -1.3; 1529 -1.8; 1636 -1.7; 1751 -1.2; 1873 -0.4; 2004 1.0; 2145 2.3; 2295 3.7; 2455 5.5; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.2; 6331 4.3; 6775 3.5; 7249 0.9; 7756 -1.6; 8299 -2.5; 8880 -1.4; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999993319dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 91 Hz    | 0.45 | -1.8 dB |
| Peaking | 270 Hz   | 0.36 | -3.8 dB |
| Peaking | 1685 Hz  | 2.05 | -5.9 dB |
| Peaking | 3377 Hz  | 0.48 | 7.5 dB  |
| Peaking | 8291 Hz  | 2.95 | -5.9 dB |
| Peaking | 2192 Hz  | 4.91 | -1.3 dB |
| Peaking | 2473 Hz  | 3.44 | 1.7 dB  |
| Peaking | 3640 Hz  | 1.74 | -1.0 dB |
| Peaking | 5782 Hz  | 2.58 | 1.4 dB  |
| Peaking | 12758 Hz | 1.38 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)