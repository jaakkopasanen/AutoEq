# Urbanears Plattan

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.8; 49 5.6; 52 5.5; 56 5.4; 59 5.4; 64 5.2; 68 5.1; 73 5.0; 78 4.8; 83 4.7; 89 4.7; 95 4.7; 102 4.7; 109 4.5; 117 4.6; 125 4.8; 134 4.6; 143 4.5; 153 4.2; 164 3.9; 175 3.7; 188 3.6; 201 3.6; 215 3.7; 230 3.8; 246 3.8; 263 3.8; 282 4.1; 301 4.4; 323 4.8; 345 5.2; 369 5.5; 395 5.5; 423 4.9; 452 4.1; 484 3.6; 518 3.0; 554 2.6; 593 2.2; 635 1.8; 679 1.3; 726 0.8; 777 0.5; 832 0.1; 890 -0.2; 952 -0.3; 1019 0.2; 1090 1.1; 1167 2.7; 1248 3.2; 1336 3.5; 1429 4.5; 1529 5.6; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Urbanears Plattan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.29 | 6.0 dB  |
| Peaking | 152 Hz  | 0.77 | 2.3 dB  |
| Peaking | 376 Hz  | 1.95 | 4.6 dB  |
| Peaking | 2086 Hz | 1.16 | 5.9 dB  |
| Peaking | 4759 Hz | 1.37 | 5.7 dB  |
| Peaking | 927 Hz  | 3.9  | -2.2 dB |
| Peaking | 1529 Hz | 5.19 | 1.6 dB  |
| Peaking | 4734 Hz | 5.95 | -1.0 dB |
| Peaking | 6324 Hz | 2.97 | 3.8 dB  |
| Peaking | 7668 Hz | 1.95 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Urbanears%20Plattan/Urbanears%20Plattan.png)