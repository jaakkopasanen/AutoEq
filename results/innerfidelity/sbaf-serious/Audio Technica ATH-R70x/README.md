# Audio Technica ATH-R70x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 10 -84; 20 6.7; 22 5.8; 23 5.3; 25 4.5; 26 4.2; 28 3.5; 30 2.9; 32 2.4; 35 1.7; 37 1.3; 40 0.8; 42 0.5; 45 0.0; 49 -0.4; 52 -0.7; 56 -1.1; 59 -1.3; 64 -1.6; 68 -1.8; 73 -2.1; 78 -2.3; 83 -2.4; 89 -2.3; 95 -2.1; 102 -2.5; 109 -2.9; 117 -3.0; 125 -3.2; 134 -3.1; 143 -3.2; 153 -3.3; 164 -3.3; 175 -3.2; 188 -3.2; 201 -3.2; 215 -3.0; 230 -2.8; 246 -2.8; 263 -2.6; 282 -2.4; 301 -2.3; 323 -2.1; 345 -1.9; 369 -1.7; 395 -1.5; 423 -1.4; 452 -1.2; 484 -1.3; 518 -1.1; 554 -0.9; 593 -0.7; 635 -0.6; 679 -0.7; 726 -0.8; 777 -0.4; 832 -0.4; 890 -0.5; 952 -0.3; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.2; 1429 -1.7; 1529 -2.2; 1636 -2.7; 1751 -2.8; 1873 -2.5; 2004 -2.2; 2145 -1.7; 2295 -1.1; 2455 -0.3; 2627 0.8; 2811 2.8; 3008 2.0; 3219 1.5; 3444 -0.1; 3685 -0.5; 3943 0.7; 4219 1.7; 4514 2.6; 4830 3.8; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -1.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.80116105038619dB` and instead set Global volume in the UI for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-R70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.12 | 6.7 dB  |
| Peaking | 146 Hz  |  0.46 | -3.4 dB |
| Peaking | 1808 Hz |  2.14 | -2.9 dB |
| Peaking | 2844 Hz |  6.77 | 3.1 dB  |
| Peaking | 5683 Hz |  2.95 | 6.8 dB  |
| Peaking | 1036 Hz |  4.62 | 0.5 dB  |
| Peaking | 3604 Hz | 13.23 | -1.6 dB |
| Peaking | 6565 Hz | 10.29 | 1.7 dB  |
| Peaking | 8898 Hz |  3.11 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-R70x/Audio%20Technica%20ATH-R70x.png)