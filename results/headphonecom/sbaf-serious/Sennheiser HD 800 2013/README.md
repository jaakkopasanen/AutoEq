# Sennheiser HD 800 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 10 -84; 20 2.3; 22 2.0; 23 1.8; 25 1.5; 26 1.3; 28 1.1; 30 0.9; 32 0.7; 35 0.5; 37 0.4; 40 0.3; 42 0.2; 45 0.1; 49 0.5; 52 0.8; 56 0.5; 59 0.1; 64 0.3; 68 0.5; 73 -0.3; 78 -1.0; 83 -1.3; 89 -1.6; 95 -2.0; 102 -2.4; 109 -2.8; 117 -3.1; 125 -3.5; 134 -3.8; 143 -4.0; 153 -4.2; 164 -4.2; 175 -4.3; 188 -4.4; 201 -4.4; 215 -4.3; 230 -4.3; 246 -4.2; 263 -4.2; 282 -4.1; 301 -4.0; 323 -3.7; 345 -3.5; 369 -3.4; 395 -3.3; 423 -3.0; 452 -2.9; 484 -2.9; 518 -2.6; 554 -2.4; 593 -2.1; 635 -1.8; 679 -1.8; 726 -1.5; 777 -1.1; 832 -1.1; 890 -0.8; 952 -0.1; 1019 0.1; 1090 0.6; 1167 1.3; 1248 1.2; 1336 1.1; 1429 0.8; 1529 0.6; 1636 1.0; 1751 1.1; 1873 1.1; 2004 1.3; 2145 0.8; 2295 0.4; 2455 1.6; 2627 2.0; 2811 1.0; 3008 0.0; 3219 0.1; 3444 0.7; 3685 -0.7; 3943 -2.6; 4219 -3.3; 4514 -3.2; 4830 -3.3; 5168 -4.0; 5530 -4.9; 5917 -8.0; 6331 -9.8; 6775 -5.6; 7249 -4.1; 7756 -4.5; 8299 -6.2; 8880 -8.3; 9502 -9.2; 10167 -6.5; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -2.9; 15258 -3.9; 16326 -3.7; 17469 -4.3; 18692 -5.2; 20000 -5.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.9dB` and instead set Global volume in the UI for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.49 | 3.6 dB  |
| Peaking | 164 Hz   | 0.33 | -5.6 dB |
| Peaking | 2563 Hz  | 0.52 | 2.9 dB  |
| Peaking | 6633 Hz  | 0.88 | -8.1 dB |
| Peaking | 28868 Hz | 1.16 | -5.7 dB |
| Peaking | 6233 Hz  | 9.54 | -5.5 dB |
| Peaking | 7288 Hz  | 2.94 | 4.1 dB  |
| Peaking | 9566 Hz  | 3.02 | -9.2 dB |
| Peaking | 11255 Hz | 1.77 | 6.2 dB  |
| Peaking | 15114 Hz | 3.18 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%202013/Sennheiser%20HD%20800%202013.png)