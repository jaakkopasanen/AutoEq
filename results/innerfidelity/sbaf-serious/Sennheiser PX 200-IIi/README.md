# Sennheiser PX 200-IIi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.8; 78 5.3; 83 4.7; 89 4.3; 95 4.3; 102 4.5; 109 4.1; 117 3.5; 125 3.0; 134 2.4; 143 1.9; 153 1.5; 164 1.2; 175 1.2; 188 1.0; 201 0.8; 215 0.6; 230 0.4; 246 0.2; 263 0.3; 282 0.3; 301 0.1; 323 0.0; 345 0.1; 369 0.1; 395 0.6; 423 1.0; 452 0.7; 484 0.5; 518 0.4; 554 0.7; 593 1.1; 635 1.5; 679 2.1; 726 2.1; 777 2.2; 832 2.1; 890 1.8; 952 0.9; 1019 0.1; 1090 1.6; 1167 1.6; 1248 2.3; 1336 1.8; 1429 1.0; 1529 0.1; 1636 -0.6; 1751 -1.1; 1873 -1.2; 2004 -1.1; 2145 -1.2; 2295 -0.9; 2455 0.2; 2627 1.3; 2811 1.7; 3008 2.7; 3219 3.4; 3444 4.1; 3685 4.9; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.43 | 6.7 dB  |
| Peaking | 751 Hz  | 2.96 | 2.2 dB  |
| Peaking | 1271 Hz | 4.32 | 2.2 dB  |
| Peaking | 1988 Hz | 2.18 | -2.6 dB |
| Peaking | 4622 Hz | 1.32 | 6.9 dB  |
| Peaking | 27 Hz   | 0.61 | 1.7 dB  |
| Peaking | 36 Hz   | 1.39 | -2.4 dB |
| Peaking | 4800 Hz | 6.18 | -1.1 dB |
| Peaking | 6416 Hz | 2.84 | 3.9 dB  |
| Peaking | 7524 Hz | 1.95 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200-IIi/Sennheiser%20PX%20200-IIi.png)