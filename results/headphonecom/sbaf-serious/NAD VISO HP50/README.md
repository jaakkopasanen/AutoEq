# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 -6.5; 22 -6.4; 23 -6.4; 25 -6.3; 26 -6.3; 28 -6.2; 30 -6.2; 32 -6.1; 35 -5.9; 37 -5.8; 40 -5.7; 42 -5.6; 45 -5.5; 49 -5.3; 52 -5.2; 56 -5.0; 59 -4.9; 64 -4.7; 68 -4.6; 73 -4.4; 78 -4.2; 83 -4.1; 89 -3.8; 95 -3.4; 102 -3.2; 109 -3.2; 117 -3.6; 125 -5.0; 134 -6.1; 143 -6.3; 153 -5.6; 164 -4.6; 175 -4.4; 188 -5.4; 201 -5.6; 215 -5.4; 230 -5.1; 246 -4.7; 263 -4.3; 282 -3.7; 301 -3.1; 323 -2.4; 345 -1.9; 369 -2.1; 395 -1.7; 423 -1.4; 452 -1.3; 484 -1.2; 518 -1.0; 554 -0.7; 593 -0.4; 635 -0.2; 679 -0.0; 726 -0.1; 777 -0.4; 832 -0.8; 890 -0.8; 952 -0.5; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.7; 1336 -2.7; 1429 -3.4; 1529 -3.8; 1636 -3.7; 1751 -3.3; 1873 -2.1; 2004 -1.7; 2145 -1.0; 2295 -0.1; 2455 0.8; 2627 1.8; 2811 2.7; 3008 2.8; 3219 2.7; 3444 2.4; 3685 1.7; 3943 0.7; 4219 -0.9; 4514 -2.5; 4830 -2.6; 5168 -0.3; 5530 2.0; 5917 2.7; 6331 3.3; 6775 2.7; 7249 1.3; 7756 0.2; 8299 -0.8; 8880 -1.7; 9502 -1.3; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.486625124528033dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1    | -4.5 dB |
| Peaking | 46 Hz   | 0.74 | -4.0 dB |
| Peaking | 185 Hz  | 0.92 | -5.2 dB |
| Peaking | 1560 Hz | 3.73 | -4.3 dB |
| Peaking | 664 Hz  | 5.6  | 0.6 dB  |
| Peaking | 3133 Hz | 3.05 | 3.4 dB  |
| Peaking | 4746 Hz | 4.7  | -4.6 dB |
| Peaking | 6183 Hz | 2.46 | 3.9 dB  |
| Peaking | 8878 Hz | 3.88 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)