# AKG K812

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -4.6; 22 -5.0; 23 -5.1; 25 -5.4; 26 -5.5; 28 -5.7; 30 -5.8; 32 -6.0; 35 -6.1; 37 -6.2; 40 -6.3; 42 -6.4; 45 -6.5; 49 -6.6; 52 -6.6; 56 -6.6; 59 -6.6; 64 -6.8; 68 -6.8; 73 -6.6; 78 -6.4; 83 -6.4; 89 -6.3; 95 -6.2; 102 -6.1; 109 -6.2; 117 -6.0; 125 -6.0; 134 -6.0; 143 -6.0; 153 -6.0; 164 -5.8; 175 -5.6; 188 -5.6; 201 -5.6; 215 -5.5; 230 -5.4; 246 -5.2; 263 -5.1; 282 -5.0; 301 -4.7; 323 -4.6; 345 -4.3; 369 -4.1; 395 -4.0; 423 -3.6; 452 -3.5; 484 -3.4; 518 -3.1; 554 -2.8; 593 -2.4; 635 -2.1; 679 -1.9; 726 -1.5; 777 -0.9; 832 -0.6; 890 -0.6; 952 -0.3; 1019 0.0; 1090 0.4; 1167 1.0; 1248 1.2; 1336 1.2; 1429 0.1; 1529 -1.0; 1636 -0.9; 1751 0.1; 1873 0.4; 2004 0.2; 2145 0.1; 2295 -0.2; 2455 1.8; 2627 5.2; 2811 2.3; 3008 -0.5; 3219 -0.8; 3444 -0.6; 3685 -2.5; 3943 -3.0; 4219 0.9; 4514 1.9; 4830 -0.1; 5168 -2.8; 5530 -5.3; 5917 -7.7; 6331 -7.0; 6775 -1.3; 7249 0.6; 7756 -0.0; 8299 -2.1; 8880 -4.5; 9502 -6.2; 10167 -5.7; 10879 -2.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -2.2; 16326 -1.7; 17469 0.0; 18692 -0.0; 20000 -7.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 0.24 | -6.4 dB |
| Peaking | 341 Hz   | 0.73 | -2.3 dB |
| Peaking | 3858 Hz  | 0.56 | 4.9 dB  |
| Peaking | 5760 Hz  | 0.66 | -7.3 dB |
| Peaking | 20020 Hz | 5.21 | -7.0 dB |
| Peaking | 3865 Hz  | 5.66 | -5.2 dB |
| Peaking | 4414 Hz  | 4.28 | 5.5 dB  |
| Peaking | 6124 Hz  | 4.25 | -9.0 dB |
| Peaking | 7062 Hz  | 2.7  | 7.2 dB  |
| Peaking | 9551 Hz  | 5.28 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K812/AKG%20K812.png)