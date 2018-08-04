# AKG K 550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.3; 22 1.9; 23 1.7; 25 1.3; 26 1.2; 28 0.9; 30 0.7; 32 0.5; 35 0.4; 37 0.3; 40 0.2; 42 0.1; 45 0.1; 49 0.1; 52 0.2; 56 0.3; 59 0.3; 64 0.2; 68 0.3; 73 0.7; 78 1.2; 83 1.9; 89 2.7; 95 2.8; 102 1.7; 109 0.6; 117 -0.5; 125 -1.4; 134 -1.8; 143 -1.9; 153 -1.9; 164 -0.2; 175 -0.8; 188 -1.9; 201 -1.9; 215 -1.9; 230 -2.0; 246 -2.0; 263 -1.9; 282 -1.6; 301 -1.6; 323 -1.4; 345 -1.2; 369 -0.9; 395 -0.7; 423 -0.4; 452 -0.2; 484 -0.2; 518 -0.1; 554 0.4; 593 0.9; 635 1.2; 679 1.2; 726 1.3; 777 1.6; 832 0.9; 890 0.3; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.6; 1248 -0.8; 1336 -1.1; 1429 -1.4; 1529 -1.9; 1636 -1.8; 1751 -1.2; 1873 -0.5; 2004 -0.1; 2145 0.4; 2295 0.7; 2455 1.0; 2627 1.0; 2811 1.7; 3008 2.7; 3219 3.6; 3444 4.7; 3685 5.8; 3943 6.0; 4219 4.8; 4514 3.6; 4830 3.1; 5168 0.8; 5530 -0.8; 5917 -0.3; 6331 3.3; 6775 3.9; 7249 1.3; 7756 -0.0; 8299 -4.0; 8880 -6.9; 9502 -5.8; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 6 Hz    | 1.6  | 1.9 dB  |
| Peaking | 14 Hz   | 0.87 | 2.7 dB  |
| Peaking | 3805 Hz | 2.93 | 6.4 dB  |
| Peaking | 6719 Hz | 8.27 | 4.8 dB  |
| Peaking | 9020 Hz | 5.32 | -8.1 dB |
| Peaking | 92 Hz   | 3.84 | 3.3 dB  |
| Peaking | 133 Hz  | 4.18 | -1.9 dB |
| Peaking | 251 Hz  | 1.25 | -2.1 dB |
| Peaking | 707 Hz  | 2.5  | 1.7 dB  |
| Peaking | 1543 Hz | 3.2  | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K%20550/AKG%20K%20550.png)