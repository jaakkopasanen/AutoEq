# iMetal iM590

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.4; 22 -7.4; 23 -7.3; 25 -7.3; 26 -7.3; 28 -7.2; 30 -7.1; 32 -7.0; 35 -6.9; 37 -6.8; 40 -6.7; 42 -6.6; 45 -6.5; 49 -6.3; 52 -6.2; 56 -6.0; 59 -5.9; 64 -5.7; 68 -5.5; 73 -5.2; 78 -5.2; 83 -5.3; 89 -5.4; 95 -5.6; 102 -5.8; 109 -6.0; 117 -6.2; 125 -6.5; 134 -6.6; 143 -6.6; 153 -6.5; 164 -6.2; 175 -5.9; 188 -5.6; 201 -5.3; 215 -4.9; 230 -4.5; 246 -4.1; 263 -3.7; 282 -3.2; 301 -2.9; 323 -2.4; 345 -2.0; 369 -1.7; 395 -1.3; 423 -0.8; 452 -0.5; 484 -0.3; 518 -0.1; 554 0.3; 593 0.7; 635 0.9; 679 0.9; 726 1.0; 777 1.1; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.6; 1248 -1.0; 1336 -1.4; 1429 -1.9; 1529 -2.6; 1636 -3.4; 1751 -4.2; 1873 -4.8; 2004 -5.4; 2145 -5.9; 2295 -5.7; 2455 -4.2; 2627 -2.3; 2811 -0.1; 3008 2.6; 3219 4.6; 3444 5.9; 3685 6.0; 3943 4.9; 4219 2.2; 4514 -0.7; 4830 -3.4; 5168 -3.8; 5530 -2.3; 5917 -3.2; 6331 -2.5; 6775 -0.1; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -1.1; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iMetal iM590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 9 Hz     | 0.73 | -6.8 dB |
| Peaking | 35 Hz    | 0.41 | -5.7 dB |
| Peaking | 159 Hz   | 1.01 | -5.2 dB |
| Peaking | 2127 Hz  | 2.08 | -6.6 dB |
| Peaking | 3456 Hz  | 4.2  | 8.2 dB  |
| Peaking | 286 Hz   | 2.62 | -0.8 dB |
| Peaking | 705 Hz   | 1.8  | 1.8 dB  |
| Peaking | 4043 Hz  | 6.04 | 3.4 dB  |
| Peaking | 5105 Hz  | 3.03 | -4.5 dB |
| Peaking | 72000 Hz | 1.88 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iMetal%20iM590/iMetal%20iM590.png)