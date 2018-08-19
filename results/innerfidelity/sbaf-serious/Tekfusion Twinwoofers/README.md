# Tekfusion Twinwoofers

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -10.2; 22 -10.2; 23 -10.3; 25 -10.3; 26 -10.4; 28 -10.5; 30 -10.5; 32 -10.6; 35 -10.6; 37 -10.6; 40 -10.6; 42 -10.6; 45 -10.7; 49 -10.8; 52 -10.8; 56 -10.9; 59 -10.9; 64 -11.0; 68 -11.1; 73 -11.3; 78 -11.4; 83 -11.4; 89 -11.5; 95 -11.6; 102 -11.6; 109 -11.5; 117 -11.4; 125 -11.3; 134 -11.2; 143 -11.1; 153 -10.9; 164 -10.6; 175 -10.3; 188 -10.0; 201 -9.6; 215 -9.2; 230 -8.7; 246 -8.3; 263 -7.8; 282 -7.1; 301 -6.6; 323 -6.0; 345 -5.3; 369 -4.7; 395 -4.0; 423 -3.3; 452 -2.5; 484 -2.0; 518 -1.4; 554 -0.8; 593 -0.2; 635 -0.0; 679 -0.1; 726 -0.4; 777 -0.4; 832 0.6; 890 0.9; 952 0.3; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.1; 1336 -0.1; 1429 0.0; 1529 0.1; 1636 0.4; 1751 1.0; 1873 1.6; 2004 2.4; 2145 3.2; 2295 4.0; 2455 5.0; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.5; 3943 3.7; 4219 1.3; 4514 -1.0; 4830 -2.7; 5168 -4.2; 5530 -3.5; 5917 -1.9; 6331 1.2; 6775 2.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999938477dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tekfusion Twinwoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.25 | -10.0 dB |
| Peaking | 129 Hz  | 0.74 | -6.1 dB  |
| Peaking | 253 Hz  | 1.32 | -3.6 dB  |
| Peaking | 3160 Hz | 1.35 | 7.0 dB   |
| Peaking | 5066 Hz | 3.85 | -6.9 dB  |
| Peaking | 607 Hz  | 3.34 | 1.7 dB   |
| Peaking | 884 Hz  | 4.62 | 1.9 dB   |
| Peaking | 2137 Hz | 0.38 | -1.7 dB  |
| Peaking | 2555 Hz | 1.05 | 2.0 dB   |
| Peaking | 6818 Hz | 7.5  | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Tekfusion%20Twinwoofers/Tekfusion%20Twinwoofers.png)