# Focal Elear with Utopia Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 5.4; 37 5.2; 40 5.0; 42 4.8; 45 4.7; 49 4.5; 52 4.3; 56 4.1; 59 4.0; 64 3.7; 68 3.5; 73 3.2; 78 2.9; 83 2.7; 89 2.3; 95 2.0; 102 1.7; 109 1.6; 117 1.5; 125 1.2; 134 1.1; 143 0.9; 153 0.8; 164 0.7; 175 0.8; 188 0.7; 201 0.6; 215 0.6; 230 0.8; 246 0.8; 263 0.8; 282 0.9; 301 0.9; 323 1.0; 345 1.1; 369 1.2; 395 1.2; 423 1.4; 452 1.4; 484 1.4; 518 1.3; 554 1.4; 593 1.6; 635 1.4; 679 1.3; 726 1.2; 777 1.2; 832 0.9; 890 0.6; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.7; 1248 -1.1; 1336 -1.5; 1429 -1.4; 1529 -1.5; 1636 -1.6; 1751 -1.4; 1873 -0.4; 2004 0.8; 2145 1.6; 2295 2.4; 2455 2.8; 2627 3.2; 2811 3.2; 3008 3.5; 3219 4.0; 3444 4.5; 3685 5.3; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear with Utopia Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.7  | 5.7 dB  |
| Peaking | 59 Hz   | 0.93 | 2.2 dB  |
| Peaking | 551 Hz  | 0.79 | 1.4 dB  |
| Peaking | 1472 Hz | 2.18 | -2.9 dB |
| Peaking | 4427 Hz | 1.12 | 6.7 dB  |
| Peaking | 1778 Hz | 8.55 | -1.1 dB |
| Peaking | 2388 Hz | 3.41 | 1.2 dB  |
| Peaking | 4501 Hz | 4.57 | -0.5 dB |
| Peaking | 6338 Hz | 2.84 | 5.2 dB  |
| Peaking | 7199 Hz | 1.55 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20with%20Utopia%20Pads/Focal%20Elear%20with%20Utopia%20Pads.png)