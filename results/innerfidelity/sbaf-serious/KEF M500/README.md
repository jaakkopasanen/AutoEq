# KEF M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.0; 22 -3.0; 23 -3.0; 25 -3.1; 26 -3.1; 28 -3.1; 30 -3.1; 32 -3.1; 35 -3.1; 37 -3.1; 40 -3.1; 42 -3.1; 45 -3.1; 49 -3.0; 52 -3.0; 56 -3.1; 59 -3.2; 64 -3.4; 68 -3.4; 73 -3.6; 78 -3.7; 83 -3.8; 89 -3.7; 95 -3.8; 102 -3.9; 109 -4.2; 117 -4.5; 125 -5.0; 134 -5.4; 143 -5.6; 153 -5.5; 164 -5.1; 175 -5.3; 188 -5.2; 201 -5.0; 215 -4.8; 230 -5.1; 246 -4.4; 263 -3.8; 282 -3.2; 301 -2.6; 323 -2.0; 345 -1.3; 369 -1.2; 395 -1.0; 423 -0.8; 452 -1.3; 484 -2.1; 518 -2.7; 554 -2.7; 593 -2.4; 635 -2.4; 679 -2.3; 726 -2.0; 777 -1.7; 832 -1.2; 890 -0.8; 952 -0.2; 1019 0.2; 1090 0.7; 1167 1.1; 1248 1.1; 1336 1.1; 1429 0.9; 1529 0.9; 1636 0.7; 1751 1.0; 1873 0.8; 2004 0.7; 2145 0.4; 2295 -0.0; 2455 -0.2; 2627 -0.8; 2811 -1.4; 3008 -1.7; 3219 -2.2; 3444 -1.9; 3685 -1.0; 3943 0.3; 4219 1.2; 4514 2.3; 4830 3.5; 5168 4.2; 5530 5.7; 5917 5.6; 6331 3.9; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.072548682101091dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.23 | -2.9 dB |
| Peaking | 175 Hz  | 0.98 | -4.5 dB |
| Peaking | 613 Hz  | 3.01 | -2.3 dB |
| Peaking | 3270 Hz | 4.21 | -3.0 dB |
| Peaking | 5613 Hz | 2.77 | 6.0 dB  |
| Peaking | 242 Hz  | 6.8  | -0.9 dB |
| Peaking | 381 Hz  | 4.72 | 0.8 dB  |
| Peaking | 802 Hz  | 2.75 | -1.1 dB |
| Peaking | 1266 Hz | 1.51 | 1.5 dB  |
| Peaking | 8344 Hz | 4.16 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M500/KEF%20M500.png)