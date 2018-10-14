# Yamaha HP1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.6; 22 5.2; 23 5.0; 25 4.6; 26 4.4; 28 4.0; 30 3.7; 32 3.5; 35 3.2; 37 3.0; 40 2.8; 42 2.7; 45 2.5; 49 2.3; 52 2.1; 56 1.9; 59 1.8; 64 1.6; 68 1.5; 73 1.3; 78 1.1; 83 1.0; 89 0.8; 95 0.5; 102 0.2; 109 0.1; 117 -0.1; 125 -0.4; 134 -0.5; 143 -0.7; 153 -0.8; 164 -0.9; 175 -0.9; 188 -1.1; 201 -1.2; 215 -1.2; 230 -1.1; 246 -1.2; 263 -1.1; 282 -0.9; 301 -0.9; 323 -1.0; 345 -0.9; 369 -0.9; 395 -1.0; 423 -0.9; 452 -0.8; 484 -1.0; 518 -1.1; 554 -1.0; 593 -0.8; 635 -0.8; 679 -1.0; 726 -0.9; 777 -0.6; 832 -0.5; 890 -0.3; 952 -0.1; 1019 0.2; 1090 0.7; 1167 1.4; 1248 2.3; 1336 2.7; 1429 2.9; 1529 2.8; 1636 3.2; 1751 3.4; 1873 3.1; 2004 2.3; 2145 1.2; 2295 0.5; 2455 1.4; 2627 1.3; 2811 1.9; 3008 3.1; 3219 4.2; 3444 5.2; 3685 5.4; 3943 4.7; 4219 3.8; 4514 3.8; 4830 4.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.21 | 5.2 dB  |
| Peaking | 50 Hz   | 1.85 | 1.5 dB  |
| Peaking | 1605 Hz | 2.63 | 3.4 dB  |
| Peaking | 3575 Hz | 3.05 | 4.7 dB  |
| Peaking | 5652 Hz | 2.78 | 6.2 dB  |
| Peaking | 79 Hz   | 1.89 | 0.8 dB  |
| Peaking | 204 Hz  | 0.78 | -1.2 dB |
| Peaking | 645 Hz  | 0.94 | -0.9 dB |
| Peaking | 1256 Hz | 5.46 | 1.4 dB  |
| Peaking | 8251 Hz | 4.76 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1/Yamaha%20HP1.png)