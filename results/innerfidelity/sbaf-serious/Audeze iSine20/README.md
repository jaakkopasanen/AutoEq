# Audeze iSine20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 5.9; 109 5.8; 117 5.5; 125 5.2; 134 5.0; 143 4.8; 153 4.6; 164 4.3; 175 4.2; 188 4.1; 201 4.0; 215 3.9; 230 3.9; 246 3.8; 263 3.7; 282 3.7; 301 3.6; 323 3.5; 345 3.4; 369 3.3; 395 3.2; 423 3.2; 452 3.2; 484 2.8; 518 2.7; 554 2.6; 593 2.6; 635 2.4; 679 1.9; 726 1.6; 777 1.5; 832 1.1; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -0.6; 1336 -0.3; 1429 -1.3; 1529 -2.1; 1636 -1.8; 1751 -0.6; 1873 1.0; 2004 2.7; 2145 4.3; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 145 Hz  | 0.13 | 11.0 dB |
| Peaking | 582 Hz  | 0.09 | -6.9 dB |
| Peaking | 2381 Hz | 3.03 | 6.5 dB  |
| Peaking | 3480 Hz | 1.5  | 7.8 dB  |
| Peaking | 5593 Hz | 1.74 | 7.4 dB  |
| Peaking | 14 Hz   | 1.87 | 1.4 dB  |
| Peaking | 215 Hz  | 2.2  | -0.5 dB |
| Peaking | 629 Hz  | 2.21 | 0.7 dB  |
| Peaking | 1588 Hz | 5.35 | -1.9 dB |
| Peaking | 1995 Hz | 6.56 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20iSine20/Audeze%20iSine20.png)