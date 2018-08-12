# AKG K271 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.7; 78 5.2; 83 4.8; 89 4.5; 95 4.4; 102 4.5; 109 4.7; 117 5.3; 125 5.9; 134 6.0; 143 6.0; 153 6.0; 164 5.9; 175 4.6; 188 3.4; 201 2.5; 215 1.5; 230 0.8; 246 0.3; 263 -0.1; 282 -0.5; 301 -0.6; 323 -0.7; 345 -0.7; 369 -0.7; 395 -0.7; 423 -0.8; 452 -0.9; 484 -1.0; 518 -1.2; 554 -1.5; 593 -2.2; 635 -3.8; 679 -3.4; 726 1.0; 777 2.0; 832 1.4; 890 1.1; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -1.8; 1429 -2.3; 1529 -2.9; 1636 -3.3; 1751 -3.6; 1873 -3.5; 2004 -2.3; 2145 0.1; 2295 1.3; 2455 1.8; 2627 3.0; 2811 3.9; 3008 4.6; 3219 4.0; 3444 3.3; 3685 4.3; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 4.7; 5917 2.3; 6331 0.6; 6775 -2.2; 7249 -3.5; 7756 -3.9; 8299 -3.5; 8880 -1.2; 9502 0.0; 10167 0.0; 10879 -0.1; 11640 -2.8; 12455 -4.9; 13327 -3.5; 14260 -0.4; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.9dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.45 | 6.6 dB  |
| Peaking | 145 Hz   | 2.4  | 4.8 dB  |
| Peaking | 2904 Hz  | 1.98 | 7.6 dB  |
| Peaking | 4146 Hz  | 0.4  | -7.3 dB |
| Peaking | 4734 Hz  | 1.64 | 12.8 dB |
| Peaking | 686 Hz   | 2.18 | -8.9 dB |
| Peaking | 767 Hz   | 2.65 | 10.1 dB |
| Peaking | 7718 Hz  | 3.11 | -4.8 dB |
| Peaking | 11089 Hz | 1    | 5.4 dB  |
| Peaking | 12434 Hz | 3.12 | -8.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K271%20MKII/AKG%20K271%20MKII.png)