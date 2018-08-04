# Sennheiser HD238

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 4.6; 22 3.8; 23 3.5; 25 2.8; 26 2.5; 28 1.9; 30 1.5; 32 1.1; 35 0.6; 37 0.3; 40 -0.0; 42 -0.2; 45 -0.4; 49 -0.7; 52 -1.0; 56 -1.4; 59 -1.5; 64 -1.4; 68 -1.5; 73 -1.8; 78 -2.1; 83 -2.3; 89 -2.7; 95 -3.0; 102 -3.5; 109 -3.7; 117 -4.0; 125 -4.4; 134 -4.6; 143 -4.6; 153 -4.6; 164 -4.8; 175 -4.8; 188 -4.6; 201 -4.6; 215 -4.4; 230 -4.1; 246 -4.0; 263 -3.9; 282 -3.6; 301 -3.3; 323 -3.0; 345 -2.7; 369 -2.4; 395 -2.2; 423 -1.8; 452 -1.7; 484 -1.6; 518 -1.5; 554 -1.0; 593 -0.7; 635 -0.4; 679 -0.4; 726 -0.3; 777 0.0; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.0; 1636 -1.4; 1751 -1.6; 1873 -1.2; 2004 -0.5; 2145 0.7; 2295 1.7; 2455 2.2; 2627 1.1; 2811 -0.6; 3008 -2.1; 3219 -3.6; 3444 -2.2; 3685 0.9; 3943 1.5; 4219 -2.4; 4514 -4.3; 4830 -2.2; 5168 0.0; 5530 -0.0; 5917 -1.5; 6331 -1.9; 6775 -1.2; 7249 -0.6; 7756 -0.3; 8299 -1.4; 8880 -2.8; 9502 -2.0; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.7; 15258 -2.4; 16326 -1.7; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.51 | 4.6 dB  |
| Peaking | 168 Hz   | 0.63 | -4.9 dB |
| Peaking | 1552 Hz  | 5.04 | -2.0 dB |
| Peaking | 4525 Hz  | 8.66 | -4.5 dB |
| Peaking | 39230 Hz | 4.54 | -2.6 dB |
| Peaking | 2433 Hz  | 5.88 | 3.0 dB  |
| Peaking | 3219 Hz  | 4.95 | -4.0 dB |
| Peaking | 3788 Hz  | 8.8  | 3.5 dB  |
| Peaking | 6264 Hz  | 8.88 | -1.7 dB |
| Peaking | 32547 Hz | 4.73 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD238/Sennheiser%20HD238.png)