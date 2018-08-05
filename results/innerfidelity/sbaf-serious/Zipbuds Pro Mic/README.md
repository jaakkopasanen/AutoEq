# Zipbuds Pro Mic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 10 -84; 20 -6.6; 22 -7.0; 23 -7.2; 25 -7.6; 26 -7.7; 28 -7.9; 30 -8.1; 32 -8.2; 35 -8.2; 37 -8.3; 40 -8.3; 42 -8.4; 45 -8.5; 49 -8.5; 52 -8.5; 56 -8.4; 59 -8.4; 64 -8.4; 68 -8.3; 73 -8.2; 78 -8.3; 83 -8.3; 89 -8.5; 95 -8.8; 102 -9.1; 109 -9.3; 117 -9.6; 125 -9.9; 134 -10.1; 143 -10.2; 153 -10.1; 164 -10.0; 175 -9.7; 188 -9.3; 201 -9.1; 215 -8.7; 230 -8.3; 246 -7.9; 263 -7.5; 282 -7.0; 301 -6.6; 323 -6.1; 345 -5.6; 369 -5.2; 395 -4.7; 423 -4.0; 452 -3.6; 484 -3.3; 518 -2.8; 554 -2.3; 593 -1.6; 635 -1.2; 679 -0.9; 726 -0.5; 777 -0.0; 832 0.1; 890 0.2; 952 0.2; 1019 0.0; 1090 0.2; 1167 0.4; 1248 0.1; 1336 -0.3; 1429 -0.9; 1529 -1.6; 1636 -2.2; 1751 -2.8; 1873 -3.1; 2004 -3.3; 2145 -3.4; 2295 -3.6; 2455 -3.5; 2627 -3.9; 2811 -3.6; 3008 -3.2; 3219 -2.6; 3444 -1.6; 3685 -1.6; 3943 -2.9; 4219 -5.7; 4514 -8.9; 4830 -12.3; 5168 -12.1; 5530 -8.3; 5917 -4.3; 6331 -2.4; 6775 -2.4; 7249 -4.4; 7756 -8.0; 8299 -10.3; 8880 -8.7; 9502 -4.5; 10167 -1.4; 10879 -1.4; 11640 -2.0; 12455 -1.5; 13327 -0.7; 14260 -0.4; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.0dB` and instead set Global volume in the UI for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zipbuds Pro Mic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 6 Hz     | 1.65 | -6.0 dB  |
| Peaking | 33 Hz    | 0.36 | -7.3 dB  |
| Peaking | 177 Hz   | 0.62 | -8.2 dB  |
| Peaking | 4918 Hz  | 2.95 | -11.3 dB |
| Peaking | 39417 Hz | 3.32 | -8.1 dB  |
| Peaking | 1109 Hz  | 0.86 | 6.3 dB   |
| Peaking | 1652 Hz  | 0.47 | -5.9 dB  |
| Peaking | 3714 Hz  | 3.5  | 4.3 dB   |
| Peaking | 6479 Hz  | 4.33 | 3.5 dB   |
| Peaking | 7947 Hz  | 9.03 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zipbuds%20Pro%20Mic/Zipbuds%20Pro%20Mic.png)