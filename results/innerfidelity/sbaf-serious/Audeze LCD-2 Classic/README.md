# Audeze LCD-2 Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.7; 22 5.7; 23 5.6; 25 5.6; 26 5.5; 28 5.5; 30 5.4; 32 5.3; 35 5.3; 37 5.2; 40 5.1; 42 5.0; 45 5.0; 49 4.8; 52 4.7; 56 4.5; 59 4.4; 64 4.2; 68 4.0; 73 3.7; 78 3.4; 83 3.2; 89 2.9; 95 2.7; 102 2.5; 109 2.5; 117 2.3; 125 2.1; 134 1.9; 143 1.7; 153 1.6; 164 1.5; 175 1.4; 188 1.2; 201 1.2; 215 1.1; 230 1.1; 246 1.0; 263 0.9; 282 0.9; 301 0.8; 323 0.7; 345 0.7; 369 0.6; 395 0.5; 423 0.7; 452 0.8; 484 0.7; 518 0.7; 554 0.9; 593 1.0; 635 0.5; 679 0.0; 726 -0.3; 777 -0.4; 832 -0.6; 890 -0.2; 952 0.3; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.4; 1336 0.0; 1429 0.3; 1529 -0.6; 1636 -1.0; 1751 -0.5; 1873 0.7; 2004 1.5; 2145 0.9; 2295 1.5; 2455 3.2; 2627 3.7; 2811 3.8; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.8; 5917 3.5; 6331 3.0; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999996093441dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.52 | 4.0 dB  |
| Peaking | 41 Hz   | 0.39 | 4.1 dB  |
| Peaking | 482 Hz  | 2.27 | 0.5 dB  |
| Peaking | 1655 Hz | 4.04 | -2.1 dB |
| Peaking | 4023 Hz | 1.12 | 6.8 dB  |
| Peaking | 349 Hz  | 0.55 | 0.1 dB  |
| Peaking | 811 Hz  | 4.86 | -1.1 dB |
| Peaking | 4195 Hz | 3.36 | -2.3 dB |
| Peaking | 5153 Hz | 1.23 | 2.2 dB  |
| Peaking | 8363 Hz | 1.61 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)