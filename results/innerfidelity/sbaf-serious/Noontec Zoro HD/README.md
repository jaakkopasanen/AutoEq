# Noontec Zoro HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.7; 22 -3.8; 23 -3.9; 25 -4.0; 26 -4.1; 28 -4.2; 30 -4.3; 32 -4.3; 35 -4.5; 37 -4.5; 40 -4.6; 42 -4.6; 45 -4.7; 49 -4.8; 52 -4.9; 56 -5.0; 59 -5.0; 64 -5.2; 68 -5.4; 73 -5.6; 78 -5.8; 83 -5.9; 89 -6.1; 95 -6.3; 102 -6.5; 109 -6.6; 117 -6.8; 125 -6.8; 134 -6.7; 143 -6.6; 153 -6.7; 164 -6.8; 175 -6.3; 188 -6.5; 201 -6.6; 215 -6.4; 230 -6.0; 246 -5.6; 263 -5.2; 282 -4.7; 301 -4.5; 323 -4.4; 345 -3.9; 369 -3.6; 395 -3.3; 423 -2.8; 452 -2.6; 484 -2.6; 518 -2.1; 554 -1.7; 593 -1.5; 635 -1.2; 679 -1.1; 726 -0.8; 777 -0.6; 832 -0.4; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.1; 1336 0.9; 1429 0.9; 1529 0.7; 1636 0.7; 1751 0.9; 1873 1.3; 2004 1.5; 2145 1.6; 2295 1.7; 2455 2.4; 2627 2.8; 2811 3.1; 3008 2.5; 3219 1.8; 3444 2.4; 3685 3.5; 3943 5.4; 4219 6.0; 4514 6.0; 4830 5.9; 5168 4.5; 5530 5.3; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099996068419182dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.3  | -3.8 dB |
| Peaking | 126 Hz  | 0.73 | -3.8 dB |
| Peaking | 252 Hz  | 0.83 | -3.3 dB |
| Peaking | 4323 Hz | 1.38 | 5.4 dB  |
| Peaking | 6105 Hz | 5.29 | 3.6 dB  |
| Peaking | 1253 Hz | 3.86 | 1.1 dB  |
| Peaking | 2743 Hz | 2.03 | 2.0 dB  |
| Peaking | 3421 Hz | 3.27 | -3.6 dB |
| Peaking | 4017 Hz | 2.07 | 1.1 dB  |
| Peaking | 8349 Hz | 2.7  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20HD/Noontec%20Zoro%20HD.png)