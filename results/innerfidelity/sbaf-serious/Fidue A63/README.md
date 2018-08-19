# Fidue A63

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 0.0; 22 -0.4; 23 -0.6; 25 -1.0; 26 -1.2; 28 -1.7; 30 -2.2; 32 -2.5; 35 -3.0; 37 -3.3; 40 -3.7; 42 -3.9; 45 -4.3; 49 -4.6; 52 -4.9; 56 -5.2; 59 -5.4; 64 -5.8; 68 -6.2; 73 -6.4; 78 -6.8; 83 -7.1; 89 -7.3; 95 -7.6; 102 -7.9; 109 -7.9; 117 -8.1; 125 -8.1; 134 -8.3; 143 -8.3; 153 -8.4; 164 -8.3; 175 -8.1; 188 -8.0; 201 -7.9; 215 -7.6; 230 -7.4; 246 -7.1; 263 -6.9; 282 -6.5; 301 -6.2; 323 -5.8; 345 -5.4; 369 -5.0; 395 -4.7; 423 -4.1; 452 -3.7; 484 -3.4; 518 -3.0; 554 -2.4; 593 -1.8; 635 -1.5; 679 -1.2; 726 -1.2; 777 -0.8; 832 -0.7; 890 -0.3; 952 0.1; 1019 -0.0; 1090 -0.4; 1167 -0.9; 1248 -1.4; 1336 -1.9; 1429 -2.5; 1529 -3.0; 1636 -3.3; 1751 -3.4; 1873 -3.4; 2004 -3.2; 2145 -3.0; 2295 -2.8; 2455 -2.1; 2627 -1.4; 2811 -0.5; 3008 1.0; 3219 2.5; 3444 3.8; 3685 4.2; 3943 4.0; 4219 2.9; 4514 2.3; 4830 2.4; 5168 3.1; 5530 3.3; 5917 3.2; 6331 3.4; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.328848100145779dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A63 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.48 | -7.3 dB |
| Peaking | 262 Hz  | 0.9  | -3.4 dB |
| Peaking | 1978 Hz | 1.67 | -3.9 dB |
| Peaking | 3655 Hz | 2.86 | 4.8 dB  |
| Peaking | 5955 Hz | 2.75 | 3.5 dB  |
| Peaking | 19 Hz   | 2.04 | 1.0 dB  |
| Peaking | 459 Hz  | 3.1  | -0.6 dB |
| Peaking | 991 Hz  | 1.77 | 1.3 dB  |
| Peaking | 1427 Hz | 3.41 | -1.1 dB |
| Peaking | 8343 Hz | 5.07 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A63/Fidue%20A63.png)