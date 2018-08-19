# Audio Technica ATH-W1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.5; 45 4.8; 49 3.9; 52 3.4; 56 2.4; 59 1.7; 64 0.8; 68 0.4; 73 -0.1; 78 -0.8; 83 -1.4; 89 -1.8; 95 -2.1; 102 -2.3; 109 -2.3; 117 -2.3; 125 -2.4; 134 -2.4; 143 -2.3; 153 -2.3; 164 -2.0; 175 -1.9; 188 -1.8; 201 -1.7; 215 -1.5; 230 -1.2; 246 -1.0; 263 -0.8; 282 -0.3; 301 -0.1; 323 0.2; 345 0.7; 369 1.0; 395 1.7; 423 2.7; 452 3.1; 484 2.7; 518 1.8; 554 1.0; 593 0.6; 635 0.4; 679 0.2; 726 0.3; 777 1.0; 832 1.1; 890 0.3; 952 -0.0; 1019 0.0; 1090 0.1; 1167 -0.0; 1248 -0.2; 1336 -0.4; 1429 -1.0; 1529 -1.5; 1636 -1.4; 1751 -1.0; 1873 -0.7; 2004 -0.8; 2145 -0.7; 2295 -0.2; 2455 1.0; 2627 2.9; 2811 4.3; 3008 5.1; 3219 5.7; 3444 5.9; 3685 5.4; 3943 5.7; 4219 5.0; 4514 3.4; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -1.7; 18692 -2.5; 20000 -1.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.49 | 8.5 dB  |
| Peaking | 89 Hz    | 0.57 | -6.0 dB |
| Peaking | 445 Hz   | 2.75 | 3.5 dB  |
| Peaking | 3400 Hz  | 2.84 | 5.8 dB  |
| Peaking | 5557 Hz  | 2.57 | 6.2 dB  |
| Peaking | 815 Hz   | 8.24 | 1.3 dB  |
| Peaking | 1856 Hz  | 1.65 | -1.8 dB |
| Peaking | 2806 Hz  | 6.14 | 2.1 dB  |
| Peaking | 8200 Hz  | 5.42 | -1.2 dB |
| Peaking | 18994 Hz | 1.98 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W1000X/Audio%20Technica%20ATH-W1000X.png)