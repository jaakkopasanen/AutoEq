# Sennheiser MX 560

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.7; 102 5.2; 109 4.9; 117 4.6; 125 4.2; 134 4.0; 143 3.8; 153 3.7; 164 3.6; 175 3.4; 188 3.2; 201 2.9; 215 2.9; 230 3.0; 246 3.0; 263 2.9; 282 2.7; 301 2.6; 323 2.5; 345 2.2; 369 1.9; 395 1.7; 423 1.6; 452 2.2; 484 2.7; 518 2.4; 554 2.2; 593 2.1; 635 1.8; 679 1.3; 726 1.2; 777 1.1; 832 0.8; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -1.0; 1336 -1.7; 1429 -2.6; 1529 -3.7; 1636 -4.8; 1751 -6.1; 1873 -7.4; 2004 -9.0; 2145 -10.7; 2295 -11.9; 2455 -12.5; 2627 -12.4; 2811 -11.3; 3008 -8.9; 3219 -6.2; 3444 -4.3; 3685 -3.1; 3943 -2.9; 4219 -4.3; 4514 -5.6; 4830 -6.1; 5168 -6.2; 5530 -6.6; 5917 -6.2; 6331 -5.5; 6775 -4.5; 7249 -3.3; 7756 -2.9; 8299 -4.5; 8880 -6.2; 9502 -6.2; 10167 -4.3; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.8; 15258 -2.3; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.23 | 6.3 dB   |
| Peaking | 581 Hz   | 0.85 | 1.8 dB   |
| Peaking | 2386 Hz  | 1.85 | -12.5 dB |
| Peaking | 6779 Hz  | 0.88 | -4.8 dB  |
| Peaking | 24000 Hz | 2.16 | -3.9 dB  |
| Peaking | 3801 Hz  | 3.72 | 4.7 dB   |
| Peaking | 4478 Hz  | 1.1  | -2.5 dB  |
| Peaking | 7556 Hz  | 3.27 | 4.3 dB   |
| Peaking | 9328 Hz  | 2.64 | -4.3 dB  |
| Peaking | 11491 Hz | 3.31 | 3.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)