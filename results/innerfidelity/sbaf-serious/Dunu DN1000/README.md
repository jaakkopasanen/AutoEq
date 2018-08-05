# Dunu DN1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.1; 23 -4.1; 25 -4.1; 26 -4.0; 28 -4.0; 30 -3.9; 32 -3.9; 35 -3.8; 37 -3.8; 40 -3.7; 42 -3.7; 45 -3.6; 49 -3.5; 52 -3.4; 56 -3.3; 59 -3.2; 64 -3.1; 68 -3.0; 73 -3.0; 78 -3.0; 83 -3.1; 89 -3.2; 95 -3.5; 102 -3.8; 109 -4.0; 117 -4.4; 125 -4.7; 134 -4.9; 143 -5.0; 153 -5.0; 164 -4.9; 175 -4.7; 188 -4.4; 201 -4.2; 215 -3.9; 230 -3.6; 246 -3.3; 263 -3.1; 282 -2.7; 301 -2.5; 323 -2.2; 345 -1.9; 369 -1.7; 395 -1.5; 423 -1.1; 452 -0.9; 484 -0.8; 518 -0.6; 554 -0.3; 593 0.1; 635 0.2; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.0; 1529 -1.2; 1636 -1.3; 1751 -1.1; 1873 -0.7; 2004 -0.3; 2145 0.1; 2295 0.7; 2455 1.7; 2627 2.2; 2811 2.8; 3008 3.9; 3219 5.4; 3444 6.0; 3685 6.0; 3943 5.7; 4219 2.1; 4514 -1.0; 4830 -1.3; 5168 0.8; 5530 1.6; 5917 1.6; 6331 1.8; 6775 1.7; 7249 0.7; 7756 -1.4; 8299 -4.5; 8880 -7.3; 9502 -8.2; 10167 -6.5; 10879 -2.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.83 | -3.2 dB |
| Peaking | 39 Hz   | 0.78 | -2.4 dB |
| Peaking | 159 Hz  | 0.81 | -4.7 dB |
| Peaking | 3478 Hz | 3.11 | 6.8 dB  |
| Peaking | 9399 Hz | 4.42 | -9.4 dB |
| Peaking | 750 Hz  | 2.3  | 0.9 dB  |
| Peaking | 1622 Hz | 2.45 | -1.7 dB |
| Peaking | 4674 Hz | 6.25 | -4.9 dB |
| Peaking | 6147 Hz | 1.06 | 2.5 dB  |
| Peaking | 8465 Hz | 5.32 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN1000/Dunu%20DN1000.png)