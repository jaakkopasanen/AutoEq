# SMS Over Ear ANC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.2; 23 4.5; 25 2.6; 26 1.5; 28 -0.7; 30 -2.4; 32 -3.4; 35 -4.1; 37 -4.2; 40 -4.0; 42 -3.7; 45 -3.3; 49 -2.8; 52 -2.4; 56 -2.1; 59 -1.9; 64 -1.6; 68 -1.3; 73 -1.1; 78 -0.9; 83 -0.7; 89 -0.6; 95 -0.5; 102 -0.2; 109 0.1; 117 0.3; 125 0.6; 134 0.7; 143 0.9; 153 1.1; 164 1.3; 175 1.6; 188 1.9; 201 2.2; 215 2.5; 230 2.7; 246 2.8; 263 3.0; 282 3.3; 301 3.6; 323 3.7; 345 3.9; 369 4.1; 395 4.2; 423 4.5; 452 4.9; 484 5.4; 518 5.6; 554 5.8; 593 6.0; 635 5.8; 679 5.4; 726 4.8; 777 4.3; 832 3.2; 890 2.0; 952 0.9; 1019 -0.4; 1090 -1.3; 1167 -2.3; 1248 -4.0; 1336 -6.3; 1429 -8.7; 1529 -10.6; 1636 -11.9; 1751 -11.5; 1873 -9.2; 2004 -7.0; 2145 -6.2; 2295 -5.3; 2455 -3.7; 2627 -2.9; 2811 -1.5; 3008 0.4; 3219 0.8; 3444 1.1; 3685 1.6; 3943 2.6; 4219 4.5; 4514 5.9; 4830 6.0; 5168 6.0; 5530 2.1; 5917 2.2; 6331 3.6; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Over Ear ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.44 | 9.6 dB   |
| Peaking | 33 Hz   | 1.01 | -7.4 dB  |
| Peaking | 628 Hz  | 0.55 | 7.0 dB   |
| Peaking | 1630 Hz | 1.54 | -15.0 dB |
| Peaking | 4665 Hz | 1.86 | 6.7 dB   |
| Peaking | 687 Hz  | 3.36 | 0.5 dB   |
| Peaking | 1029 Hz | 3.5  | -1.1 dB  |
| Peaking | 1155 Hz | 4.12 | 0.9 dB   |
| Peaking | 6588 Hz | 6.19 | 4.2 dB   |
| Peaking | 6938 Hz | 2.24 | -2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20Over%20Ear%20ANC/SMS%20Over%20Ear%20ANC.png)