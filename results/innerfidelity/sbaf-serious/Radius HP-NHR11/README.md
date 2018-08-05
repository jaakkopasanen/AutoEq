# Radius HP-NHR11

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 10 -84; 20 -12.3; 22 -12.2; 23 -12.2; 25 -12.1; 26 -12.0; 28 -11.9; 30 -11.8; 32 -11.6; 35 -11.4; 37 -11.3; 40 -11.1; 42 -11.0; 45 -10.7; 49 -10.5; 52 -10.3; 56 -10.0; 59 -9.8; 64 -9.5; 68 -9.3; 73 -9.1; 78 -9.0; 83 -8.9; 89 -8.9; 95 -9.0; 102 -9.2; 109 -9.3; 117 -9.4; 125 -9.6; 134 -9.7; 143 -9.5; 153 -9.3; 164 -9.1; 175 -8.7; 188 -8.3; 201 -7.9; 215 -7.4; 230 -6.9; 246 -6.4; 263 -6.0; 282 -5.4; 301 -4.9; 323 -4.4; 345 -3.9; 369 -3.5; 395 -3.0; 423 -2.4; 452 -2.0; 484 -1.6; 518 -1.3; 554 -0.8; 593 -0.2; 635 0.1; 679 0.1; 726 0.3; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.6; 1429 -2.3; 1529 -3.0; 1636 -3.5; 1751 -3.9; 1873 -4.1; 2004 -4.2; 2145 -4.2; 2295 -4.2; 2455 -3.5; 2627 -3.0; 2811 -2.3; 3008 -1.1; 3219 -0.1; 3444 0.6; 3685 0.4; 3943 -0.7; 4219 -2.9; 4514 -5.2; 4830 -7.0; 5168 -7.5; 5530 -5.7; 5917 -2.4; 6331 0.0; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -1.9; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.9dB` and instead set Global volume in the UI for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHR11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 9 Hz     | 0.87 | -12.1 dB |
| Peaking | 32 Hz    | 0.31 | -9.8 dB  |
| Peaking | 170 Hz   | 0.83 | -6.3 dB  |
| Peaking | 2008 Hz  | 2.19 | -4.7 dB  |
| Peaking | 5029 Hz  | 5.06 | -8.3 dB  |
| Peaking | 780 Hz   | 2.2  | 1.7 dB   |
| Peaking | 3680 Hz  | 1.2  | -2.4 dB  |
| Peaking | 3568 Hz  | 3.38 | 4.4 dB   |
| Peaking | 6846 Hz  | 5.59 | 3.6 dB   |
| Peaking | 10224 Hz | 7.5  | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHR11/Radius%20HP-NHR11.png)