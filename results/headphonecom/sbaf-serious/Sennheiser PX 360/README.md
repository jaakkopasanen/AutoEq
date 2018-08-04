# Sennheiser PX 360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.6; 45 5.2; 49 4.7; 52 4.4; 56 4.1; 59 3.8; 64 3.4; 68 3.2; 73 2.9; 78 2.7; 83 2.6; 89 2.4; 95 2.2; 102 2.3; 109 2.7; 117 3.8; 125 5.0; 134 4.6; 143 3.8; 153 3.8; 164 4.5; 175 6.0; 188 5.7; 201 5.0; 215 4.3; 230 3.9; 246 3.9; 263 3.3; 282 1.7; 301 0.3; 323 -0.3; 345 -0.5; 369 -0.6; 395 -1.2; 423 -1.6; 452 -1.4; 484 -1.1; 518 -0.6; 554 0.0; 593 0.6; 635 0.6; 679 0.5; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.6; 1167 -1.5; 1248 -2.6; 1336 -4.2; 1429 -5.9; 1529 -7.7; 1636 -8.9; 1751 -9.8; 1873 -9.7; 2004 -8.9; 2145 -7.4; 2295 -5.4; 2455 -3.0; 2627 -1.2; 2811 -0.1; 3008 1.6; 3219 3.1; 3444 4.8; 3685 6.0; 3943 6.0; 4219 4.0; 4514 2.4; 4830 1.5; 5168 2.7; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.2; 10167 -2.7; 10879 -3.2; 11640 -1.8; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.5  | 6.2 dB   |
| Peaking | 180 Hz   | 1.7  | 5.2 dB   |
| Peaking | 1827 Hz  | 2.18 | -11.1 dB |
| Peaking | 3662 Hz  | 2.95 | 7.2 dB   |
| Peaking | 6045 Hz  | 4.64 | 6.3 dB   |
| Peaking | 254 Hz   | 6.26 | 2.0 dB   |
| Peaking | 416 Hz   | 1.48 | -2.7 dB  |
| Peaking | 784 Hz   | 0.92 | 2.0 dB   |
| Peaking | 1464 Hz  | 4.64 | -2.0 dB  |
| Peaking | 10635 Hz | 4.38 | -3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)