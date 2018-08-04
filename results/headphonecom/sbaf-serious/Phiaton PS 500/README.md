# Phiaton PS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.7dB
GraphicEQ: 10 -84; 20 7.1; 22 5.7; 23 5.1; 25 4.0; 26 3.5; 28 2.6; 30 1.7; 32 0.9; 35 0.1; 37 -0.1; 40 -0.2; 42 -0.4; 45 -1.2; 49 -2.2; 52 -2.1; 56 -1.5; 59 -1.4; 64 -2.0; 68 -2.8; 73 -3.4; 78 -3.8; 83 -4.0; 89 -4.2; 95 -4.4; 102 -4.3; 109 -4.2; 117 -4.3; 125 -4.2; 134 -4.2; 143 -4.2; 153 -4.1; 164 -3.6; 175 -3.8; 188 -3.7; 201 -3.3; 215 -3.2; 230 -2.8; 246 -2.2; 263 -1.5; 282 -0.4; 301 0.8; 323 1.8; 345 2.5; 369 2.8; 395 2.8; 423 2.8; 452 2.6; 484 2.3; 518 2.1; 554 2.1; 593 2.2; 635 1.9; 679 1.6; 726 1.2; 777 1.0; 832 1.4; 890 1.3; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -0.7; 1336 -0.7; 1429 -0.5; 1529 -0.5; 1636 -1.0; 1751 -1.7; 1873 -2.1; 2004 -1.2; 2145 0.2; 2295 2.1; 2455 4.6; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.8; 4514 5.7; 4830 6.0; 5168 6.0; 5530 5.9; 5917 4.4; 6331 3.0; 6775 2.6; 7249 1.3; 7756 0.2; 8299 -0.8; 8880 -1.2; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.7dB` and instead set Global volume in the UI for both channels to **-77**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.82 | 10.5 dB |
| Peaking | 579 Hz  | 0.1  | -9.2 dB |
| Peaking | 518 Hz  | 0.47 | 11.8 dB |
| Peaking | 2970 Hz | 1.45 | 10.2 dB |
| Peaking | 5094 Hz | 1.54 | 7.9 dB  |
| Peaking | 349 Hz  | 1.06 | -3.4 dB |
| Peaking | 350 Hz  | 2.09 | 5.0 dB  |
| Peaking | 1934 Hz | 3.27 | -5.1 dB |
| Peaking | 1961 Hz | 1.38 | 3.4 dB  |
| Peaking | 3071 Hz | 6.06 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20500/Phiaton%20PS%20500.png)