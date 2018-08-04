# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.5; 35 4.8; 37 4.3; 40 3.5; 42 2.9; 45 2.0; 49 0.8; 52 -0.1; 56 -1.0; 59 -1.7; 64 -2.7; 68 -3.4; 73 -4.1; 78 -4.8; 83 -5.4; 89 -6.0; 95 -6.5; 102 -6.9; 109 -7.0; 117 -7.0; 125 -6.9; 134 -6.6; 143 -6.4; 153 -6.0; 164 -5.6; 175 -5.0; 188 -4.5; 201 -4.2; 215 -3.7; 230 -3.1; 246 -2.8; 263 -2.3; 282 -2.0; 301 -2.0; 323 -2.0; 345 -1.9; 369 -1.6; 395 -1.4; 423 -1.0; 452 -0.8; 484 -0.8; 518 -0.7; 554 -0.5; 593 -0.3; 635 -0.2; 679 -0.2; 726 -0.2; 777 0.1; 832 0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -0.6; 1336 -1.1; 1429 -1.4; 1529 -1.7; 1636 -0.8; 1751 -1.7; 1873 -1.7; 2004 -1.6; 2145 -1.4; 2295 -1.3; 2455 -1.2; 2627 -1.4; 2811 -1.4; 3008 -1.1; 3219 -0.8; 3444 -2.0; 3685 -2.7; 3943 -5.0; 4219 -9.3; 4514 -9.5; 4830 -6.5; 5168 -7.7; 5530 -9.7; 5917 -11.0; 6331 -11.4; 6775 -9.9; 7249 -7.8; 7756 -5.8; 8299 -6.0; 8880 -8.6; 9502 -10.8; 10167 -10.0; 10879 -6.8; 11640 -3.6; 12455 -2.2; 13327 -1.9; 14260 -0.9; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.7  | 7.5 dB   |
| Peaking | 107 Hz   | 0.66 | -8.1 dB  |
| Peaking | 264 Hz   | 2.45 | 0.3 dB   |
| Peaking | 5836 Hz  | 1.37 | -10.5 dB |
| Peaking | 9873 Hz  | 3.77 | -8.7 dB  |
| Peaking | 2142 Hz  | 0.37 | -2.2 dB  |
| Peaking | 3819 Hz  | 1.15 | 4.4 dB   |
| Peaking | 4256 Hz  | 7.13 | -7.0 dB  |
| Peaking | 889 Hz   | 0.96 | 1.8 dB   |
| Peaking | 23996 Hz | 3.99 | -0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)