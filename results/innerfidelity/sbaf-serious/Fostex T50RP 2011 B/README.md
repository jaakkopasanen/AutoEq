# Fostex T50RP 2011 B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.4; 102 4.5; 109 3.9; 117 3.3; 125 2.6; 134 2.0; 143 1.6; 153 1.2; 164 1.2; 175 0.6; 188 0.3; 201 0.1; 215 -0.0; 230 -0.0; 246 -0.1; 263 -0.1; 282 -0.1; 301 -0.1; 323 -0.0; 345 0.5; 369 0.8; 395 0.5; 423 0.4; 452 0.3; 484 0.2; 518 0.4; 554 0.5; 593 0.6; 635 0.8; 679 0.4; 726 0.0; 777 0.4; 832 -0.0; 890 -0.7; 952 -0.3; 1019 0.2; 1090 0.3; 1167 0.0; 1248 -0.2; 1336 -0.4; 1429 -0.7; 1529 -1.2; 1636 -0.9; 1751 -0.4; 1873 0.3; 2004 1.1; 2145 2.3; 2295 3.6; 2455 5.1; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.24 | 6.8 dB  |
| Peaking | 189 Hz  | 0.88 | -3.9 dB |
| Peaking | 1526 Hz | 1.99 | -2.8 dB |
| Peaking | 1864 Hz | 4.94 | -1.3 dB |
| Peaking | 3622 Hz | 0.8  | 7.0 dB  |
| Peaking | 21 Hz   | 2.24 | 1.3 dB  |
| Peaking | 2614 Hz | 4.4  | 2.0 dB  |
| Peaking | 3412 Hz | 1.2  | -1.1 dB |
| Peaking | 6283 Hz | 2.16 | 5.7 dB  |
| Peaking | 7357 Hz | 1.5  | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20B/Fostex%20T50RP%202011%20B.png)