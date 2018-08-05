# Audio Technica ATH-IM02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.2; 22 2.1; 23 2.1; 25 2.0; 26 1.9; 28 1.8; 30 1.7; 32 1.7; 35 1.6; 37 1.6; 40 1.5; 42 1.5; 45 1.4; 49 1.4; 52 1.3; 56 1.3; 59 1.2; 64 1.1; 68 1.0; 73 0.9; 78 0.7; 83 0.4; 89 0.0; 95 -0.4; 102 -1.0; 109 -1.5; 117 -2.0; 125 -2.6; 134 -3.1; 143 -3.5; 153 -3.7; 164 -3.8; 175 -3.8; 188 -3.9; 201 -3.9; 215 -3.7; 230 -3.6; 246 -3.6; 263 -3.5; 282 -3.3; 301 -3.2; 323 -3.0; 345 -2.7; 369 -2.6; 395 -2.4; 423 -2.0; 452 -1.8; 484 -1.6; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.3; 832 0.3; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.0; 1751 -2.3; 1873 -2.4; 2004 -2.6; 2145 -2.5; 2295 -2.0; 2455 -0.7; 2627 1.6; 2811 4.2; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.6; 4514 3.4; 4830 2.1; 5168 0.4; 5530 -0.1; 5917 1.3; 6331 2.7; 6775 2.6; 7249 0.7; 7756 -0.9; 8299 -0.3; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -1.1; 15258 -0.1; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.22 | 2.5 dB  |
| Peaking | 184 Hz  | 0.69 | -5.8 dB |
| Peaking | 2226 Hz | 1.79 | -5.8 dB |
| Peaking | 3067 Hz | 1.82 | 7.9 dB  |
| Peaking | 3963 Hz | 4.46 | 2.9 dB  |
| Peaking | 390 Hz  | 1.99 | -0.7 dB |
| Peaking | 799 Hz  | 2.5  | 1.0 dB  |
| Peaking | 5472 Hz | 6.85 | -2.3 dB |
| Peaking | 6591 Hz | 3.91 | 3.3 dB  |
| Peaking | 7677 Hz | 4.47 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)