# Sennheiser HD202

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.4; 22 4.5; 23 4.0; 25 3.1; 26 2.7; 28 1.9; 30 1.2; 32 0.5; 35 -0.4; 37 -0.9; 40 -1.6; 42 -2.0; 45 -2.6; 49 -3.1; 52 -3.3; 56 -3.4; 59 -3.7; 64 -4.2; 68 -4.2; 73 -4.1; 78 -4.3; 83 -4.3; 89 -4.1; 95 -4.0; 102 -3.7; 109 -3.4; 117 -2.9; 125 -2.7; 134 -2.3; 143 -2.0; 153 -1.5; 164 -0.8; 175 -0.1; 188 1.2; 201 3.2; 215 4.7; 230 4.9; 246 4.5; 263 4.3; 282 4.2; 301 4.2; 323 4.0; 345 3.2; 369 2.9; 395 2.8; 423 2.9; 452 2.6; 484 2.1; 518 1.8; 554 1.6; 593 1.4; 635 1.1; 679 0.7; 726 0.5; 777 0.5; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.2; 1336 -0.0; 1429 -0.6; 1529 -0.6; 1636 -0.5; 1751 0.3; 1873 1.2; 2004 2.2; 2145 3.4; 2295 4.7; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.3; 4514 -0.4; 4830 2.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.66 | 8.1 dB   |
| Peaking | 160 Hz  | 0.22 | -11.0 dB |
| Peaking | 265 Hz  | 0.57 | 14.9 dB  |
| Peaking | 2987 Hz | 1.67 | 6.9 dB   |
| Peaking | 5856 Hz | 3.76 | 5.9 dB   |
| Peaking | 601 Hz  | 2.3  | 0.7 dB   |
| Peaking | 1585 Hz | 3.63 | -1.5 dB  |
| Peaking | 2334 Hz | 6.5  | 1.6 dB   |
| Peaking | 6676 Hz | 7.11 | 2.2 dB   |
| Peaking | 7551 Hz | 2.05 | -1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD202/Sennheiser%20HD202.png)