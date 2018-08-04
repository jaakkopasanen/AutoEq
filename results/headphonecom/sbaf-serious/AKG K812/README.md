# AKG K812

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -0.6; 22 -1.0; 23 -1.1; 25 -1.4; 26 -1.5; 28 -1.7; 30 -1.8; 32 -2.0; 35 -2.1; 37 -2.2; 40 -2.3; 42 -2.4; 45 -2.5; 49 -2.6; 52 -2.6; 56 -2.6; 59 -2.7; 64 -2.9; 68 -2.9; 73 -2.8; 78 -2.8; 83 -2.9; 89 -3.1; 95 -3.3; 102 -3.7; 109 -4.1; 117 -4.5; 125 -4.9; 134 -5.2; 143 -5.4; 153 -5.6; 164 -5.5; 175 -5.4; 188 -5.5; 201 -5.5; 215 -5.4; 230 -5.4; 246 -5.2; 263 -5.1; 282 -5.0; 301 -4.7; 323 -4.6; 345 -4.3; 369 -4.1; 395 -4.0; 423 -3.6; 452 -3.5; 484 -3.4; 518 -3.1; 554 -2.8; 593 -2.4; 635 -2.1; 679 -1.9; 726 -1.5; 777 -0.9; 832 -0.6; 890 -0.6; 952 -0.3; 1019 0.0; 1090 0.4; 1167 1.0; 1248 1.2; 1336 1.2; 1429 0.1; 1529 -1.0; 1636 -0.9; 1751 0.1; 1873 0.4; 2004 0.2; 2145 0.1; 2295 -0.2; 2455 1.8; 2627 5.2; 2811 2.3; 3008 -0.5; 3219 -0.8; 3444 -0.6; 3685 -2.5; 3943 -3.0; 4219 0.9; 4514 1.9; 4830 -0.1; 5168 -2.8; 5530 -5.3; 5917 -7.7; 6331 -7.0; 6775 -1.3; 7249 0.6; 7756 -0.0; 8299 -2.1; 8880 -4.5; 9502 -6.2; 10167 -5.7; 10879 -2.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -2.2; 16326 -1.7; 17469 0.0; 18692 -0.0; 20000 -7.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 1    | -1.5 dB  |
| Peaking | 205 Hz   | 0.47 | -5.6 dB  |
| Peaking | 3841 Hz  | 0.55 | 4.9 dB   |
| Peaking | 5781 Hz  | 0.66 | -7.3 dB  |
| Peaking | 20014 Hz | 5.01 | -6.9 dB  |
| Peaking | 3897 Hz  | 5.43 | -5.4 dB  |
| Peaking | 4380 Hz  | 4.32 | 5.6 dB   |
| Peaking | 6073 Hz  | 3.93 | -10.4 dB |
| Peaking | 7038 Hz  | 2.14 | 8.0 dB   |
| Peaking | 9556 Hz  | 4.74 | -6.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K812/AKG%20K812.png)