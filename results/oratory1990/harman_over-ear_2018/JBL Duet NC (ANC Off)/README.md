# JBL Duet NC (ANC Off)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.3; 23 -1.6; 25 -1.9; 26 -2.0; 28 -2.2; 30 -2.3; 32 -2.4; 35 -2.6; 37 -2.7; 40 -2.8; 42 -2.8; 45 -2.6; 49 -2.2; 52 -1.9; 56 -1.3; 59 -0.9; 64 -0.4; 68 0.1; 73 1.2; 78 2.2; 83 2.4; 89 2.2; 95 1.7; 102 1.3; 109 1.4; 117 1.6; 125 1.4; 134 0.9; 143 0.3; 153 -0.2; 164 -0.0; 175 0.8; 188 1.8; 201 2.9; 215 4.3; 230 5.8; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 5.5; 518 4.2; 554 3.3; 593 3.0; 635 2.5; 679 2.0; 726 1.3; 777 0.9; 832 0.4; 890 0.2; 952 0.0; 1019 0.0; 1090 0.2; 1167 0.6; 1248 1.2; 1336 1.4; 1429 1.0; 1529 1.5; 1636 2.4; 1751 3.2; 1873 3.9; 2004 4.6; 2145 5.3; 2295 5.7; 2455 5.5; 2627 4.9; 2811 5.7; 3008 6.0; 3219 6.0; 3444 3.6; 3685 0.7; 3943 0.6; 4219 1.5; 4514 2.1; 4830 3.1; 5168 5.8; 5530 5.0; 5917 1.3; 6331 4.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC Off) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 81 Hz   |  0.4  | -6.1 dB |
| Peaking | 85 Hz   |  1.19 | 7.5 dB  |
| Peaking | 306 Hz  |  0.92 | 8.4 dB  |
| Peaking | 2539 Hz |  1.68 | 6.0 dB  |
| Peaking | 5326 Hz |  4.38 | 4.8 dB  |
| Peaking | 469 Hz  |  6.34 | 1.8 dB  |
| Peaking | 934 Hz  |  2.8  | -1.5 dB |
| Peaking | 3311 Hz |  6.46 | 4.3 dB  |
| Peaking | 3637 Hz |  3.72 | -3.2 dB |
| Peaking | 6631 Hz | 11.85 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20Off)/JBL%20Duet%20NC%20(ANC%20Off).png)