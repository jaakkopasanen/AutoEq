# Ortofon 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.9; 102 5.8; 109 5.8; 117 5.8; 125 5.4; 134 5.1; 143 5.0; 153 4.9; 164 5.1; 175 5.3; 188 5.1; 201 4.6; 215 4.8; 230 4.2; 246 3.3; 263 2.6; 282 1.4; 301 0.3; 323 -0.8; 345 -1.6; 369 -1.8; 395 -1.7; 423 -1.2; 452 -1.0; 484 -0.9; 518 -0.8; 554 -0.5; 593 -0.2; 635 0.1; 679 0.1; 726 0.2; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 0.6; 1336 0.4; 1429 0.5; 1529 0.4; 1636 -0.2; 1751 -1.2; 1873 -0.9; 2004 -0.5; 2145 0.2; 2295 1.0; 2455 2.1; 2627 3.0; 2811 3.6; 3008 3.3; 3219 2.6; 3444 3.6; 3685 4.1; 3943 3.3; 4219 4.8; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.2; 9502 -3.7; 10167 -4.0; 10879 -2.4; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.38 | 6.6 dB  |
| Peaking | 170 Hz  | 1.76 | 3.3 dB  |
| Peaking | 5988 Hz | 3.35 | 3.5 dB  |
| Peaking | 4479 Hz | 1.3  | 5.0 dB  |
| Peaking | 9851 Hz | 3.64 | -5.2 dB |
| Peaking | 23 Hz   | 2.58 | 1.2 dB  |
| Peaking | 237 Hz  | 3.08 | 2.0 dB  |
| Peaking | 365 Hz  | 1.99 | -3.1 dB |
| Peaking | 1862 Hz | 4.75 | -1.9 dB |
| Peaking | 2730 Hz | 5.91 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%202/Ortofon%202.png)