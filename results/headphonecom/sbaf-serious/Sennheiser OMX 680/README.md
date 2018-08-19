# Sennheiser OMX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.9; 23 -4.1; 25 -4.4; 26 -4.6; 28 -4.8; 30 -5.1; 32 -5.3; 35 -5.5; 37 -5.7; 40 -5.9; 42 -6.0; 45 -6.1; 49 -6.3; 52 -6.4; 56 -6.6; 59 -6.7; 64 -6.8; 68 -6.9; 73 -7.0; 78 -7.0; 83 -7.1; 89 -7.0; 95 -7.0; 102 -7.0; 109 -6.9; 117 -7.0; 125 -6.9; 134 -7.0; 143 -7.1; 153 -7.1; 164 -7.2; 175 -7.3; 188 -7.2; 201 -7.2; 215 -7.1; 230 -7.1; 246 -7.0; 263 -6.7; 282 -6.6; 301 -6.3; 323 -5.9; 345 -5.5; 369 -5.0; 395 -4.6; 423 -4.2; 452 -3.8; 484 -3.4; 518 -2.8; 554 -2.2; 593 -1.9; 635 -1.3; 679 -0.3; 726 0.3; 777 0.4; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.2; 1529 -2.9; 1636 -3.4; 1751 -3.7; 1873 -4.0; 2004 -4.3; 2145 -4.5; 2295 -4.4; 2455 -4.2; 2627 -3.5; 2811 -2.3; 3008 -0.6; 3219 1.2; 3444 2.6; 3685 3.0; 3943 1.9; 4219 -0.3; 4514 -2.8; 4830 -5.3; 5168 -6.3; 5530 -3.7; 5917 0.4; 6331 3.2; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -1.5; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.166842802267921dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser OMX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 68 Hz   | 0.33 | -6.7 dB  |
| Peaking | 261 Hz  | 0.98 | -4.2 dB  |
| Peaking | 2316 Hz | 1.46 | -8.0 dB  |
| Peaking | 3847 Hz | 0.87 | 6.6 dB   |
| Peaking | 4967 Hz | 4.1  | -11.2 dB |
| Peaking | 494 Hz  | 1.92 | -1.1 dB  |
| Peaking | 789 Hz  | 1.77 | 2.0 dB   |
| Peaking | 1559 Hz | 4.34 | -1.2 dB  |
| Peaking | 6667 Hz | 6.28 | 4.6 dB   |
| Peaking | 8387 Hz | 1.15 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20OMX%20680/Sennheiser%20OMX%20680.png)