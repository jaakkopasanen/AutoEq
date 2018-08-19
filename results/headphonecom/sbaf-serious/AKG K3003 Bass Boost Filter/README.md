# AKG K3003 Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -1.4; 22 -2.0; 23 -2.3; 25 -2.7; 26 -2.9; 28 -3.3; 30 -3.7; 32 -4.0; 35 -4.4; 37 -4.6; 40 -5.0; 42 -5.2; 45 -5.5; 49 -5.8; 52 -6.1; 56 -6.4; 59 -6.7; 64 -7.0; 68 -7.2; 73 -7.6; 78 -7.9; 83 -8.1; 89 -8.4; 95 -8.5; 102 -8.7; 109 -8.9; 117 -8.9; 125 -9.1; 134 -9.2; 143 -9.3; 153 -9.4; 164 -9.3; 175 -9.3; 188 -9.2; 201 -9.0; 215 -8.8; 230 -8.6; 246 -8.4; 263 -8.1; 282 -7.7; 301 -7.3; 323 -6.9; 345 -6.3; 369 -5.9; 395 -5.4; 423 -4.8; 452 -4.5; 484 -4.0; 518 -3.4; 554 -2.9; 593 -2.3; 635 -1.7; 679 -1.3; 726 -0.8; 777 -0.5; 832 -0.2; 890 -0.1; 952 -0.1; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.7; 1429 -0.3; 1529 -0.0; 1636 -0.7; 1751 -1.3; 1873 -1.8; 2004 -2.0; 2145 -2.2; 2295 -2.1; 2455 -1.8; 2627 -0.8; 2811 0.7; 3008 2.5; 3219 4.3; 3444 5.5; 3685 5.6; 3943 4.2; 4219 1.8; 4514 -0.7; 4830 -2.9; 5168 -4.2; 5530 -2.7; 5917 0.8; 6331 3.0; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -3.4; 10167 -2.2; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.823726953073414dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 95 Hz    | 0.42 | -7.6 dB |
| Peaking | 248 Hz   | 0.85 | -4.5 dB |
| Peaking | 3688 Hz  | 2.52 | 12.6 dB |
| Peaking | 4831 Hz  | 0.88 | -8.7 dB |
| Peaking | 6560 Hz  | 3.15 | 8.8 dB  |
| Peaking | 908 Hz   | 2.21 | 1.3 dB  |
| Peaking | 2255 Hz  | 3.2  | -1.7 dB |
| Peaking | 3054 Hz  | 7.31 | 1.7 dB  |
| Peaking | 9749 Hz  | 7.04 | -3.9 dB |
| Peaking | 10599 Hz | 1.71 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)