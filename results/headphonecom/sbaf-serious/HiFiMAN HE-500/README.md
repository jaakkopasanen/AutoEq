# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 3.0; 22 2.6; 23 2.4; 25 2.1; 26 1.9; 28 1.7; 30 1.5; 32 1.3; 35 1.2; 37 1.2; 40 1.2; 42 1.2; 45 1.3; 49 1.4; 52 1.4; 56 1.3; 59 1.1; 64 0.9; 68 1.0; 73 1.1; 78 1.2; 83 1.1; 89 0.8; 95 0.6; 102 0.4; 109 0.1; 117 0.0; 125 -0.3; 134 -0.7; 143 -0.8; 153 -0.8; 164 -1.1; 175 -1.0; 188 -1.1; 201 -1.0; 215 -1.0; 230 -1.1; 246 -1.1; 263 -1.3; 282 -1.2; 301 -1.1; 323 -1.0; 345 -1.0; 369 -1.1; 395 -0.8; 423 -0.7; 452 -1.0; 484 -1.2; 518 -0.9; 554 -0.9; 593 -0.9; 635 -0.6; 679 -0.8; 726 0.1; 777 0.7; 832 0.3; 890 -0.3; 952 0.1; 1019 -0.2; 1090 -0.3; 1167 0.2; 1248 0.3; 1336 1.0; 1429 1.0; 1529 0.6; 1636 0.8; 1751 1.7; 1873 2.5; 2004 2.8; 2145 1.7; 2295 0.9; 2455 2.6; 2627 2.6; 2811 1.7; 3008 0.9; 3219 0.5; 3444 0.1; 3685 0.7; 3943 0.4; 4219 -1.2; 4514 -1.8; 4830 -1.2; 5168 1.3; 5530 2.6; 5917 1.9; 6331 0.6; 6775 -0.2; 7249 -0.0; 7756 -0.6; 8299 -3.0; 8880 -5.6; 9502 -5.5; 10167 -1.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.1; 18692 -3.7; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.5dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.3  | 2.7 dB  |
| Peaking | 55 Hz   | 1.9  | 1.2 dB  |
| Peaking | 2135 Hz | 1.94 | 2.4 dB  |
| Peaking | 5638 Hz | 8.32 | 2.9 dB  |
| Peaking | 9116 Hz | 5.35 | -6.7 dB |
| Peaking | 85 Hz   | 2.08 | 1.1 dB  |
| Peaking | 246 Hz  | 0.55 | -1.3 dB |
| Peaking | 2630 Hz | 9.98 | 1.3 dB  |
| Peaking | 4563 Hz | 5.4  | -3.4 dB |
| Peaking | 4987 Hz | 2.43 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)