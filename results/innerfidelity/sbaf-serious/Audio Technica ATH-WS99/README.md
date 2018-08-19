# Audio Technica ATH-WS99

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.4; 22 2.7; 23 2.4; 25 1.9; 26 1.6; 28 1.2; 30 0.9; 32 0.6; 35 0.2; 37 -0.1; 40 -0.4; 42 -0.6; 45 -0.9; 49 -1.2; 52 -1.4; 56 -1.6; 59 -1.7; 64 -1.9; 68 -2.1; 73 -2.7; 78 -3.2; 83 -3.3; 89 -3.6; 95 -4.1; 102 -4.6; 109 -4.8; 117 -4.9; 125 -5.1; 134 -5.2; 143 -5.3; 153 -5.4; 164 -5.3; 175 -5.2; 188 -5.3; 201 -5.3; 215 -5.1; 230 -4.8; 246 -4.6; 263 -4.1; 282 -3.7; 301 -3.5; 323 -3.2; 345 -2.7; 369 -2.3; 395 -1.8; 423 -1.5; 452 -1.2; 484 -0.5; 518 0.4; 554 1.5; 593 2.7; 635 3.4; 679 3.5; 726 3.3; 777 3.0; 832 2.3; 890 1.4; 952 0.7; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.8; 1336 -2.3; 1429 -2.7; 1529 -2.9; 1636 -2.9; 1751 -2.3; 1873 -1.4; 2004 -0.3; 2145 0.8; 2295 2.1; 2455 3.7; 2627 5.1; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.0; 4514 0.3; 4830 -1.7; 5168 1.1; 5530 4.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999859594dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-WS99 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.46 | 4.6 dB  |
| Peaking | 603 Hz  | 0.12 | -7.3 dB |
| Peaking | 671 Hz  | 0.98 | 10.4 dB |
| Peaking | 3091 Hz | 1.46 | 11.5 dB |
| Peaking | 6174 Hz | 4.35 | 7.1 dB  |
| Peaking | 301 Hz  | 3.63 | 0.7 dB  |
| Peaking | 1586 Hz | 4.36 | -1.5 dB |
| Peaking | 4010 Hz | 8.7  | 2.8 dB  |
| Peaking | 4759 Hz | 9.15 | -4.4 dB |
| Peaking | 5370 Hz | 0.22 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS99/Audio%20Technica%20ATH-WS99.png)