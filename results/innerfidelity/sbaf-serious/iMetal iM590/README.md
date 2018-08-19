# iMetal iM590

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.5; 22 -7.4; 23 -7.4; 25 -7.4; 26 -7.4; 28 -7.4; 30 -7.3; 32 -7.3; 35 -7.2; 37 -7.2; 40 -7.1; 42 -7.1; 45 -7.1; 49 -7.0; 52 -7.0; 56 -7.0; 59 -7.0; 64 -7.0; 68 -6.9; 73 -6.8; 78 -6.8; 83 -6.9; 89 -7.0; 95 -7.0; 102 -6.9; 109 -6.7; 117 -6.6; 125 -6.5; 134 -6.3; 143 -6.2; 153 -6.0; 164 -5.7; 175 -5.4; 188 -5.1; 201 -4.8; 215 -4.5; 230 -4.1; 246 -3.8; 263 -3.5; 282 -3.1; 301 -2.7; 323 -2.3; 345 -1.9; 369 -1.6; 395 -1.2; 423 -0.7; 452 -0.4; 484 -0.2; 518 -0.1; 554 0.3; 593 0.7; 635 0.9; 679 0.9; 726 1.0; 777 1.1; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.6; 1248 -1.0; 1336 -1.4; 1429 -1.9; 1529 -2.6; 1636 -3.4; 1751 -4.2; 1873 -4.8; 2004 -5.4; 2145 -5.9; 2295 -5.7; 2455 -4.2; 2627 -2.3; 2811 -0.1; 3008 2.6; 3219 4.6; 3444 5.9; 3685 6.0; 3943 4.9; 4219 2.2; 4514 -0.7; 4830 -3.4; 5168 -3.8; 5530 -2.3; 5917 -3.2; 6331 -2.5; 6775 -0.1; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -1.1; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999918362885dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iMetal iM590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 28 Hz   |  0.25 | -7.2 dB |
| Peaking | 147 Hz  |  0.86 | -3.6 dB |
| Peaking | 2214 Hz |  1.91 | -8.7 dB |
| Peaking | 3658 Hz |  1.59 | 10.6 dB |
| Peaking | 4944 Hz |  2.23 | -8.1 dB |
| Peaking | 279 Hz  |  2.41 | -0.8 dB |
| Peaking | 706 Hz  |  1.51 | 1.8 dB  |
| Peaking | 1595 Hz |  3.56 | -0.9 dB |
| Peaking | 7140 Hz | 12.43 | 1.9 dB  |
| Peaking | 9283 Hz | 10.31 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iMetal%20iM590/iMetal%20iM590.png)