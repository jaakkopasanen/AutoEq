# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.1; 59 4.3; 64 3.3; 68 2.8; 73 2.5; 78 2.8; 83 2.9; 89 2.7; 95 1.5; 102 0.0; 109 -0.7; 117 -1.2; 125 -1.5; 134 -1.9; 143 -2.0; 153 -2.1; 164 -1.0; 175 -1.4; 188 -2.0; 201 -2.2; 215 -2.4; 230 -2.6; 246 -2.6; 263 -2.5; 282 -2.5; 301 -3.0; 323 -3.4; 345 -4.5; 369 -3.9; 395 -3.5; 423 -3.4; 452 -3.4; 484 -3.0; 518 -2.6; 554 -2.1; 593 -1.4; 635 -0.8; 679 -0.2; 726 0.0; 777 -0.2; 832 0.1; 890 0.1; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.5; 1529 -2.6; 1636 -3.6; 1751 -5.0; 1873 -6.0; 2004 -7.2; 2145 -7.5; 2295 -7.0; 2455 -6.1; 2627 -5.2; 2811 -4.5; 3008 -3.5; 3219 -1.8; 3444 -0.1; 3685 2.4; 3943 5.3; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.0; 5530 3.0; 5917 4.2; 6331 3.9; 6775 3.5; 7249 0.9; 7756 -4.7; 8299 -9.8; 8880 -11.2; 9502 -8.4; 10167 -3.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1    | 7.2 dB   |
| Peaking | 2284 Hz | 1.52 | -8.4 dB  |
| Peaking | 4237 Hz | 3.43 | 5.9 dB   |
| Peaking | 6738 Hz | 1.04 | 7.2 dB   |
| Peaking | 8707 Hz | 3.25 | -17.5 dB |
| Peaking | 89 Hz   | 1.16 | 2.5 dB   |
| Peaking | 120 Hz  | 1.94 | -3.2 dB  |
| Peaking | 218 Hz  | 1.14 | -1.5 dB  |
| Peaking | 394 Hz  | 1.35 | -3.6 dB  |
| Peaking | 960 Hz  | 1.4  | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)