# Westone W2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.9; 22 2.9; 23 2.9; 25 2.8; 26 2.8; 28 2.7; 30 2.7; 32 2.7; 35 2.7; 37 2.7; 40 2.6; 42 2.5; 45 2.5; 49 2.5; 52 2.5; 56 2.4; 59 2.4; 64 2.3; 68 2.2; 73 2.0; 78 1.8; 83 1.6; 89 1.2; 95 0.7; 102 0.1; 109 -0.3; 117 -0.9; 125 -1.5; 134 -2.0; 143 -2.3; 153 -2.6; 164 -2.7; 175 -2.8; 188 -2.8; 201 -2.8; 215 -2.8; 230 -2.7; 246 -2.6; 263 -2.6; 282 -2.5; 301 -2.3; 323 -2.2; 345 -2.0; 369 -1.9; 395 -1.8; 423 -1.5; 452 -1.3; 484 -1.1; 518 -0.8; 554 -0.5; 593 -0.0; 635 0.1; 679 0.2; 726 0.3; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.7; 1636 -2.0; 1751 -2.1; 1873 -2.1; 2004 -1.9; 2145 -1.6; 2295 -0.9; 2455 0.5; 2627 2.1; 2811 4.0; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.6; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.38 | 2.8 dB  |
| Peaking | 76 Hz   | 1.2  | 1.9 dB  |
| Peaking | 183 Hz  | 0.7  | -3.6 dB |
| Peaking | 1989 Hz | 1.72 | -5.2 dB |
| Peaking | 3768 Hz | 0.9  | 7.6 dB  |
| Peaking | 779 Hz  | 2.2  | 1.3 dB  |
| Peaking | 3014 Hz | 8.66 | 1.9 dB  |
| Peaking | 1930 Hz | 0.16 | -0.3 dB |
| Peaking | 6185 Hz | 2.82 | 5.9 dB  |
| Peaking | 7091 Hz | 1.37 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W2/Westone%20W2.png)