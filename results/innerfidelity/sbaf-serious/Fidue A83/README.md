# Fidue A83

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.1; 22 -1.4; 23 -1.5; 25 -1.8; 26 -1.9; 28 -2.1; 30 -2.3; 32 -2.5; 35 -2.7; 37 -2.8; 40 -3.0; 42 -3.1; 45 -3.2; 49 -3.4; 52 -3.6; 56 -3.7; 59 -3.9; 64 -4.2; 68 -4.4; 73 -4.6; 78 -4.7; 83 -4.9; 89 -5.2; 95 -5.4; 102 -5.4; 109 -5.5; 117 -5.5; 125 -5.6; 134 -5.7; 143 -5.7; 153 -5.6; 164 -5.6; 175 -5.4; 188 -5.3; 201 -5.1; 215 -4.9; 230 -4.6; 246 -4.4; 263 -4.1; 282 -3.7; 301 -3.4; 323 -3.1; 345 -2.5; 369 -2.4; 395 -2.0; 423 -1.4; 452 -1.1; 484 -1.0; 518 0.1; 554 0.5; 593 0.8; 635 1.1; 679 1.0; 726 1.2; 777 1.4; 832 1.2; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.4; 1248 -2.4; 1336 -3.6; 1429 -5.0; 1529 -6.2; 1636 -7.1; 1751 -7.2; 1873 -6.6; 2004 -5.6; 2145 -4.7; 2295 -4.1; 2455 -3.8; 2627 -4.1; 2811 -4.3; 3008 -1.8; 3219 1.2; 3444 4.7; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.6; 6331 3.7; 6775 -0.0; 7249 -5.0; 7756 -8.5; 8299 -10.3; 8880 -10.0; 9502 -7.9; 10167 -4.3; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999892437424dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A83 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 134 Hz   | 0.37 | -6.0 dB  |
| Peaking | 1690 Hz  | 1.31 | -15.6 dB |
| Peaking | 2756 Hz  | 1.75 | -14.1 dB |
| Peaking | 3300 Hz  | 0.38 | 17.5 dB  |
| Peaking | 8444 Hz  | 1.88 | -19.6 dB |
| Peaking | 624 Hz   | 4.09 | 0.8 dB   |
| Peaking | 4713 Hz  | 3.61 | -1.9 dB  |
| Peaking | 6237 Hz  | 2.03 | 2.9 dB   |
| Peaking | 7291 Hz  | 6    | -3.8 dB  |
| Peaking | 16361 Hz | 1.55 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A83/Fidue%20A83.png)