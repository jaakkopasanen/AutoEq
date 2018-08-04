# Philips Cityscape Downtown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.0; 22 5.0; 23 5.0; 25 5.0; 26 5.0; 28 4.9; 30 4.9; 32 4.9; 35 5.0; 37 5.0; 40 5.1; 42 5.1; 45 5.2; 49 5.3; 52 5.4; 56 5.5; 59 5.6; 64 5.7; 68 5.8; 73 5.9; 78 6.0; 83 6.0; 89 5.8; 95 5.7; 102 5.4; 109 5.4; 117 5.2; 125 5.1; 134 4.9; 143 4.6; 153 4.2; 164 4.5; 175 4.3; 188 3.9; 201 3.8; 215 3.7; 230 3.7; 246 3.6; 263 3.6; 282 3.7; 301 3.6; 323 3.6; 345 3.6; 369 3.5; 395 3.4; 423 3.1; 452 2.8; 484 2.3; 518 1.9; 554 1.8; 593 1.7; 635 1.4; 679 1.0; 726 0.8; 777 0.7; 832 0.4; 890 0.1; 952 -0.0; 1019 -0.0; 1090 0.1; 1167 0.4; 1248 0.7; 1336 0.8; 1429 0.9; 1529 1.3; 1636 2.0; 1751 2.6; 1873 3.6; 2004 4.8; 2145 5.9; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 5.2; 4514 3.9; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Cityscape Downtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.07 | 4.0 dB  |
| Peaking | 76 Hz   | 0.23 | 5.4 dB  |
| Peaking | 2845 Hz | 1.27 | 6.4 dB  |
| Peaking | 5589 Hz | 2.65 | 5.2 dB  |
| Peaking | 399 Hz  | 2.66 | 1.2 dB  |
| Peaking | 1065 Hz | 1.29 | -1.2 dB |
| Peaking | 2103 Hz | 6.14 | 1.9 dB  |
| Peaking | 6468 Hz | 6.86 | 2.3 dB  |
| Peaking | 7813 Hz | 2.25 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Cityscape%20Downtown/Philips%20Cityscape%20Downtown.png)