# Logitech UE 6000 passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.1; 23 -2.1; 25 -2.2; 26 -2.2; 28 -2.3; 30 -2.3; 32 -2.3; 35 -2.2; 37 -2.2; 40 -2.1; 42 -2.0; 45 -1.9; 49 -1.8; 52 -1.6; 56 -1.5; 59 -1.3; 64 -1.1; 68 -1.0; 73 -0.9; 78 -0.8; 83 -0.7; 89 -0.6; 95 -0.7; 102 -0.8; 109 -0.9; 117 -1.4; 125 -1.6; 134 -1.6; 143 -1.9; 153 -1.9; 164 -0.8; 175 -0.4; 188 -1.0; 201 -1.1; 215 -0.8; 230 -0.3; 246 0.2; 263 0.7; 282 1.3; 301 1.8; 323 2.0; 345 2.3; 369 2.5; 395 2.5; 423 2.6; 452 2.4; 484 2.1; 518 1.8; 554 1.6; 593 1.5; 635 1.0; 679 0.6; 726 0.3; 777 0.3; 832 0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.4; 1336 0.5; 1429 0.7; 1529 0.9; 1636 1.4; 1751 1.9; 1873 2.7; 2004 4.0; 2145 5.1; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.4; 4514 4.7; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 6000 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.75 | -2.4 dB |
| Peaking | 148 Hz  | 1.48 | -1.6 dB |
| Peaking | 390 Hz  | 1.73 | 2.9 dB  |
| Peaking | 2893 Hz | 1.33 | 6.4 dB  |
| Peaking | 5561 Hz | 2.57 | 5.3 dB  |
| Peaking | 1269 Hz | 1.52 | -0.9 dB |
| Peaking | 2215 Hz | 4.06 | 1.6 dB  |
| Peaking | 2836 Hz | 6.96 | -1.0 dB |
| Peaking | 6516 Hz | 7.13 | 2.3 dB  |
| Peaking | 7873 Hz | 2.32 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%206000%20passive/Logitech%20UE%206000%20passive.png)