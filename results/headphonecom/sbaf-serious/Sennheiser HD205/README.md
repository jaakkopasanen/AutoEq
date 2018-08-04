# Sennheiser HD205

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.6; 22 2.1; 23 1.9; 25 1.6; 26 1.4; 28 1.2; 30 0.9; 32 0.7; 35 0.3; 37 0.0; 40 -0.2; 42 -0.3; 45 -0.4; 49 -0.7; 52 -1.1; 56 -1.5; 59 -1.6; 64 -1.5; 68 -1.3; 73 -1.3; 78 -1.7; 83 -2.0; 89 -2.1; 95 -2.3; 102 -2.3; 109 -2.1; 117 -2.0; 125 -1.9; 134 -1.6; 143 -0.7; 153 0.1; 164 -0.2; 175 -0.5; 188 -0.4; 201 -0.1; 215 0.6; 230 0.8; 246 0.6; 263 0.5; 282 0.8; 301 1.2; 323 1.6; 345 2.2; 369 3.0; 395 3.8; 423 4.3; 452 3.9; 484 2.5; 518 1.2; 554 0.5; 593 0.8; 635 1.8; 679 3.5; 726 4.4; 777 3.9; 832 2.6; 890 1.3; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.0; 1248 -1.2; 1336 -1.6; 1429 -1.9; 1529 -2.2; 1636 -2.3; 1751 -2.2; 1873 -1.7; 2004 -1.3; 2145 -0.6; 2295 0.2; 2455 1.3; 2627 2.5; 2811 3.3; 3008 3.7; 3219 4.0; 3444 5.1; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 2.3; 5168 0.0; 5530 2.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.92 | 2.3 dB  |
| Peaking | 413 Hz   | 3.52 | 4.5 dB  |
| Peaking | 738 Hz   | 5.59 | 4.5 dB  |
| Peaking | 4015 Hz  | 1.85 | 6.3 dB  |
| Peaking | 24000 Hz | 2.38 | 3.0 dB  |
| Peaking | 93 Hz    | 1.47 | -2.4 dB |
| Peaking | 1672 Hz  | 1.81 | -3.1 dB |
| Peaking | 2811 Hz  | 3.76 | 1.7 dB  |
| Peaking | 5152 Hz  | 8.86 | -4.6 dB |
| Peaking | 6136 Hz  | 5.23 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD205/Sennheiser%20HD205.png)