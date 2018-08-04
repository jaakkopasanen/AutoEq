# Audio Technica ATH-ES55

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 5.7; 125 4.7; 134 4.1; 143 3.6; 153 3.3; 164 3.4; 175 3.1; 188 2.7; 201 2.5; 215 2.3; 230 2.2; 246 2.1; 263 2.1; 282 2.6; 301 2.9; 323 3.0; 345 2.6; 369 2.5; 395 2.4; 423 2.7; 452 2.7; 484 2.6; 518 2.6; 554 2.8; 593 2.8; 635 2.5; 679 2.1; 726 1.7; 777 1.4; 832 0.9; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.6; 1529 -2.0; 1636 -2.2; 1751 -1.9; 1873 -1.5; 2004 -0.7; 2145 0.2; 2295 1.3; 2455 2.8; 2627 3.9; 2811 4.7; 3008 5.4; 3219 5.5; 3444 5.3; 3685 5.1; 3943 5.4; 4219 5.4; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -1.6; 16326 -1.3; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.28 | 6.5 dB  |
| Peaking | 539 Hz   | 1.16 | 2.4 dB  |
| Peaking | 1732 Hz  | 1.35 | -4.0 dB |
| Peaking | 3123 Hz  | 1.3  | 6.1 dB  |
| Peaking | 5487 Hz  | 2.43 | 5.2 dB  |
| Peaking | 2 Hz     | 1.75 | 0.2 dB  |
| Peaking | 108 Hz   | 5.86 | 1.2 dB  |
| Peaking | 6515 Hz  | 6.76 | 2.4 dB  |
| Peaking | 7769 Hz  | 2.32 | -1.7 dB |
| Peaking | 32205 Hz | 4.11 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ES55/Audio%20Technica%20ATH-ES55.png)