# Sony MDR-7550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.2; 22 4.9; 23 4.7; 25 4.5; 26 4.3; 28 4.1; 30 3.9; 32 3.8; 35 3.5; 37 3.4; 40 3.2; 42 3.1; 45 2.9; 49 2.7; 52 2.5; 56 2.3; 59 2.1; 64 1.8; 68 1.5; 73 1.2; 78 1.0; 83 0.7; 89 0.4; 95 0.1; 102 -0.2; 109 -0.3; 117 -0.5; 125 -0.8; 134 -1.0; 143 -1.2; 153 -1.4; 164 -1.5; 175 -1.6; 188 -1.7; 201 -1.7; 215 -1.7; 230 -1.7; 246 -1.7; 263 -1.7; 282 -1.5; 301 -1.5; 323 -1.3; 345 -1.2; 369 -1.1; 395 -0.9; 423 -0.7; 452 -0.5; 484 -0.4; 518 -0.3; 554 -0.0; 593 0.4; 635 0.5; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.4; 952 0.2; 1019 -0.0; 1090 0.0; 1167 -0.2; 1248 -0.9; 1336 -1.6; 1429 -2.4; 1529 -3.1; 1636 -3.5; 1751 -3.6; 1873 -3.2; 2004 -2.6; 2145 -1.6; 2295 -0.3; 2455 1.5; 2627 3.2; 2811 4.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.0; 4514 0.7; 4830 -2.1; 5168 -2.6; 5530 0.7; 5917 4.4; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999437614dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.39 | 4.8 dB  |
| Peaking | 47 Hz   | 2.1  | 2.2 dB  |
| Peaking | 1772 Hz | 2.31 | -4.6 dB |
| Peaking | 3242 Hz | 2.41 | 7.4 dB  |
| Peaking | 6363 Hz | 7.77 | 5.7 dB  |
| Peaking | 228 Hz  | 0.94 | -1.9 dB |
| Peaking | 758 Hz  | 2.03 | 1.2 dB  |
| Peaking | 4038 Hz | 6.79 | 3.7 dB  |
| Peaking | 5055 Hz | 3.95 | -5.4 dB |
| Peaking | 5799 Hz | 6.42 | 3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)