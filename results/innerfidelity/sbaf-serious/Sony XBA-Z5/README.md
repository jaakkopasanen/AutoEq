# Sony XBA-Z5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.7; 23 -3.8; 25 -3.9; 26 -4.0; 28 -4.1; 30 -4.1; 32 -4.2; 35 -4.3; 37 -4.3; 40 -4.3; 42 -4.3; 45 -4.3; 49 -4.3; 52 -4.3; 56 -4.3; 59 -4.4; 64 -4.4; 68 -4.5; 73 -4.5; 78 -4.6; 83 -4.9; 89 -5.1; 95 -5.5; 102 -6.0; 109 -6.3; 117 -6.7; 125 -7.2; 134 -7.5; 143 -7.7; 153 -7.7; 164 -7.7; 175 -7.5; 188 -7.3; 201 -7.0; 215 -6.7; 230 -6.3; 246 -6.0; 263 -5.6; 282 -5.2; 301 -4.8; 323 -4.4; 345 -3.9; 369 -3.4; 395 -3.2; 423 -2.8; 452 -2.4; 484 -2.2; 518 -1.9; 554 -1.4; 593 -1.0; 635 -0.6; 679 -0.2; 726 0.3; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.3; 1248 -0.4; 1336 -0.6; 1429 -0.7; 1529 -0.8; 1636 -0.8; 1751 -0.4; 1873 0.1; 2004 0.8; 2145 1.4; 2295 1.7; 2455 2.3; 2627 3.0; 2811 3.6; 3008 3.9; 3219 4.9; 3444 5.2; 3685 4.3; 3943 2.3; 4219 0.3; 4514 -0.8; 4830 -0.7; 5168 0.9; 5530 3.3; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.3; 10167 -4.3; 10879 -5.2; 11640 -3.9; 12455 -2.2; 13327 -2.0; 14260 -2.2; 15258 -0.6; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.47 | -3.6 dB |
| Peaking | 169 Hz   | 0.68 | -7.3 dB |
| Peaking | 3185 Hz  | 2.82 | 5.3 dB  |
| Peaking | 6165 Hz  | 4.96 | 6.5 dB  |
| Peaking | 10916 Hz | 2.78 | -5.3 dB |
| Peaking | 777 Hz   | 3.69 | 1.3 dB  |
| Peaking | 1549 Hz  | 3.23 | -1.3 dB |
| Peaking | 4557 Hz  | 0.44 | 0.8 dB  |
| Peaking | 4634 Hz  | 5    | -3.4 dB |
| Peaking | 14148 Hz | 5.09 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20XBA-Z5/Sony%20XBA-Z5.png)