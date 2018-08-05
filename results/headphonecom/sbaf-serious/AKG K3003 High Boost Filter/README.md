# AKG K3003 High Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 3.2; 22 2.7; 23 2.5; 25 2.0; 26 1.8; 28 1.5; 30 1.2; 32 0.9; 35 0.6; 37 0.5; 40 0.2; 42 0.1; 45 -0.2; 49 -0.4; 52 -0.5; 56 -0.7; 59 -0.8; 64 -1.0; 68 -1.1; 73 -1.4; 78 -1.5; 83 -1.7; 89 -2.0; 95 -2.4; 102 -2.9; 109 -3.4; 117 -3.9; 125 -4.6; 134 -5.0; 143 -5.1; 153 -5.4; 164 -5.4; 175 -5.4; 188 -5.4; 201 -5.3; 215 -5.0; 230 -4.8; 246 -4.6; 263 -4.5; 282 -4.2; 301 -3.9; 323 -3.5; 345 -3.1; 369 -2.8; 395 -2.5; 423 -2.1; 452 -1.9; 484 -1.8; 518 -1.5; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.0; 777 0.5; 832 0.3; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.8; 1429 -0.9; 1529 -1.2; 1636 -1.6; 1751 -1.9; 1873 -1.8; 2004 -1.7; 2145 -1.7; 2295 -1.5; 2455 -1.4; 2627 -1.5; 2811 -1.6; 3008 -1.3; 3219 -0.3; 3444 2.5; 3685 4.4; 3943 4.2; 4219 0.9; 4514 -4.0; 4830 -6.3; 5168 -5.7; 5530 -5.6; 5917 -3.5; 6331 0.1; 6775 2.1; 7249 1.3; 7756 0.0; 8299 -3.3; 8880 -7.7; 9502 -10.6; 10167 -10.2; 10879 -6.0; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.9  | 4.2 dB   |
| Peaking | 183 Hz   | 0.71 | -5.6 dB  |
| Peaking | 6825 Hz  | 0.98 | 5.7 dB   |
| Peaking | 5287 Hz  | 3.51 | -10.5 dB |
| Peaking | 9598 Hz  | 3.18 | -14.9 dB |
| Peaking | 814 Hz   | 2.3  | 1.3 dB   |
| Peaking | 2566 Hz  | 0.94 | -2.7 dB  |
| Peaking | 3827 Hz  | 3.96 | 6.8 dB   |
| Peaking | 4592 Hz  | 9.16 | -3.9 dB  |
| Peaking | 12060 Hz | 7.71 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)