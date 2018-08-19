# ZMF Atticus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.8; 22 2.0; 23 1.7; 25 1.2; 26 1.0; 28 0.7; 30 0.5; 32 0.2; 35 -0.2; 37 -0.4; 40 -0.7; 42 -0.9; 45 -1.3; 49 -1.7; 52 -1.9; 56 -2.1; 59 -2.2; 64 -2.6; 68 -3.1; 73 -3.8; 78 -4.3; 83 -4.8; 89 -5.4; 95 -5.9; 102 -6.3; 109 -6.4; 117 -6.8; 125 -7.0; 134 -7.1; 143 -7.1; 153 -6.8; 164 -6.0; 175 -6.4; 188 -6.1; 201 -5.5; 215 -5.0; 230 -4.4; 246 -3.9; 263 -3.4; 282 -3.1; 301 -2.9; 323 -2.7; 345 -2.6; 369 -2.6; 395 -2.5; 423 -2.1; 452 -2.1; 484 -2.3; 518 -2.1; 554 -1.9; 593 -1.8; 635 -1.7; 679 -1.7; 726 -1.6; 777 -1.1; 832 -0.9; 890 -0.8; 952 -0.3; 1019 0.2; 1090 0.2; 1167 0.5; 1248 0.6; 1336 0.8; 1429 1.1; 1529 3.3; 1636 3.3; 1751 0.8; 1873 0.3; 2004 0.6; 2145 -0.2; 2295 -0.7; 2455 -0.3; 2627 0.2; 2811 0.6; 3008 1.1; 3219 1.1; 3444 2.0; 3685 3.7; 3943 4.9; 4219 4.9; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.8; 7249 0.3; 7756 -1.5; 8299 -2.3; 8880 -2.8; 9502 -2.2; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099952559277957dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Atticus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.21 | 3.4 dB  |
| Peaking | 123 Hz  | 0.49 | -9.8 dB |
| Peaking | 1563 Hz | 8.11 | 3.9 dB  |
| Peaking | 5418 Hz | 1.44 | 7.5 dB  |
| Peaking | 8371 Hz | 2.63 | -5.3 dB |
| Peaking | 65 Hz   | 4.72 | 0.5 dB  |
| Peaking | 279 Hz  | 4.61 | 0.7 dB  |
| Peaking | 610 Hz  | 2.3  | -0.8 dB |
| Peaking | 2443 Hz | 3.42 | -1.4 dB |
| Peaking | 3871 Hz | 9.05 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Atticus/ZMF%20Atticus.png)