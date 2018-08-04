# Blue MOFI Active On Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.2; 22 0.9; 23 0.8; 25 0.5; 26 0.3; 28 0.0; 30 -0.2; 32 -0.5; 35 -0.9; 37 -1.2; 40 -1.6; 42 -1.9; 45 -2.3; 49 -2.8; 52 -3.1; 56 -3.5; 59 -3.7; 64 -4.0; 68 -4.1; 73 -4.2; 78 -4.1; 83 -3.9; 89 -3.8; 95 -3.8; 102 -3.8; 109 -3.6; 117 -3.4; 125 -3.4; 134 -3.5; 143 -3.8; 153 -3.9; 164 -3.3; 175 -2.8; 188 -3.2; 201 -3.0; 215 -2.7; 230 -2.1; 246 -1.5; 263 -0.8; 282 0.2; 301 0.7; 323 1.1; 345 1.0; 369 1.1; 395 1.0; 423 1.9; 452 2.9; 484 3.3; 518 3.0; 554 2.6; 593 2.6; 635 2.5; 679 2.0; 726 1.6; 777 1.4; 832 1.1; 890 0.5; 952 0.1; 1019 -0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 0.1; 1429 -0.2; 1529 -0.4; 1636 -0.4; 1751 -0.2; 1873 0.3; 2004 1.1; 2145 2.0; 2295 2.3; 2455 2.4; 2627 3.2; 2811 3.7; 3008 4.0; 3219 4.0; 3444 4.5; 3685 5.6; 3943 3.8; 4219 -0.8; 4514 1.9; 4830 5.1; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 1.1  | -3.8 dB |
| Peaking | 163 Hz  | 1.19 | -3.1 dB |
| Peaking | 498 Hz  | 1.53 | 3.5 dB  |
| Peaking | 3173 Hz | 2.26 | 4.3 dB  |
| Peaking | 5718 Hz | 3.16 | 6.4 dB  |
| Peaking | 20 Hz   | 2.04 | 1.4 dB  |
| Peaking | 700 Hz  | 4.43 | 0.5 dB  |
| Peaking | 1794 Hz | 1.45 | -1.5 dB |
| Peaking | 2182 Hz | 2.86 | 1.9 dB  |
| Peaking | 8297 Hz | 4.73 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On%20Plus/Blue%20MOFI%20Active%20On%20Plus.png)