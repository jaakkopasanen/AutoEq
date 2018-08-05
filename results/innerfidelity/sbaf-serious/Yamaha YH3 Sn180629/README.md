# Yamaha YH3 Sn180629

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.3; 22 3.0; 23 2.8; 25 2.6; 26 2.4; 28 2.2; 30 2.1; 32 1.9; 35 1.7; 37 1.6; 40 1.5; 42 1.5; 45 1.4; 49 1.4; 52 1.3; 56 1.2; 59 1.1; 64 0.9; 68 0.9; 73 0.8; 78 0.7; 83 0.6; 89 0.4; 95 0.1; 102 -0.5; 109 -0.8; 117 -1.1; 125 -1.5; 134 -1.9; 143 -2.2; 153 -2.4; 164 -2.5; 175 -2.6; 188 -2.8; 201 -2.8; 215 -2.8; 230 -2.7; 246 -2.8; 263 -2.8; 282 -2.6; 301 -2.5; 323 -2.3; 345 -2.2; 369 -2.2; 395 -2.3; 423 -2.3; 452 -2.2; 484 -2.3; 518 -2.3; 554 -2.1; 593 -2.0; 635 -2.0; 679 -2.2; 726 -1.9; 777 -1.3; 832 -1.0; 890 -0.9; 952 -0.5; 1019 0.2; 1090 1.1; 1167 2.2; 1248 3.2; 1336 4.0; 1429 4.4; 1529 4.3; 1636 4.2; 1751 3.9; 1873 3.3; 2004 1.9; 2145 1.2; 2295 0.6; 2455 0.7; 2627 1.5; 2811 2.8; 3008 5.3; 3219 6.0; 3444 5.7; 3685 3.5; 3943 3.4; 4219 3.2; 4514 4.0; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.8; 16326 -1.4; 17469 -0.2; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH3 Sn180629 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.2  | 2.8 dB  |
| Peaking | 281 Hz   | 0.29 | -3.1 dB |
| Peaking | 1463 Hz  | 2.01 | 5.6 dB  |
| Peaking | 3252 Hz  | 4.27 | 5.6 dB  |
| Peaking | 5533 Hz  | 2.51 | 6.5 dB  |
| Peaking | 84 Hz    | 4.82 | 0.8 dB  |
| Peaking | 5122 Hz  | 0.4  | 0.4 dB  |
| Peaking | 2402 Hz  | 5.56 | -1.4 dB |
| Peaking | 8700 Hz  | 2.6  | -1.5 dB |
| Peaking | 31973 Hz | 4.35 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH3%20Sn180629/Yamaha%20YH3%20Sn180629.png)