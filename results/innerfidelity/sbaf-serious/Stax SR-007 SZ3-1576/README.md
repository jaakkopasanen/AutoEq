# Stax SR-007 SZ3-1576

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.0; 37 4.5; 40 4.1; 42 3.9; 45 3.8; 49 4.0; 52 4.4; 56 4.8; 59 4.9; 64 4.4; 68 3.4; 73 2.4; 78 2.4; 83 2.8; 89 3.1; 95 3.1; 102 3.1; 109 3.2; 117 3.2; 125 3.2; 134 3.2; 143 3.2; 153 3.2; 164 3.1; 175 3.0; 188 3.0; 201 3.0; 215 3.0; 230 3.0; 246 2.9; 263 2.9; 282 2.9; 301 2.8; 323 2.7; 345 2.7; 369 2.6; 395 2.5; 423 2.5; 452 2.3; 484 2.2; 518 3.0; 554 4.4; 593 3.4; 635 2.5; 679 1.9; 726 1.5; 777 1.2; 832 0.6; 890 0.1; 952 -0.0; 1019 0.3; 1090 0.5; 1167 1.1; 1248 3.4; 1336 5.0; 1429 4.1; 1529 0.8; 1636 -0.0; 1751 1.0; 1873 3.0; 2004 4.2; 2145 4.7; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.2; 4830 3.8; 5168 4.3; 5530 5.8; 5917 5.7; 6331 4.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 SZ3-1576 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.25 | 6.3 dB  |
| Peaking | 221 Hz  | 0.57 | 2.7 dB  |
| Peaking | 563 Hz  | 5.48 | 2.9 dB  |
| Peaking | 3084 Hz | 1.02 | 6.5 dB  |
| Peaking | 5805 Hz | 4.44 | 3.9 dB  |
| Peaking | 1046 Hz | 2.14 | -2.9 dB |
| Peaking | 1354 Hz | 5.89 | 4.0 dB  |
| Peaking | 1370 Hz | 1.06 | 2.1 dB  |
| Peaking | 1618 Hz | 4.77 | -4.7 dB |
| Peaking | 8671 Hz | 2.89 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007%20SZ3-1576/Stax%20SR-007%20SZ3-1576.png)