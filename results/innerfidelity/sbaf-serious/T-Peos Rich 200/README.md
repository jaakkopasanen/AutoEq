# T-Peos Rich 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.0; 23 -4.0; 25 -3.9; 26 -3.9; 28 -3.9; 30 -3.9; 32 -3.9; 35 -3.9; 37 -3.8; 40 -3.8; 42 -3.8; 45 -3.8; 49 -3.8; 52 -3.8; 56 -3.7; 59 -3.6; 64 -3.7; 68 -3.7; 73 -3.7; 78 -3.8; 83 -3.9; 89 -4.2; 95 -4.5; 102 -5.0; 109 -5.3; 117 -5.7; 125 -6.1; 134 -6.4; 143 -6.5; 153 -6.6; 164 -6.5; 175 -6.3; 188 -6.1; 201 -5.9; 215 -5.5; 230 -5.2; 246 -4.9; 263 -4.6; 282 -4.2; 301 -3.8; 323 -3.5; 345 -3.1; 369 -2.6; 395 -2.3; 423 -1.8; 452 -1.4; 484 -1.2; 518 -0.8; 554 -0.4; 593 0.1; 635 0.4; 679 0.5; 726 0.6; 777 0.9; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.5; 1529 -3.3; 1636 -3.9; 1751 -4.4; 1873 -4.8; 2004 -5.0; 2145 -5.0; 2295 -4.5; 2455 -3.0; 2627 -1.4; 2811 0.3; 3008 2.4; 3219 3.9; 3444 4.8; 3685 4.3; 3943 2.8; 4219 -0.3; 4514 -3.5; 4830 -7.0; 5168 -8.2; 5530 -6.0; 5917 -2.3; 6331 -0.0; 6775 0.5; 7249 -1.0; 7756 -3.7; 8299 -5.8; 8880 -5.9; 9502 -4.3; 10167 -1.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Rich 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 128 Hz  | 0.47 | -6.1 dB  |
| Peaking | 2066 Hz | 2.03 | -6.3 dB  |
| Peaking | 3483 Hz | 2.34 | 6.9 dB   |
| Peaking | 5023 Hz | 4.61 | -10.1 dB |
| Peaking | 8711 Hz | 4.65 | -6.6 dB  |
| Peaking | 27 Hz   | 0.12 | -3.5 dB  |
| Peaking | 80 Hz   | 0.83 | 4.3 dB   |
| Peaking | 713 Hz  | 1.19 | 2.1 dB   |
| Peaking | 1514 Hz | 3.64 | -1.3 dB  |
| Peaking | 6621 Hz | 9.29 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Rich%20200/T-Peos%20Rich%20200.png)