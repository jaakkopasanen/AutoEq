# Sol Republic Tracks

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.0; 22 -0.8; 23 -1.1; 25 -1.8; 26 -2.0; 28 -2.5; 30 -2.9; 32 -3.2; 35 -3.6; 37 -3.9; 40 -4.2; 42 -4.4; 45 -4.5; 49 -4.7; 52 -4.8; 56 -4.9; 59 -4.9; 64 -4.9; 68 -5.0; 73 -5.0; 78 -5.1; 83 -5.1; 89 -4.8; 95 -4.6; 102 -4.7; 109 -4.7; 117 -4.8; 125 -4.9; 134 -5.1; 143 -5.1; 153 -5.2; 164 -4.7; 175 -4.7; 188 -4.8; 201 -4.6; 215 -4.3; 230 -3.5; 246 -2.8; 263 -1.8; 282 -0.3; 301 1.1; 323 2.7; 345 4.0; 369 5.8; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 5.8; 554 4.6; 593 3.4; 635 2.4; 679 1.4; 726 0.6; 777 0.3; 832 -0.0; 890 -0.1; 952 -0.0; 1019 -0.1; 1090 0.1; 1167 0.7; 1248 1.2; 1336 1.4; 1429 1.7; 1529 2.7; 1636 3.1; 1751 1.4; 1873 1.6; 2004 2.2; 2145 2.8; 2295 3.8; 2455 4.9; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.5; 4830 3.9; 5168 4.1; 5530 5.3; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Tracks ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 151 Hz  | 0.23 | -6.2 dB |
| Peaking | 425 Hz  | 1.33 | 11.5 dB |
| Peaking | 2708 Hz | 1.25 | 4.1 dB  |
| Peaking | 3850 Hz | 1.74 | 3.8 dB  |
| Peaking | 6039 Hz | 4.59 | 4.9 dB  |
| Peaking | 15 Hz   | 2.88 | 1.1 dB  |
| Peaking | 214 Hz  | 5.15 | -1.1 dB |
| Peaking | 1586 Hz | 5.43 | 3.0 dB  |
| Peaking | 1800 Hz | 3.98 | -1.9 dB |
| Peaking | 8360 Hz | 3.89 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Tracks/Sol%20Republic%20Tracks.png)