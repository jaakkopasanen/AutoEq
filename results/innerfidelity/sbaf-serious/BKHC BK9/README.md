# BKHC BK9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.2; 22 3.6; 23 3.4; 25 3.0; 26 2.8; 28 2.5; 30 2.3; 32 2.1; 35 1.8; 37 1.6; 40 1.4; 42 1.3; 45 1.2; 49 1.0; 52 0.9; 56 0.8; 59 0.7; 64 0.6; 68 0.5; 73 0.4; 78 0.2; 83 0.1; 89 0.2; 95 0.2; 102 -0.2; 109 -0.4; 117 -0.3; 125 0.4; 134 0.4; 143 0.2; 153 0.1; 164 -0.2; 175 0.1; 188 -0.1; 201 -0.2; 215 -0.7; 230 -1.0; 246 -1.2; 263 -1.4; 282 -1.4; 301 -1.4; 323 -1.5; 345 -1.7; 369 -2.0; 395 -2.3; 423 -2.4; 452 -2.6; 484 -2.9; 518 -3.2; 554 -3.1; 593 -3.0; 635 -3.0; 679 -3.1; 726 -2.7; 777 -2.0; 832 -1.0; 890 -0.4; 952 -0.2; 1019 0.3; 1090 1.2; 1167 2.3; 1248 3.3; 1336 4.2; 1429 4.9; 1529 5.6; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BKHC BK9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.79 | 4.3 dB  |
| Peaking | 31 Hz   | 0.08 | 0.2 dB  |
| Peaking | 666 Hz  | 0.72 | -5.3 dB |
| Peaking | 1869 Hz | 0.61 | 7.4 dB  |
| Peaking | 5106 Hz | 1.84 | 4.5 dB  |
| Peaking | 2260 Hz | 2.73 | -1.0 dB |
| Peaking | 3987 Hz | 0.83 | 1.3 dB  |
| Peaking | 4873 Hz | 3.85 | -1.2 dB |
| Peaking | 6401 Hz | 4.07 | 3.7 dB  |
| Peaking | 7321 Hz | 1.42 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BKHC%20BK9/BKHC%20BK9.png)