# AKG K3003 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.2; 22 2.7; 23 2.5; 25 2.1; 26 1.9; 28 1.6; 30 1.3; 32 1.0; 35 0.7; 37 0.5; 40 0.3; 42 0.1; 45 -0.1; 49 -0.3; 52 -0.5; 56 -0.6; 59 -0.7; 64 -1.0; 68 -1.0; 73 -1.2; 78 -1.5; 83 -1.7; 89 -2.0; 95 -2.4; 102 -2.9; 109 -3.4; 117 -3.9; 125 -4.5; 134 -4.8; 143 -5.1; 153 -5.4; 164 -5.4; 175 -5.4; 188 -5.3; 201 -5.2; 215 -5.0; 230 -4.8; 246 -4.6; 263 -4.4; 282 -4.1; 301 -3.8; 323 -3.5; 345 -3.1; 369 -2.7; 395 -2.4; 423 -2.0; 452 -1.8; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.5; 635 -0.2; 679 -0.1; 726 0.2; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -0.9; 1336 -1.0; 1429 -1.1; 1529 -1.6; 1636 -2.1; 1751 -2.4; 1873 -2.3; 2004 -2.3; 2145 -2.1; 2295 -1.5; 2455 -0.6; 2627 0.5; 2811 1.8; 3008 3.2; 3219 4.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.8; 4514 -0.9; 4830 -3.2; 5168 -2.5; 5530 -0.2; 5917 2.8; 6331 4.8; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -3.1; 8880 -6.9; 9502 -8.8; 10167 -6.8; 10879 -1.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.83 | 4.2 dB  |
| Peaking | 184 Hz  | 0.73 | -5.6 dB |
| Peaking | 3556 Hz | 4.64 | 7.3 dB  |
| Peaking | 6535 Hz | 6.64 | 6.0 dB  |
| Peaking | 9412 Hz | 4.44 | -9.8 dB |
| Peaking | 824 Hz  | 1.87 | 1.6 dB  |
| Peaking | 2510 Hz | 0.86 | -4.0 dB |
| Peaking | 4480 Hz | 1.64 | 5.9 dB  |
| Peaking | 4875 Hz | 4.6  | -8.7 dB |
| Peaking | 2830 Hz | 3.6  | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)