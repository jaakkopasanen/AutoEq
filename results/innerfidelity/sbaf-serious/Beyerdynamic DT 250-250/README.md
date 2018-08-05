# Beyerdynamic DT 250-250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.6; 35 5.3; 37 5.1; 40 4.8; 42 4.6; 45 4.4; 49 4.2; 52 4.1; 56 4.0; 59 3.9; 64 3.9; 68 3.9; 73 4.1; 78 4.7; 83 5.4; 89 5.3; 95 4.8; 102 4.4; 109 4.3; 117 3.6; 125 2.4; 134 1.6; 143 1.3; 153 1.2; 164 1.9; 175 1.4; 188 0.9; 201 0.9; 215 0.9; 230 1.0; 246 1.1; 263 1.2; 282 1.1; 301 1.0; 323 1.0; 345 1.2; 369 1.3; 395 1.3; 423 1.4; 452 1.2; 484 1.0; 518 0.9; 554 0.9; 593 1.0; 635 0.8; 679 0.6; 726 0.3; 777 0.3; 832 -0.0; 890 -0.3; 952 -0.6; 1019 0.3; 1090 0.3; 1167 0.1; 1248 -0.9; 1336 -1.7; 1429 -2.4; 1529 -2.9; 1636 -3.2; 1751 -3.1; 1873 -2.6; 2004 -1.8; 2145 -1.0; 2295 -0.4; 2455 0.6; 2627 1.4; 2811 2.4; 3008 3.9; 3219 4.9; 3444 4.9; 3685 3.6; 3943 2.6; 4219 1.8; 4514 1.5; 4830 2.4; 5168 4.2; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.13 | 1.0 dB  |
| Peaking | 24 Hz   | 0.58 | 5.0 dB  |
| Peaking | 91 Hz   | 2.3  | 3.4 dB  |
| Peaking | 3321 Hz | 4.59 | 5.3 dB  |
| Peaking | 5869 Hz | 3.65 | 6.6 dB  |
| Peaking | 191 Hz  | 1.55 | -0.5 dB |
| Peaking | 443 Hz  | 1.03 | 0.8 dB  |
| Peaking | 1688 Hz | 2.28 | -3.8 dB |
| Peaking | 2792 Hz | 2.72 | 1.1 dB  |
| Peaking | 9357 Hz | 5.77 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)