# Fidue A65

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 3.6; 22 2.9; 23 2.6; 25 2.0; 26 1.7; 28 1.3; 30 0.8; 32 0.5; 35 -0.1; 37 -0.4; 40 -0.8; 42 -1.0; 45 -1.3; 49 -1.7; 52 -1.9; 56 -2.1; 59 -2.3; 64 -2.6; 68 -2.8; 73 -3.0; 78 -3.3; 83 -3.6; 89 -4.1; 95 -4.6; 102 -5.2; 109 -5.6; 117 -6.2; 125 -6.7; 134 -7.1; 143 -7.4; 153 -7.5; 164 -7.6; 175 -7.5; 188 -7.3; 201 -7.2; 215 -7.0; 230 -6.7; 246 -6.5; 263 -6.2; 282 -5.8; 301 -5.5; 323 -5.2; 345 -4.8; 369 -4.4; 395 -4.0; 423 -3.4; 452 -3.1; 484 -2.8; 518 -2.4; 554 -1.9; 593 -1.3; 635 -1.0; 679 -0.9; 726 -0.8; 777 -0.4; 832 -0.3; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.4; 1429 -2.5; 1529 -3.6; 1636 -4.3; 1751 -4.4; 1873 -4.3; 2004 -4.1; 2145 -4.0; 2295 -3.7; 2455 -2.9; 2627 -2.5; 2811 -1.5; 3008 0.2; 3219 1.6; 3444 3.1; 3685 3.6; 3943 3.4; 4219 2.2; 4514 1.3; 4830 1.3; 5168 2.0; 5530 2.3; 5917 2.3; 6331 1.8; 6775 1.6; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 -0.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A65 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.97 | 3.7 dB  |
| Peaking | 154 Hz  | 0.73 | -7.2 dB |
| Peaking | 311 Hz  | 1.44 | -2.3 dB |
| Peaking | 2122 Hz | 1.54 | -6.0 dB |
| Peaking | 3720 Hz | 1.14 | 4.2 dB  |
| Peaking | 17 Hz   | 1.28 | 0.7 dB  |
| Peaking | 1020 Hz | 1.77 | 1.3 dB  |
| Peaking | 1567 Hz | 5.94 | -1.8 dB |
| Peaking | 6242 Hz | 1.37 | -1.9 dB |
| Peaking | 6186 Hz | 2.69 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A65/Fidue%20A65.png)