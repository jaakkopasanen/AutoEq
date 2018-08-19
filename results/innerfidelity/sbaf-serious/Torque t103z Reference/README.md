# Torque t103z Reference

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.3; 52 4.8; 56 4.3; 59 3.9; 64 3.2; 68 2.7; 73 2.1; 78 1.5; 83 0.9; 89 0.3; 95 -0.3; 102 -0.8; 109 -1.3; 117 -1.8; 125 -2.4; 134 -3.0; 143 -3.5; 153 -4.0; 164 -4.6; 175 -5.0; 188 -5.6; 201 -6.1; 215 -6.4; 230 -6.8; 246 -7.2; 263 -7.5; 282 -7.6; 301 -7.7; 323 -7.6; 345 -7.3; 369 -7.0; 395 -6.5; 423 -5.7; 452 -5.2; 484 -4.5; 518 -3.9; 554 -3.2; 593 -2.4; 635 -2.0; 679 -1.0; 726 -0.2; 777 -0.0; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.1; 1751 -2.4; 1873 -2.5; 2004 -2.4; 2145 -2.0; 2295 -0.9; 2455 1.0; 2627 3.0; 2811 5.1; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.61 | 6.9 dB  |
| Peaking | 271 Hz  | 0.73 | -8.3 dB |
| Peaking | 2042 Hz | 1.56 | -9.7 dB |
| Peaking | 3024 Hz | 0.68 | 9.6 dB  |
| Peaking | 428 Hz  | 2.71 | -0.8 dB |
| Peaking | 775 Hz  | 2.73 | 1.5 dB  |
| Peaking | 1465 Hz | 5.53 | -0.8 dB |
| Peaking | 6212 Hz | 2.26 | 6.0 dB  |
| Peaking | 7254 Hz | 1.32 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Reference/Torque%20t103z%20Reference.png)