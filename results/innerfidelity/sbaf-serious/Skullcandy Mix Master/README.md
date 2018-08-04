# Skullcandy Mix Master

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.5; 22 4.7; 23 4.3; 25 3.6; 26 3.3; 28 2.7; 30 2.3; 32 1.9; 35 1.5; 37 1.3; 40 1.1; 42 0.9; 45 0.8; 49 0.7; 52 0.6; 56 0.6; 59 0.6; 64 0.7; 68 0.8; 73 0.8; 78 0.5; 83 0.2; 89 -0.0; 95 -0.4; 102 -0.8; 109 -0.9; 117 -1.3; 125 -1.7; 134 -2.1; 143 -2.3; 153 -2.5; 164 -2.5; 175 -2.5; 188 -2.7; 201 -2.8; 215 -2.8; 230 -2.7; 246 -2.5; 263 -2.2; 282 -1.8; 301 -1.5; 323 -1.5; 345 -1.3; 369 -1.0; 395 -1.1; 423 -1.0; 452 -0.5; 484 -0.2; 518 0.4; 554 1.1; 593 1.5; 635 1.6; 679 1.5; 726 1.4; 777 1.4; 832 0.9; 890 0.3; 952 -0.0; 1019 -0.0; 1090 -0.0; 1167 -0.3; 1248 -0.8; 1336 -1.7; 1429 -2.5; 1529 -2.8; 1636 -3.1; 1751 -2.7; 1873 -1.9; 2004 -1.6; 2145 -0.7; 2295 0.4; 2455 1.9; 2627 3.1; 2811 4.1; 3008 4.9; 3219 5.4; 3444 4.3; 3685 0.6; 3943 -1.4; 4219 -0.2; 4514 1.8; 4830 3.5; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.83 | 7.5 dB  |
| Peaking | 192 Hz  | 1.22 | -3.1 dB |
| Peaking | 1649 Hz | 3.11 | -3.6 dB |
| Peaking | 3017 Hz | 4.09 | 5.7 dB  |
| Peaking | 5762 Hz | 3.4  | 6.8 dB  |
| Peaking | 71 Hz   | 4.65 | 0.7 dB  |
| Peaking | 670 Hz  | 2.9  | 2.1 dB  |
| Peaking | 4008 Hz | 5.83 | -5.6 dB |
| Peaking | 4002 Hz | 2.02 | 2.3 dB  |
| Peaking | 8259 Hz | 4.02 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Mix%20Master/Skullcandy%20Mix%20Master.png)