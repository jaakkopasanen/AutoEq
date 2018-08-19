# Etymotic MC5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.8; 56 5.6; 59 5.3; 64 5.0; 68 4.8; 73 4.6; 78 4.4; 83 4.2; 89 3.8; 95 3.5; 102 3.3; 109 3.2; 117 3.0; 125 2.8; 134 2.5; 143 2.4; 153 2.2; 164 2.1; 175 1.9; 188 1.8; 201 1.8; 215 1.7; 230 1.7; 246 1.7; 263 1.7; 282 1.7; 301 1.8; 323 1.9; 345 2.0; 369 2.1; 395 2.2; 423 2.1; 452 2.1; 484 2.2; 518 2.2; 554 2.2; 593 2.2; 635 2.3; 679 2.2; 726 2.1; 777 1.9; 832 1.6; 890 1.1; 952 0.5; 1019 -0.1; 1090 -0.8; 1167 -1.4; 1248 -2.1; 1336 -3.0; 1429 -3.9; 1529 -4.8; 1636 -5.5; 1751 -5.7; 1873 -4.5; 2004 -2.4; 2145 -1.6; 2295 -1.1; 2455 -0.3; 2627 0.7; 2811 1.8; 3008 3.1; 3219 4.4; 3444 5.7; 3685 6.0; 3943 6.0; 4219 5.5; 4514 4.9; 4830 5.2; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.34 | 6.2 dB  |
| Peaking | 616 Hz  | 0.66 | 2.5 dB  |
| Peaking | 1641 Hz | 1.71 | -6.8 dB |
| Peaking | 3705 Hz | 1.89 | 6.2 dB  |
| Peaking | 5780 Hz | 3.16 | 5.3 dB  |
| Peaking | 1057 Hz | 1.78 | 0.5 dB  |
| Peaking | 1090 Hz | 3.55 | -0.8 dB |
| Peaking | 6566 Hz | 8.21 | 2.0 dB  |
| Peaking | 7815 Hz | 2.39 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC5/Etymotic%20MC5.png)