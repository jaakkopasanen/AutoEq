# LG Quadbeat HSS-F420

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.2; 23 -1.2; 25 -1.3; 26 -1.3; 28 -1.4; 30 -1.4; 32 -1.5; 35 -1.5; 37 -1.5; 40 -1.5; 42 -1.5; 45 -1.5; 49 -1.5; 52 -1.5; 56 -1.5; 59 -1.6; 64 -1.6; 68 -1.7; 73 -1.8; 78 -1.9; 83 -2.2; 89 -2.6; 95 -3.0; 102 -3.5; 109 -4.0; 117 -4.5; 125 -5.0; 134 -5.4; 143 -5.7; 153 -5.9; 164 -5.9; 175 -5.9; 188 -5.8; 201 -5.7; 215 -5.5; 230 -5.3; 246 -5.2; 263 -4.9; 282 -4.7; 301 -4.4; 323 -4.1; 345 -3.8; 369 -3.5; 395 -3.2; 423 -2.8; 452 -2.4; 484 -2.2; 518 -1.9; 554 -1.4; 593 -0.9; 635 -0.7; 679 -0.5; 726 -0.2; 777 0.2; 832 0.3; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.6; 1429 -1.0; 1529 -1.3; 1636 -1.5; 1751 -1.6; 1873 -1.4; 2004 -1.3; 2145 -1.3; 2295 -1.3; 2455 -1.0; 2627 -0.8; 2811 -0.4; 3008 0.5; 3219 1.4; 3444 2.4; 3685 2.5; 3943 2.2; 4219 1.2; 4514 0.5; 4830 0.6; 5168 1.3; 5530 1.2; 5917 0.8; 6331 0.8; 6775 0.8; 7249 0.5; 7756 -0.0; 8299 -0.8; 8880 -1.3; 9502 -1.2; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -2.0; 16326 -2.9; 17469 -0.6; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.0dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LG Quadbeat HSS-F420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.05 | -1.2 dB |
| Peaking | 187 Hz   | 0.69 | -6.1 dB |
| Peaking | 2171 Hz  | 1.71 | -1.8 dB |
| Peaking | 3648 Hz  | 2.38 | 2.9 dB  |
| Peaking | 16157 Hz | 4.41 | -3.4 dB |
| Peaking | 400 Hz   | 2.38 | -0.6 dB |
| Peaking | 832 Hz   | 1.92 | 1.1 dB  |
| Peaking | 1580 Hz  | 4.79 | -0.7 dB |
| Peaking | 6341 Hz  | 2.91 | 0.9 dB  |
| Peaking | 8902 Hz  | 4.99 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/LG%20Quadbeat%20HSS-F420/LG%20Quadbeat%20HSS-F420.png)