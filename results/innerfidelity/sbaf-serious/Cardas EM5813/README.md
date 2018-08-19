# Cardas EM5813

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -6.3; 22 -6.3; 23 -6.3; 25 -6.3; 26 -6.3; 28 -6.4; 30 -6.4; 32 -6.4; 35 -6.5; 37 -6.6; 40 -6.6; 42 -6.7; 45 -6.8; 49 -6.9; 52 -7.0; 56 -7.2; 59 -7.3; 64 -7.6; 68 -7.7; 73 -7.9; 78 -8.2; 83 -8.4; 89 -8.6; 95 -8.8; 102 -9.0; 109 -9.1; 117 -9.2; 125 -9.3; 134 -9.4; 143 -9.5; 153 -9.6; 164 -9.5; 175 -9.5; 188 -9.4; 201 -9.4; 215 -9.2; 230 -8.9; 246 -8.8; 263 -8.6; 282 -8.3; 301 -8.1; 323 -7.8; 345 -7.5; 369 -7.2; 395 -6.9; 423 -6.5; 452 -6.1; 484 -5.8; 518 -5.4; 554 -4.8; 593 -4.3; 635 -3.9; 679 -3.7; 726 -3.3; 777 -2.9; 832 -2.6; 890 -0.6; 952 -0.2; 1019 -0.1; 1090 -0.7; 1167 -0.3; 1248 -0.5; 1336 -1.0; 1429 -1.3; 1529 -1.5; 1636 -1.6; 1751 -1.5; 1873 -1.2; 2004 -1.6; 2145 -2.0; 2295 -3.0; 2455 -4.2; 2627 -5.2; 2811 -2.9; 3008 0.1; 3219 1.7; 3444 2.3; 3685 1.3; 3943 -1.0; 4219 -4.6; 4514 -5.9; 4830 -2.5; 5168 2.4; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.072548682101091dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.21 | -5.8 dB |
| Peaking | 123 Hz  | 0.66 | -4.0 dB |
| Peaking | 294 Hz  | 0.55 | -6.2 dB |
| Peaking | 4504 Hz | 6.41 | -8.1 dB |
| Peaking | 5848 Hz | 3.47 | 7.4 dB  |
| Peaking | 1017 Hz | 2.42 | 2.8 dB  |
| Peaking | 1172 Hz | 0.56 | -1.0 dB |
| Peaking | 2604 Hz | 4.37 | -5.2 dB |
| Peaking | 3324 Hz | 4.31 | 4.0 dB  |
| Peaking | 8200 Hz | 5.29 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)