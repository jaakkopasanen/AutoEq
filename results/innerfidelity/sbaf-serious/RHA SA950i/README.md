# RHA SA950i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.7; 23 -5.9; 25 -6.2; 26 -6.4; 28 -6.6; 30 -6.7; 32 -6.8; 35 -6.9; 37 -6.9; 40 -7.0; 42 -7.0; 45 -6.9; 49 -6.9; 52 -6.8; 56 -6.8; 59 -6.8; 64 -6.8; 68 -6.8; 73 -6.8; 78 -6.9; 83 -7.0; 89 -6.8; 95 -6.7; 102 -6.9; 109 -7.0; 117 -6.9; 125 -6.9; 134 -7.3; 143 -7.5; 153 -7.7; 164 -7.5; 175 -7.5; 188 -7.7; 201 -7.7; 215 -7.4; 230 -7.2; 246 -7.2; 263 -7.2; 282 -7.1; 301 -7.3; 323 -7.5; 345 -7.7; 369 -7.8; 395 -7.8; 423 -7.6; 452 -7.6; 484 -7.6; 518 -7.4; 554 -6.9; 593 -6.2; 635 -5.7; 679 -4.9; 726 -3.8; 777 -2.7; 832 -1.6; 890 -1.0; 952 -0.5; 1019 0.1; 1090 -0.5; 1167 -1.4; 1248 -2.9; 1336 -4.4; 1429 -5.6; 1529 -5.9; 1636 -5.8; 1751 -5.1; 1873 -3.8; 2004 -2.3; 2145 -1.0; 2295 -0.2; 2455 1.1; 2627 2.1; 2811 2.6; 3008 3.3; 3219 4.4; 3444 4.3; 3685 4.5; 3943 5.8; 4219 6.0; 4514 6.0; 4830 1.5; 5168 -1.7; 5530 -1.4; 5917 3.0; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099997016566144dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA SA950i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.25 | -6.5 dB |
| Peaking | 229 Hz  | 0.72 | -4.5 dB |
| Peaking | 483 Hz  | 1.57 | -5.4 dB |
| Peaking | 1616 Hz | 2.89 | -6.7 dB |
| Peaking | 3736 Hz | 1.55 | 5.7 dB  |
| Peaking | 654 Hz  | 6.15 | -1.2 dB |
| Peaking | 990 Hz  | 4.69 | 2.2 dB  |
| Peaking | 4530 Hz | 4.87 | 6.4 dB  |
| Peaking | 5230 Hz | 2.68 | -8.2 dB |
| Peaking | 6268 Hz | 4.93 | 7.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20SA950i/RHA%20SA950i.png)