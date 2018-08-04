# Audio Technica ATH-AD700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.6; 95 5.0; 102 4.4; 109 4.1; 117 3.6; 125 3.0; 134 2.6; 143 2.3; 153 2.0; 164 2.0; 175 1.8; 188 1.7; 201 1.6; 215 1.5; 230 1.5; 246 1.4; 263 1.4; 282 1.5; 301 1.6; 323 1.6; 345 1.6; 369 1.6; 395 1.7; 423 1.8; 452 1.7; 484 1.6; 518 1.5; 554 1.6; 593 1.7; 635 1.6; 679 1.5; 726 1.3; 777 1.3; 832 1.0; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.1; 1167 -0.4; 1248 -0.6; 1336 -0.8; 1429 -1.1; 1529 -1.0; 1636 -0.6; 1751 -0.7; 1873 -0.5; 2004 -0.3; 2145 -0.1; 2295 0.5; 2455 1.0; 2627 1.3; 2811 1.0; 3008 1.2; 3219 0.8; 3444 2.3; 3685 4.7; 3943 4.4; 4219 1.4; 4514 0.1; 4830 1.4; 5168 4.2; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.8; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 47 Hz   |  0.23 | 6.5 dB  |
| Peaking | 577 Hz  |  2.09 | 1.2 dB  |
| Peaking | 162 Hz  |  1.2  | -2.4 dB |
| Peaking | 3745 Hz |  6.86 | 4.7 dB  |
| Peaking | 5914 Hz |  3.88 | 6.7 dB  |
| Peaking | 12 Hz   |  1.96 | 1.1 dB  |
| Peaking | 1491 Hz |  2.26 | -1.3 dB |
| Peaking | 2597 Hz |  4.91 | 1.2 dB  |
| Peaking | 4512 Hz | 13.31 | -1.8 dB |
| Peaking | 9712 Hz |  5.03 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD700/Audio%20Technica%20ATH-AD700.png)