# Audio Technica ATH-MSR7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.4; 32 5.1; 35 4.8; 37 4.6; 40 4.3; 42 4.2; 45 4.0; 49 3.8; 52 3.6; 56 3.4; 59 3.2; 64 3.0; 68 2.8; 73 2.5; 78 2.3; 83 2.1; 89 1.8; 95 1.5; 102 1.3; 109 1.2; 117 1.1; 125 0.9; 134 0.8; 143 0.7; 153 0.5; 164 0.3; 175 0.8; 188 0.9; 201 0.8; 215 0.7; 230 0.7; 246 0.7; 263 0.8; 282 1.1; 301 1.3; 323 1.6; 345 2.1; 369 2.5; 395 2.9; 423 3.4; 452 3.6; 484 3.6; 518 3.5; 554 3.6; 593 3.4; 635 2.9; 679 2.2; 726 1.7; 777 1.5; 832 0.9; 890 0.5; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.8; 1429 -1.3; 1529 -1.8; 1636 -2.2; 1751 -2.2; 1873 -2.0; 2004 -1.5; 2145 -0.3; 2295 0.9; 2455 2.1; 2627 3.3; 2811 4.1; 3008 5.0; 3219 5.3; 3444 5.5; 3685 5.5; 3943 4.8; 4219 2.3; 4514 1.0; 4830 1.4; 5168 4.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.68 | 5.8 dB  |
| Peaking | 60 Hz   |  0.99 | 1.5 dB  |
| Peaking | 487 Hz  |  1.7  | 4.0 dB  |
| Peaking | 3343 Hz |  3.09 | 6.1 dB  |
| Peaking | 5925 Hz |  3.92 | 6.4 dB  |
| Peaking | 642 Hz  |  4.68 | 0.8 dB  |
| Peaking | 1769 Hz |  2.06 | -3.1 dB |
| Peaking | 2611 Hz |  3.3  | 2.1 dB  |
| Peaking | 4589 Hz | 12.13 | -1.5 dB |
| Peaking | 8223 Hz |  5.71 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7/Audio%20Technica%20ATH-MSR7.png)