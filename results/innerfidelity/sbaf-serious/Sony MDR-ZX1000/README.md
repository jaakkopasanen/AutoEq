# Sony MDR-ZX1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.8; 64 4.9; 68 4.3; 73 3.6; 78 3.0; 83 2.5; 89 2.1; 95 1.8; 102 1.6; 109 1.4; 117 0.9; 125 0.4; 134 0.0; 143 -0.2; 153 -0.2; 164 0.4; 175 0.9; 188 1.0; 201 1.2; 215 1.5; 230 1.8; 246 1.9; 263 1.6; 282 1.7; 301 1.4; 323 0.7; 345 0.2; 369 -0.3; 395 -0.5; 423 -0.6; 452 -0.6; 484 -0.7; 518 -0.7; 554 -0.5; 593 -0.1; 635 0.1; 679 0.1; 726 -0.1; 777 0.0; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.6; 1336 -1.3; 1429 -2.2; 1529 -3.1; 1636 -4.0; 1751 -4.7; 1873 -4.8; 2004 -4.6; 2145 -4.2; 2295 -3.5; 2455 -2.6; 2627 -1.6; 2811 -0.7; 3008 0.3; 3219 1.4; 3444 3.5; 3685 5.3; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.4; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.6; 8299 -4.3; 8880 -6.6; 9502 -6.6; 10167 -3.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.66 | 6.8 dB   |
| Peaking | 253 Hz  | 3.79 | 1.8 dB   |
| Peaking | 2110 Hz | 1.36 | -7.6 dB  |
| Peaking | 4935 Hz | 0.71 | 8.2 dB   |
| Peaking | 8992 Hz | 2.86 | -11.1 dB |
| Peaking | 59 Hz   | 4.65 | 1.3 dB   |
| Peaking | 137 Hz  | 4.18 | -1.4 dB  |
| Peaking | 470 Hz  | 2.99 | -1.0 dB  |
| Peaking | 1155 Hz | 1.13 | 0.8 dB   |
| Peaking | 1625 Hz | 4.34 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX1000/Sony%20MDR-ZX1000.png)