# Fostex T40RP Mk3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.3; 49 4.5; 52 3.9; 56 3.3; 59 2.8; 64 2.2; 68 1.7; 73 1.3; 78 0.9; 83 0.6; 89 0.3; 95 0.2; 102 0.0; 109 -0.0; 117 -0.1; 125 -0.2; 134 -0.3; 143 -0.3; 153 -0.3; 164 -0.1; 175 0.2; 188 0.4; 201 0.5; 215 0.7; 230 0.7; 246 0.7; 263 0.8; 282 0.4; 301 0.2; 323 0.0; 345 0.1; 369 0.6; 395 0.5; 423 1.1; 452 1.2; 484 -0.0; 518 -0.6; 554 -0.6; 593 -0.8; 635 -0.8; 679 -0.8; 726 -1.3; 777 -1.2; 832 -0.5; 890 -0.5; 952 -0.3; 1019 0.1; 1090 0.2; 1167 0.4; 1248 1.2; 1336 1.1; 1429 1.4; 1529 1.3; 1636 1.1; 1751 1.0; 1873 0.4; 2004 1.0; 2145 1.7; 2295 1.4; 2455 1.5; 2627 1.7; 2811 1.9; 3008 1.5; 3219 1.1; 3444 0.1; 3685 -0.1; 3943 -1.4; 4219 -2.4; 4514 -2.0; 4830 -0.7; 5168 2.8; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.9; 9502 -3.9; 10167 -2.2; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T40RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.94 | 6.9 dB  |
| Peaking | 2714 Hz | 1.12 | 2.0 dB  |
| Peaking | 4452 Hz | 2.62 | -5.7 dB |
| Peaking | 5809 Hz | 2.56 | 7.9 dB  |
| Peaking | 9293 Hz | 4.26 | -4.9 dB |
| Peaking | 120 Hz  | 1.43 | -1.0 dB |
| Peaking | 234 Hz  | 2.09 | 1.0 dB  |
| Peaking | 437 Hz  | 5.41 | 1.9 dB  |
| Peaking | 676 Hz  | 1    | -1.2 dB |
| Peaking | 1330 Hz | 3.12 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T40RP%20Mk3/Fostex%20T40RP%20Mk3.png)