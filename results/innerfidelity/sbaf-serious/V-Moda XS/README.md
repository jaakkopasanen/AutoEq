# V-Moda XS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.4; 23 -2.6; 25 -2.9; 26 -3.1; 28 -3.4; 30 -3.6; 32 -3.8; 35 -4.0; 37 -4.1; 40 -4.3; 42 -4.3; 45 -4.4; 49 -4.5; 52 -4.5; 56 -4.5; 59 -4.4; 64 -4.4; 68 -4.4; 73 -4.3; 78 -4.2; 83 -4.3; 89 -4.4; 95 -4.5; 102 -4.5; 109 -4.5; 117 -4.8; 125 -5.1; 134 -5.2; 143 -5.3; 153 -5.2; 164 -4.9; 175 -4.6; 188 -4.5; 201 -4.0; 215 -3.5; 230 -3.5; 246 -4.0; 263 -3.4; 282 -2.5; 301 -1.6; 323 -0.8; 345 0.1; 369 0.8; 395 0.9; 423 1.2; 452 1.5; 484 1.7; 518 1.9; 554 2.3; 593 2.6; 635 2.6; 679 2.4; 726 2.2; 777 2.1; 832 1.5; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.6; 1167 -0.9; 1248 -1.1; 1336 -1.2; 1429 -1.1; 1529 -1.0; 1636 -0.9; 1751 -0.6; 1873 -0.4; 2004 -0.6; 2145 -0.6; 2295 -0.4; 2455 -0.6; 2627 -1.2; 2811 -2.1; 3008 -2.4; 3219 -2.2; 3444 -0.9; 3685 0.8; 3943 3.1; 4219 4.0; 4514 2.1; 4830 0.8; 5168 3.1; 5530 3.0; 5917 2.4; 6331 2.8; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.63 | -3.7 dB |
| Peaking | 160 Hz   | 0.68 | -4.6 dB |
| Peaking | 529 Hz   | 1.41 | 3.6 dB  |
| Peaking | 5537 Hz  | 2.38 | 3.2 dB  |
| Peaking | 24000 Hz | 2.27 | 1.1 dB  |
| Peaking | 4741 Hz  | 8.8  | -2.7 dB |
| Peaking | 779 Hz   | 3.44 | 1.3 dB  |
| Peaking | 1293 Hz  | 1.77 | -1.5 dB |
| Peaking | 3120 Hz  | 3.03 | -3.3 dB |
| Peaking | 4152 Hz  | 4.15 | 4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)