# KEF M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.0; 22 -3.0; 23 -3.0; 25 -3.1; 26 -3.1; 28 -3.1; 30 -3.1; 32 -3.1; 35 -3.0; 37 -3.0; 40 -3.0; 42 -3.0; 45 -2.9; 49 -2.8; 52 -2.7; 56 -2.7; 59 -2.8; 64 -2.9; 68 -2.8; 73 -2.9; 78 -2.9; 83 -3.0; 89 -2.9; 95 -3.0; 102 -3.4; 109 -3.8; 117 -4.3; 125 -5.0; 134 -5.6; 143 -5.8; 153 -5.7; 164 -5.4; 175 -5.6; 188 -5.4; 201 -5.2; 215 -5.0; 230 -5.3; 246 -4.5; 263 -3.9; 282 -3.3; 301 -2.7; 323 -2.0; 345 -1.4; 369 -1.2; 395 -1.0; 423 -0.8; 452 -1.3; 484 -2.1; 518 -2.7; 554 -2.7; 593 -2.4; 635 -2.4; 679 -2.3; 726 -2.0; 777 -1.7; 832 -1.2; 890 -0.8; 952 -0.2; 1019 0.2; 1090 0.7; 1167 1.1; 1248 1.1; 1336 1.1; 1429 0.9; 1529 0.9; 1636 0.7; 1751 1.0; 1873 0.8; 2004 0.7; 2145 0.4; 2295 -0.0; 2455 -0.2; 2627 -0.8; 2811 -1.4; 3008 -1.7; 3219 -2.2; 3444 -1.9; 3685 -1.0; 3943 0.3; 4219 1.2; 4514 2.3; 4830 3.5; 5168 4.2; 5530 5.7; 5917 5.6; 6331 3.9; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.36 | -2.9 dB |
| Peaking | 172 Hz  | 0.99 | -5.5 dB |
| Peaking | 611 Hz  | 2.97 | -2.3 dB |
| Peaking | 3270 Hz | 4.21 | -3.0 dB |
| Peaking | 5613 Hz | 2.77 | 6.0 dB  |
| Peaking | 243 Hz  | 6.02 | -0.9 dB |
| Peaking | 382 Hz  | 4.82 | 0.8 dB  |
| Peaking | 803 Hz  | 2.82 | -1.1 dB |
| Peaking | 1274 Hz | 1.52 | 1.5 dB  |
| Peaking | 8368 Hz | 4.17 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M500/KEF%20M500.png)