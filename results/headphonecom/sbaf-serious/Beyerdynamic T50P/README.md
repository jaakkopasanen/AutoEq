# beyerdynamic T50P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.7; 32 5.3; 35 4.7; 37 4.3; 40 3.8; 42 3.5; 45 3.1; 49 2.5; 52 2.1; 56 1.4; 59 1.2; 64 1.8; 68 2.6; 73 2.1; 78 1.2; 83 0.8; 89 0.3; 95 0.4; 102 0.4; 109 0.1; 117 0.0; 125 0.2; 134 0.4; 143 1.1; 153 2.4; 164 3.9; 175 3.1; 188 1.0; 201 -0.8; 215 -1.4; 230 -1.6; 246 -2.1; 263 -3.2; 282 -4.7; 301 -5.6; 323 -5.5; 345 -5.2; 369 -4.9; 395 -4.5; 423 -4.3; 452 -4.2; 484 -3.9; 518 -3.7; 554 -3.3; 593 -2.8; 635 -2.6; 679 -2.2; 726 -0.7; 777 -0.6; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.0; 1090 0.3; 1167 0.5; 1248 0.7; 1336 0.7; 1429 0.5; 1529 0.4; 1636 0.2; 1751 0.1; 1873 0.3; 2004 0.7; 2145 1.6; 2295 2.5; 2455 3.7; 2627 4.3; 2811 4.8; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.7; 5917 3.3; 6331 2.5; 6775 2.6; 7249 0.6; 7756 -4.0; 8299 -6.8; 8880 -7.1; 9502 -5.1; 10167 -1.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -1.7; 18692 -2.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `beyerdynamic T50P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.73 | 6.2 dB   |
| Peaking | 168 Hz   | 4.17 | 5.3 dB   |
| Peaking | 355 Hz   | 0.97 | -5.5 dB  |
| Peaking | 4293 Hz  | 0.87 | 7.0 dB   |
| Peaking | 8605 Hz  | 3.45 | -10.3 dB |
| Peaking | 237 Hz   | 9.18 | 0.8 dB   |
| Peaking | 1913 Hz  | 2.08 | -3.4 dB  |
| Peaking | 2367 Hz  | 0.82 | 2.2 dB   |
| Peaking | 4071 Hz  | 3.18 | -1.6 dB  |
| Peaking | 29697 Hz | 3.18 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/beyerdynamic%20T50P/beyerdynamic%20T50P.png)