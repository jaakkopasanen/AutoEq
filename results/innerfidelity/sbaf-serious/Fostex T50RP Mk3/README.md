# Fostex T50RP Mk3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.5; 52 4.9; 56 4.0; 59 3.4; 64 2.4; 68 1.8; 73 1.1; 78 0.6; 83 0.2; 89 -0.3; 95 -0.4; 102 -0.6; 109 -0.7; 117 -0.7; 125 -0.9; 134 -0.9; 143 -0.8; 153 -0.6; 164 -0.4; 175 -0.1; 188 0.1; 201 0.3; 215 0.5; 230 0.7; 246 0.9; 263 1.0; 282 1.0; 301 1.1; 323 1.4; 345 1.6; 369 1.8; 395 2.0; 423 2.6; 452 2.6; 484 2.3; 518 2.4; 554 2.3; 593 2.2; 635 2.1; 679 1.6; 726 1.4; 777 1.1; 832 0.8; 890 0.1; 952 -0.2; 1019 0.1; 1090 0.3; 1167 0.7; 1248 1.0; 1336 1.0; 1429 1.4; 1529 1.5; 1636 1.3; 1751 1.8; 1873 2.1; 2004 2.1; 2145 2.3; 2295 2.3; 2455 2.2; 2627 2.6; 2811 2.0; 3008 1.7; 3219 1.4; 3444 1.0; 3685 0.1; 3943 -0.4; 4219 -1.3; 4514 -1.4; 4830 0.4; 5168 3.9; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.8; 8880 -3.3; 9502 -4.2; 10167 -2.4; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.05 | 7.1 dB  |
| Peaking | 482 Hz  | 1.54 | 2.7 dB  |
| Peaking | 2195 Hz | 1.83 | 2.5 dB  |
| Peaking | 6019 Hz | 4.02 | 6.9 dB  |
| Peaking | 9339 Hz | 4.85 | -4.9 dB |
| Peaking | 51 Hz   | 3.33 | 2.1 dB  |
| Peaking | 110 Hz  | 1.49 | -1.7 dB |
| Peaking | 3069 Hz | 3.19 | 0.9 dB  |
| Peaking | 4520 Hz | 3.44 | -3.4 dB |
| Peaking | 5253 Hz | 6.53 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk3/Fostex%20T50RP%20Mk3.png)