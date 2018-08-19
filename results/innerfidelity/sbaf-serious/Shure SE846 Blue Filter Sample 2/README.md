# Shure SE846 Blue Filter Sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.6; 23 -3.6; 25 -3.7; 26 -3.7; 28 -3.7; 30 -3.6; 32 -3.6; 35 -3.6; 37 -3.6; 40 -3.5; 42 -3.5; 45 -3.5; 49 -3.5; 52 -3.5; 56 -3.5; 59 -3.5; 64 -3.5; 68 -3.5; 73 -3.5; 78 -3.6; 83 -3.6; 89 -3.6; 95 -3.7; 102 -3.6; 109 -3.5; 117 -3.4; 125 -3.3; 134 -3.3; 143 -3.2; 153 -3.1; 164 -2.9; 175 -2.7; 188 -2.5; 201 -2.4; 215 -2.1; 230 -2.0; 246 -1.8; 263 -1.7; 282 -1.4; 301 -1.3; 323 -1.2; 345 -1.0; 369 -0.8; 395 -0.8; 423 -0.5; 452 -0.4; 484 -0.4; 518 -0.3; 554 -0.1; 593 0.2; 635 0.3; 679 0.3; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.1; 1529 -1.3; 1636 -1.4; 1751 -1.4; 1873 -1.2; 2004 -0.8; 2145 -0.3; 2295 0.5; 2455 1.8; 2627 3.6; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 5.3; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678131dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.18 | -3.7 dB |
| Peaking | 701 Hz  | 0.79 | 1.1 dB  |
| Peaking | 1927 Hz | 1.15 | -3.7 dB |
| Peaking | 3219 Hz | 1.4  | 7.4 dB  |
| Peaking | 5614 Hz | 2.71 | 5.0 dB  |
| Peaking | 4654 Hz | 3.06 | 1.2 dB  |
| Peaking | 6492 Hz | 5.21 | 3.7 dB  |
| Peaking | 6788 Hz | 1.53 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Blue%20Filter%20Sample%202/Shure%20SE846%20Blue%20Filter%20Sample%202.png)