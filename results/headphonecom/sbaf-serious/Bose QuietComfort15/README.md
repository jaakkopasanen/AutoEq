# Bose QuietComfort15

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -5.6; 22 -8.1; 23 -9.0; 25 -10.3; 26 -10.6; 28 -10.7; 30 -10.3; 32 -9.6; 35 -8.4; 37 -7.8; 40 -7.3; 42 -7.0; 45 -6.7; 49 -6.3; 52 -6.1; 56 -5.8; 59 -5.6; 64 -5.5; 68 -5.5; 73 -5.5; 78 -5.5; 83 -5.4; 89 -5.4; 95 -5.5; 102 -5.5; 109 -5.5; 117 -5.6; 125 -5.7; 134 -5.8; 143 -5.7; 153 -5.6; 164 -5.3; 175 -5.2; 188 -5.1; 201 -4.9; 215 -4.7; 230 -4.5; 246 -4.5; 263 -4.4; 282 -4.1; 301 -3.9; 323 -3.6; 345 -3.2; 369 -2.9; 395 -2.6; 423 -2.3; 452 -2.0; 484 -1.8; 518 -1.7; 554 -1.2; 593 -0.8; 635 -0.2; 679 -0.3; 726 -0.0; 777 0.5; 832 0.8; 890 0.7; 952 0.4; 1019 -0.0; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -1.9; 1429 -2.0; 1529 -2.1; 1636 -3.4; 1751 -5.0; 1873 -6.6; 2004 -8.3; 2145 -9.6; 2295 -9.7; 2455 -9.3; 2627 -8.0; 2811 -6.1; 3008 -3.7; 3219 -2.4; 3444 -3.1; 3685 -3.5; 3943 -6.6; 4219 -9.6; 4514 -9.6; 4830 -6.5; 5168 -4.1; 5530 -3.7; 5917 -7.5; 6331 -3.8; 6775 -2.2; 7249 -1.5; 7756 0.3; 8299 -0.3; 8880 -3.0; 9502 -5.8; 10167 -6.6; 10879 -5.1; 11640 -2.9; 12455 -1.4; 13327 -0.9; 14260 -1.2; 15258 -1.6; 16326 -2.2; 17469 -3.7; 18692 -5.9; 20000 -8.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 27 Hz    |  0.94 | -9.6 dB  |
| Peaking | 146 Hz   |  0.52 | -5.3 dB  |
| Peaking | 2241 Hz  |  2.54 | -10.1 dB |
| Peaking | 4464 Hz  |  3.17 | -8.8 dB  |
| Peaking | 37618 Hz |  3.06 | -6.4 dB  |
| Peaking | 844 Hz   |  3.24 | 1.9 dB   |
| Peaking | 2726 Hz  |  5.94 | -2.0 dB  |
| Peaking | 3212 Hz  |  4.23 | 2.1 dB   |
| Peaking | 5972 Hz  | 12.26 | -5.5 dB  |
| Peaking | 7936 Hz  |  9.09 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort15/Bose%20QuietComfort15.png)