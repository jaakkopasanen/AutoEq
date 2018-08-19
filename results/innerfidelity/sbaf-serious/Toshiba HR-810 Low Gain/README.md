# Toshiba HR-810 Low Gain

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.7; 102 4.7; 109 4.2; 117 3.5; 125 2.6; 134 1.9; 143 1.4; 153 0.9; 164 0.6; 175 0.1; 188 -0.2; 201 -0.3; 215 -0.4; 230 -0.4; 246 -0.4; 263 -0.5; 282 -0.4; 301 -0.3; 323 -0.2; 345 -0.1; 369 0.0; 395 0.1; 423 0.3; 452 0.5; 484 0.5; 518 0.5; 554 0.7; 593 0.9; 635 0.9; 679 0.8; 726 0.8; 777 0.9; 832 0.8; 890 0.3; 952 0.1; 1019 0.0; 1090 0.7; 1167 0.8; 1248 -0.8; 1336 -2.3; 1429 -2.9; 1529 -3.3; 1636 -3.7; 1751 -3.7; 1873 -3.5; 2004 -3.4; 2145 -4.0; 2295 -3.9; 2455 -2.9; 2627 -2.7; 2811 -2.2; 3008 -0.8; 3219 -0.0; 3444 0.7; 3685 1.5; 3943 2.2; 4219 2.5; 4514 3.4; 4830 5.1; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Toshiba HR-810 Low Gain ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.33 | 7.8 dB  |
| Peaking | 634 Hz  | 0.65 | 7.6 dB  |
| Peaking | 1069 Hz | 0.12 | -7.4 dB |
| Peaking | 1133 Hz | 4.68 | 3.2 dB  |
| Peaking | 5193 Hz | 1.09 | 11.3 dB |
| Peaking | 19 Hz   | 2.15 | 1.3 dB  |
| Peaking | 92 Hz   | 5.83 | 1.3 dB  |
| Peaking | 6376 Hz | 4.4  | 3.5 dB  |
| Peaking | 7129 Hz | 1.46 | -3.5 dB |
| Peaking | 8686 Hz | 0.52 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Toshiba%20HR-810%20Low%20Gain/Toshiba%20HR-810%20Low%20Gain.png)