# Earsonics Velvet Pot CCW

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 0.5; 22 0.3; 23 0.2; 25 0.0; 26 -0.0; 28 -0.1; 30 -0.2; 32 -0.2; 35 -0.2; 37 -0.2; 40 -0.2; 42 -0.1; 45 -0.0; 49 0.1; 52 0.3; 56 0.4; 59 0.6; 64 0.8; 68 1.0; 73 1.3; 78 1.5; 83 1.6; 89 1.8; 95 1.8; 102 1.9; 109 2.0; 117 2.1; 125 2.4; 134 2.7; 143 3.2; 153 3.8; 164 4.5; 175 5.3; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 5.6; 282 5.1; 301 4.5; 323 3.9; 345 3.5; 369 3.0; 395 2.6; 423 2.3; 452 2.0; 484 1.6; 518 1.4; 554 1.4; 593 1.5; 635 1.4; 679 1.2; 726 1.1; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.2; 1429 -1.5; 1529 -1.7; 1636 -1.6; 1751 -1.1; 1873 -0.2; 2004 1.3; 2145 2.8; 2295 3.6; 2455 4.7; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.0; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CCW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 2.5  | -0.5 dB |
| Peaking | 221 Hz  | 0.94 | 6.1 dB  |
| Peaking | 1583 Hz | 1.9  | -4.5 dB |
| Peaking | 3518 Hz | 0.78 | 7.1 dB  |
| Peaking | 82 Hz   | 3.92 | 0.5 dB  |
| Peaking | 2642 Hz | 4.63 | 1.2 dB  |
| Peaking | 3500 Hz | 2.47 | -0.9 dB |
| Peaking | 6130 Hz | 2.55 | 5.4 dB  |
| Peaking | 7254 Hz | 1.4  | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CCW/Earsonics%20Velvet%20Pot%20CCW.png)