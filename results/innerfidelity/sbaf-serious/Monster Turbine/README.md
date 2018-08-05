# Monster Turbine

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 -11.4; 22 -11.3; 23 -11.2; 25 -11.1; 26 -11.0; 28 -10.9; 30 -10.7; 32 -10.6; 35 -10.4; 37 -10.2; 40 -10.0; 42 -9.8; 45 -9.6; 49 -9.3; 52 -9.0; 56 -8.8; 59 -8.5; 64 -8.2; 68 -8.0; 73 -7.7; 78 -7.6; 83 -7.4; 89 -7.5; 95 -7.6; 102 -7.7; 109 -7.8; 117 -7.9; 125 -8.0; 134 -8.1; 143 -8.0; 153 -7.9; 164 -7.6; 175 -7.2; 188 -6.8; 201 -6.5; 215 -6.0; 230 -5.5; 246 -5.2; 263 -4.8; 282 -4.2; 301 -3.8; 323 -3.4; 345 -2.9; 369 -2.5; 395 -2.1; 423 -1.6; 452 -1.2; 484 -0.9; 518 -0.6; 554 -0.1; 593 0.3; 635 0.6; 679 0.7; 726 0.8; 777 0.9; 832 0.8; 890 0.6; 952 0.3; 1019 -0.2; 1090 -0.9; 1167 -0.3; 1248 -0.9; 1336 -1.4; 1429 -1.6; 1529 -2.4; 1636 -3.1; 1751 -3.7; 1873 -4.0; 2004 -4.4; 2145 -5.0; 2295 -5.5; 2455 -5.7; 2627 -6.0; 2811 -5.7; 3008 -4.4; 3219 -3.0; 3444 -1.6; 3685 -1.4; 3943 -2.3; 4219 -4.3; 4514 -5.8; 4830 -5.7; 5168 -3.6; 5530 -1.0; 5917 1.7; 6331 3.4; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -2.1; 10879 -2.5; 11640 -1.4; 12455 -1.0; 13327 -1.9; 14260 -1.8; 15258 -0.1; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 9 Hz     | 0.71 | -10.9 dB |
| Peaking | 33 Hz    | 0.37 | -8.5 dB  |
| Peaking | 164 Hz   | 0.91 | -5.5 dB  |
| Peaking | 2396 Hz  | 1.87 | -6.2 dB  |
| Peaking | 4640 Hz  | 6.42 | -5.9 dB  |
| Peaking | 744 Hz   | 2.19 | 1.8 dB   |
| Peaking | 1662 Hz  | 4.74 | -1.2 dB  |
| Peaking | 5184 Hz  | 6.44 | -2.1 dB  |
| Peaking | 6486 Hz  | 3.84 | 5.0 dB   |
| Peaking | 11511 Hz | 1.5  | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)