# Audio Technica ATH-AD700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.6; 89 5.0; 95 4.5; 102 4.2; 109 4.0; 117 3.7; 125 3.3; 134 3.0; 143 2.7; 153 2.4; 164 2.6; 175 2.3; 188 2.0; 201 1.9; 215 1.8; 230 1.6; 246 1.5; 263 1.6; 282 1.4; 301 1.5; 323 1.5; 345 1.5; 369 1.6; 395 1.7; 423 1.6; 452 1.6; 484 1.7; 518 1.6; 554 1.5; 593 1.6; 635 1.6; 679 1.6; 726 1.4; 777 1.1; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.1; 1167 -0.2; 1248 -0.1; 1336 -0.1; 1429 -0.0; 1529 0.1; 1636 0.5; 1751 0.8; 1873 0.7; 2004 0.7; 2145 0.3; 2295 0.7; 2455 0.2; 2627 -0.3; 2811 -0.7; 3008 -1.3; 3219 -1.3; 3444 1.0; 3685 4.3; 3943 5.3; 4219 0.9; 4514 0.1; 4830 1.6; 5168 3.8; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.2; 7756 -1.5; 8299 -3.4; 8880 -5.1; 9502 -5.8; 10167 -3.4; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.33 | 6.4 dB  |
| Peaking | 532 Hz   | 1.32 | 1.4 dB  |
| Peaking | 5973 Hz  | 2.23 | 4.9 dB  |
| Peaking | 6086 Hz  | 2.76 | 1.9 dB  |
| Peaking | 9007 Hz  | 3.26 | -7.1 dB |
| Peaking | 12 Hz    | 2.21 | 1.0 dB  |
| Peaking | 3154 Hz  | 4.91 | -2.8 dB |
| Peaking | 3873 Hz  | 5.67 | 6.5 dB  |
| Peaking | 4386 Hz  | 6    | -3.8 dB |
| Peaking | 11262 Hz | 8.03 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD700/Audio%20Technica%20ATH-AD700.png)