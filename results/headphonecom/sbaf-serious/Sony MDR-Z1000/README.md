# Sony MDR-Z1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.5; 68 4.8; 73 4.1; 78 3.6; 83 3.1; 89 2.7; 95 2.5; 102 2.2; 109 1.7; 117 1.2; 125 0.6; 134 0.1; 143 -0.2; 153 -0.2; 164 0.2; 175 0.4; 188 0.5; 201 0.7; 215 0.9; 230 1.2; 246 1.6; 263 2.4; 282 2.6; 301 1.7; 323 1.0; 345 0.5; 369 0.2; 395 -0.1; 423 -0.3; 452 -0.4; 484 -0.6; 518 -0.5; 554 -0.3; 593 -0.1; 635 0.0; 679 0.2; 726 0.2; 777 -0.0; 832 0.1; 890 0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 -0.2; 1248 -0.6; 1336 -1.3; 1429 -2.1; 1529 -3.0; 1636 -3.8; 1751 -4.2; 1873 -4.1; 2004 -3.9; 2145 -2.9; 2295 -1.4; 2455 -0.5; 2627 0.4; 2811 1.6; 3008 2.6; 3219 3.6; 3444 5.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.5; 8880 -5.6; 9502 -7.1; 10167 -3.8; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.62 | 6.8 dB   |
| Peaking | 275 Hz  | 5.79 | 2.5 dB   |
| Peaking | 1919 Hz | 1.7  | -6.7 dB  |
| Peaking | 4643 Hz | 0.73 | 7.3 dB   |
| Peaking | 9261 Hz | 3.56 | -10.2 dB |
| Peaking | 38 Hz   | 2.66 | -1.1 dB  |
| Peaking | 61 Hz   | 2.54 | 1.3 dB   |
| Peaking | 141 Hz  | 3.83 | -1.6 dB  |
| Peaking | 474 Hz  | 4.2  | -0.8 dB  |
| Peaking | 1098 Hz | 4.5  | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)