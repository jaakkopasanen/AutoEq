# Bedphones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 5.9; 175 5.1; 188 4.3; 201 3.6; 215 3.0; 230 2.6; 246 2.1; 263 1.7; 282 1.5; 301 1.2; 323 1.0; 345 0.8; 369 0.7; 395 0.6; 423 0.7; 452 0.8; 484 0.6; 518 0.6; 554 0.8; 593 1.3; 635 1.1; 679 0.6; 726 0.6; 777 0.6; 832 0.4; 890 0.2; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.5; 1429 -0.6; 1529 -0.6; 1636 -0.1; 1751 0.8; 1873 2.3; 2004 3.7; 2145 5.2; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bedphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.26 | 9.9 dB  |
| Peaking | 60 Hz   | 0.71 | -3.9 dB |
| Peaking | 308 Hz  | 0.73 | -2.8 dB |
| Peaking | 2671 Hz | 2.01 | 5.6 dB  |
| Peaking | 4935 Hz | 1.57 | 6.1 dB  |
| Peaking | 1828 Hz | 0.85 | -5.8 dB |
| Peaking | 2080 Hz | 3.64 | 3.8 dB  |
| Peaking | 2572 Hz | 0.37 | 3.6 dB  |
| Peaking | 6355 Hz | 3.9  | 4.9 dB  |
| Peaking | 6632 Hz | 1.13 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bedphones/Bedphones.png)