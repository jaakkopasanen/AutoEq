# Teknmotion London Underground

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.7; 40 5.2; 42 4.8; 45 4.3; 49 3.7; 52 3.2; 56 2.7; 59 2.4; 64 2.0; 68 1.7; 73 1.4; 78 1.2; 83 1.1; 89 1.1; 95 0.9; 102 0.8; 109 0.8; 117 0.9; 125 1.0; 134 1.1; 143 1.2; 153 1.4; 164 1.6; 175 1.9; 188 2.2; 201 2.5; 215 2.8; 230 3.2; 246 3.5; 263 3.7; 282 4.1; 301 4.5; 323 5.0; 345 5.5; 369 5.9; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 5.9; 554 5.4; 593 4.8; 635 3.6; 679 2.5; 726 1.5; 777 1.1; 832 0.6; 890 0.4; 952 0.3; 1019 0.0; 1090 0.1; 1167 0.8; 1248 0.7; 1336 -0.3; 1429 -0.5; 1529 -0.1; 1636 0.7; 1751 1.7; 1873 3.1; 2004 4.7; 2145 5.6; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teknmotion London Underground ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | 6.5 dB  |
| Peaking | 335 Hz  | 1.28 | 4.8 dB  |
| Peaking | 513 Hz  | 2.76 | 4.1 dB  |
| Peaking | 2621 Hz | 1.86 | 5.6 dB  |
| Peaking | 4936 Hz | 1.57 | 6.0 dB  |
| Peaking | 949 Hz  | 3.91 | -0.9 dB |
| Peaking | 1477 Hz | 4.19 | -2.0 dB |
| Peaking | 2071 Hz | 6.46 | 1.9 dB  |
| Peaking | 6414 Hz | 4.5  | 3.6 dB  |
| Peaking | 7479 Hz | 1.76 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teknmotion%20London%20Underground/Teknmotion%20London%20Underground.png)