# Fostex T50RP Mk3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.7; 52 5.2; 56 4.3; 59 3.8; 64 3.0; 68 2.4; 73 1.8; 78 1.4; 83 1.0; 89 0.5; 95 0.3; 102 -0.1; 109 -0.3; 117 -0.5; 125 -0.8; 134 -1.0; 143 -1.0; 153 -0.9; 164 -0.7; 175 -0.3; 188 -0.1; 201 0.1; 215 0.4; 230 0.6; 246 0.8; 263 0.9; 282 0.9; 301 1.0; 323 1.3; 345 1.5; 369 1.8; 395 2.0; 423 2.6; 452 2.6; 484 2.3; 518 2.4; 554 2.3; 593 2.2; 635 2.1; 679 1.6; 726 1.4; 777 1.1; 832 0.8; 890 0.1; 952 -0.2; 1019 0.1; 1090 0.3; 1167 0.7; 1248 1.0; 1336 1.0; 1429 1.4; 1529 1.5; 1636 1.3; 1751 1.8; 1873 2.1; 2004 2.1; 2145 2.3; 2295 2.3; 2455 2.2; 2627 2.6; 2811 2.0; 3008 1.7; 3219 1.4; 3444 1.0; 3685 0.1; 3943 -0.4; 4219 -1.3; 4514 -1.4; 4830 0.4; 5168 3.9; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.8; 8880 -3.3; 9502 -4.2; 10167 -2.4; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.94 | 7.1 dB  |
| Peaking | 486 Hz  | 1.6  | 2.7 dB  |
| Peaking | 2192 Hz | 1.82 | 2.5 dB  |
| Peaking | 6020 Hz | 4.02 | 6.9 dB  |
| Peaking | 9348 Hz | 4.87 | -5.0 dB |
| Peaking | 51 Hz   | 3.6  | 1.7 dB  |
| Peaking | 127 Hz  | 1.92 | -1.7 dB |
| Peaking | 5251 Hz | 7.1  | 3.0 dB  |
| Peaking | 3064 Hz | 3.03 | 0.9 dB  |
| Peaking | 4487 Hz | 3.49 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk3/Fostex%20T50RP%20Mk3.png)