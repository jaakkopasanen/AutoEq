# Westone UM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.5; 52 5.2; 56 4.8; 59 4.6; 64 4.2; 68 3.8; 73 3.5; 78 3.1; 83 2.7; 89 2.3; 95 2.0; 102 1.6; 109 1.4; 117 1.2; 125 0.8; 134 0.6; 143 0.4; 153 0.2; 164 0.1; 175 -0.0; 188 -0.1; 201 -0.3; 215 -0.3; 230 -0.3; 246 -0.4; 263 -0.4; 282 -0.4; 301 -0.4; 323 -0.3; 345 -0.3; 369 -0.2; 395 -0.1; 423 0.1; 452 0.2; 484 0.1; 518 0.1; 554 0.3; 593 0.6; 635 0.7; 679 0.6; 726 0.7; 777 0.8; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.6; 1636 -1.7; 1751 -1.4; 1873 -1.0; 2004 -0.4; 2145 0.3; 2295 1.2; 2455 2.4; 2627 3.6; 2811 4.7; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 5.1; 4514 5.8; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.63 | 6.7 dB  |
| Peaking | 773 Hz  | 2.59 | 1.0 dB  |
| Peaking | 1742 Hz | 1.41 | -3.0 dB |
| Peaking | 3283 Hz | 1.45 | 6.5 dB  |
| Peaking | 5589 Hz | 2.64 | 5.1 dB  |
| Peaking | 21 Hz   | 0.35 | 2.0 dB  |
| Peaking | 31 Hz   | 1.49 | -2.5 dB |
| Peaking | 204 Hz  | 1.04 | -0.9 dB |
| Peaking | 6542 Hz | 7.16 | 2.3 dB  |
| Peaking | 7835 Hz | 2.22 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM1/Westone%20UM1.png)