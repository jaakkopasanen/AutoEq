# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 4.2; 22 3.6; 23 3.3; 25 2.7; 26 2.5; 28 2.0; 30 1.6; 32 1.2; 35 0.7; 37 0.4; 40 0.1; 42 -0.1; 45 -0.4; 49 -0.7; 52 -0.9; 56 -1.2; 59 -1.3; 64 -1.4; 68 -1.4; 73 -1.5; 78 -2.0; 83 -2.6; 89 -2.9; 95 -3.1; 102 -3.8; 109 -4.2; 117 -4.6; 125 -5.1; 134 -5.4; 143 -5.4; 153 -5.4; 164 -5.0; 175 -4.9; 188 -4.6; 201 -4.1; 215 -3.6; 230 -2.8; 246 -2.0; 263 -1.4; 282 -0.8; 301 -0.3; 323 0.3; 345 0.9; 369 1.3; 395 1.7; 423 2.0; 452 1.9; 484 1.7; 518 1.4; 554 1.5; 593 1.5; 635 1.3; 679 1.0; 726 0.9; 777 0.9; 832 0.6; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.7; 1529 -2.2; 1636 -2.8; 1751 -3.1; 1873 -3.3; 2004 -3.3; 2145 -3.0; 2295 -1.9; 2455 -0.5; 2627 0.6; 2811 1.4; 3008 2.2; 3219 2.3; 3444 2.3; 3685 2.2; 3943 2.4; 4219 2.6; 4514 3.3; 4830 3.3; 5168 4.4; 5530 4.5; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.3; 8299 -4.7; 8880 -5.7; 9502 -3.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 2.02 | 4.0 dB   |
| Peaking | 139 Hz  | 1.31 | -5.9 dB  |
| Peaking | 1887 Hz | 2.59 | -4.4 dB  |
| Peaking | 6612 Hz | 0.97 | 7.9 dB   |
| Peaking | 8565 Hz | 2.55 | -11.5 dB |
| Peaking | 215 Hz  | 2.61 | -1.8 dB  |
| Peaking | 447 Hz  | 1.09 | 2.4 dB   |
| Peaking | 1395 Hz | 2.84 | -0.8 dB  |
| Peaking | 3035 Hz | 6.06 | 1.3 dB   |
| Peaking | 4681 Hz | 4.52 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)