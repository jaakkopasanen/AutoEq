# HiFiMAN HE-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.6; 32 5.0; 35 4.1; 37 3.7; 40 3.5; 42 3.4; 45 3.0; 49 2.3; 52 2.0; 56 1.6; 59 1.3; 64 1.2; 68 1.2; 73 1.2; 78 1.2; 83 1.0; 89 0.8; 95 0.7; 102 0.7; 109 0.7; 117 0.4; 125 0.1; 134 -0.0; 143 -0.2; 153 -0.3; 164 -0.4; 175 -0.6; 188 -0.8; 201 -0.8; 215 -0.8; 230 -0.8; 246 -0.8; 263 -0.7; 282 -0.7; 301 -0.6; 323 -0.5; 345 -0.6; 369 -0.7; 395 -1.2; 423 -1.3; 452 -0.8; 484 -0.7; 518 -0.7; 554 -0.6; 593 -0.4; 635 -0.3; 679 -0.2; 726 0.3; 777 0.5; 832 0.3; 890 -0.1; 952 0.1; 1019 0.0; 1090 0.4; 1167 1.4; 1248 1.5; 1336 1.8; 1429 1.9; 1529 1.4; 1636 1.9; 1751 3.0; 1873 3.6; 2004 4.2; 2145 3.8; 2295 2.1; 2455 2.8; 2627 2.9; 2811 1.9; 3008 0.6; 3219 0.2; 3444 -0.2; 3685 -0.0; 3943 -0.9; 4219 -3.1; 4514 -2.8; 4830 -1.3; 5168 0.2; 5530 -0.8; 5917 -2.2; 6331 -3.6; 6775 -5.0; 7249 -5.2; 7756 -5.6; 8299 -6.7; 8880 -8.3; 9502 -8.8; 10167 -7.0; 10879 -3.9; 11640 -2.0; 12455 -2.0; 13327 -2.0; 14260 -1.1; 15258 -0.8; 16326 -2.5; 17469 -5.4; 18692 -7.0; 20000 -5.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.93 | 6.2 dB  |
| Peaking | 2044 Hz  | 1.73 | 4.0 dB  |
| Peaking | 4321 Hz  | 7.66 | -3.1 dB |
| Peaking | 8909 Hz  | 1.9  | -8.6 dB |
| Peaking | 19026 Hz | 1.7  | -7.6 dB |
| Peaking | 328 Hz   | 0.73 | -1.0 dB |
| Peaking | 1261 Hz  | 6.08 | 0.9 dB  |
| Peaking | 5247 Hz  | 9.33 | 1.7 dB  |
| Peaking | 6679 Hz  | 7.62 | -1.9 dB |
| Peaking | 11633 Hz | 8.01 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)