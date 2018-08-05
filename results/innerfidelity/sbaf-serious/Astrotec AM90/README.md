# Astrotec AM90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.3; 22 3.2; 23 3.2; 25 3.1; 26 3.1; 28 3.1; 30 3.1; 32 3.1; 35 3.0; 37 3.0; 40 2.9; 42 2.9; 45 2.9; 49 2.9; 52 2.9; 56 2.9; 59 2.8; 64 2.7; 68 2.6; 73 2.5; 78 2.3; 83 2.0; 89 1.5; 95 1.1; 102 0.6; 109 0.1; 117 -0.5; 125 -1.1; 134 -1.6; 143 -1.9; 153 -2.1; 164 -2.3; 175 -2.4; 188 -2.5; 201 -2.5; 215 -2.3; 230 -2.3; 246 -2.4; 263 -2.3; 282 -2.1; 301 -2.0; 323 -1.9; 345 -1.7; 369 -1.7; 395 -1.5; 423 -1.2; 452 -1.0; 484 -1.0; 518 -0.8; 554 -0.5; 593 -0.1; 635 0.1; 679 0.2; 726 0.3; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.6; 1429 0.0; 1529 0.6; 1636 0.8; 1751 0.5; 1873 0.4; 2004 0.3; 2145 0.1; 2295 -0.5; 2455 -1.2; 2627 -2.3; 2811 -3.2; 3008 -0.3; 3219 4.3; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AM90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.37 | 3.1 dB  |
| Peaking | 78 Hz   | 1    | 2.4 dB  |
| Peaking | 174 Hz  | 0.64 | -3.4 dB |
| Peaking | 2729 Hz | 4.47 | -6.7 dB |
| Peaking | 4266 Hz | 1.18 | 7.4 dB  |
| Peaking | 1285 Hz | 7.58 | -1.0 dB |
| Peaking | 3386 Hz | 7.43 | 3.0 dB  |
| Peaking | 4188 Hz | 1.44 | -1.3 dB |
| Peaking | 6311 Hz | 2.61 | 5.3 dB  |
| Peaking | 7339 Hz | 1.67 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AM90/Astrotec%20AM90.png)