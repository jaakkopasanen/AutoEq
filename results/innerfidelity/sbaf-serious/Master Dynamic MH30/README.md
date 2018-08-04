# Master Dynamic MH30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.2; 23 -4.2; 25 -4.3; 26 -4.3; 28 -4.3; 30 -4.3; 32 -4.3; 35 -4.3; 37 -4.3; 40 -4.2; 42 -4.1; 45 -4.1; 49 -4.1; 52 -4.0; 56 -4.0; 59 -4.0; 64 -3.9; 68 -3.8; 73 -3.7; 78 -3.7; 83 -3.7; 89 -3.7; 95 -3.8; 102 -4.0; 109 -4.3; 117 -4.5; 125 -4.8; 134 -4.9; 143 -5.0; 153 -5.1; 164 -4.6; 175 -4.6; 188 -4.6; 201 -4.3; 215 -3.9; 230 -3.4; 246 -2.9; 263 -2.3; 282 -1.8; 301 -1.6; 323 -1.6; 345 -1.6; 369 -1.7; 395 -1.8; 423 -1.9; 452 -2.0; 484 -2.2; 518 -2.3; 554 -2.1; 593 -1.9; 635 -1.9; 679 -2.0; 726 -1.8; 777 -1.5; 832 -1.3; 890 -0.9; 952 -0.4; 1019 0.2; 1090 0.9; 1167 1.5; 1248 2.0; 1336 2.3; 1429 2.4; 1529 2.6; 1636 2.7; 1751 2.7; 1873 2.9; 2004 3.0; 2145 2.7; 2295 2.5; 2455 2.6; 2627 3.0; 2811 3.0; 3008 3.2; 3219 3.4; 3444 4.3; 3685 5.7; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.31 | -4.2 dB |
| Peaking | 159 Hz  | 1.09 | -3.9 dB |
| Peaking | 731 Hz  | 0.88 | -3.3 dB |
| Peaking | 1440 Hz | 0.74 | 3.5 dB  |
| Peaking | 4769 Hz | 1.45 | 6.4 dB  |
| Peaking | 294 Hz  | 6.64 | 0.6 dB  |
| Peaking | 3815 Hz | 5.48 | 1.7 dB  |
| Peaking | 4623 Hz | 2.3  | -1.1 dB |
| Peaking | 6359 Hz | 3.29 | 4.3 dB  |
| Peaking | 7380 Hz | 1.7  | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH30/Master%20Dynamic%20MH30.png)