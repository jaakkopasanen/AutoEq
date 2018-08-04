# Sennheiser HD238

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 10 -84; 20 0.6; 22 -0.2; 23 -0.5; 25 -1.2; 26 -1.5; 28 -2.1; 30 -2.5; 32 -2.9; 35 -3.4; 37 -3.7; 40 -4.0; 42 -4.2; 45 -4.4; 49 -4.7; 52 -5.0; 56 -5.3; 59 -5.4; 64 -5.3; 68 -5.3; 73 -5.6; 78 -5.7; 83 -5.8; 89 -5.9; 95 -5.8; 102 -5.9; 109 -5.7; 117 -5.6; 125 -5.6; 134 -5.4; 143 -5.2; 153 -5.0; 164 -5.0; 175 -4.9; 188 -4.7; 201 -4.7; 215 -4.4; 230 -4.2; 246 -4.0; 263 -3.9; 282 -3.6; 301 -3.4; 323 -3.0; 345 -2.7; 369 -2.4; 395 -2.2; 423 -1.8; 452 -1.7; 484 -1.6; 518 -1.5; 554 -1.0; 593 -0.7; 635 -0.4; 679 -0.4; 726 -0.3; 777 0.0; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.0; 1636 -1.4; 1751 -1.6; 1873 -1.2; 2004 -0.5; 2145 0.7; 2295 1.7; 2455 2.2; 2627 1.1; 2811 -0.6; 3008 -2.1; 3219 -3.6; 3444 -2.2; 3685 0.9; 3943 1.5; 4219 -2.4; 4514 -4.3; 4830 -2.2; 5168 0.0; 5530 -0.0; 5917 -1.5; 6331 -1.9; 6775 -1.2; 7249 -0.6; 7756 -0.3; 8299 -1.4; 8880 -2.8; 9502 -2.0; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.7; 15258 -2.4; 16326 -1.7; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.8dB` and instead set Global volume in the UI for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 82 Hz    | 0.49 | -5.7 dB |
| Peaking | 243 Hz   | 0.97 | -2.1 dB |
| Peaking | 1550 Hz  | 4.9  | -2.0 dB |
| Peaking | 4523 Hz  | 8.62 | -4.5 dB |
| Peaking | 39000 Hz | 4.21 | -2.5 dB |
| Peaking | 21 Hz    | 2.79 | 1.7 dB  |
| Peaking | 2335 Hz  | 1.45 | 3.7 dB  |
| Peaking | 3151 Hz  | 5.71 | -5.3 dB |
| Peaking | 1896 Hz  | 2.73 | -3.2 dB |
| Peaking | 32266 Hz | 4.62 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD238/Sennheiser%20HD238.png)