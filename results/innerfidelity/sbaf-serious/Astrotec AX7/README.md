# Astrotec AX7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.6; 52 5.4; 56 5.2; 59 5.0; 64 4.7; 68 4.4; 73 4.0; 78 3.7; 83 3.4; 89 3.0; 95 2.6; 102 2.3; 109 2.1; 117 1.8; 125 1.4; 134 1.2; 143 0.9; 153 0.6; 164 0.4; 175 0.3; 188 0.1; 201 -0.1; 215 -0.2; 230 -0.2; 246 -0.4; 263 -0.4; 282 -0.4; 301 -0.5; 323 -0.5; 345 -0.4; 369 -0.4; 395 -0.4; 423 -0.2; 452 -0.1; 484 -0.1; 518 -0.0; 554 0.3; 593 0.5; 635 0.6; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.7; 1636 -1.8; 1751 -1.9; 1873 -1.8; 2004 -1.7; 2145 -1.4; 2295 -0.9; 2455 0.2; 2627 1.8; 2811 4.0; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.1; 4514 1.2; 4830 1.6; 5168 3.0; 5530 4.0; 5917 4.6; 6331 5.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.55 | 6.6 dB  |
| Peaking | 837 Hz  |  2.18 | 1.3 dB  |
| Peaking | 2171 Hz |  0.92 | -3.8 dB |
| Peaking | 3256 Hz |  1.93 | 8.9 dB  |
| Peaking | 6279 Hz |  4.27 | 4.9 dB  |
| Peaking | 37 Hz   |  2.17 | -0.8 dB |
| Peaking | 59 Hz   |  0.69 | 0.7 dB  |
| Peaking | 231 Hz  |  1.11 | -0.9 dB |
| Peaking | 5497 Hz | 11.01 | 1.4 dB  |
| Peaking | 8065 Hz |  3.15 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX7/Astrotec%20AX7.png)