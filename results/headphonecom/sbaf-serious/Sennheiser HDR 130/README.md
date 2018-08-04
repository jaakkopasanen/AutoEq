# Sennheiser HDR 130

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.6; 56 4.3; 59 3.3; 64 2.1; 68 1.3; 73 0.1; 78 -0.8; 83 -1.6; 89 -2.4; 95 -2.9; 102 -3.7; 109 -4.0; 117 -4.2; 125 -4.4; 134 -4.9; 143 -5.2; 153 -5.4; 164 -5.4; 175 -5.5; 188 -5.6; 201 -5.3; 215 -5.6; 230 -6.1; 246 -5.7; 263 -5.7; 282 -5.7; 301 -5.6; 323 -5.2; 345 -5.0; 369 -5.0; 395 -4.5; 423 -4.6; 452 -4.5; 484 -4.5; 518 -4.4; 554 -3.7; 593 -2.4; 635 -2.0; 679 -1.5; 726 -1.1; 777 -1.4; 832 -1.6; 890 -1.2; 952 -0.6; 1019 0.1; 1090 0.3; 1167 -0.7; 1248 -2.2; 1336 -3.3; 1429 -4.5; 1529 -5.5; 1636 -5.5; 1751 -5.6; 1873 -5.7; 2004 -4.5; 2145 -3.3; 2295 -1.4; 2455 -0.4; 2627 -3.3; 2811 -5.7; 3008 -7.1; 3219 -6.5; 3444 -6.6; 3685 -7.2; 3943 -4.0; 4219 -9.5; 4514 -10.8; 4830 -8.0; 5168 -5.7; 5530 -6.0; 5917 -6.3; 6331 -5.7; 6775 1.1; 7249 1.3; 7756 0.3; 8299 -3.6; 8880 -8.3; 9502 -9.3; 10167 -6.6; 10879 -1.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HDR 130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.53 | 10.7 dB  |
| Peaking | 132 Hz   | 0.34 | -8.4 dB  |
| Peaking | 1661 Hz  | 3.76 | -4.6 dB  |
| Peaking | 4403 Hz  | 1.05 | -8.1 dB  |
| Peaking | 24996 Hz | 2.35 | -5.6 dB  |
| Peaking | 1049 Hz  | 5.7  | 2.4 dB   |
| Peaking | 11456 Hz | 2.29 | 3.6 dB   |
| Peaking | 6179 Hz  | 7.71 | -4.9 dB  |
| Peaking | 7121 Hz  | 3.18 | 8.5 dB   |
| Peaking | 9411 Hz  | 2.88 | -11.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HDR%20130/Sennheiser%20HDR%20130.png)