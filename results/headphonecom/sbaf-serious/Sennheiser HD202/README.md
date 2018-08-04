# Sennheiser HD202

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.2; 32 4.5; 35 3.6; 37 3.1; 40 2.4; 42 2.0; 45 1.4; 49 0.9; 52 0.7; 56 0.5; 59 0.2; 64 -0.4; 68 -0.4; 73 -0.3; 78 -0.6; 83 -0.9; 89 -0.9; 95 -1.1; 102 -1.3; 109 -1.3; 117 -1.3; 125 -1.5; 134 -1.5; 143 -1.4; 153 -1.1; 164 -0.5; 175 0.1; 188 1.3; 201 3.2; 215 4.7; 230 4.9; 246 4.5; 263 4.3; 282 4.2; 301 4.2; 323 4.0; 345 3.2; 369 2.9; 395 2.8; 423 2.9; 452 2.6; 484 2.1; 518 1.8; 554 1.6; 593 1.4; 635 1.1; 679 0.7; 726 0.5; 777 0.5; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.2; 1336 -0.0; 1429 -0.6; 1529 -0.6; 1636 -0.5; 1751 0.3; 1873 1.2; 2004 2.2; 2145 3.4; 2295 4.7; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.3; 4514 -0.4; 4830 2.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.22 | 6.6 dB  |
| Peaking | 161 Hz  | 0.86 | -6.4 dB |
| Peaking | 232 Hz  | 1.01 | 9.1 dB  |
| Peaking | 3017 Hz | 1.83 | 6.8 dB  |
| Peaking | 5849 Hz | 3.7  | 6.0 dB  |
| Peaking | 2676 Hz | 0.95 | -5.5 dB |
| Peaking | 2377 Hz | 2.57 | 6.0 dB  |
| Peaking | 4200 Hz | 1.97 | 6.5 dB  |
| Peaking | 4499 Hz | 8.06 | -7.9 dB |
| Peaking | 8241 Hz | 3.63 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD202/Sennheiser%20HD202.png)