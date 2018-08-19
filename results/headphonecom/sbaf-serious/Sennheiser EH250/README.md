# Sennheiser EH250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 5.1; 64 4.5; 68 4.2; 73 3.7; 78 3.0; 83 2.6; 89 2.2; 95 1.9; 102 1.6; 109 1.3; 117 1.3; 125 1.4; 134 2.4; 143 3.3; 153 3.5; 164 3.7; 175 3.8; 188 4.0; 201 4.3; 215 4.7; 230 4.9; 246 5.1; 263 5.1; 282 4.4; 301 2.4; 323 1.2; 345 1.7; 369 2.1; 395 2.4; 423 2.3; 452 2.1; 484 1.5; 518 0.8; 554 0.6; 593 0.5; 635 0.5; 679 0.4; 726 0.5; 777 0.7; 832 0.6; 890 0.3; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.1; 1429 -0.1; 1529 -0.2; 1636 -0.3; 1751 -0.2; 1873 0.2; 2004 0.5; 2145 0.8; 2295 1.5; 2455 1.6; 2627 2.0; 2811 2.9; 3008 4.5; 3219 6.0; 3444 6.0; 3685 4.9; 3943 -0.9; 4219 -2.2; 4514 0.4; 4830 2.7; 5168 3.1; 5530 4.8; 5917 5.9; 6331 4.0; 6775 0.2; 7249 -1.4; 7756 -0.6; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.2; 13327 -3.0; 14260 -4.4; 15258 -3.7; 16326 -2.9; 17469 -2.4; 18692 -1.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.62 | 6.7 dB  |
| Peaking | 231 Hz   | 1.43 | 4.7 dB  |
| Peaking | 4454 Hz  | 0.7  | 3.3 dB  |
| Peaking | 11932 Hz | 2.43 | 5.1 dB  |
| Peaking | 13543 Hz | 1    | -6.4 dB |
| Peaking | 1739 Hz  | 1.87 | -1.3 dB |
| Peaking | 3487 Hz  | 3.5  | 6.0 dB  |
| Peaking | 4117 Hz  | 4.92 | -8.2 dB |
| Peaking | 6001 Hz  | 4.54 | 4.9 dB  |
| Peaking | 7115 Hz  | 5.12 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH250/Sennheiser%20EH250.png)