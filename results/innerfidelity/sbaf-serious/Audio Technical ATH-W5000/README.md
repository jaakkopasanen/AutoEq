# Audio Technical ATH-W5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.5; 59 5.1; 64 4.5; 68 4.2; 73 3.8; 78 3.8; 83 3.5; 89 3.3; 95 2.9; 102 2.4; 109 2.1; 117 1.8; 125 1.4; 134 1.1; 143 0.8; 153 0.7; 164 0.8; 175 0.8; 188 0.6; 201 0.6; 215 0.6; 230 0.9; 246 0.7; 263 0.7; 282 0.8; 301 0.7; 323 1.0; 345 1.5; 369 1.5; 395 1.7; 423 1.9; 452 2.1; 484 2.3; 518 2.3; 554 2.7; 593 2.6; 635 2.3; 679 1.7; 726 1.1; 777 1.3; 832 1.2; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.3; 1336 -1.7; 1429 -2.0; 1529 -2.3; 1636 -2.6; 1751 -2.7; 1873 -3.3; 2004 -3.8; 2145 -3.1; 2295 -1.8; 2455 0.1; 2627 1.9; 2811 4.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.2; 3943 2.2; 4219 2.2; 4514 4.7; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.51 | 6.5 dB  |
| Peaking | 560 Hz  | 1.34 | 2.7 dB  |
| Peaking | 2083 Hz | 1.26 | -5.5 dB |
| Peaking | 3069 Hz | 2.27 | 8.7 dB  |
| Peaking | 5613 Hz | 2.68 | 6.4 dB  |
| Peaking | 32 Hz   | 1.46 | -1.9 dB |
| Peaking | 20 Hz   | 0.28 | 1.3 dB  |
| Peaking | 148 Hz  | 1.99 | -0.8 dB |
| Peaking | 6598 Hz | 7.49 | 2.3 dB  |
| Peaking | 7697 Hz | 2.26 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-W5000/Audio%20Technical%20ATH-W5000.png)