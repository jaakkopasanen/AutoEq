# Stax SR-40 Electret SR4 Adapter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.5; 102 4.1; 109 3.1; 117 1.9; 125 0.7; 134 -0.2; 143 -0.7; 153 -1.1; 164 -1.3; 175 -1.3; 188 -1.2; 201 -1.1; 215 -0.9; 230 -0.7; 246 -0.6; 263 -0.5; 282 -0.2; 301 -0.1; 323 0.0; 345 0.2; 369 0.3; 395 0.4; 423 0.5; 452 0.5; 484 0.5; 518 0.2; 554 0.1; 593 0.3; 635 0.6; 679 0.6; 726 0.5; 777 0.5; 832 0.3; 890 -0.0; 952 0.1; 1019 0.1; 1090 0.3; 1167 -0.2; 1248 -0.9; 1336 -1.9; 1429 -3.1; 1529 -4.0; 1636 -4.6; 1751 -4.5; 1873 -3.0; 2004 -0.8; 2145 0.5; 2295 1.0; 2455 2.7; 2627 4.0; 2811 3.9; 3008 4.1; 3219 4.1; 3444 3.3; 3685 2.5; 3943 2.0; 4219 2.0; 4514 1.4; 4830 1.2; 5168 1.2; 5530 2.3; 5917 1.4; 6331 1.3; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-40 Electret SR4 Adapter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 60 Hz   | 0.28 | 7.4 dB  |
| Peaking | 165 Hz  | 1.07 | -6.5 dB |
| Peaking | 1679 Hz | 2.83 | -6.2 dB |
| Peaking | 2891 Hz | 1.56 | 4.7 dB  |
| Peaking | 6614 Hz | 3.85 | 1.6 dB  |
| Peaking | 16 Hz   | 1.04 | 1.9 dB  |
| Peaking | 43 Hz   | 1.11 | -0.9 dB |
| Peaking | 91 Hz   | 4.32 | 1.7 dB  |
| Peaking | 284 Hz  | 0.16 | -0.3 dB |
| Peaking | 883 Hz  | 1.34 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-40%20Electret%20SR4%20Adapter/Stax%20SR-40%20Electret%20SR4%20Adapter.png)