# Audio Technica ATH-IM02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.2; 22 2.0; 23 2.0; 25 1.8; 26 1.8; 28 1.7; 30 1.6; 32 1.5; 35 1.3; 37 1.2; 40 1.1; 42 1.0; 45 0.9; 49 0.6; 52 0.5; 56 0.3; 59 0.1; 64 -0.1; 68 -0.4; 73 -0.7; 78 -1.0; 83 -1.2; 89 -1.5; 95 -1.8; 102 -2.1; 109 -2.2; 117 -2.4; 125 -2.6; 134 -2.8; 143 -3.0; 153 -3.2; 164 -3.3; 175 -3.3; 188 -3.4; 201 -3.4; 215 -3.4; 230 -3.3; 246 -3.3; 263 -3.3; 282 -3.1; 301 -3.0; 323 -2.8; 345 -2.6; 369 -2.5; 395 -2.3; 423 -1.9; 452 -1.7; 484 -1.6; 518 -1.3; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.3; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.0; 1751 -2.3; 1873 -2.4; 2004 -2.6; 2145 -2.5; 2295 -2.0; 2455 -0.7; 2627 1.6; 2811 4.2; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.6; 4514 3.4; 4830 2.1; 5168 0.4; 5530 -0.1; 5917 1.3; 6331 2.7; 6775 2.6; 7249 0.7; 7756 -0.9; 8299 -0.3; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -1.1; 15258 -0.1; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999259689dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.57 | 2.1 dB  |
| Peaking | 194 Hz  | 0.63 | -3.7 dB |
| Peaking | 2217 Hz | 1.81 | -5.8 dB |
| Peaking | 3068 Hz | 1.81 | 7.9 dB  |
| Peaking | 3984 Hz | 4.51 | 2.9 dB  |
| Peaking | 828 Hz  | 2.44 | 1.0 dB  |
| Peaking | 1585 Hz | 5.6  | -0.8 dB |
| Peaking | 5504 Hz | 6.55 | -2.3 dB |
| Peaking | 6632 Hz | 3.66 | 3.3 dB  |
| Peaking | 7704 Hz | 4.32 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)