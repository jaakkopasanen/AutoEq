# Logitech UE4000 2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.3; 22 0.1; 23 0.1; 25 -0.1; 26 -0.1; 28 -0.2; 30 -0.3; 32 -0.3; 35 -0.4; 37 -0.5; 40 -0.5; 42 -0.5; 45 -0.5; 49 -0.5; 52 -0.5; 56 -0.6; 59 -0.6; 64 -0.5; 68 -0.6; 73 -0.8; 78 -0.9; 83 -1.1; 89 -1.2; 95 -1.3; 102 -1.4; 109 -1.7; 117 -2.6; 125 -2.8; 134 -2.5; 143 -2.4; 153 -2.7; 164 -2.8; 175 -2.2; 188 -2.5; 201 -2.7; 215 -2.5; 230 -2.0; 246 -1.4; 263 -0.7; 282 0.2; 301 0.8; 323 1.5; 345 2.4; 369 2.5; 395 2.5; 423 2.6; 452 2.4; 484 1.9; 518 1.6; 554 1.4; 593 1.2; 635 0.8; 679 0.2; 726 -0.1; 777 -0.0; 832 -0.2; 890 -0.2; 952 0.3; 1019 -0.1; 1090 0.1; 1167 0.4; 1248 0.9; 1336 1.3; 1429 1.7; 1529 2.3; 1636 2.9; 1751 3.7; 1873 4.8; 2004 5.8; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE4000 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 8 Hz    | 1.04 | -0.5 dB |
| Peaking | 215 Hz  | 2.74 | -1.7 dB |
| Peaking | 139 Hz  | 1.1  | -2.6 dB |
| Peaking | 385 Hz  | 2.21 | 3.2 dB  |
| Peaking | 3437 Hz | 0.74 | 6.9 dB  |
| Peaking | 1047 Hz | 1.76 | -1.4 dB |
| Peaking | 2068 Hz | 3.4  | 2.1 dB  |
| Peaking | 3401 Hz | 2.57 | -1.2 dB |
| Peaking | 6158 Hz | 2.19 | 5.6 dB  |
| Peaking | 7512 Hz | 1.48 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE4000%202012/Logitech%20UE4000%202012.png)