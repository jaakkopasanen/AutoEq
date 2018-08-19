# Ortofon 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.8; 59 5.7; 64 5.9; 68 6.0; 73 6.0; 78 5.9; 83 5.5; 89 5.2; 95 5.2; 102 5.2; 109 5.4; 117 5.5; 125 5.4; 134 5.2; 143 5.2; 153 5.2; 164 5.4; 175 5.5; 188 5.3; 201 4.8; 215 4.9; 230 4.3; 246 3.3; 263 2.7; 282 1.5; 301 0.3; 323 -0.8; 345 -1.6; 369 -1.8; 395 -1.6; 423 -1.2; 452 -1.1; 484 -0.8; 518 -0.7; 554 -0.5; 593 -0.3; 635 0.0; 679 0.2; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 0.1; 1248 0.6; 1336 0.5; 1429 0.6; 1529 0.4; 1636 -0.2; 1751 -1.1; 1873 -0.9; 2004 -0.5; 2145 0.2; 2295 1.1; 2455 2.1; 2627 3.1; 2811 3.7; 3008 3.1; 3219 2.7; 3444 3.7; 3685 4.1; 3943 3.1; 4219 4.8; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -3.9; 10167 -4.2; 10879 -2.2; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.37 | 6.5 dB  |
| Peaking | 172 Hz  | 1.81 | 3.8 dB  |
| Peaking | 4455 Hz | 1.29 | 4.8 dB  |
| Peaking | 5961 Hz | 3.25 | 3.6 dB  |
| Peaking | 9843 Hz | 3.87 | -5.4 dB |
| Peaking | 241 Hz  | 3.23 | 1.9 dB  |
| Peaking | 366 Hz  | 2    | -3.0 dB |
| Peaking | 1862 Hz | 4.81 | -1.9 dB |
| Peaking | 2728 Hz | 6.35 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%202/Ortofon%202.png)