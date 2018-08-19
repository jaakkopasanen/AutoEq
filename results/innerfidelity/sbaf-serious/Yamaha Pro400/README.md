# Yamaha Pro400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.3; 22 1.6; 23 1.4; 25 0.9; 26 0.7; 28 0.3; 30 0.1; 32 -0.2; 35 -0.4; 37 -0.6; 40 -0.7; 42 -0.8; 45 -0.9; 49 -1.1; 52 -1.2; 56 -1.4; 59 -1.4; 64 -1.0; 68 0.3; 73 2.2; 78 0.9; 83 -1.6; 89 -2.9; 95 -3.2; 102 -0.7; 109 -0.4; 117 -2.7; 125 -3.9; 134 -4.5; 143 -4.8; 153 -4.8; 164 -3.0; 175 -3.5; 188 -3.3; 201 -1.9; 215 -0.1; 230 2.3; 246 4.6; 263 5.9; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 5.9; 423 5.4; 452 4.8; 484 3.7; 518 3.1; 554 2.6; 593 2.0; 635 1.3; 679 0.6; 726 0.0; 777 -0.2; 832 -0.4; 890 -0.5; 952 -0.3; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.1; 1336 1.1; 1429 1.0; 1529 0.6; 1636 0.6; 1751 1.0; 1873 1.8; 2004 2.6; 2145 3.3; 2295 4.0; 2455 4.9; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.5; 3685 4.7; 3943 4.8; 4219 5.4; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.83 | 2.0 dB  |
| Peaking | 164 Hz  | 1.28 | -7.0 dB |
| Peaking | 303 Hz  | 1.21 | 8.7 dB  |
| Peaking | 2895 Hz | 1.84 | 5.7 dB  |
| Peaking | 5306 Hz | 2.06 | 5.9 dB  |
| Peaking | 35 Hz   | 0.58 | 1.0 dB  |
| Peaking | 45 Hz   | 1.69 | -1.9 dB |
| Peaking | 445 Hz  | 4.85 | 1.3 dB  |
| Peaking | 822 Hz  | 2.75 | -1.7 dB |
| Peaking | 8356 Hz | 4.33 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro400/Yamaha%20Pro400.png)