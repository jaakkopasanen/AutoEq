# AKG K450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.4; 37 5.0; 40 4.6; 42 4.4; 45 4.1; 49 3.7; 52 3.5; 56 3.2; 59 3.1; 64 2.8; 68 2.6; 73 2.4; 78 2.1; 83 1.9; 89 1.7; 95 1.4; 102 1.3; 109 1.0; 117 0.8; 125 0.6; 134 0.2; 143 -0.0; 153 -0.1; 164 -0.2; 175 -0.4; 188 -0.5; 201 -0.6; 215 -0.7; 230 -0.7; 246 -0.9; 263 -0.7; 282 -0.8; 301 -0.8; 323 -0.9; 345 -0.9; 369 -0.8; 395 -0.4; 423 -0.3; 452 -0.6; 484 -0.8; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.3; 679 -0.2; 726 -0.1; 777 -0.0; 832 0.1; 890 -0.2; 952 0.5; 1019 0.7; 1090 0.8; 1167 1.2; 1248 1.9; 1336 2.5; 1429 3.1; 1529 4.0; 1636 4.9; 1751 5.1; 1873 5.7; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 5.9; 2811 4.8; 3008 3.2; 3219 1.5; 3444 0.4; 3685 0.2; 3943 1.4; 4219 2.3; 4514 3.6; 4830 5.8; 5168 6.0; 5530 5.9; 5917 5.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.36 | 6.2 dB  |
| Peaking | 1372 Hz | 0.09 | -1.5 dB |
| Peaking | 2228 Hz | 0.93 | 7.9 dB  |
| Peaking | 3541 Hz | 3.27 | -4.2 dB |
| Peaking | 5512 Hz | 2.07 | 6.6 dB  |
| Peaking | 1105 Hz | 7.6  | -0.5 dB |
| Peaking | 5685 Hz | 6.85 | -2.3 dB |
| Peaking | 6501 Hz | 2.68 | 2.8 dB  |
| Peaking | 7497 Hz | 3.47 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K450/AKG%20K450.png)