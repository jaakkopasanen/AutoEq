# Audio Technica ATH A1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.7; 23 5.5; 25 5.0; 26 4.6; 28 4.0; 30 3.4; 32 2.9; 35 2.2; 37 1.8; 40 1.3; 42 1.0; 45 0.6; 49 0.2; 52 -0.1; 56 -0.2; 59 -0.3; 64 -0.3; 68 -0.2; 73 0.2; 78 0.6; 83 0.6; 89 0.6; 95 0.7; 102 0.3; 109 -0.5; 117 -1.5; 125 -2.2; 134 -2.3; 143 -2.2; 153 -1.6; 164 -0.5; 175 -0.9; 188 -1.2; 201 -0.9; 215 -0.3; 230 0.3; 246 0.7; 263 1.0; 282 1.1; 301 1.1; 323 1.1; 345 1.1; 369 1.0; 395 0.9; 423 0.9; 452 0.8; 484 0.6; 518 0.5; 554 0.5; 593 0.6; 635 0.6; 679 0.4; 726 0.3; 777 0.4; 832 0.4; 890 0.2; 952 0.0; 1019 0.0; 1090 -0.2; 1167 -0.2; 1248 0.1; 1336 -0.4; 1429 -0.5; 1529 -0.4; 1636 -0.2; 1751 -0.3; 1873 -2.1; 2004 -4.1; 2145 -3.3; 2295 -1.0; 2455 1.0; 2627 3.0; 2811 4.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 3.1; 4830 5.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -2.1; 18692 -2.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH A1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.53 | 6.0 dB  |
| Peaking | 135 Hz   | 3.97 | -2.7 dB |
| Peaking | 2079 Hz  | 3.89 | -6.2 dB |
| Peaking | 3297 Hz  | 1.56 | 6.6 dB  |
| Peaking | 5732 Hz  | 3.13 | 5.3 dB  |
| Peaking | 145 Hz   | 0.35 | -1.0 dB |
| Peaking | 94 Hz    | 2.64 | 1.6 dB  |
| Peaking | 322 Hz   | 1.09 | 1.9 dB  |
| Peaking | 8234 Hz  | 4.61 | -1.2 dB |
| Peaking | 29515 Hz | 2.85 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH%20A1000X/Audio%20Technica%20ATH%20A1000X.png)