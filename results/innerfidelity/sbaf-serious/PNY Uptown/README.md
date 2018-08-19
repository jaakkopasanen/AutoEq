# PNY Uptown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -11.6; 22 -11.5; 23 -11.4; 25 -11.3; 26 -11.3; 28 -11.2; 30 -11.1; 32 -10.9; 35 -10.8; 37 -10.7; 40 -10.5; 42 -10.4; 45 -10.3; 49 -10.1; 52 -10.0; 56 -9.9; 59 -9.8; 64 -9.6; 68 -9.5; 73 -9.4; 78 -9.4; 83 -9.3; 89 -9.2; 95 -9.1; 102 -8.9; 109 -8.6; 117 -8.4; 125 -8.2; 134 -8.0; 143 -7.8; 153 -7.5; 164 -7.2; 175 -6.8; 188 -6.5; 201 -6.2; 215 -5.8; 230 -5.3; 246 -5.0; 263 -4.7; 282 -4.2; 301 -3.8; 323 -3.4; 345 -3.0; 369 -2.6; 395 -2.3; 423 -1.8; 452 -1.4; 484 -1.2; 518 -0.9; 554 -0.5; 593 -0.0; 635 0.2; 679 0.2; 726 0.2; 777 0.9; 832 1.2; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.3; 1336 -1.9; 1429 -2.6; 1529 -3.4; 1636 -4.4; 1751 -5.5; 1873 -6.4; 2004 -7.1; 2145 -7.4; 2295 -7.1; 2455 -5.4; 2627 -3.2; 2811 -0.7; 3008 2.2; 3219 4.1; 3444 5.9; 3685 6.0; 3943 5.7; 4219 4.2; 4514 2.5; 4830 1.3; 5168 0.4; 5530 -2.1; 5917 -6.8; 6331 -8.3; 6775 -4.0; 7249 -1.0; 7756 0.2; 8299 0.0; 8880 -0.6; 9502 -1.1; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999529967255dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Uptown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 22 Hz   |  0.2  | -11.2 dB |
| Peaking | 159 Hz  |  0.78 | -3.6 dB  |
| Peaking | 2161 Hz |  2    | -9.5 dB  |
| Peaking | 3586 Hz |  1.99 | 8.4 dB   |
| Peaking | 6170 Hz |  5.74 | -10.1 dB |
| Peaking | 307 Hz  |  2.21 | -0.7 dB  |
| Peaking | 800 Hz  |  1.71 | 1.8 dB   |
| Peaking | 1597 Hz |  3.57 | -1.0 dB  |
| Peaking | 7735 Hz |  9.3  | 1.2 dB   |
| Peaking | 9388 Hz | 10.28 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Uptown/PNY%20Uptown.png)