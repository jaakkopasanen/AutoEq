# Audio Technica ATH-AD2000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.8; 83 5.5; 89 5.2; 95 4.8; 102 4.2; 109 3.6; 117 3.1; 125 2.6; 134 2.1; 143 1.8; 153 1.6; 164 1.5; 175 1.3; 188 1.1; 201 1.0; 215 0.9; 230 0.9; 246 0.9; 263 0.9; 282 0.9; 301 0.9; 323 0.9; 345 0.9; 369 0.8; 395 0.9; 423 1.0; 452 0.9; 484 0.7; 518 0.7; 554 0.8; 593 0.8; 635 0.7; 679 0.8; 726 0.7; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 0.1; 1090 0.2; 1167 0.2; 1248 0.5; 1336 0.4; 1429 0.5; 1529 0.8; 1636 1.1; 1751 2.1; 1873 3.3; 2004 4.5; 2145 5.7; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.8; 3685 2.9; 3943 2.4; 4219 3.6; 4514 5.3; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD2000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.22 | 6.4 dB  |
| Peaking | 201 Hz   | 1.17 | -2.0 dB |
| Peaking | 135 Hz   | 2.36 | -1.6 dB |
| Peaking | 2631 Hz  | 1.67 | 6.4 dB  |
| Peaking | 5482 Hz  | 2.45 | 6.0 dB  |
| Peaking | 1478 Hz  | 1.73 | -0.9 dB |
| Peaking | 2065 Hz  | 5.76 | 1.6 dB  |
| Peaking | 10343 Hz | 1.54 | -0.3 dB |
| Peaking | 6563 Hz  | 6.78 | 2.4 dB  |
| Peaking | 7615 Hz  | 2.7  | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD2000X/Audio%20Technica%20ATH-AD2000X.png)