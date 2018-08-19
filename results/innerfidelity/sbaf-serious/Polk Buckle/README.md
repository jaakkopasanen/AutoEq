# Polk Buckle

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -6.8; 22 -6.9; 23 -6.9; 25 -7.0; 26 -7.0; 28 -7.0; 30 -7.0; 32 -6.9; 35 -6.8; 37 -6.7; 40 -6.6; 42 -6.5; 45 -6.4; 49 -6.1; 52 -6.0; 56 -5.8; 59 -5.6; 64 -5.3; 68 -5.0; 73 -4.5; 78 -4.1; 83 -4.0; 89 -4.3; 95 -4.7; 102 -5.1; 109 -5.1; 117 -5.0; 125 -4.9; 134 -4.9; 143 -4.8; 153 -4.7; 164 -4.0; 175 -4.0; 188 -4.2; 201 -4.3; 215 -4.1; 230 -4.0; 246 -3.9; 263 -3.5; 282 -2.4; 301 -1.3; 323 -1.2; 345 -0.7; 369 -0.2; 395 -0.1; 423 0.2; 452 0.3; 484 0.6; 518 0.8; 554 1.2; 593 1.3; 635 1.6; 679 1.7; 726 1.3; 777 0.8; 832 0.1; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.2; 1167 0.6; 1248 1.1; 1336 1.4; 1429 1.6; 1529 1.9; 1636 2.3; 1751 2.7; 1873 3.3; 2004 3.8; 2145 4.2; 2295 4.5; 2455 4.9; 2627 5.4; 2811 5.3; 3008 4.8; 3219 4.5; 3444 4.9; 3685 5.8; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999571206119dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Buckle ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.51 | -5.1 dB |
| Peaking | 50 Hz   | 0.48 | -3.2 dB |
| Peaking | 168 Hz  | 1.07 | -3.5 dB |
| Peaking | 2791 Hz | 0.92 | 4.8 dB  |
| Peaking | 5294 Hz | 2.09 | 4.9 dB  |
| Peaking | 250 Hz  | 6.29 | -1.5 dB |
| Peaking | 566 Hz  | 2.23 | 1.6 dB  |
| Peaking | 4073 Hz | 4.59 | 1.7 dB  |
| Peaking | 6410 Hz | 3.95 | 4.5 dB  |
| Peaking | 6661 Hz | 1.29 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Buckle/Polk%20Buckle.png)