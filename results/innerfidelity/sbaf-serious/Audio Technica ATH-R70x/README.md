# Audio Technica ATH-R70x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.3dB
GraphicEQ: 10 -84; 20 6.7; 22 5.8; 23 5.3; 25 4.6; 26 4.2; 28 3.6; 30 3.0; 32 2.5; 35 1.8; 37 1.4; 40 0.9; 42 0.6; 45 0.2; 49 -0.2; 52 -0.4; 56 -0.7; 59 -0.9; 64 -1.1; 68 -1.2; 73 -1.4; 78 -1.5; 83 -1.6; 89 -1.5; 95 -1.4; 102 -1.9; 109 -2.5; 117 -2.8; 125 -3.2; 134 -3.3; 143 -3.4; 153 -3.5; 164 -3.5; 175 -3.4; 188 -3.4; 201 -3.3; 215 -3.1; 230 -2.9; 246 -2.9; 263 -2.7; 282 -2.5; 301 -2.3; 323 -2.2; 345 -1.9; 369 -1.8; 395 -1.6; 423 -1.4; 452 -1.2; 484 -1.3; 518 -1.1; 554 -0.9; 593 -0.7; 635 -0.6; 679 -0.7; 726 -0.8; 777 -0.4; 832 -0.4; 890 -0.5; 952 -0.3; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.2; 1429 -1.7; 1529 -2.2; 1636 -2.7; 1751 -2.8; 1873 -2.5; 2004 -2.2; 2145 -1.7; 2295 -1.1; 2455 -0.3; 2627 0.8; 2811 2.8; 3008 2.0; 3219 1.5; 3444 -0.1; 3685 -0.5; 3943 0.7; 4219 1.7; 4514 2.6; 4830 3.8; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -1.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.3dB` and instead set Global volume in the UI for both channels to **-73**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-R70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.39 | 6.5 dB  |
| Peaking | 174 Hz  |  0.61 | -3.5 dB |
| Peaking | 1815 Hz |  2.08 | -2.9 dB |
| Peaking | 2857 Hz |  6.72 | 3.2 dB  |
| Peaking | 5681 Hz |  2.94 | 6.8 dB  |
| Peaking | 28 Hz   |  1.9  | 0.5 dB  |
| Peaking | 1041 Hz |  4.9  | 0.5 dB  |
| Peaking | 3620 Hz | 13.28 | -1.6 dB |
| Peaking | 6541 Hz | 10.53 | 1.8 dB  |
| Peaking | 8889 Hz |  3.15 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-R70x/Audio%20Technica%20ATH-R70x.png)