# BlueAnt Embrace

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.6; 52 4.9; 56 4.2; 59 3.8; 64 3.3; 68 2.8; 73 2.1; 78 1.6; 83 1.1; 89 0.4; 95 -0.2; 102 -0.6; 109 -0.9; 117 -1.2; 125 -1.7; 134 -2.2; 143 -2.5; 153 -2.7; 164 -2.6; 175 -2.8; 188 -2.8; 201 -2.8; 215 -2.4; 230 -1.8; 246 -1.4; 263 -1.4; 282 -1.1; 301 -1.0; 323 -0.5; 345 0.2; 369 1.0; 395 1.9; 423 3.0; 452 3.8; 484 4.5; 518 4.9; 554 5.4; 593 5.9; 635 5.9; 679 5.6; 726 4.7; 777 3.5; 832 2.2; 890 1.2; 952 0.4; 1019 -0.2; 1090 -0.5; 1167 -0.6; 1248 -0.7; 1336 -0.8; 1429 -1.0; 1529 -1.3; 1636 -1.4; 1751 -1.1; 1873 -0.6; 2004 0.1; 2145 1.7; 2295 2.7; 2455 3.4; 2627 5.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.8; 4830 3.0; 5168 -0.0; 5530 -0.3; 5917 1.1; 6331 2.3; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BlueAnt Embrace ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.41 | 6.9 dB  |
| Peaking | 144 Hz   |  0.63 | -4.6 dB |
| Peaking | 570 Hz   |  1.92 | 6.9 dB  |
| Peaking | 3505 Hz  |  1.8  | 7.0 dB  |
| Peaking | 24000 Hz |  2.27 | 0.6 dB  |
| Peaking | 722 Hz   |  5.57 | 2.0 dB  |
| Peaking | 1563 Hz  |  1.23 | -2.4 dB |
| Peaking | 2605 Hz  |  3.54 | 2.6 dB  |
| Peaking | 5370 Hz  | 11.05 | -2.9 dB |
| Peaking | 6692 Hz  |  9.68 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BlueAnt%20Embrace/BlueAnt%20Embrace.png)