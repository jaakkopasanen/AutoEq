# Phiaton MS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.5; 22 4.8; 23 4.5; 25 4.0; 26 3.7; 28 3.2; 30 2.7; 32 2.1; 35 1.3; 37 0.9; 40 0.5; 42 0.3; 45 -0.1; 49 -0.7; 52 -1.1; 56 -1.6; 59 -1.8; 64 -1.5; 68 -0.9; 73 -0.9; 78 -1.6; 83 -2.1; 89 -2.4; 95 -2.7; 102 -2.8; 109 -3.0; 117 -2.9; 125 -2.7; 134 -2.2; 143 -0.8; 153 0.6; 164 0.4; 175 0.2; 188 0.4; 201 0.6; 215 0.4; 230 -0.0; 246 -0.1; 263 0.1; 282 0.4; 301 0.5; 323 0.6; 345 0.8; 369 1.1; 395 1.3; 423 1.7; 452 1.7; 484 1.7; 518 1.9; 554 2.1; 593 2.2; 635 2.3; 679 2.3; 726 2.3; 777 2.2; 832 2.2; 890 1.4; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.1; 1248 0.2; 1336 0.6; 1429 0.9; 1529 1.0; 1636 1.0; 1751 1.1; 1873 1.5; 2004 2.6; 2145 4.4; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.02 | 5.5 dB  |
| Peaking | 56 Hz   | 1.84 | -2.0 dB |
| Peaking | 106 Hz  | 2.52 | -3.3 dB |
| Peaking | 561 Hz  | 1.51 | 2.2 dB  |
| Peaking | 3781 Hz | 0.89 | 7.0 dB  |
| Peaking | 1837 Hz | 2.78 | -1.7 dB |
| Peaking | 1109 Hz | 5.56 | -1.6 dB |
| Peaking | 2329 Hz | 3.39 | 3.1 dB  |
| Peaking | 6053 Hz | 2.37 | 6.9 dB  |
| Peaking | 6572 Hz | 1.06 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Phiaton%20MS%20400/Phiaton%20MS%20400.png)