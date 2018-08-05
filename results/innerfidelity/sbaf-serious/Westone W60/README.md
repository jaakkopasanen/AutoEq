# Westone W60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.0; 23 -0.1; 25 -0.2; 26 -0.2; 28 -0.3; 30 -0.4; 32 -0.4; 35 -0.4; 37 -0.5; 40 -0.5; 42 -0.6; 45 -0.7; 49 -0.7; 52 -0.7; 56 -0.7; 59 -0.7; 64 -0.8; 68 -0.9; 73 -1.0; 78 -1.1; 83 -1.4; 89 -1.8; 95 -2.2; 102 -2.7; 109 -3.1; 117 -3.6; 125 -4.1; 134 -4.6; 143 -4.8; 153 -5.0; 164 -5.1; 175 -5.0; 188 -5.0; 201 -4.9; 215 -4.7; 230 -4.5; 246 -4.4; 263 -4.2; 282 -3.9; 301 -3.7; 323 -3.4; 345 -3.2; 369 -2.9; 395 -2.7; 423 -2.3; 452 -2.0; 484 -1.8; 518 -1.5; 554 -1.1; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.4; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.5; 1429 -2.1; 1529 -2.4; 1636 -2.4; 1751 -2.0; 1873 -1.0; 2004 0.5; 2145 2.2; 2295 3.8; 2455 5.3; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -2.3; 10167 -3.4; 10879 -1.8; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.98 | 2.6 dB  |
| Peaking | 163 Hz  | 0.45 | -5.8 dB |
| Peaking | 1620 Hz | 1.54 | -8.3 dB |
| Peaking | 3262 Hz | 0.37 | 8.0 dB  |
| Peaking | 9676 Hz | 1.7  | -5.9 dB |
| Peaking | 1996 Hz | 5.6  | -0.8 dB |
| Peaking | 2518 Hz | 3.38 | 1.5 dB  |
| Peaking | 4012 Hz | 1.13 | -1.1 dB |
| Peaking | 6613 Hz | 1.88 | 2.4 dB  |
| Peaking | 7377 Hz | 5.37 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W60/Westone%20W60.png)