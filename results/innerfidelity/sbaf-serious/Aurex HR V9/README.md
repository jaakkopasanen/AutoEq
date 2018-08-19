# Aurex HR V9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.5; 52 5.2; 56 5.0; 59 4.8; 64 4.6; 68 4.4; 73 4.2; 78 3.9; 83 3.7; 89 3.5; 95 3.4; 102 3.0; 109 2.5; 117 2.2; 125 2.0; 134 1.8; 143 1.7; 153 1.6; 164 1.6; 175 1.4; 188 1.3; 201 1.3; 215 1.3; 230 1.3; 246 1.2; 263 1.3; 282 1.4; 301 1.4; 323 1.3; 345 1.4; 369 1.3; 395 1.2; 423 1.4; 452 1.4; 484 1.2; 518 1.1; 554 1.2; 593 1.4; 635 1.3; 679 1.1; 726 1.0; 777 1.0; 832 0.5; 890 0.1; 952 -0.1; 1019 0.1; 1090 0.1; 1167 0.4; 1248 1.0; 1336 1.3; 1429 1.7; 1529 2.2; 1636 2.5; 1751 3.1; 1873 2.8; 2004 1.6; 2145 0.5; 2295 0.1; 2455 0.8; 2627 1.6; 2811 2.2; 3008 3.3; 3219 3.7; 3444 4.0; 3685 4.4; 3943 4.3; 4219 3.7; 4514 3.4; 4830 3.9; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurex HR V9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.31 | 6.0 dB  |
| Peaking | 143 Hz  | 1.23 | -0.9 dB |
| Peaking | 546 Hz  | 0.16 | 1.0 dB  |
| Peaking | 3636 Hz | 2.24 | 3.6 dB  |
| Peaking | 5804 Hz | 3.29 | 5.8 dB  |
| Peaking | 1026 Hz | 2.84 | -1.5 dB |
| Peaking | 1871 Hz | 1.94 | 2.9 dB  |
| Peaking | 2232 Hz | 3.76 | -3.3 dB |
| Peaking | 8270 Hz | 4.17 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurex%20HR%20V9/Aurex%20HR%20V9.png)