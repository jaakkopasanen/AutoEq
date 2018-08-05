# RBH EP3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 10 -84; 20 -14.9; 22 -14.9; 23 -14.8; 25 -14.7; 26 -14.6; 28 -14.5; 30 -14.4; 32 -14.2; 35 -14.0; 37 -13.8; 40 -13.6; 42 -13.4; 45 -13.1; 49 -12.8; 52 -12.5; 56 -12.2; 59 -12.0; 64 -11.7; 68 -11.4; 73 -11.2; 78 -11.0; 83 -10.9; 89 -10.9; 95 -10.9; 102 -11.1; 109 -11.1; 117 -11.3; 125 -11.4; 134 -11.4; 143 -11.3; 153 -11.2; 164 -10.9; 175 -10.5; 188 -10.0; 201 -9.7; 215 -9.1; 230 -8.5; 246 -8.1; 263 -7.6; 282 -7.1; 301 -6.7; 323 -6.1; 345 -5.6; 369 -5.1; 395 -4.6; 423 -4.0; 452 -3.5; 484 -3.1; 518 -2.6; 554 -2.0; 593 -1.4; 635 -1.0; 679 -0.8; 726 -0.5; 777 -0.0; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 0.1; 1167 -0.0; 1248 -0.7; 1336 -1.8; 1429 -2.6; 1529 -3.2; 1636 -3.7; 1751 -3.9; 1873 -4.0; 2004 -4.1; 2145 -4.1; 2295 -4.0; 2455 -3.5; 2627 -2.9; 2811 -2.2; 3008 -0.5; 3219 1.1; 3444 2.2; 3685 2.0; 3943 1.2; 4219 -1.2; 4514 -3.6; 4830 -6.2; 5168 -9.0; 5530 -9.1; 5917 -4.9; 6331 -0.8; 6775 1.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.0; 10167 -0.7; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -3.1; 16326 -1.8; 17469 -0.0; 18692 0.0; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.8dB` and instead set Global volume in the UI for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 0.94 | -14.8 dB |
| Peaking | 29 Hz    | 0.28 | -12.2 dB |
| Peaking | 180 Hz   | 0.69 | -7.1 dB  |
| Peaking | 1971 Hz  | 2.41 | -4.6 dB  |
| Peaking | 5304 Hz  | 6.12 | -10.7 dB |
| Peaking | 891 Hz   | 2.13 | 1.6 dB   |
| Peaking | 3746 Hz  | 1.09 | -3.8 dB  |
| Peaking | 3597 Hz  | 2.99 | 7.3 dB   |
| Peaking | 6920 Hz  | 5.26 | 3.8 dB   |
| Peaking | 15595 Hz | 5.35 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP3/RBH%20EP3.png)