# V-Moda XS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.4; 23 -2.6; 25 -3.0; 26 -3.1; 28 -3.4; 30 -3.7; 32 -3.9; 35 -4.1; 37 -4.2; 40 -4.4; 42 -4.5; 45 -4.6; 49 -4.7; 52 -4.8; 56 -4.8; 59 -4.8; 64 -4.9; 68 -5.0; 73 -5.0; 78 -5.0; 83 -5.1; 89 -5.2; 95 -5.2; 102 -5.1; 109 -4.9; 117 -5.0; 125 -5.2; 134 -5.1; 143 -5.1; 153 -5.0; 164 -4.7; 175 -4.4; 188 -4.3; 201 -3.8; 215 -3.3; 230 -3.4; 246 -3.9; 263 -3.3; 282 -2.4; 301 -1.6; 323 -0.8; 345 0.2; 369 0.8; 395 0.9; 423 1.2; 452 1.5; 484 1.7; 518 1.9; 554 2.3; 593 2.6; 635 2.6; 679 2.4; 726 2.2; 777 2.1; 832 1.5; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.6; 1167 -0.9; 1248 -1.1; 1336 -1.2; 1429 -1.1; 1529 -1.0; 1636 -0.9; 1751 -0.6; 1873 -0.4; 2004 -0.6; 2145 -0.6; 2295 -0.4; 2455 -0.6; 2627 -1.2; 2811 -2.1; 3008 -2.4; 3219 -2.2; 3444 -0.9; 3685 0.8; 3943 3.1; 4219 4.0; 4514 2.1; 4830 0.8; 5168 3.1; 5530 3.0; 5917 2.4; 6331 2.8; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.141410632175254dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 190 Hz  | 0.13 | -6.0 dB |
| Peaking | 550 Hz  | 0.74 | 8.0 dB  |
| Peaking | 3115 Hz | 3.98 | -2.5 dB |
| Peaking | 4097 Hz | 5.59 | 4.2 dB  |
| Peaking | 5849 Hz | 2.64 | 3.1 dB  |
| Peaking | 254 Hz  | 7.32 | -1.0 dB |
| Peaking | 356 Hz  | 4.88 | 0.9 dB  |
| Peaking | 514 Hz  | 2.89 | -1.0 dB |
| Peaking | 1060 Hz | 0.86 | 1.5 dB  |
| Peaking | 1188 Hz | 1.77 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)