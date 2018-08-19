# Audio Technica ATH-A1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.7; 23 5.5; 25 4.9; 26 4.6; 28 4.0; 30 3.4; 32 2.8; 35 2.1; 37 1.7; 40 1.1; 42 0.8; 45 0.4; 49 -0.1; 52 -0.3; 56 -0.6; 59 -0.7; 64 -0.9; 68 -0.8; 73 -0.5; 78 -0.2; 83 -0.2; 89 -0.2; 95 0.0; 102 -0.2; 109 -0.9; 117 -1.7; 125 -2.2; 134 -2.2; 143 -2.0; 153 -1.4; 164 -0.3; 175 -0.7; 188 -1.0; 201 -0.7; 215 -0.1; 230 0.4; 246 0.8; 263 1.1; 282 1.2; 301 1.1; 323 1.2; 345 1.1; 369 1.0; 395 0.9; 423 0.9; 452 0.8; 484 0.6; 518 0.5; 554 0.5; 593 0.6; 635 0.6; 679 0.4; 726 0.3; 777 0.4; 832 0.4; 890 0.2; 952 0.0; 1019 0.0; 1090 -0.2; 1167 -0.2; 1248 0.1; 1336 -0.4; 1429 -0.5; 1529 -0.4; 1636 -0.2; 1751 -0.3; 1873 -2.1; 2004 -4.1; 2145 -3.3; 2295 -1.0; 2455 1.0; 2627 3.0; 2811 4.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 3.1; 4830 5.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -2.1; 18692 -2.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999999dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.8  | 6.2 dB  |
| Peaking | 130 Hz   | 3.46 | -2.5 dB |
| Peaking | 2079 Hz  | 3.89 | -6.2 dB |
| Peaking | 3297 Hz  | 1.56 | 6.6 dB  |
| Peaking | 5732 Hz  | 3.13 | 5.3 dB  |
| Peaking | 33 Hz    | 1.78 | 0.5 dB  |
| Peaking | 58 Hz    | 2.47 | -1.4 dB |
| Peaking | 337 Hz   | 1.71 | 1.3 dB  |
| Peaking | 8280 Hz  | 4.57 | -1.2 dB |
| Peaking | 18191 Hz | 2.87 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A1000X/Audio%20Technica%20ATH-A1000X.png)