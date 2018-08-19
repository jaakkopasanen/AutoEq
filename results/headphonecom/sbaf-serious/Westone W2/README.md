# Westone W2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.8; 22 1.7; 23 1.6; 25 1.6; 26 1.5; 28 1.5; 30 1.5; 32 1.5; 35 1.4; 37 1.2; 40 1.1; 42 1.0; 45 0.9; 49 0.7; 52 0.6; 56 0.4; 59 0.3; 64 0.0; 68 -0.2; 73 -0.4; 78 -0.6; 83 -1.0; 89 -1.3; 95 -1.5; 102 -1.7; 109 -1.8; 117 -2.0; 125 -2.2; 134 -2.2; 143 -2.4; 153 -2.6; 164 -2.7; 175 -2.8; 188 -2.9; 201 -3.0; 215 -3.0; 230 -2.8; 246 -2.8; 263 -2.8; 282 -2.8; 301 -2.5; 323 -2.4; 345 -2.2; 369 -1.9; 395 -1.9; 423 -1.6; 452 -1.4; 484 -1.1; 518 -0.9; 554 -0.5; 593 -0.3; 635 0.0; 679 0.3; 726 0.5; 777 0.7; 832 0.7; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -2.0; 1636 -2.4; 1751 -2.5; 1873 -2.4; 2004 -2.3; 2145 -1.9; 2295 -1.0; 2455 0.4; 2627 2.3; 2811 4.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.8; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999437614dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.35 | 1.9 dB  |
| Peaking | 195 Hz  | 0.44 | -3.2 dB |
| Peaking | 749 Hz  | 1.61 | 1.6 dB  |
| Peaking | 1960 Hz | 1.5  | -5.8 dB |
| Peaking | 3709 Hz | 0.9  | 7.9 dB  |
| Peaking | 2972 Hz | 7.66 | 1.9 dB  |
| Peaking | 3875 Hz | 3.51 | -0.7 dB |
| Peaking | 6310 Hz | 2.41 | 5.0 dB  |
| Peaking | 7110 Hz | 0.68 | -1.5 dB |
| Peaking | 7489 Hz | 2.77 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20W2/Westone%20W2.png)