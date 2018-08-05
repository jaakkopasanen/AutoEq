# AKG K3003 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.5; 22 4.0; 23 3.7; 25 3.3; 26 3.1; 28 2.8; 30 2.5; 32 2.2; 35 1.8; 37 1.6; 40 1.4; 42 1.2; 45 1.0; 49 0.8; 52 0.6; 56 0.4; 59 0.3; 64 0.1; 68 -0.1; 73 -0.3; 78 -0.5; 83 -0.8; 89 -1.2; 95 -1.8; 102 -2.4; 109 -2.8; 117 -3.3; 125 -3.9; 134 -4.4; 143 -4.7; 153 -4.8; 164 -5.0; 175 -4.9; 188 -4.9; 201 -4.8; 215 -4.6; 230 -4.4; 246 -4.3; 263 -4.1; 282 -3.8; 301 -3.6; 323 -3.3; 345 -3.0; 369 -2.7; 395 -2.4; 423 -2.0; 452 -1.7; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.4; 635 -0.2; 679 -0.1; 726 0.1; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.5; 1636 -2.0; 1751 -2.3; 1873 -2.2; 2004 -2.1; 2145 -1.9; 2295 -1.6; 2455 -0.6; 2627 0.4; 2811 1.6; 3008 3.0; 3219 4.2; 3444 5.9; 3685 6.0; 3943 5.9; 4219 2.8; 4514 -1.5; 4830 -3.7; 5168 -3.1; 5530 -1.5; 5917 1.3; 6331 3.6; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -3.7; 9502 -6.1; 10167 -6.5; 10879 -3.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 9 Hz     | 0.32 | 5.4 dB   |
| Peaking | 184 Hz   | 0.79 | -5.4 dB  |
| Peaking | 3688 Hz  | 2.09 | 15.2 dB  |
| Peaking | 6523 Hz  | 2.85 | 12.7 dB  |
| Peaking | 5179 Hz  | 0.74 | -12.3 dB |
| Peaking | 832 Hz   | 2.17 | 1.3 dB   |
| Peaking | 1842 Hz  | 3.23 | -1.4 dB  |
| Peaking | 8116 Hz  | 7.2  | 2.3 dB   |
| Peaking | 9999 Hz  | 3.13 | -7.5 dB  |
| Peaking | 11482 Hz | 1.52 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)