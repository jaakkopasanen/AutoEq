# Audio Technica ATH-FC700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.8; 68 5.4; 73 4.9; 78 4.7; 83 4.3; 89 3.5; 95 2.9; 102 2.2; 109 1.7; 117 1.2; 125 0.6; 134 0.1; 143 -0.1; 153 -0.3; 164 -0.2; 175 -0.2; 188 -0.1; 201 -0.1; 215 0.1; 230 0.1; 246 -0.3; 263 -0.5; 282 -0.4; 301 -0.3; 323 -0.4; 345 -0.7; 369 -0.7; 395 -0.5; 423 -0.3; 452 -0.2; 484 -0.2; 518 -0.3; 554 -0.1; 593 0.2; 635 0.4; 679 0.5; 726 0.6; 777 0.6; 832 0.4; 890 0.2; 952 0.1; 1019 0.1; 1090 0.0; 1167 -0.1; 1248 -0.1; 1336 -0.1; 1429 -0.8; 1529 -1.7; 1636 -2.4; 1751 -3.0; 1873 -3.3; 2004 -3.4; 2145 -3.3; 2295 -2.8; 2455 -1.7; 2627 -0.6; 2811 -0.1; 3008 0.9; 3219 1.6; 3444 2.5; 3685 3.7; 3943 4.6; 4219 4.0; 4514 4.1; 4830 5.2; 5168 6.0; 5530 0.4; 5917 -1.6; 6331 -2.2; 6775 -6.6; 7249 -8.0; 7756 -6.7; 8299 -4.6; 8880 -2.4; 9502 -1.2; 10167 -0.7; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.2; 15258 -2.5; 16326 -4.5; 17469 -4.8; 18692 -2.3; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-FC700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.64 | 7.0 dB   |
| Peaking | 2052 Hz  | 2.04 | -4.6 dB  |
| Peaking | 4706 Hz  | 1.3  | 6.8 dB   |
| Peaking | 7158 Hz  | 2.74 | -10.9 dB |
| Peaking | 30914 Hz | 2.5  | -5.6 dB  |
| Peaking | 37 Hz    | 1.11 | -4.5 dB  |
| Peaking | 66 Hz    | 0.13 | 3.8 dB   |
| Peaking | 141 Hz   | 1.06 | -4.1 dB  |
| Peaking | 334 Hz   | 0.94 | -2.7 dB  |
| Peaking | 12453 Hz | 2.53 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-FC700/Audio%20Technica%20ATH-FC700.png)