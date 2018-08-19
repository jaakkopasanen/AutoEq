# Etymotic MC3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.7; 64 5.3; 68 5.0; 73 4.7; 78 4.4; 83 4.2; 89 3.9; 95 3.6; 102 3.3; 109 3.2; 117 3.0; 125 2.8; 134 2.5; 143 2.4; 153 2.2; 164 2.1; 175 1.9; 188 1.8; 201 1.8; 215 1.7; 230 1.5; 246 1.5; 263 1.5; 282 1.5; 301 1.6; 323 1.7; 345 1.8; 369 1.9; 395 2.0; 423 2.0; 452 1.9; 484 2.0; 518 2.0; 554 2.0; 593 2.1; 635 2.1; 679 2.1; 726 1.9; 777 1.8; 832 1.4; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -1.9; 1336 -2.6; 1429 -3.3; 1529 -4.0; 1636 -4.1; 1751 -3.8; 1873 -3.8; 2004 -3.4; 2145 -2.7; 2295 -2.0; 2455 -1.1; 2627 -0.1; 2811 1.1; 3008 2.2; 3219 3.6; 3444 5.0; 3685 5.8; 3943 5.6; 4219 4.7; 4514 3.9; 4830 4.0; 5168 4.8; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.35 | 6.3 dB  |
| Peaking | 759 Hz  | 0.61 | 3.1 dB  |
| Peaking | 1660 Hz | 0.99 | -6.1 dB |
| Peaking | 3660 Hz | 2.06 | 6.5 dB  |
| Peaking | 5884 Hz | 3.46 | 5.8 dB  |
| Peaking | 8194 Hz | 4.75 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC3/Etymotic%20MC3.png)