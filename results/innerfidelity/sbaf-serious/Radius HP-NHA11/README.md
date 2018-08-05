# Radius HP-NHA11

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -13.1; 22 -12.9; 23 -12.9; 25 -12.7; 26 -12.6; 28 -12.5; 30 -12.3; 32 -12.1; 35 -11.9; 37 -11.8; 40 -11.5; 42 -11.3; 45 -11.1; 49 -10.7; 52 -10.5; 56 -10.2; 59 -10.0; 64 -9.7; 68 -9.4; 73 -9.2; 78 -9.0; 83 -8.9; 89 -8.9; 95 -8.9; 102 -9.1; 109 -9.2; 117 -9.3; 125 -9.4; 134 -9.4; 143 -9.4; 153 -9.2; 164 -8.9; 175 -8.4; 188 -8.0; 201 -7.6; 215 -7.1; 230 -6.6; 246 -6.2; 263 -5.8; 282 -5.2; 301 -4.7; 323 -4.2; 345 -3.7; 369 -3.3; 395 -3.0; 423 -2.4; 452 -2.0; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.3; 635 -0.0; 679 0.1; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.4; 1529 -3.2; 1636 -3.9; 1751 -4.4; 1873 -4.7; 2004 -4.8; 2145 -5.0; 2295 -4.8; 2455 -4.1; 2627 -3.8; 2811 -3.0; 3008 -1.6; 3219 -0.5; 3444 0.3; 3685 -0.1; 3943 -1.5; 4219 -4.3; 4514 -7.2; 4830 -8.7; 5168 -6.7; 5530 -3.0; 5917 0.2; 6331 2.1; 6775 3.0; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.9; 9502 -0.8; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHA11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.81 | -12.9 dB |
| Peaking | 32 Hz   | 0.33 | -10.0 dB |
| Peaking | 168 Hz  | 0.82 | -6.1 dB  |
| Peaking | 2040 Hz | 2.11 | -5.4 dB  |
| Peaking | 4790 Hz | 6.02 | -9.4 dB  |
| Peaking | 794 Hz  | 2.33 | 1.7 dB   |
| Peaking | 3547 Hz | 0.95 | -1.2 dB  |
| Peaking | 3550 Hz | 4.29 | 3.3 dB   |
| Peaking | 6255 Hz | 1.3  | -1.7 dB  |
| Peaking | 6529 Hz | 3.76 | 5.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHA11/Radius%20HP-NHA11.png)