# PNY Uptown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -11.5; 22 -11.4; 23 -11.3; 25 -11.2; 26 -11.1; 28 -11.0; 30 -10.9; 32 -10.7; 35 -10.5; 37 -10.3; 40 -10.1; 42 -10.0; 45 -9.7; 49 -9.4; 52 -9.2; 56 -8.9; 59 -8.7; 64 -8.4; 68 -8.1; 73 -7.9; 78 -7.7; 83 -7.6; 89 -7.6; 95 -7.7; 102 -7.8; 109 -7.9; 117 -8.0; 125 -8.2; 134 -8.3; 143 -8.2; 153 -8.0; 164 -7.8; 175 -7.4; 188 -7.0; 201 -6.6; 215 -6.2; 230 -5.7; 246 -5.3; 263 -4.9; 282 -4.4; 301 -4.0; 323 -3.6; 345 -3.1; 369 -2.7; 395 -2.4; 423 -1.8; 452 -1.4; 484 -1.2; 518 -0.9; 554 -0.5; 593 -0.1; 635 0.1; 679 0.2; 726 0.2; 777 0.9; 832 1.1; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.3; 1336 -1.9; 1429 -2.6; 1529 -3.4; 1636 -4.4; 1751 -5.5; 1873 -6.4; 2004 -7.1; 2145 -7.4; 2295 -7.1; 2455 -5.4; 2627 -3.2; 2811 -0.7; 3008 2.2; 3219 4.1; 3444 5.9; 3685 6.0; 3943 5.7; 4219 4.2; 4514 2.5; 4830 1.3; 5168 0.4; 5530 -2.1; 5917 -6.8; 6331 -8.3; 6775 -4.0; 7249 -1.0; 7756 0.2; 8299 0.0; 8880 -0.6; 9502 -1.1; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Uptown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 9 Hz     | 0.78 | -11.1 dB |
| Peaking | 33 Hz    | 0.37 | -8.5 dB  |
| Peaking | 165 Hz   | 0.85 | -5.7 dB  |
| Peaking | 2019 Hz  | 3.3  | -8.4 dB  |
| Peaking | 22585 Hz | 2.23 | -4.4 dB  |
| Peaking | 802 Hz   | 2.7  | 1.7 dB   |
| Peaking | 2495 Hz  | 4.53 | -4.5 dB  |
| Peaking | 1524 Hz  | 3.78 | -1.9 dB  |
| Peaking | 3625 Hz  | 2    | 7.4 dB   |
| Peaking | 6194 Hz  | 5.67 | -10.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Uptown/PNY%20Uptown.png)