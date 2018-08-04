# Takstar Pro 80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.2; 22 2.8; 23 2.6; 25 2.3; 26 2.2; 28 1.9; 30 1.8; 32 1.6; 35 1.5; 37 1.4; 40 1.3; 42 1.3; 45 1.3; 49 1.2; 52 1.2; 56 1.2; 59 1.2; 64 1.2; 68 1.2; 73 1.1; 78 1.1; 83 1.0; 89 0.7; 95 0.5; 102 0.3; 109 0.2; 117 -0.2; 125 -0.8; 134 -1.3; 143 -1.7; 153 -1.6; 164 -1.3; 175 -1.5; 188 -1.6; 201 -1.5; 215 -1.4; 230 -1.1; 246 -1.0; 263 -0.9; 282 -0.6; 301 -0.3; 323 0.1; 345 0.5; 369 0.8; 395 1.3; 423 1.8; 452 2.1; 484 2.0; 518 2.0; 554 1.9; 593 1.8; 635 1.5; 679 1.1; 726 0.9; 777 0.9; 832 1.3; 890 1.0; 952 0.5; 1019 0.1; 1090 -0.2; 1167 -0.5; 1248 -1.1; 1336 -1.6; 1429 -2.2; 1529 -3.0; 1636 -3.5; 1751 -3.6; 1873 -4.0; 2004 -3.9; 2145 -3.0; 2295 -1.5; 2455 0.6; 2627 2.7; 2811 4.5; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.7; 4830 2.5; 5168 3.3; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.2; 8880 -3.6; 9502 -4.1; 10167 -3.0; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Takstar Pro 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.69 | 2.8 dB   |
| Peaking | 1953 Hz |  1.15 | -15.9 dB |
| Peaking | 2632 Hz |  0.55 | 13.1 dB  |
| Peaking | 6226 Hz |  6.12 | 2.9 dB   |
| Peaking | 9226 Hz |  2.53 | -6.6 dB  |
| Peaking | 88 Hz   |  0.91 | 3.3 dB   |
| Peaking | 133 Hz  |  0.55 | -3.4 dB  |
| Peaking | 465 Hz  |  1.52 | 2.3 dB   |
| Peaking | 1306 Hz |  3.89 | -0.8 dB  |
| Peaking | 4935 Hz | 13.67 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Takstar%20Pro%2080/Takstar%20Pro%2080.png)