# Sennheiser HD218

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.8; 45 5.3; 49 4.5; 52 4.0; 56 3.6; 59 3.3; 64 2.5; 68 2.0; 73 1.5; 78 1.6; 83 1.6; 89 1.0; 95 0.3; 102 -0.4; 109 -0.8; 117 -1.3; 125 -1.8; 134 -2.2; 143 -2.6; 153 -2.9; 164 -2.7; 175 -2.2; 188 -2.7; 201 -3.4; 215 -3.8; 230 -4.1; 246 -4.5; 263 -4.9; 282 -5.1; 301 -5.2; 323 -5.6; 345 -6.0; 369 -6.4; 395 -5.5; 423 -4.1; 452 -3.5; 484 -3.0; 518 -2.9; 554 -2.2; 593 -0.8; 635 -0.1; 679 0.3; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.0; 1019 0.0; 1090 0.0; 1167 0.3; 1248 1.0; 1336 2.1; 1429 3.3; 1529 4.1; 1636 3.8; 1751 3.3; 1873 3.5; 2004 3.9; 2145 4.8; 2295 5.6; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.9; 4830 2.8; 5168 3.2; 5530 3.6; 5917 3.2; 6331 3.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.59 | 6.7 dB  |
| Peaking | 422 Hz  | 0.44 | -7.0 dB |
| Peaking | 652 Hz  | 1.53 | 5.0 dB  |
| Peaking | 2052 Hz | 0.68 | 4.7 dB  |
| Peaking | 3742 Hz | 1.12 | 3.8 dB  |
| Peaking | 1534 Hz | 4.74 | 2.9 dB  |
| Peaking | 2406 Hz | 3.47 | 1.2 dB  |
| Peaking | 1713 Hz | 1.76 | -1.9 dB |
| Peaking | 6640 Hz | 4.62 | 3.6 dB  |
| Peaking | 7510 Hz | 1.72 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD218/Sennheiser%20HD218.png)