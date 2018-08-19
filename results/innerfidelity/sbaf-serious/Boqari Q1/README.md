# Boqari Q1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.6; 64 5.2; 68 4.8; 73 4.4; 78 3.9; 83 3.5; 89 3.0; 95 2.6; 102 2.2; 109 1.9; 117 1.6; 125 1.1; 134 0.8; 143 0.5; 153 0.1; 164 -0.2; 175 -0.5; 188 -0.8; 201 -1.1; 215 -1.4; 230 -1.6; 246 -1.9; 263 -2.2; 282 -2.3; 301 -2.6; 323 -2.8; 345 -3.0; 369 -3.1; 395 -3.3; 423 -3.2; 452 -3.1; 484 -2.8; 518 -2.8; 554 -2.3; 593 -2.0; 635 -1.7; 679 -1.5; 726 -1.2; 777 -0.8; 832 -0.5; 890 0.0; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.3; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.0; 1636 -0.9; 1751 -0.4; 1873 0.2; 2004 1.0; 2145 1.9; 2295 2.7; 2455 3.8; 2627 4.9; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.1; 4514 0.3; 4830 -2.2; 5168 -2.2; 5530 0.8; 5917 4.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Boqari Q1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.41 | 6.5 dB  |
| Peaking | 349 Hz  | 0.63 | -3.4 dB |
| Peaking | 3346 Hz | 1.69 | 7.2 dB  |
| Peaking | 4974 Hz | 4.53 | -6.0 dB |
| Peaking | 6198 Hz | 5.33 | 6.1 dB  |
| Peaking | 922 Hz  | 3.53 | 1.2 dB  |
| Peaking | 1597 Hz | 2.62 | -1.6 dB |
| Peaking | 2560 Hz | 5.21 | 1.3 dB  |
| Peaking | 6789 Hz | 8.11 | 1.4 dB  |
| Peaking | 7758 Hz | 2.37 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Boqari%20Q1/Boqari%20Q1.png)