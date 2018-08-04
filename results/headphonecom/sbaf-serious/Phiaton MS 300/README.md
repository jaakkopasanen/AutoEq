# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.3; 35 4.4; 37 3.9; 40 3.3; 42 2.9; 45 2.2; 49 1.3; 52 0.8; 56 0.4; 59 0.2; 64 -0.1; 68 -0.2; 73 -0.2; 78 0.0; 83 0.2; 89 0.4; 95 0.4; 102 0.5; 109 0.6; 117 0.9; 125 1.0; 134 1.1; 143 1.4; 153 1.5; 164 1.7; 175 1.9; 188 2.1; 201 2.4; 215 2.8; 230 3.0; 246 3.0; 263 3.0; 282 3.1; 301 3.0; 323 3.0; 345 3.1; 369 3.2; 395 3.6; 423 3.7; 452 3.7; 484 3.9; 518 4.2; 554 4.5; 593 4.7; 635 4.8; 679 4.5; 726 3.9; 777 3.2; 832 2.4; 890 1.5; 952 0.8; 1019 -0.2; 1090 -1.1; 1167 -1.8; 1248 -2.1; 1336 -1.9; 1429 -2.1; 1529 -1.4; 1636 -1.0; 1751 -1.0; 1873 -0.7; 2004 0.8; 2145 2.2; 2295 4.2; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.44 | 6.8 dB  |
| Peaking | 243 Hz  | 1.25 | 2.3 dB  |
| Peaking | 634 Hz  | 1.02 | 5.3 dB  |
| Peaking | 1393 Hz | 1.04 | -6.1 dB |
| Peaking | 3355 Hz | 0.74 | 7.8 dB  |
| Peaking | 67 Hz   | 3.01 | -1.2 dB |
| Peaking | 2510 Hz | 4.52 | 3.0 dB  |
| Peaking | 2787 Hz | 1.29 | -1.5 dB |
| Peaking | 6248 Hz | 2.18 | 5.8 dB  |
| Peaking | 7350 Hz | 1.45 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)