# HiFiMAN HE-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.6; 32 5.1; 35 4.2; 37 3.8; 40 3.6; 42 3.5; 45 3.2; 49 2.6; 52 2.2; 56 1.9; 59 1.7; 64 1.7; 68 1.8; 73 1.9; 78 1.9; 83 1.8; 89 1.6; 95 1.4; 102 1.2; 109 1.1; 117 0.6; 125 0.1; 134 -0.1; 143 -0.4; 153 -0.6; 164 -0.7; 175 -0.8; 188 -1.0; 201 -1.0; 215 -0.9; 230 -0.9; 246 -0.8; 263 -0.8; 282 -0.7; 301 -0.6; 323 -0.6; 345 -0.6; 369 -0.8; 395 -1.2; 423 -1.3; 452 -0.7; 484 -0.7; 518 -0.8; 554 -0.6; 593 -0.3; 635 -0.2; 679 -0.2; 726 0.3; 777 0.6; 832 0.3; 890 -0.1; 952 0.1; 1019 0.0; 1090 0.4; 1167 1.4; 1248 1.5; 1336 1.8; 1429 1.9; 1529 1.5; 1636 1.9; 1751 3.0; 1873 3.6; 2004 4.2; 2145 3.8; 2295 2.1; 2455 2.8; 2627 2.9; 2811 1.8; 3008 0.7; 3219 0.1; 3444 -0.2; 3685 -0.1; 3943 -0.7; 4219 -3.1; 4514 -3.0; 4830 -1.3; 5168 0.2; 5530 -0.8; 5917 -2.3; 6331 -3.6; 6775 -4.9; 7249 -5.1; 7756 -5.6; 8299 -6.9; 8880 -8.4; 9502 -8.7; 10167 -6.8; 10879 -4.1; 11640 -2.3; 12455 -1.8; 13327 -1.7; 14260 -1.1; 15258 -1.0; 16326 -2.6; 17469 -5.3; 18692 -6.9; 20000 -5.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.72 | 6.1 dB  |
| Peaking | 2043 Hz  | 1.75 | 4.0 dB  |
| Peaking | 4329 Hz  | 8.02 | -3.2 dB |
| Peaking | 8906 Hz  | 1.92 | -8.6 dB |
| Peaking | 29161 Hz | 1.65 | -7.5 dB |
| Peaking | 91 Hz    | 1.45 | 1.9 dB  |
| Peaking | 167 Hz   | 0.44 | -1.4 dB |
| Peaking | 5205 Hz  | 9.89 | 1.7 dB  |
| Peaking | 6629 Hz  | 7.34 | -1.8 dB |
| Peaking | 14385 Hz | 2.21 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)