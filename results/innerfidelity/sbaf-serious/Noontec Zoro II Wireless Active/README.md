# Noontec Zoro II Wireless Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 0.6; 22 0.0; 23 -0.3; 25 -0.7; 26 -0.9; 28 -1.2; 30 -1.5; 32 -1.7; 35 -2.0; 37 -2.2; 40 -2.4; 42 -2.5; 45 -2.6; 49 -2.7; 52 -2.8; 56 -2.9; 59 -2.9; 64 -2.9; 68 -2.9; 73 -3.0; 78 -3.3; 83 -3.7; 89 -4.2; 95 -4.5; 102 -4.8; 109 -5.3; 117 -5.7; 125 -6.1; 134 -6.4; 143 -6.8; 153 -6.9; 164 -6.7; 175 -6.8; 188 -6.9; 201 -6.8; 215 -6.6; 230 -6.4; 246 -6.1; 263 -5.8; 282 -5.2; 301 -4.9; 323 -4.7; 345 -4.4; 369 -4.1; 395 -4.1; 423 -3.9; 452 -3.7; 484 -3.4; 518 -3.0; 554 -2.5; 593 -1.9; 635 -1.5; 679 -1.2; 726 -0.7; 777 -0.3; 832 -0.1; 890 -0.0; 952 0.0; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.7; 1636 -1.9; 1751 -1.9; 1873 -1.5; 2004 -1.0; 2145 -0.3; 2295 0.3; 2455 1.0; 2627 1.5; 2811 1.8; 3008 2.0; 3219 1.8; 3444 1.9; 3685 2.9; 3943 5.0; 4219 4.9; 4514 3.9; 4830 2.8; 5168 1.5; 5530 1.7; 5917 2.1; 6331 0.4; 6775 -0.1; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.9  | 1.5 dB  |
| Peaking | 37 Hz   | 1.18 | -1.7 dB |
| Peaking | 182 Hz  | 0.56 | -7.0 dB |
| Peaking | 1716 Hz | 4.22 | -2.2 dB |
| Peaking | 4120 Hz | 2.17 | 4.7 dB  |
| Peaking | 11 Hz   | 0.49 | 0.4 dB  |
| Peaking | 482 Hz  | 3.17 | -1.0 dB |
| Peaking | 887 Hz  | 1.5  | 1.3 dB  |
| Peaking | 2665 Hz | 3.87 | 1.4 dB  |
| Peaking | 1976 Hz | 0.57 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Active/Noontec%20Zoro%20II%20Wireless%20Active.png)