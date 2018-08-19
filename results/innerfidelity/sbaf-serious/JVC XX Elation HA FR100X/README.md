# JVC XX Elation HA FR100X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 2.4; 22 1.2; 23 0.8; 25 0.1; 26 -0.1; 28 -0.5; 30 -0.7; 32 -1.0; 35 -1.4; 37 -1.6; 40 -2.0; 42 -2.2; 45 -2.6; 49 -3.0; 52 -3.4; 56 -3.7; 59 -3.9; 64 -4.3; 68 -4.7; 73 -5.1; 78 -5.4; 83 -5.9; 89 -6.2; 95 -6.5; 102 -6.8; 109 -7.0; 117 -7.2; 125 -7.3; 134 -7.6; 143 -7.8; 153 -8.0; 164 -8.1; 175 -8.0; 188 -8.1; 201 -8.1; 215 -7.9; 230 -7.9; 246 -7.8; 263 -7.6; 282 -7.4; 301 -7.2; 323 -6.8; 345 -6.5; 369 -6.1; 395 -5.8; 423 -5.2; 452 -4.8; 484 -4.5; 518 -4.0; 554 -3.3; 593 -2.6; 635 -2.1; 679 -1.7; 726 -1.2; 777 -0.7; 832 -0.3; 890 -0.2; 952 0.0; 1019 0.2; 1090 0.7; 1167 0.9; 1248 1.1; 1336 1.0; 1429 1.1; 1529 1.0; 1636 1.0; 1751 0.9; 1873 0.7; 2004 0.1; 2145 -0.6; 2295 -1.0; 2455 -1.0; 2627 -1.2; 2811 -1.1; 3008 -0.3; 3219 0.4; 3444 0.9; 3685 0.3; 3943 -1.2; 4219 -3.8; 4514 -6.3; 4830 -7.3; 5168 -5.4; 5530 -1.6; 5917 2.1; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.867412575634299dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC XX Elation HA FR100X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.09 | 3.0 dB  |
| Peaking | 129 Hz  | 0.53 | -7.1 dB |
| Peaking | 311 Hz  | 1.09 | -4.1 dB |
| Peaking | 4819 Hz | 4.65 | -8.6 dB |
| Peaking | 6403 Hz | 4.97 | 5.9 dB  |
| Peaking | 510 Hz  | 2.96 | -1.1 dB |
| Peaking | 1676 Hz | 0.8  | 2.9 dB  |
| Peaking | 2629 Hz | 1.05 | -3.3 dB |
| Peaking | 3416 Hz | 3.82 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20XX%20Elation%20HA%20FR100X/JVC%20XX%20Elation%20HA%20FR100X.png)