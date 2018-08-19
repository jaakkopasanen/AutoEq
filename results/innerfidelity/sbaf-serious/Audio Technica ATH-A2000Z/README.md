# Audio Technica ATH-A2000Z

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 6.3; 22 5.5; 23 5.2; 25 4.5; 26 4.2; 28 3.6; 30 3.1; 32 2.7; 35 2.1; 37 1.7; 40 1.2; 42 1.0; 45 0.6; 49 0.3; 52 0.1; 56 -0.2; 59 -0.3; 64 -0.5; 68 -0.6; 73 -0.7; 78 -0.8; 83 -0.9; 89 -1.3; 95 -1.8; 102 -2.4; 109 -2.6; 117 -2.6; 125 -2.6; 134 -2.6; 143 -2.6; 153 -2.5; 164 -1.7; 175 -1.8; 188 -1.8; 201 -1.5; 215 -1.2; 230 -0.7; 246 -0.4; 263 -0.2; 282 0.1; 301 0.2; 323 0.2; 345 0.2; 369 0.1; 395 -0.0; 423 -0.1; 452 -0.0; 484 -0.2; 518 -0.2; 554 -0.2; 593 0.1; 635 0.1; 679 -0.0; 726 -0.1; 777 0.1; 832 0.4; 890 0.1; 952 -0.1; 1019 0.2; 1090 0.4; 1167 0.1; 1248 0.0; 1336 -0.4; 1429 -1.2; 1529 -2.4; 1636 -3.6; 1751 -4.3; 1873 -4.8; 2004 -5.1; 2145 -5.2; 2295 -4.6; 2455 -2.7; 2627 -0.8; 2811 0.6; 3008 1.6; 3219 1.6; 3444 0.0; 3685 -2.3; 3943 -3.4; 4219 -3.8; 4514 -2.0; 4830 1.3; 5168 5.7; 5530 6.0; 5917 4.6; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -2.6; 9502 -5.2; 10167 -4.2; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.4; 16326 -3.7; 17469 -3.6; 18692 -1.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.449946125755469dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A2000Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 23 Hz    |  2.13 | 6.3 dB   |
| Peaking | 2008 Hz  |  2.46 | -6.8 dB  |
| Peaking | 4275 Hz  |  3.25 | -12.3 dB |
| Peaking | 4934 Hz  |  1.18 | 9.8 dB   |
| Peaking | 9479 Hz  |  3.24 | -7.0 dB  |
| Peaking | 34 Hz    |  2.52 | 0.9 dB   |
| Peaking | 127 Hz   |  1.17 | -3.0 dB  |
| Peaking | 3500 Hz  |  0.03 | 0.2 dB   |
| Peaking | 3733 Hz  | 11.44 | -2.2 dB  |
| Peaking | 16987 Hz |  2.91 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A2000Z/Audio%20Technica%20ATH-A2000Z.png)