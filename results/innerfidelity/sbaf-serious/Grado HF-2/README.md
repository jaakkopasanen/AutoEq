# Grado HF-2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.5; 45 4.7; 49 3.5; 52 2.9; 56 2.0; 59 1.4; 64 0.2; 68 -0.5; 73 -1.1; 78 -1.7; 83 -2.2; 89 -2.6; 95 -2.8; 102 -3.0; 109 -2.9; 117 -2.8; 125 -2.8; 134 -2.6; 143 -2.4; 153 -2.3; 164 -2.1; 175 -1.9; 188 -1.7; 201 -1.6; 215 -1.3; 230 -0.9; 246 -0.7; 263 -0.9; 282 -0.7; 301 -0.6; 323 -0.5; 345 -0.3; 369 -0.3; 395 -0.1; 423 0.1; 452 0.2; 484 0.2; 518 0.2; 554 0.3; 593 0.5; 635 0.6; 679 0.6; 726 0.5; 777 0.6; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.5; 1248 -1.0; 1336 -1.7; 1429 -2.6; 1529 -3.7; 1636 -4.4; 1751 -4.6; 1873 -5.8; 2004 -8.2; 2145 -8.4; 2295 -7.3; 2455 -6.0; 2627 -5.4; 2811 -4.0; 3008 -3.5; 3219 -2.8; 3444 -2.0; 3685 -0.9; 3943 1.0; 4219 1.8; 4514 2.4; 4830 0.8; 5168 -2.6; 5530 -2.1; 5917 -0.6; 6331 -1.0; 6775 -2.1; 7249 -2.9; 7756 -3.8; 8299 -6.3; 8880 -8.8; 9502 -7.8; 10167 -2.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.51 | 7.6 dB   |
| Peaking | 91 Hz    | 0.79 | -5.9 dB  |
| Peaking | 2138 Hz  | 2.28 | -8.6 dB  |
| Peaking | 9069 Hz  | 3.32 | -10.7 dB |
| Peaking | 10626 Hz | 2.89 | 3.3 dB   |
| Peaking | 710 Hz   | 0.94 | 1.5 dB   |
| Peaking | 1411 Hz  | 0.17 | -0.6 dB  |
| Peaking | 3268 Hz  | 3.47 | -1.4 dB  |
| Peaking | 4473 Hz  | 2.63 | 4.4 dB   |
| Peaking | 5220 Hz  | 8.13 | -4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-2/Grado%20HF-2.png)