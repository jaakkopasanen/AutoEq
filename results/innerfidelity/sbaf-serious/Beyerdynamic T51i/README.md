# Beyerdynamic T51i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 0.6; 22 -0.1; 23 -0.4; 25 -0.9; 26 -1.1; 28 -1.6; 30 -2.0; 32 -2.4; 35 -2.8; 37 -3.1; 40 -3.5; 42 -3.7; 45 -3.9; 49 -4.3; 52 -4.7; 56 -5.1; 59 -5.4; 64 -5.7; 68 -5.9; 73 -6.2; 78 -6.4; 83 -6.6; 89 -6.7; 95 -6.9; 102 -7.2; 109 -7.6; 117 -7.7; 125 -7.5; 134 -7.5; 143 -7.8; 153 -7.7; 164 -7.0; 175 -7.0; 188 -6.5; 201 -5.9; 215 -5.3; 230 -4.6; 246 -4.0; 263 -3.4; 282 -2.8; 301 -2.5; 323 -2.6; 345 -2.8; 369 -3.2; 395 -3.4; 423 -3.3; 452 -3.1; 484 -3.0; 518 -2.9; 554 -2.5; 593 -2.1; 635 -1.9; 679 -1.8; 726 -1.6; 777 -0.7; 832 -0.2; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.6; 1248 0.9; 1336 1.0; 1429 1.2; 1529 1.5; 1636 2.0; 1751 2.9; 1873 4.0; 2004 4.8; 2145 4.4; 2295 2.9; 2455 1.8; 2627 1.5; 2811 2.2; 3008 3.4; 3219 4.5; 3444 5.4; 3685 5.5; 3943 5.5; 4219 4.4; 4514 2.4; 4830 1.8; 5168 3.4; 5530 5.1; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -3.7; 9502 -4.5; 10167 -1.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.018036382676667dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T51i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 1.61 | -0.7 dB |
| Peaking | 122 Hz  | 0.47 | -7.4 dB |
| Peaking | 1972 Hz | 2.95 | 4.5 dB  |
| Peaking | 3658 Hz | 3.03 | 5.7 dB  |
| Peaking | 6037 Hz | 4.84 | 6.2 dB  |
| Peaking | 288 Hz  | 2.16 | 2.7 dB  |
| Peaking | 653 Hz  | 0.48 | -2.7 dB |
| Peaking | 972 Hz  | 0.91 | 2.7 dB  |
| Peaking | 8510 Hz | 1.05 | 1.3 dB  |
| Peaking | 9208 Hz | 3.87 | -6.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T51i/Beyerdynamic%20T51i.png)