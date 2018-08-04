# Phiaton MS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.5; 40 5.1; 42 4.9; 45 4.5; 49 3.8; 52 3.4; 56 3.0; 59 2.7; 64 3.0; 68 3.5; 73 3.5; 78 2.7; 83 2.1; 89 1.6; 95 1.1; 102 0.6; 109 0.2; 117 -0.0; 125 -0.3; 134 -0.1; 143 1.1; 153 2.3; 164 2.0; 175 1.8; 188 1.9; 201 2.0; 215 1.8; 230 1.4; 246 1.3; 263 1.5; 282 1.7; 301 1.9; 323 2.0; 345 2.2; 369 2.5; 395 2.6; 423 2.9; 452 2.7; 484 2.4; 518 2.4; 554 2.5; 593 2.6; 635 2.6; 679 2.4; 726 2.3; 777 2.4; 832 2.3; 890 1.4; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.4; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.0; 1751 -2.0; 1873 -1.4; 2004 -0.3; 2145 1.4; 2295 3.0; 2455 4.8; 2627 5.6; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.63 | 6.3 dB  |
| Peaking | 409 Hz  | 0.82 | 2.4 dB  |
| Peaking | 720 Hz  | 2.79 | 1.3 dB  |
| Peaking | 1679 Hz | 1.63 | -5.3 dB |
| Peaking | 3477 Hz | 0.77 | 7.5 dB  |
| Peaking | 128 Hz  | 3.29 | -2.8 dB |
| Peaking | 150 Hz  | 2.58 | 2.2 dB  |
| Peaking | 2564 Hz | 6.19 | 1.6 dB  |
| Peaking | 6055 Hz | 2.23 | 6.9 dB  |
| Peaking | 6696 Hz | 1.05 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20400/Phiaton%20MS%20400.png)