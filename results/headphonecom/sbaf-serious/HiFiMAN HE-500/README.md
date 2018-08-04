# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.4; 23 -1.6; 25 -1.9; 26 -2.1; 28 -2.3; 30 -2.5; 32 -2.7; 35 -2.8; 37 -2.8; 40 -2.8; 42 -2.8; 45 -2.7; 49 -2.6; 52 -2.5; 56 -2.7; 59 -2.9; 64 -2.9; 68 -2.8; 73 -2.7; 78 -2.5; 83 -2.3; 89 -2.4; 95 -2.2; 102 -2.0; 109 -1.9; 117 -1.6; 125 -1.5; 134 -1.5; 143 -1.4; 153 -1.2; 164 -1.3; 175 -1.1; 188 -1.2; 201 -1.0; 215 -1.0; 230 -1.1; 246 -1.2; 263 -1.3; 282 -1.2; 301 -1.1; 323 -1.0; 345 -1.0; 369 -1.1; 395 -0.8; 423 -0.7; 452 -1.0; 484 -1.2; 518 -0.9; 554 -0.9; 593 -0.9; 635 -0.6; 679 -0.8; 726 0.1; 777 0.7; 832 0.3; 890 -0.3; 952 0.1; 1019 -0.2; 1090 -0.3; 1167 0.2; 1248 0.3; 1336 1.0; 1429 1.0; 1529 0.6; 1636 0.8; 1751 1.7; 1873 2.5; 2004 2.8; 2145 1.7; 2295 0.9; 2455 2.6; 2627 2.6; 2811 1.7; 3008 0.9; 3219 0.5; 3444 0.1; 3685 0.7; 3943 0.4; 4219 -1.2; 4514 -1.8; 4830 -1.2; 5168 1.3; 5530 2.6; 5917 1.9; 6331 0.6; 6775 -0.2; 7249 -0.0; 7756 -0.6; 8299 -3.0; 8880 -5.6; 9502 -5.5; 10167 -1.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.1; 18692 -3.7; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.4dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.2  | -2.4 dB |
| Peaking | 2211 Hz | 1.47 | 2.3 dB  |
| Peaking | 4675 Hz | 4.46 | -3.4 dB |
| Peaking | 5486 Hz | 4.12 | 3.6 dB  |
| Peaking | 9167 Hz | 5.23 | -6.7 dB |
| Peaking | 16 Hz   | 1.28 | 1.8 dB  |
| Peaking | 63 Hz   | 0.2  | -0.7 dB |
| Peaking | 144 Hz  | 1.04 | 1.2 dB  |
| Peaking | 517 Hz  | 3.18 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)