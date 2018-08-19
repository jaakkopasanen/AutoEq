# Denon AH-D1001

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.4; 52 5.1; 56 4.9; 59 4.9; 64 4.7; 68 4.3; 73 3.9; 78 3.5; 83 3.0; 89 2.6; 95 2.2; 102 1.9; 109 1.7; 117 1.6; 125 1.3; 134 1.1; 143 1.1; 153 1.1; 164 1.1; 175 1.2; 188 1.2; 201 1.3; 215 1.5; 230 1.8; 246 2.0; 263 2.3; 282 2.6; 301 2.9; 323 3.2; 345 3.4; 369 3.6; 395 3.8; 423 4.1; 452 4.2; 484 4.1; 518 3.9; 554 3.8; 593 3.4; 635 2.7; 679 1.7; 726 0.9; 777 0.5; 832 0.1; 890 -0.2; 952 0.0; 1019 0.1; 1090 0.5; 1167 0.8; 1248 1.2; 1336 1.3; 1429 1.4; 1529 1.6; 1636 1.9; 1751 2.5; 1873 3.3; 2004 4.0; 2145 4.2; 2295 4.1; 2455 3.6; 2627 2.7; 2811 2.3; 3008 4.3; 3219 4.8; 3444 2.9; 3685 1.4; 3943 0.9; 4219 -0.3; 4514 -0.5; 4830 0.8; 5168 3.0; 5530 4.1; 5917 4.7; 6331 3.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -2.2; 10167 -1.7; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.52 | 6.4 dB  |
| Peaking | 431 Hz  | 1.34 | 4.3 dB  |
| Peaking | 2125 Hz | 2.56 | 4.2 dB  |
| Peaking | 3169 Hz | 6.36 | 4.1 dB  |
| Peaking | 5941 Hz | 4.22 | 4.9 dB  |
| Peaking | 587 Hz  | 5.75 | 1.1 dB  |
| Peaking | 858 Hz  | 3.42 | -1.3 dB |
| Peaking | 4468 Hz | 6.05 | -2.4 dB |
| Peaking | 5610 Hz | 0.86 | 0.7 dB  |
| Peaking | 9439 Hz | 4.54 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1001/Denon%20AH-D1001.png)