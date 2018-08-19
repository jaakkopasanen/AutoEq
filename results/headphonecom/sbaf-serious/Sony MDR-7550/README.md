# Sony MDR-7550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.1; 22 3.8; 23 3.7; 25 3.5; 26 3.4; 28 3.2; 30 3.0; 32 2.9; 35 2.7; 37 2.6; 40 2.4; 42 2.3; 45 2.1; 49 1.9; 52 1.8; 56 1.5; 59 1.3; 64 0.9; 68 0.7; 73 0.5; 78 0.3; 83 0.1; 89 -0.1; 95 -0.3; 102 -0.5; 109 -0.7; 117 -0.9; 125 -1.1; 134 -1.3; 143 -1.5; 153 -1.7; 164 -1.8; 175 -1.9; 188 -2.0; 201 -2.1; 215 -2.1; 230 -2.0; 246 -1.9; 263 -1.9; 282 -1.9; 301 -1.8; 323 -1.5; 345 -1.4; 369 -1.2; 395 -1.0; 423 -0.9; 452 -0.7; 484 -0.5; 518 -0.4; 554 -0.3; 593 -0.0; 635 0.3; 679 0.4; 726 0.5; 777 0.4; 832 0.4; 890 0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 -0.5; 1248 -1.3; 1336 -2.1; 1429 -2.8; 1529 -3.5; 1636 -4.0; 1751 -4.0; 1873 -3.8; 2004 -3.3; 2145 -2.4; 2295 -1.1; 2455 0.5; 2627 2.2; 2811 4.1; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.9; 4514 0.8; 4830 -2.3; 5168 -2.6; 5530 1.5; 5917 5.4; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715982dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.49 | 3.9 dB  |
| Peaking | 196 Hz  | 0.87 | -2.4 dB |
| Peaking | 1792 Hz | 2.23 | -5.1 dB |
| Peaking | 3301 Hz | 2.6  | 7.5 dB  |
| Peaking | 6283 Hz | 7.2  | 6.0 dB  |
| Peaking | 863 Hz  | 1.6  | 0.9 dB  |
| Peaking | 1425 Hz | 5.45 | -1.0 dB |
| Peaking | 4064 Hz | 7.41 | 3.4 dB  |
| Peaking | 5059 Hz | 4.82 | -5.5 dB |
| Peaking | 5774 Hz | 7.56 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)