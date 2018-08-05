# Beats Tour 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.6; 22 -5.9; 23 -6.1; 25 -6.4; 26 -6.5; 28 -6.7; 30 -6.8; 32 -7.0; 35 -7.1; 37 -7.2; 40 -7.2; 42 -7.3; 45 -7.3; 49 -7.4; 52 -7.4; 56 -7.4; 59 -7.4; 64 -7.3; 68 -7.3; 73 -7.4; 78 -7.4; 83 -7.6; 89 -7.8; 95 -8.1; 102 -8.4; 109 -8.7; 117 -9.1; 125 -9.4; 134 -9.6; 143 -9.7; 153 -9.6; 164 -9.5; 175 -9.2; 188 -8.9; 201 -8.6; 215 -8.2; 230 -7.8; 246 -7.4; 263 -7.0; 282 -6.5; 301 -6.1; 323 -5.6; 345 -5.2; 369 -4.7; 395 -4.2; 423 -3.7; 452 -3.2; 484 -2.9; 518 -2.4; 554 -1.8; 593 -1.2; 635 -0.9; 679 -0.6; 726 -0.3; 777 0.1; 832 0.1; 890 0.1; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.3; 1336 -0.5; 1429 -0.9; 1529 -1.1; 1636 -1.2; 1751 -1.1; 1873 -0.8; 2004 -0.4; 2145 0.0; 2295 0.5; 2455 1.6; 2627 2.3; 2811 3.1; 3008 4.5; 3219 5.5; 3444 6.0; 3685 6.0; 3943 5.5; 4219 3.7; 4514 2.1; 4830 1.5; 5168 1.6; 5530 1.8; 5917 2.7; 6331 3.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Tour 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 7 Hz     | 1.51 | -5.1 dB |
| Peaking | 34 Hz    | 0.4  | -6.0 dB |
| Peaking | 171 Hz   | 0.62 | -8.2 dB |
| Peaking | 3570 Hz  | 2.09 | 6.3 dB  |
| Peaking | 23022 Hz | 2.37 | 1.5 dB  |
| Peaking | 379 Hz   | 2.19 | -0.7 dB |
| Peaking | 785 Hz   | 1.68 | 1.3 dB  |
| Peaking | 1701 Hz  | 2.73 | -1.7 dB |
| Peaking | 6612 Hz  | 1.63 | -2.0 dB |
| Peaking | 6519 Hz  | 4.17 | 5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Tour%202014/Beats%20Tour%202014.png)