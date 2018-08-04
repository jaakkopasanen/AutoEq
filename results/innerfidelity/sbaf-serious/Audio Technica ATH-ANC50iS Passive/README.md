# Audio Technica ATH-ANC50iS Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -0.5; 22 -1.3; 23 -1.7; 25 -2.3; 26 -2.6; 28 -3.2; 30 -3.7; 32 -4.1; 35 -4.5; 37 -4.8; 40 -5.0; 42 -5.2; 45 -5.4; 49 -5.6; 52 -5.6; 56 -5.7; 59 -5.7; 64 -5.7; 68 -5.6; 73 -5.5; 78 -5.4; 83 -5.7; 89 -6.1; 95 -6.5; 102 -7.0; 109 -7.2; 117 -7.4; 125 -7.8; 134 -8.2; 143 -8.4; 153 -8.6; 164 -8.6; 175 -8.7; 188 -9.0; 201 -9.0; 215 -9.1; 230 -9.0; 246 -9.0; 263 -8.9; 282 -8.5; 301 -7.8; 323 -7.3; 345 -7.0; 369 -7.2; 395 -7.0; 423 -7.0; 452 -7.0; 484 -6.6; 518 -5.6; 554 -3.9; 593 -2.2; 635 -0.6; 679 0.6; 726 1.1; 777 1.8; 832 1.7; 890 0.1; 952 -0.3; 1019 0.4; 1090 1.8; 1167 2.8; 1248 4.0; 1336 4.9; 1429 5.7; 1529 6.0; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC50iS Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.33 | -4.9 dB |
| Peaking | 233 Hz  | 0.79 | -6.6 dB |
| Peaking | 460 Hz  | 3.06 | -4.2 dB |
| Peaking | 2080 Hz | 0.65 | 6.5 dB  |
| Peaking | 5162 Hz | 1.92 | 4.5 dB  |
| Peaking | 17 Hz   | 2.2  | 1.3 dB  |
| Peaking | 766 Hz  | 3.48 | 2.2 dB  |
| Peaking | 951 Hz  | 5.41 | -3.0 dB |
| Peaking | 6390 Hz | 5.09 | 2.9 dB  |
| Peaking | 7813 Hz | 1.86 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC50iS%20Passive/Audio%20Technica%20ATH-ANC50iS%20Passive.png)