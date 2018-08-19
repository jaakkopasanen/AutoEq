# Phiaton PS 210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.5; 26 5.3; 28 4.9; 30 4.5; 32 4.2; 35 3.7; 37 3.5; 40 3.1; 42 2.9; 45 2.5; 49 2.1; 52 1.8; 56 1.5; 59 1.2; 64 0.8; 68 0.4; 73 0.1; 78 -0.3; 83 -0.7; 89 -1.1; 95 -1.4; 102 -1.7; 109 -1.8; 117 -2.1; 125 -2.4; 134 -2.7; 143 -2.9; 153 -3.1; 164 -3.2; 175 -3.3; 188 -3.3; 201 -3.5; 215 -3.5; 230 -3.5; 246 -3.5; 263 -3.6; 282 -3.6; 301 -3.6; 323 -3.5; 345 -3.4; 369 -3.2; 395 -3.4; 423 -4.0; 452 -3.8; 484 -3.4; 518 -3.2; 554 -3.2; 593 -3.1; 635 -3.0; 679 -2.9; 726 -2.4; 777 -1.8; 832 -1.3; 890 -0.8; 952 -0.3; 1019 0.1; 1090 0.5; 1167 0.7; 1248 0.8; 1336 0.5; 1429 -0.1; 1529 -0.9; 1636 -1.8; 1751 -2.7; 1873 -3.6; 2004 -4.5; 2145 -5.2; 2295 -5.2; 2455 -3.5; 2627 -1.2; 2811 1.2; 3008 3.8; 3219 5.4; 3444 6.0; 3685 5.6; 3943 3.8; 4219 0.9; 4514 -1.0; 4830 0.5; 5168 0.9; 5530 1.9; 5917 5.0; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.47 | 6.2 dB   |
| Peaking | 378 Hz  | 0.28 | -4.7 dB  |
| Peaking | 1958 Hz | 0.45 | 5.9 dB   |
| Peaking | 2184 Hz | 1.76 | -10.3 dB |
| Peaking | 3314 Hz | 4.17 | 5.7 dB   |
| Peaking | 655 Hz  | 1.61 | -2.2 dB  |
| Peaking | 684 Hz  | 0.9  | 1.5 dB   |
| Peaking | 4574 Hz | 7.46 | -3.7 dB  |
| Peaking | 6324 Hz | 5.13 | 5.5 dB   |
| Peaking | 7995 Hz | 1.57 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20210/Phiaton%20PS%20210.png)