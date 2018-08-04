# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.4; 32 4.8; 35 3.8; 37 3.3; 40 2.7; 42 2.3; 45 1.6; 49 0.7; 52 0.2; 56 -0.2; 59 -0.4; 64 -0.7; 68 -0.8; 73 -0.8; 78 -0.6; 83 -0.5; 89 -0.4; 95 -0.5; 102 -0.5; 109 -0.5; 117 -0.4; 125 -0.3; 134 -0.2; 143 0.1; 153 0.2; 164 0.4; 175 0.5; 188 0.7; 201 1.0; 215 1.4; 230 1.6; 246 1.6; 263 1.7; 282 1.8; 301 1.7; 323 1.6; 345 1.6; 369 1.8; 395 2.3; 423 2.5; 452 2.7; 484 3.2; 518 3.7; 554 4.0; 593 4.3; 635 4.5; 679 4.5; 726 4.0; 777 3.0; 832 2.3; 890 1.5; 952 0.7; 1019 -0.2; 1090 -1.0; 1167 -1.5; 1248 -1.4; 1336 -0.6; 1429 0.0; 1529 1.3; 1636 2.0; 1751 2.1; 1873 2.2; 2004 3.7; 2145 5.2; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.76 | 7.0 dB  |
| Peaking | 253 Hz  | 2.78 | 1.2 dB  |
| Peaking | 629 Hz  | 1.27 | 4.5 dB  |
| Peaking | 1186 Hz | 2.04 | -4.4 dB |
| Peaking | 3427 Hz | 0.71 | 6.9 dB  |
| Peaking | 14 Hz   | 1.85 | 3.4 dB  |
| Peaking | 72 Hz   | 1.39 | -1.3 dB |
| Peaking | 3569 Hz | 4.52 | -1.0 dB |
| Peaking | 6235 Hz | 2.31 | 4.9 dB  |
| Peaking | 7574 Hz | 1.53 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Phiaton%20MS%20300/Phiaton%20MS%20300.png)