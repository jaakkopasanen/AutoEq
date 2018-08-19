# Klipsch Image One B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 10 -84; 20 -9.5; 22 -9.7; 23 -9.8; 25 -10.0; 26 -10.0; 28 -10.1; 30 -10.2; 32 -10.3; 35 -10.3; 37 -10.4; 40 -10.4; 42 -10.4; 45 -10.4; 49 -10.4; 52 -10.4; 56 -10.4; 59 -10.5; 64 -10.5; 68 -10.5; 73 -10.5; 78 -10.6; 83 -10.7; 89 -10.7; 95 -10.8; 102 -10.6; 109 -10.3; 117 -10.1; 125 -10.1; 134 -10.3; 143 -10.4; 153 -10.4; 164 -10.1; 175 -9.7; 188 -9.8; 201 -9.6; 215 -9.2; 230 -8.9; 246 -8.7; 263 -8.4; 282 -8.0; 301 -7.5; 323 -6.8; 345 -6.0; 369 -4.9; 395 -4.0; 423 -2.7; 452 -1.7; 484 -1.1; 518 -0.5; 554 0.1; 593 0.7; 635 1.1; 679 1.5; 726 1.9; 777 1.9; 832 1.3; 890 0.5; 952 -0.1; 1019 -0.0; 1090 -0.5; 1167 -1.5; 1248 -2.1; 1336 -2.7; 1429 -3.2; 1529 -3.8; 1636 -4.4; 1751 -5.0; 1873 -5.4; 2004 -5.8; 2145 -6.1; 2295 -6.5; 2455 -6.9; 2627 -7.4; 2811 -7.9; 3008 -7.4; 3219 -6.5; 3444 -5.1; 3685 -3.6; 3943 -1.9; 4219 -1.0; 4514 0.1; 4830 1.3; 5168 0.4; 5530 -1.0; 5917 -0.2; 6331 1.1; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.0; 10167 -0.3; 10879 -0.4; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.433108046900153dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.23 | -9.6 dB  |
| Peaking | 268 Hz  | 0.41 | -8.2 dB  |
| Peaking | 636 Hz  | 0.79 | 7.9 dB   |
| Peaking | 2971 Hz | 0.74 | -12.9 dB |
| Peaking | 4439 Hz | 0.84 | 8.4 dB   |
| Peaking | 2358 Hz | 6    | 0.7 dB   |
| Peaking | 4922 Hz | 4.56 | 2.2 dB   |
| Peaking | 5508 Hz | 4.92 | -2.5 dB  |
| Peaking | 6594 Hz | 1.28 | -1.0 dB  |
| Peaking | 6822 Hz | 7.3  | 3.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One%20B/Klipsch%20Image%20One%20B.png)