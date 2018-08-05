# Thermaltake Isurus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.0; 23 -0.1; 25 -0.2; 26 -0.2; 28 -0.3; 30 -0.3; 32 -0.4; 35 -0.5; 37 -0.5; 40 -0.6; 42 -0.6; 45 -0.6; 49 -0.7; 52 -0.7; 56 -0.8; 59 -0.8; 64 -0.8; 68 -0.9; 73 -1.0; 78 -1.3; 83 -1.6; 89 -2.0; 95 -2.5; 102 -3.1; 109 -3.5; 117 -4.1; 125 -4.7; 134 -5.2; 143 -5.5; 153 -5.7; 164 -5.9; 175 -6.0; 188 -6.0; 201 -6.1; 215 -6.1; 230 -6.0; 246 -6.0; 263 -5.9; 282 -5.8; 301 -5.6; 323 -5.5; 345 -5.4; 369 -5.2; 395 -5.0; 423 -4.7; 452 -4.5; 484 -3.8; 518 -2.9; 554 -2.9; 593 -2.3; 635 -1.9; 679 -1.7; 726 -1.2; 777 -0.7; 832 -0.4; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.1; 1336 -0.2; 1429 -0.5; 1529 -1.0; 1636 -1.3; 1751 -1.6; 1873 -1.6; 2004 -1.6; 2145 -1.6; 2295 -1.4; 2455 -0.8; 2627 -0.5; 2811 -0.4; 3008 0.3; 3219 0.7; 3444 1.2; 3685 1.2; 3943 0.6; 4219 -1.0; 4514 -1.6; 4830 -2.1; 5168 -2.6; 5530 -3.4; 5917 -4.3; 6331 -5.0; 6775 -3.6; 7249 -2.3; 7756 -1.6; 8299 -2.1; 8880 -3.1; 9502 -3.2; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -0.9; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.8dB` and instead set Global volume in the UI for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thermaltake Isurus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 225 Hz  | 0.62 | -6.6 dB |
| Peaking | 2017 Hz | 3.33 | -1.6 dB |
| Peaking | 3557 Hz | 4.34 | 2.1 dB  |
| Peaking | 6078 Hz | 2.43 | -4.7 dB |
| Peaking | 9188 Hz | 6.23 | -3.0 dB |
| Peaking | 78 Hz   | 1.81 | 0.8 dB  |
| Peaking | 133 Hz  | 1.99 | -1.0 dB |
| Peaking | 224 Hz  | 1.96 | 0.8 dB  |
| Peaking | 424 Hz  | 2.58 | -1.1 dB |
| Peaking | 956 Hz  | 2.13 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thermaltake%20Isurus/Thermaltake%20Isurus.png)