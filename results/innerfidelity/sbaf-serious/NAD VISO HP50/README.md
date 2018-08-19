# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.2; 23 -3.2; 25 -3.3; 26 -3.3; 28 -3.3; 30 -3.3; 32 -3.3; 35 -3.3; 37 -3.3; 40 -3.2; 42 -3.1; 45 -3.0; 49 -2.9; 52 -2.8; 56 -2.7; 59 -2.6; 64 -2.5; 68 -2.5; 73 -2.4; 78 -2.3; 83 -2.2; 89 -2.1; 95 -2.1; 102 -2.5; 109 -2.8; 117 -2.6; 125 -2.4; 134 -2.9; 143 -4.0; 153 -4.6; 164 -3.0; 175 -3.1; 188 -4.5; 201 -4.3; 215 -4.2; 230 -3.6; 246 -3.2; 263 -2.7; 282 -2.1; 301 -1.4; 323 -1.0; 345 -0.9; 369 -0.7; 395 -0.4; 423 -0.1; 452 0.0; 484 -0.1; 518 -0.1; 554 0.1; 593 0.3; 635 0.2; 679 0.1; 726 -0.1; 777 -0.1; 832 -0.1; 890 -0.1; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.7; 1248 -1.5; 1336 -2.1; 1429 -2.4; 1529 -2.7; 1636 -2.8; 1751 -2.4; 1873 -1.9; 2004 -1.4; 2145 -0.7; 2295 0.1; 2455 1.0; 2627 1.8; 2811 2.2; 3008 2.3; 3219 2.2; 3444 1.9; 3685 1.2; 3943 0.7; 4219 0.2; 4514 -0.2; 4830 -1.3; 5168 1.4; 5530 4.0; 5917 5.0; 6331 5.1; 6775 3.8; 7249 1.3; 7756 -0.5; 8299 -1.4; 8880 -1.5; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.242608418578785dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.31 | -3.2 dB |
| Peaking | 193 Hz  | 1.28 | -3.8 dB |
| Peaking | 1540 Hz | 2.76 | 0.6 dB  |
| Peaking | 1608 Hz | 1.49 | -6.1 dB |
| Peaking | 2290 Hz | 0.41 | 3.0 dB  |
| Peaking | 2147 Hz | 5.17 | -0.6 dB |
| Peaking | 2834 Hz | 3.73 | 1.0 dB  |
| Peaking | 4860 Hz | 3.06 | -5.3 dB |
| Peaking | 6003 Hz | 2.17 | 6.7 dB  |
| Peaking | 8121 Hz | 2.39 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)