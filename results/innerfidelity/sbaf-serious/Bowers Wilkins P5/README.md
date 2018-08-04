# Bowers Wilkins P5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 4.6; 22 4.4; 23 4.2; 25 4.0; 26 3.8; 28 3.6; 30 3.4; 32 3.2; 35 2.9; 37 2.7; 40 2.5; 42 2.3; 45 2.1; 49 1.8; 52 1.6; 56 1.4; 59 1.2; 64 0.8; 68 0.5; 73 0.1; 78 -0.2; 83 -0.7; 89 -1.2; 95 -1.8; 102 -2.4; 109 -2.9; 117 -3.4; 125 -4.1; 134 -4.6; 143 -4.9; 153 -5.2; 164 -5.5; 175 -5.3; 188 -5.6; 201 -5.7; 215 -5.6; 230 -5.4; 246 -5.0; 263 -4.6; 282 -3.9; 301 -3.1; 323 -2.4; 345 -1.7; 369 -1.2; 395 -0.6; 423 0.1; 452 0.4; 484 0.5; 518 0.4; 554 0.5; 593 0.6; 635 0.4; 679 0.2; 726 0.1; 777 0.2; 832 0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.5; 1429 -0.9; 1529 -1.4; 1636 -1.8; 1751 -2.0; 1873 -2.3; 2004 -2.3; 2145 -2.6; 2295 -3.2; 2455 -2.8; 2627 -2.2; 2811 -1.8; 3008 -1.5; 3219 -1.0; 3444 -0.1; 3685 0.3; 3943 1.5; 4219 1.7; 4514 1.8; 4830 2.1; 5168 2.8; 5530 2.7; 5917 3.3; 6331 3.7; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -0.2; 18692 -0.7; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers Wilkins P5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.84 | 4.4 dB  |
| Peaking | 51 Hz   | 1.64 | 1.1 dB  |
| Peaking | 178 Hz  | 1.08 | -6.3 dB |
| Peaking | 2277 Hz | 1.94 | -3.3 dB |
| Peaking | 5711 Hz | 1.9  | 3.7 dB  |
| Peaking | 181 Hz  | 2.94 | 2.0 dB  |
| Peaking | 252 Hz  | 0.88 | -2.1 dB |
| Peaking | 455 Hz  | 1.2  | 2.2 dB  |
| Peaking | 4046 Hz | 9.76 | 1.0 dB  |
| Peaking | 8418 Hz | 4.48 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20Wilkins%20P5/Bowers%20Wilkins%20P5.png)