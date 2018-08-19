# T-Peos Tank

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -10.1; 22 -9.9; 23 -9.9; 25 -9.8; 26 -9.8; 28 -9.7; 30 -9.7; 32 -9.6; 35 -9.5; 37 -9.5; 40 -9.3; 42 -9.3; 45 -9.2; 49 -9.1; 52 -9.0; 56 -9.0; 59 -8.9; 64 -8.8; 68 -8.8; 73 -8.7; 78 -8.7; 83 -8.7; 89 -8.6; 95 -8.6; 102 -8.4; 109 -8.2; 117 -8.0; 125 -7.8; 134 -7.6; 143 -7.4; 153 -7.2; 164 -6.9; 175 -6.6; 188 -6.2; 201 -5.9; 215 -5.5; 230 -5.1; 246 -4.7; 263 -4.4; 282 -3.9; 301 -3.6; 323 -3.1; 345 -2.7; 369 -2.3; 395 -1.9; 423 -1.5; 452 -1.1; 484 -0.8; 518 -0.5; 554 -0.0; 593 0.4; 635 0.6; 679 0.7; 726 0.8; 777 1.0; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.4; 1336 -2.2; 1429 -3.2; 1529 -4.3; 1636 -5.1; 1751 -5.8; 1873 -6.1; 2004 -6.3; 2145 -6.2; 2295 -5.3; 2455 -3.5; 2627 -1.5; 2811 0.5; 3008 2.7; 3219 4.2; 3444 5.2; 3685 4.9; 3943 3.5; 4219 0.6; 4514 -2.3; 4830 -5.6; 5168 -8.9; 5530 -7.7; 5917 -3.1; 6331 -0.4; 6775 0.7; 7249 0.2; 7756 -1.9; 8299 -4.2; 8880 -5.2; 9502 -4.4; 10167 -2.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.33967998149963dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Tank ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.22 | -9.7 dB  |
| Peaking | 153 Hz  | 0.81 | -3.9 dB  |
| Peaking | 2005 Hz | 2.03 | -7.6 dB  |
| Peaking | 3495 Hz | 2.6  | 7.7 dB   |
| Peaking | 5195 Hz | 4.28 | -10.4 dB |
| Peaking | 303 Hz  | 2.28 | -0.8 dB  |
| Peaking | 746 Hz  | 1.38 | 1.9 dB   |
| Peaking | 1520 Hz | 4.96 | -1.5 dB  |
| Peaking | 6792 Hz | 4.8  | 3.0 dB   |
| Peaking | 8862 Hz | 3.91 | -5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Tank/T-Peos%20Tank.png)