# Phiaton MS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.3; 23 5.1; 25 4.5; 26 4.3; 28 3.8; 30 3.2; 32 2.6; 35 1.8; 37 1.5; 40 1.1; 42 0.9; 45 0.5; 49 -0.1; 52 -0.5; 56 -1.0; 59 -1.2; 64 -0.9; 68 -0.4; 73 -0.3; 78 -0.9; 83 -1.4; 89 -1.6; 95 -1.8; 102 -1.8; 109 -1.9; 117 -1.6; 125 -1.5; 134 -0.9; 143 0.6; 153 1.9; 164 1.7; 175 1.6; 188 1.8; 201 1.9; 215 1.8; 230 1.4; 246 1.3; 263 1.5; 282 1.7; 301 1.9; 323 2.0; 345 2.2; 369 2.5; 395 2.6; 423 2.9; 452 2.7; 484 2.4; 518 2.4; 554 2.5; 593 2.6; 635 2.6; 679 2.4; 726 2.3; 777 2.4; 832 2.3; 890 1.4; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.4; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.0; 1751 -2.0; 1873 -1.4; 2004 -0.3; 2145 1.4; 2295 3.0; 2455 4.8; 2627 5.6; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.61 | 5.8 dB  |
| Peaking | 100 Hz  | 1.41 | -3.3 dB |
| Peaking | 646 Hz  | 0.19 | 2.9 dB  |
| Peaking | 1620 Hz | 1.21 | -7.1 dB |
| Peaking | 3440 Hz | 0.78 | 6.9 dB  |
| Peaking | 157 Hz  | 9    | 1.4 dB  |
| Peaking | 2634 Hz | 3.88 | 2.3 dB  |
| Peaking | 3076 Hz | 1.32 | -1.4 dB |
| Peaking | 6233 Hz | 2.18 | 5.6 dB  |
| Peaking | 7425 Hz | 1.48 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20400/Phiaton%20MS%20400.png)