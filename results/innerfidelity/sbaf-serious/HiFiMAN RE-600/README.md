# HiFiMAN RE-600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.1; 22 4.1; 23 4.1; 25 4.1; 26 4.1; 28 4.0; 30 4.0; 32 4.0; 35 3.9; 37 3.9; 40 3.9; 42 3.9; 45 3.9; 49 3.9; 52 3.8; 56 3.8; 59 3.7; 64 3.7; 68 3.6; 73 3.5; 78 3.3; 83 3.0; 89 2.6; 95 2.2; 102 1.7; 109 1.2; 117 0.7; 125 0.2; 134 -0.3; 143 -0.6; 153 -0.8; 164 -0.9; 175 -0.9; 188 -0.9; 201 -0.9; 215 -0.8; 230 -0.7; 246 -0.6; 263 -0.5; 282 -0.3; 301 -0.1; 323 -0.0; 345 0.2; 369 0.3; 395 0.5; 423 0.7; 452 1.0; 484 0.9; 518 1.1; 554 1.3; 593 1.5; 635 1.6; 679 1.5; 726 1.5; 777 1.5; 832 1.2; 890 0.8; 952 0.5; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -2.8; 1429 -3.8; 1529 -4.7; 1636 -5.6; 1751 -6.2; 1873 -5.2; 2004 -4.6; 2145 -4.2; 2295 -2.1; 2455 0.8; 2627 3.4; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.7; 5530 5.1; 5917 5.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 45 Hz   | 0.24 | 4.5 dB   |
| Peaking | 164 Hz  | 0.91 | -3.8 dB  |
| Peaking | 734 Hz  | 1.14 | 2.1 dB   |
| Peaking | 1861 Hz | 1.35 | -11.0 dB |
| Peaking | 3312 Hz | 0.84 | 9.6 dB   |
| Peaking | 2259 Hz | 8.66 | -1.5 dB  |
| Peaking | 2812 Hz | 3.96 | 1.7 dB   |
| Peaking | 3528 Hz | 3.64 | -1.4 dB  |
| Peaking | 6416 Hz | 2.32 | 5.3 dB   |
| Peaking | 7436 Hz | 1.62 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-600/HiFiMAN%20RE-600.png)