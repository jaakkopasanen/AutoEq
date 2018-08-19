# Skullcandy Mix Master

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.5; 22 4.6; 23 4.3; 25 3.6; 26 3.3; 28 2.7; 30 2.2; 32 1.9; 35 1.4; 37 1.2; 40 0.9; 42 0.8; 45 0.6; 49 0.5; 52 0.3; 56 0.2; 59 0.2; 64 0.2; 68 0.2; 73 0.1; 78 -0.2; 83 -0.6; 89 -0.8; 95 -1.2; 102 -1.3; 109 -1.3; 117 -1.5; 125 -1.8; 134 -2.0; 143 -2.1; 153 -2.3; 164 -2.3; 175 -2.2; 188 -2.5; 201 -2.6; 215 -2.7; 230 -2.5; 246 -2.4; 263 -2.1; 282 -1.7; 301 -1.5; 323 -1.5; 345 -1.2; 369 -1.0; 395 -1.1; 423 -1.0; 452 -0.5; 484 -0.2; 518 0.4; 554 1.1; 593 1.5; 635 1.6; 679 1.5; 726 1.4; 777 1.4; 832 0.9; 890 0.3; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.3; 1248 -0.8; 1336 -1.7; 1429 -2.5; 1529 -2.8; 1636 -3.1; 1751 -2.7; 1873 -1.9; 2004 -1.6; 2145 -0.7; 2295 0.4; 2455 1.9; 2627 3.1; 2811 4.1; 3008 4.9; 3219 5.4; 3444 4.3; 3685 0.6; 3943 -1.4; 4219 -0.2; 4514 1.8; 4830 3.5; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.097714767088153dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.22 | 5.4 dB  |
| Peaking | 184 Hz  | 1.04 | -2.8 dB |
| Peaking | 1649 Hz | 3.13 | -3.6 dB |
| Peaking | 3018 Hz | 4.1  | 5.7 dB  |
| Peaking | 5762 Hz | 3.4  | 6.8 dB  |
| Peaking | 671 Hz  | 2.79 | 2.1 dB  |
| Peaking | 3443 Hz | 8.89 | 2.8 dB  |
| Peaking | 3944 Hz | 5.33 | -3.5 dB |
| Peaking | 5078 Hz | 9.66 | 2.1 dB  |
| Peaking | 8291 Hz | 4.89 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Mix%20Master/Skullcandy%20Mix%20Master.png)