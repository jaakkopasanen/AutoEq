# Sansui SS35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 5.7; 369 4.2; 395 2.6; 423 1.6; 452 1.1; 484 1.1; 518 1.3; 554 1.4; 593 1.6; 635 1.6; 679 1.5; 726 1.4; 777 1.3; 832 1.0; 890 0.6; 952 0.3; 1019 -0.2; 1090 -0.5; 1167 -0.7; 1248 -0.9; 1336 -1.1; 1429 -1.0; 1529 -0.5; 1636 0.3; 1751 1.2; 1873 1.9; 2004 1.6; 2145 0.0; 2295 -0.9; 2455 0.5; 2627 2.9; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.8; 4514 3.4; 4830 4.4; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.21 | 6.1 dB  |
| Peaking | 200 Hz  | 1.02 | 3.1 dB  |
| Peaking | 315 Hz  | 3.34 | 3.2 dB  |
| Peaking | 3371 Hz | 2.54 | 6.4 dB  |
| Peaking | 5713 Hz | 2.95 | 6.0 dB  |
| Peaking | 103 Hz  | 3.2  | 0.2 dB  |
| Peaking | 1394 Hz | 1.93 | -4.5 dB |
| Peaking | 1679 Hz | 1.05 | 3.3 dB  |
| Peaking | 2295 Hz | 6.55 | -4.2 dB |
| Peaking | 8297 Hz | 3.68 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35/Sansui%20SS35.png)