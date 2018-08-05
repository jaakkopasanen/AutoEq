# Earsonics Velvet Pot CW

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.4; 23 -3.5; 25 -3.7; 26 -3.8; 28 -4.0; 30 -4.0; 32 -4.1; 35 -4.1; 37 -4.1; 40 -4.1; 42 -4.1; 45 -4.1; 49 -4.1; 52 -4.0; 56 -3.9; 59 -3.8; 64 -3.7; 68 -3.6; 73 -3.5; 78 -3.4; 83 -3.4; 89 -3.4; 95 -3.5; 102 -3.6; 109 -3.6; 117 -3.6; 125 -3.7; 134 -3.5; 143 -3.2; 153 -2.7; 164 -2.1; 175 -1.3; 188 -0.5; 201 0.3; 215 1.2; 230 2.1; 246 2.8; 263 3.3; 282 3.8; 301 3.9; 323 3.9; 345 3.7; 369 3.5; 395 3.1; 423 2.8; 452 2.5; 484 2.0; 518 1.8; 554 1.8; 593 1.8; 635 1.6; 679 1.3; 726 1.2; 777 1.2; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.2; 1429 -1.5; 1529 -1.7; 1636 -1.7; 1751 -1.3; 1873 -0.3; 2004 1.1; 2145 2.7; 2295 3.6; 2455 4.7; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.45 | -4.0 dB |
| Peaking | 147 Hz  | 0.98 | -4.3 dB |
| Peaking | 281 Hz  | 0.87 | 5.5 dB  |
| Peaking | 1578 Hz | 1.82 | -4.6 dB |
| Peaking | 3521 Hz | 0.78 | 7.2 dB  |
| Peaking | 1869 Hz | 8.16 | -0.7 dB |
| Peaking | 2643 Hz | 3.02 | 1.2 dB  |
| Peaking | 3460 Hz | 2.56 | -1.1 dB |
| Peaking | 6164 Hz | 2.49 | 5.3 dB  |
| Peaking | 7329 Hz | 1.44 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CW/Earsonics%20Velvet%20Pot%20CW.png)