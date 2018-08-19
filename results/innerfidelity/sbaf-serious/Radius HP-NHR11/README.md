# Radius HP-NHR11

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 10 -84; 20 -12.4; 22 -12.3; 23 -12.3; 25 -12.2; 26 -12.1; 28 -12.0; 30 -12.0; 32 -11.9; 35 -11.7; 37 -11.6; 40 -11.5; 42 -11.4; 45 -11.3; 49 -11.2; 52 -11.1; 56 -11.0; 59 -10.9; 64 -10.8; 68 -10.7; 73 -10.7; 78 -10.6; 83 -10.5; 89 -10.5; 95 -10.4; 102 -10.2; 109 -10.0; 117 -9.8; 125 -9.6; 134 -9.4; 143 -9.1; 153 -8.8; 164 -8.6; 175 -8.1; 188 -7.8; 201 -7.4; 215 -7.0; 230 -6.5; 246 -6.2; 263 -5.7; 282 -5.2; 301 -4.8; 323 -4.3; 345 -3.8; 369 -3.4; 395 -2.9; 423 -2.4; 452 -1.9; 484 -1.6; 518 -1.2; 554 -0.7; 593 -0.2; 635 0.1; 679 0.2; 726 0.4; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.6; 1429 -2.3; 1529 -3.0; 1636 -3.5; 1751 -3.9; 1873 -4.1; 2004 -4.2; 2145 -4.2; 2295 -4.2; 2455 -3.5; 2627 -3.0; 2811 -2.3; 3008 -1.1; 3219 -0.1; 3444 0.6; 3685 0.4; 3943 -0.7; 4219 -2.9; 4514 -5.2; 4830 -7.0; 5168 -7.5; 5530 -5.7; 5917 -2.4; 6331 0.0; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -1.9; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.440664858579942dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHR11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.19 | -12.0 dB |
| Peaking | 162 Hz   | 0.73 | -4.3 dB  |
| Peaking | 2004 Hz  | 2.23 | -4.6 dB  |
| Peaking | 5091 Hz  | 4.09 | -8.3 dB  |
| Peaking | 6823 Hz  | 5.37 | 3.3 dB   |
| Peaking | 781 Hz   | 1.94 | 1.6 dB   |
| Peaking | 1511 Hz  | 5.81 | -1.2 dB  |
| Peaking | 2633 Hz  | 5.74 | -1.2 dB  |
| Peaking | 3512 Hz  | 5.76 | 2.4 dB   |
| Peaking | 10206 Hz | 8.47 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHR11/Radius%20HP-NHR11.png)