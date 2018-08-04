# Sennheiser PXC150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.8; 45 5.0; 49 3.5; 52 2.4; 56 1.2; 59 0.3; 64 -0.8; 68 -1.6; 73 -2.3; 78 -2.6; 83 -2.7; 89 -1.9; 95 -1.5; 102 -1.7; 109 -1.9; 117 -2.3; 125 -2.3; 134 -2.2; 143 -2.0; 153 -1.7; 164 -1.1; 175 -0.6; 188 -0.5; 201 -0.6; 215 -0.5; 230 -0.5; 246 -0.4; 263 -0.0; 282 0.2; 301 0.3; 323 0.6; 345 0.8; 369 0.9; 395 1.1; 423 1.3; 452 1.6; 484 1.8; 518 2.1; 554 2.3; 593 2.2; 635 2.2; 679 2.1; 726 2.0; 777 1.7; 832 1.3; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.0; 1248 -1.2; 1336 -0.8; 1429 -0.9; 1529 -1.2; 1636 -1.6; 1751 -2.1; 1873 -2.4; 2004 -2.4; 2145 -1.1; 2295 0.1; 2455 1.4; 2627 2.7; 2811 3.6; 3008 4.5; 3219 5.2; 3444 5.9; 3685 6.0; 3943 6.0; 4219 4.9; 4514 4.4; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.6; 8880 -3.9; 9502 -4.1; 10167 -2.5; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 49 Hz   | 0.16 | 10.8 dB  |
| Peaking | 98 Hz   | 0.48 | -12.7 dB |
| Peaking | 3519 Hz | 3.07 | 5.5 dB   |
| Peaking | 5710 Hz | 2.05 | 6.3 dB   |
| Peaking | 9161 Hz | 3.62 | -5.7 dB  |
| Peaking | 2 Hz    | 1.9  | -0.1 dB  |
| Peaking | 71 Hz   | 5.82 | -1.4 dB  |
| Peaking | 650 Hz  | 1.89 | 1.8 dB   |
| Peaking | 1895 Hz | 4.49 | -3.3 dB  |
| Peaking | 1223 Hz | 2.51 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PXC150/Sennheiser%20PXC150.png)