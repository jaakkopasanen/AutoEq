# Bowers & Wilkins P7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 0.9; 22 0.5; 23 0.3; 25 0.0; 26 -0.1; 28 -0.4; 30 -0.6; 32 -0.9; 35 -1.1; 37 -1.2; 40 -1.2; 42 -1.3; 45 -1.4; 49 -1.6; 52 -1.6; 56 -1.3; 59 -1.4; 64 -2.0; 68 -2.2; 73 -2.5; 78 -2.5; 83 -2.4; 89 -2.4; 95 -2.2; 102 -1.3; 109 -0.9; 117 -0.6; 125 -1.1; 134 -1.5; 143 -2.1; 153 -2.2; 164 -1.0; 175 -1.1; 188 -1.4; 201 -0.9; 215 -0.6; 230 -0.1; 246 0.4; 263 0.9; 282 1.4; 301 1.7; 323 1.8; 345 2.0; 369 2.1; 395 2.0; 423 2.1; 452 2.2; 484 2.1; 518 2.0; 554 2.1; 593 2.2; 635 2.1; 679 1.6; 726 1.2; 777 0.7; 832 0.1; 890 0.0; 952 0.2; 1019 -0.0; 1090 -0.4; 1167 -0.9; 1248 -1.4; 1336 -2.2; 1429 -3.0; 1529 -3.7; 1636 -4.2; 1751 -4.3; 1873 -4.3; 2004 -4.0; 2145 -3.5; 2295 -2.9; 2455 -1.3; 2627 1.1; 2811 3.0; 3008 4.1; 3219 4.0; 3444 2.8; 3685 1.0; 3943 0.1; 4219 0.0; 4514 0.4; 4830 1.4; 5168 2.5; 5530 2.2; 5917 2.0; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.33676625927899dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 143 Hz  | 0.32 | -2.6 dB |
| Peaking | 412 Hz  | 0.64 | 4.1 dB  |
| Peaking | 1883 Hz | 1.28 | -5.5 dB |
| Peaking | 3014 Hz | 3.16 | 6.4 dB  |
| Peaking | 6387 Hz | 4.66 | 5.0 dB  |
| Peaking | 17 Hz   | 1.68 | 1.7 dB  |
| Peaking | 109 Hz  | 1.42 | -1.7 dB |
| Peaking | 115 Hz  | 3.43 | 3.0 dB  |
| Peaking | 5145 Hz | 6    | 3.2 dB  |
| Peaking | 5159 Hz | 2.18 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)