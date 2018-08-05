# AKG K272HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.3; 40 4.6; 42 4.2; 45 3.6; 49 3.0; 52 2.6; 56 2.2; 59 2.0; 64 1.4; 68 0.9; 73 0.4; 78 -0.1; 83 -0.5; 89 -0.1; 95 1.5; 102 3.9; 109 4.7; 117 3.1; 125 0.6; 134 -0.5; 143 -1.1; 153 -1.1; 164 -0.3; 175 -0.5; 188 -0.7; 201 -0.6; 215 -0.8; 230 -1.2; 246 -1.4; 263 -1.5; 282 -1.6; 301 -1.6; 323 -1.7; 345 -1.5; 369 -1.6; 395 -1.7; 423 -1.6; 452 -1.6; 484 -1.7; 518 -1.9; 554 -1.9; 593 -2.1; 635 -2.9; 679 -1.8; 726 0.6; 777 0.4; 832 0.4; 890 0.6; 952 0.4; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -1.0; 1336 -1.4; 1429 -2.1; 1529 -2.8; 1636 -2.8; 1751 -2.4; 1873 -1.3; 2004 0.7; 2145 2.4; 2295 2.5; 2455 3.9; 2627 4.2; 2811 4.8; 3008 4.9; 3219 4.7; 3444 4.8; 3685 5.8; 3943 6.0; 4219 5.4; 4514 5.3; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.1; 8299 -3.1; 8880 -5.8; 9502 -6.3; 10167 -3.8; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.8  | 5.3 dB   |
| Peaking | 35 Hz   | 1.54 | 2.7 dB   |
| Peaking | 1590 Hz | 2.27 | -5.0 dB  |
| Peaking | 4790 Hz | 0.59 | 7.0 dB   |
| Peaking | 9123 Hz | 2.8  | -10.4 dB |
| Peaking | 82 Hz   | 4.47 | -1.6 dB  |
| Peaking | 107 Hz  | 5.68 | 5.3 dB   |
| Peaking | 329 Hz  | 0.6  | -1.8 dB  |
| Peaking | 644 Hz  | 3.37 | -4.2 dB  |
| Peaking | 724 Hz  | 2.25 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)