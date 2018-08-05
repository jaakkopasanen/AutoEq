# Aurisonic Rockets

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.0; 22 1.9; 23 1.8; 25 1.7; 26 1.7; 28 1.6; 30 1.6; 32 1.5; 35 1.5; 37 1.4; 40 1.4; 42 1.3; 45 1.3; 49 1.3; 52 1.3; 56 1.3; 59 1.3; 64 1.2; 68 1.1; 73 1.0; 78 0.8; 83 0.5; 89 0.2; 95 -0.3; 102 -0.9; 109 -1.3; 117 -1.8; 125 -2.5; 134 -3.0; 143 -3.3; 153 -3.5; 164 -3.6; 175 -3.6; 188 -3.7; 201 -3.6; 215 -3.5; 230 -3.4; 246 -3.4; 263 -3.3; 282 -3.0; 301 -2.9; 323 -2.7; 345 -2.5; 369 -2.3; 395 -2.1; 423 -1.8; 452 -1.5; 484 -1.4; 518 -1.2; 554 -0.8; 593 -0.3; 635 -0.1; 679 -0.0; 726 0.1; 777 0.5; 832 0.4; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.6; 1429 -1.0; 1529 -1.4; 1636 -1.7; 1751 -1.7; 1873 -1.5; 2004 -1.1; 2145 -0.7; 2295 0.0; 2455 1.2; 2627 2.4; 2811 3.9; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurisonic Rockets ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.34 | 1.9 dB  |
| Peaking | 77 Hz   | 1.25 | 1.8 dB  |
| Peaking | 183 Hz  | 0.67 | -4.2 dB |
| Peaking | 1896 Hz | 1.91 | -3.7 dB |
| Peaking | 4007 Hz | 0.98 | 7.2 dB  |
| Peaking | 783 Hz  | 3.1  | 1.0 dB  |
| Peaking | 3077 Hz | 5.9  | 2.0 dB  |
| Peaking | 6099 Hz | 0.71 | -2.4 dB |
| Peaking | 6221 Hz | 2.17 | 5.4 dB  |
| Peaking | 7576 Hz | 3.05 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurisonic%20Rockets/Aurisonic%20Rockets.png)