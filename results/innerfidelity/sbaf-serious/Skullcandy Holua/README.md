# Skullcandy Holua

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 -10.0; 22 -9.9; 23 -9.9; 25 -9.8; 26 -9.7; 28 -9.6; 30 -9.5; 32 -9.4; 35 -9.3; 37 -9.2; 40 -9.1; 42 -9.1; 45 -9.0; 49 -8.8; 52 -8.7; 56 -8.6; 59 -8.6; 64 -8.5; 68 -8.4; 73 -8.4; 78 -8.3; 83 -8.2; 89 -8.2; 95 -8.1; 102 -8.0; 109 -7.8; 117 -7.5; 125 -7.4; 134 -7.3; 143 -7.0; 153 -6.8; 164 -6.5; 175 -6.2; 188 -5.9; 201 -5.5; 215 -5.2; 230 -4.8; 246 -4.4; 263 -4.1; 282 -3.7; 301 -3.3; 323 -2.9; 345 -2.5; 369 -2.2; 395 -1.8; 423 -1.3; 452 -0.9; 484 -0.7; 518 -0.4; 554 -0.0; 593 0.4; 635 0.6; 679 0.7; 726 0.8; 777 1.0; 832 0.9; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.3; 1336 -1.9; 1429 -2.7; 1529 -3.5; 1636 -4.3; 1751 -5.0; 1873 -5.7; 2004 -6.4; 2145 -7.5; 2295 -8.9; 2455 -8.4; 2627 -5.9; 2811 -3.4; 3008 -0.6; 3219 1.8; 3444 3.2; 3685 3.2; 3943 1.2; 4219 -1.8; 4514 -6.0; 4830 -10.2; 5168 -6.9; 5530 -1.7; 5917 2.1; 6331 4.7; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.049641258214373dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.6dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.2  | -9.6 dB  |
| Peaking | 154 Hz  | 0.82 | -3.5 dB  |
| Peaking | 2343 Hz | 1.69 | -14.9 dB |
| Peaking | 3599 Hz | 0.82 | 9.9 dB   |
| Peaking | 4802 Hz | 4.88 | -16.6 dB |
| Peaking | 758 Hz  | 1.9  | 1.8 dB   |
| Peaking | 1581 Hz | 4.26 | -1.5 dB  |
| Peaking | 5271 Hz | 9.15 | -1.9 dB  |
| Peaking | 6418 Hz | 4.59 | 5.2 dB   |
| Peaking | 7929 Hz | 1.47 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)