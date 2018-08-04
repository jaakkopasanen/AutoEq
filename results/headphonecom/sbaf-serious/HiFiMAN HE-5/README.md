# HiFiMAN HE-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.3; 23 5.0; 25 4.1; 26 3.6; 28 2.7; 30 1.9; 32 1.1; 35 0.2; 37 -0.2; 40 -0.4; 42 -0.5; 45 -0.8; 49 -1.4; 52 -1.7; 56 -2.0; 59 -2.2; 64 -2.2; 68 -2.0; 73 -1.9; 78 -1.7; 83 -1.7; 89 -1.6; 95 -1.5; 102 -1.2; 109 -0.9; 117 -1.0; 125 -1.0; 134 -1.0; 143 -1.0; 153 -1.0; 164 -0.9; 175 -0.9; 188 -1.1; 201 -1.1; 215 -1.0; 230 -0.9; 246 -0.9; 263 -0.8; 282 -0.7; 301 -0.6; 323 -0.6; 345 -0.6; 369 -0.8; 395 -1.2; 423 -1.3; 452 -0.7; 484 -0.7; 518 -0.8; 554 -0.6; 593 -0.3; 635 -0.2; 679 -0.2; 726 0.3; 777 0.6; 832 0.3; 890 -0.1; 952 0.1; 1019 0.0; 1090 0.4; 1167 1.4; 1248 1.5; 1336 1.8; 1429 1.9; 1529 1.5; 1636 1.9; 1751 3.0; 1873 3.6; 2004 4.2; 2145 3.8; 2295 2.1; 2455 2.8; 2627 2.9; 2811 1.8; 3008 0.7; 3219 0.1; 3444 -0.2; 3685 -0.1; 3943 -0.7; 4219 -3.1; 4514 -3.0; 4830 -1.3; 5168 0.2; 5530 -0.8; 5917 -2.3; 6331 -3.6; 6775 -4.9; 7249 -5.1; 7756 -5.6; 8299 -6.9; 8880 -8.4; 9502 -8.7; 10167 -6.8; 10879 -4.1; 11640 -2.3; 12455 -1.8; 13327 -1.7; 14260 -1.1; 15258 -1.0; 16326 -2.6; 17469 -5.3; 18692 -6.9; 20000 -5.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.22 | 6.5 dB  |
| Peaking | 2043 Hz  | 1.74 | 4.0 dB  |
| Peaking | 4345 Hz  | 8.03 | -3.2 dB |
| Peaking | 8897 Hz  | 1.92 | -8.6 dB |
| Peaking | 28996 Hz | 1.65 | -7.5 dB |
| Peaking | 64 Hz    | 1.41 | -2.1 dB |
| Peaking | 244 Hz   | 0.52 | -0.9 dB |
| Peaking | 5243 Hz  | 9.33 | 1.7 dB  |
| Peaking | 6637 Hz  | 7.13 | -1.8 dB |
| Peaking | 13969 Hz | 2.22 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)