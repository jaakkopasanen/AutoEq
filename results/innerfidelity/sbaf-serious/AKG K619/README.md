# AKG K619

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.4; 22 -4.6; 23 -4.6; 25 -4.7; 26 -4.7; 28 -4.8; 30 -4.9; 32 -4.9; 35 -4.9; 37 -4.9; 40 -4.8; 42 -4.8; 45 -4.7; 49 -4.4; 52 -4.2; 56 -3.9; 59 -3.7; 64 -3.3; 68 -2.8; 73 -2.1; 78 -1.3; 83 -0.5; 89 0.2; 95 0.1; 102 -0.4; 109 0.0; 117 0.6; 125 1.4; 134 1.6; 143 1.8; 153 2.4; 164 3.3; 175 3.3; 188 3.5; 201 3.6; 215 3.7; 230 3.6; 246 3.6; 263 3.6; 282 3.6; 301 3.3; 323 2.8; 345 2.6; 369 2.2; 395 1.8; 423 1.6; 452 1.5; 484 1.1; 518 1.0; 554 1.0; 593 1.1; 635 1.0; 679 0.7; 726 0.6; 777 0.6; 832 0.5; 890 0.2; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.5; 1336 0.6; 1429 0.4; 1529 0.5; 1636 0.6; 1751 1.2; 1873 2.0; 2004 2.7; 2145 3.6; 2295 5.2; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K619 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.59 | -5.4 dB |
| Peaking | 212 Hz  | 0.94 | 5.1 dB  |
| Peaking | 214 Hz  | 2.72 | -1.1 dB |
| Peaking | 2895 Hz | 1.6  | 5.9 dB  |
| Peaking | 5233 Hz | 1.91 | 5.6 dB  |
| Peaking | 1477 Hz | 1.39 | -0.7 dB |
| Peaking | 2336 Hz | 7.34 | 1.6 dB  |
| Peaking | 8567 Hz | 3.44 | 0.6 dB  |
| Peaking | 6456 Hz | 5.48 | 2.9 dB  |
| Peaking | 7916 Hz | 1.99 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K619/AKG%20K619.png)