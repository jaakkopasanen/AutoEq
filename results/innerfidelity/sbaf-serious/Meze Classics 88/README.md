# Meze Classics 88

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.7; 22 4.5; 23 4.4; 25 4.2; 26 4.1; 28 4.0; 30 3.8; 32 3.7; 35 3.6; 37 3.5; 40 3.4; 42 3.4; 45 3.3; 49 3.2; 52 3.1; 56 3.1; 59 3.0; 64 2.9; 68 2.8; 73 2.8; 78 2.6; 83 2.2; 89 1.7; 95 1.3; 102 1.4; 109 1.2; 117 0.9; 125 0.5; 134 0.3; 143 0.3; 153 0.1; 164 0.3; 175 0.2; 188 0.0; 201 0.0; 215 0.1; 230 0.3; 246 0.6; 263 0.9; 282 1.2; 301 1.2; 323 1.2; 345 1.4; 369 1.7; 395 1.9; 423 2.7; 452 3.6; 484 4.6; 518 5.7; 554 6.0; 593 6.0; 635 5.4; 679 4.1; 726 3.1; 777 2.3; 832 1.4; 890 0.7; 952 -0.0; 1019 0.3; 1090 -0.1; 1167 -1.3; 1248 -1.7; 1336 -2.0; 1429 -1.8; 1529 -1.2; 1636 -0.2; 1751 1.3; 1873 2.9; 2004 4.3; 2145 5.6; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 88 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.64 | 4.3 dB  |
| Peaking | 65 Hz   | 1.57 | 1.9 dB  |
| Peaking | 562 Hz  | 2.13 | 6.1 dB  |
| Peaking | 1373 Hz | 1.87 | -5.6 dB |
| Peaking | 3113 Hz | 0.63 | 7.2 dB  |
| Peaking | 1673 Hz | 6.78 | -0.8 dB |
| Peaking | 2174 Hz | 3.8  | 1.5 dB  |
| Peaking | 3181 Hz | 2.25 | -1.1 dB |
| Peaking | 6216 Hz | 2.07 | 5.6 dB  |
| Peaking | 7461 Hz | 1.43 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2088/Meze%20Classics%2088.png)