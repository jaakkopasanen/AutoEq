# Focal Elear with Utopia Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 5.5; 37 5.3; 40 5.1; 42 5.0; 45 4.8; 49 4.7; 52 4.6; 56 4.5; 59 4.4; 64 4.2; 68 4.1; 73 3.9; 78 3.7; 83 3.5; 89 3.1; 95 2.7; 102 2.3; 109 2.0; 117 1.7; 125 1.3; 134 0.9; 143 0.7; 153 0.5; 164 0.5; 175 0.6; 188 0.5; 201 0.5; 215 0.5; 230 0.7; 246 0.7; 263 0.7; 282 0.8; 301 0.8; 323 0.9; 345 1.1; 369 1.1; 395 1.2; 423 1.4; 452 1.4; 484 1.3; 518 1.2; 554 1.4; 593 1.6; 635 1.4; 679 1.2; 726 1.2; 777 1.2; 832 0.9; 890 0.6; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.8; 1248 -1.1; 1336 -1.5; 1429 -1.4; 1529 -1.5; 1636 -1.6; 1751 -1.4; 1873 -0.4; 2004 0.8; 2145 1.6; 2295 2.4; 2455 2.8; 2627 3.2; 2811 3.2; 3008 3.5; 3219 4.0; 3444 4.5; 3685 5.3; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear with Utopia Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.6  | 6.0 dB  |
| Peaking | 71 Hz   | 1.4  | 2.2 dB  |
| Peaking | 558 Hz  | 0.96 | 1.5 dB  |
| Peaking | 1482 Hz | 2.26 | -2.8 dB |
| Peaking | 4421 Hz | 1.12 | 6.7 dB  |
| Peaking | 1790 Hz | 8.13 | -1.0 dB |
| Peaking | 2391 Hz | 3.38 | 1.2 dB  |
| Peaking | 4483 Hz | 3.7  | -0.6 dB |
| Peaking | 6287 Hz | 2.92 | 4.7 dB  |
| Peaking | 7371 Hz | 1.57 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20with%20Utopia%20Pads/Focal%20Elear%20with%20Utopia%20Pads.png)