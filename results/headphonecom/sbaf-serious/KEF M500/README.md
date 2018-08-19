# KEF M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.0; 22 -4.9; 23 -4.9; 25 -4.9; 26 -4.9; 28 -4.9; 30 -4.9; 32 -4.9; 35 -4.9; 37 -4.8; 40 -4.8; 42 -4.8; 45 -4.8; 49 -4.9; 52 -4.9; 56 -4.9; 59 -4.9; 64 -5.0; 68 -5.2; 73 -5.3; 78 -5.5; 83 -5.5; 89 -5.4; 95 -5.3; 102 -5.5; 109 -5.7; 117 -5.7; 125 -6.2; 134 -6.7; 143 -7.0; 153 -7.2; 164 -7.0; 175 -7.2; 188 -7.0; 201 -6.9; 215 -7.0; 230 -7.1; 246 -6.8; 263 -6.4; 282 -5.7; 301 -4.9; 323 -3.8; 345 -2.8; 369 -2.2; 395 -2.1; 423 -2.1; 452 -2.3; 484 -2.6; 518 -3.0; 554 -3.2; 593 -3.3; 635 -3.1; 679 -2.8; 726 -2.4; 777 -1.9; 832 -1.3; 890 -0.8; 952 -0.3; 1019 0.2; 1090 0.7; 1167 1.2; 1248 1.3; 1336 1.2; 1429 1.1; 1529 1.2; 1636 1.1; 1751 1.4; 1873 1.4; 2004 1.4; 2145 1.4; 2295 1.4; 2455 1.3; 2627 1.0; 2811 0.8; 3008 0.7; 3219 0.3; 3444 0.4; 3685 1.1; 3943 1.8; 4219 3.3; 4514 4.3; 4830 5.3; 5168 5.4; 5530 5.8; 5917 5.9; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0725486821010906dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.18 | -4.8 dB |
| Peaking | 200 Hz  | 0.98 | -5.3 dB |
| Peaking | 651 Hz  | 2.23 | -2.7 dB |
| Peaking | 1456 Hz | 1.02 | 1.7 dB  |
| Peaking | 5448 Hz | 2.33 | 6.4 dB  |
| Peaking | 274 Hz  | 5.07 | -1.0 dB |
| Peaking | 367 Hz  | 4.61 | 1.1 dB  |
| Peaking | 3338 Hz | 8.93 | -1.0 dB |
| Peaking | 6588 Hz | 6.24 | 2.2 dB  |
| Peaking | 7771 Hz | 2.49 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KEF%20M500/KEF%20M500.png)