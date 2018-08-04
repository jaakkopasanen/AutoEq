# Audio Technica ATH-ANC7b

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.6; 32 5.3; 35 4.8; 37 4.6; 40 4.3; 42 4.1; 45 3.8; 49 3.6; 52 3.4; 56 3.2; 59 3.1; 64 3.0; 68 2.8; 73 2.6; 78 2.5; 83 2.4; 89 2.1; 95 1.8; 102 1.6; 109 1.3; 117 1.1; 125 0.9; 134 0.7; 143 0.5; 153 0.4; 164 0.5; 175 0.8; 188 0.9; 201 1.0; 215 1.2; 230 1.4; 246 1.6; 263 1.8; 282 2.1; 301 2.4; 323 2.6; 345 2.7; 369 2.8; 395 2.9; 423 2.9; 452 2.9; 484 2.6; 518 2.6; 554 2.7; 593 2.8; 635 2.9; 679 2.5; 726 1.7; 777 0.5; 832 0.1; 890 -0.4; 952 -0.1; 1019 -0.2; 1090 -0.1; 1167 1.3; 1248 4.4; 1336 6.0; 1429 5.6; 1529 5.6; 1636 6.0; 1751 6.0; 1873 5.9; 2004 5.2; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.68 | 6.1 dB  |
| Peaking | 69 Hz   | 1.72 | 1.3 dB  |
| Peaking | 391 Hz  | 1.12 | 2.0 dB  |
| Peaking | 963 Hz  | 2.53 | -5.2 dB |
| Peaking | 2368 Hz | 0.4  | 6.8 dB  |
| Peaking | 153 Hz  | 4.65 | -0.6 dB |
| Peaking | 1347 Hz | 8.8  | 2.1 dB  |
| Peaking | 2378 Hz | 1.53 | -0.8 dB |
| Peaking | 6247 Hz | 1.66 | 6.7 dB  |
| Peaking | 7430 Hz | 1.33 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC7b/Audio%20Technica%20ATH-ANC7b.png)