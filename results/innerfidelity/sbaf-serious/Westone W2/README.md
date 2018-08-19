# Westone W2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.9; 22 2.8; 23 2.8; 25 2.7; 26 2.7; 28 2.6; 30 2.5; 32 2.5; 35 2.4; 37 2.3; 40 2.1; 42 2.0; 45 1.9; 49 1.8; 52 1.6; 56 1.5; 59 1.3; 64 1.1; 68 0.8; 73 0.5; 78 0.2; 83 -0.1; 89 -0.4; 95 -0.7; 102 -0.9; 109 -1.1; 117 -1.3; 125 -1.5; 134 -1.7; 143 -1.9; 153 -2.0; 164 -2.2; 175 -2.3; 188 -2.4; 201 -2.4; 215 -2.4; 230 -2.4; 246 -2.3; 263 -2.4; 282 -2.3; 301 -2.2; 323 -2.1; 345 -1.9; 369 -1.8; 395 -1.7; 423 -1.4; 452 -1.2; 484 -1.1; 518 -0.8; 554 -0.4; 593 -0.0; 635 0.2; 679 0.2; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.7; 1636 -2.0; 1751 -2.1; 1873 -2.1; 2004 -1.9; 2145 -1.6; 2295 -0.9; 2455 0.5; 2627 2.1; 2811 4.0; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.6; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999259688dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.74 | 2.8 dB  |
| Peaking | 52 Hz   | 1.53 | 1.0 dB  |
| Peaking | 206 Hz  | 0.72 | -2.7 dB |
| Peaking | 1988 Hz | 1.71 | -5.2 dB |
| Peaking | 3770 Hz | 0.9  | 7.6 dB  |
| Peaking | 775 Hz  | 2.21 | 1.3 dB  |
| Peaking | 1837 Hz | 0.17 | -0.3 dB |
| Peaking | 2981 Hz | 8.67 | 1.8 dB  |
| Peaking | 6260 Hz | 2.81 | 5.8 dB  |
| Peaking | 7034 Hz | 1.33 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W2/Westone%20W2.png)