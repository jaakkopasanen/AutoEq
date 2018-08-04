# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.2; 23 -3.2; 25 -3.2; 26 -3.3; 28 -3.3; 30 -3.3; 32 -3.3; 35 -3.2; 37 -3.2; 40 -3.1; 42 -3.0; 45 -2.9; 49 -2.7; 52 -2.6; 56 -2.3; 59 -2.2; 64 -2.0; 68 -1.9; 73 -1.7; 78 -1.5; 83 -1.4; 89 -1.4; 95 -1.4; 102 -2.0; 109 -2.4; 117 -2.4; 125 -2.4; 134 -3.0; 143 -4.2; 153 -4.8; 164 -3.2; 175 -3.3; 188 -4.7; 201 -4.5; 215 -4.3; 230 -3.7; 246 -3.3; 263 -2.8; 282 -2.1; 301 -1.4; 323 -1.1; 345 -0.9; 369 -0.7; 395 -0.4; 423 -0.1; 452 0.0; 484 -0.1; 518 -0.1; 554 0.1; 593 0.3; 635 0.2; 679 0.1; 726 -0.1; 777 -0.1; 832 -0.1; 890 -0.1; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.7; 1248 -1.5; 1336 -2.1; 1429 -2.4; 1529 -2.7; 1636 -2.8; 1751 -2.4; 1873 -1.9; 2004 -1.4; 2145 -0.7; 2295 0.1; 2455 1.0; 2627 1.8; 2811 2.2; 3008 2.3; 3219 2.2; 3444 1.9; 3685 1.2; 3943 0.7; 4219 0.2; 4514 -0.2; 4830 -1.3; 5168 1.4; 5530 4.0; 5917 5.0; 6331 5.1; 6775 3.8; 7249 1.3; 7756 -0.5; 8299 -1.4; 8880 -1.5; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.63 | -3.4 dB |
| Peaking | 188 Hz  | 1.21 | -4.4 dB |
| Peaking | 1605 Hz | 1.51 | -6.3 dB |
| Peaking | 1543 Hz | 2.88 | 0.7 dB  |
| Peaking | 2284 Hz | 0.41 | 3.0 dB  |
| Peaking | 2176 Hz | 5.23 | -0.6 dB |
| Peaking | 2819 Hz | 3.73 | 1.0 dB  |
| Peaking | 4770 Hz | 3.06 | -5.3 dB |
| Peaking | 6025 Hz | 2.17 | 6.7 dB  |
| Peaking | 8251 Hz | 2.4  | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)