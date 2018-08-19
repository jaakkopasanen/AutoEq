# Etymotic hf5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.7; 35 5.4; 37 5.3; 40 5.1; 42 4.9; 45 4.7; 49 4.4; 52 4.3; 56 4.0; 59 3.8; 64 3.4; 68 3.3; 73 3.0; 78 2.7; 83 2.4; 89 2.1; 95 1.9; 102 1.7; 109 1.6; 117 1.4; 125 1.2; 134 1.0; 143 0.8; 153 0.6; 164 0.5; 175 0.4; 188 0.3; 201 0.2; 215 0.2; 230 0.2; 246 0.1; 263 0.1; 282 0.2; 301 0.2; 323 0.3; 345 0.4; 369 0.7; 395 0.9; 423 0.9; 452 1.0; 484 1.1; 518 1.1; 554 1.0; 593 1.0; 635 1.2; 679 1.1; 726 1.2; 777 1.1; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.5; 1336 -2.0; 1429 -2.6; 1529 -3.2; 1636 -3.5; 1751 -3.6; 1873 -3.6; 2004 -3.5; 2145 -3.3; 2295 -2.9; 2455 -2.2; 2627 -1.2; 2811 0.0; 3008 1.6; 3219 3.3; 3444 4.8; 3685 5.6; 3943 5.4; 4219 4.5; 4514 4.1; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.59 | 4.4 dB  |
| Peaking | 42 Hz   | 0.55 | 3.1 dB  |
| Peaking | 1956 Hz | 1.67 | -4.6 dB |
| Peaking | 3685 Hz | 2.67 | 5.7 dB  |
| Peaking | 5711 Hz | 2.87 | 6.1 dB  |
| Peaking | 636 Hz  | 3.38 | -1.1 dB |
| Peaking | 655 Hz  | 1.57 | 2.3 dB  |
| Peaking | 1391 Hz | 3.47 | -1.0 dB |
| Peaking | 6597 Hz | 7.92 | 2.1 dB  |
| Peaking | 7736 Hz | 2.37 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf5/Etymotic%20hf5.png)