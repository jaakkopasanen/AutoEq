# Cyberdrive Forte Classic Bass

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 -12.1; 22 -12.1; 23 -12.2; 25 -12.2; 26 -12.2; 28 -12.2; 30 -12.3; 32 -12.3; 35 -12.2; 37 -12.2; 40 -12.2; 42 -12.2; 45 -12.2; 49 -12.2; 52 -12.2; 56 -12.2; 59 -12.2; 64 -12.3; 68 -12.3; 73 -12.3; 78 -12.4; 83 -12.4; 89 -12.4; 95 -12.5; 102 -12.4; 109 -12.2; 117 -12.1; 125 -12.0; 134 -11.8; 143 -11.5; 153 -11.3; 164 -11.1; 175 -10.7; 188 -10.4; 201 -10.1; 215 -9.6; 230 -9.1; 246 -8.8; 263 -8.4; 282 -7.8; 301 -7.3; 323 -6.8; 345 -6.2; 369 -5.7; 395 -5.1; 423 -4.5; 452 -4.0; 484 -3.7; 518 -3.1; 554 -2.5; 593 -1.8; 635 -1.5; 679 -1.2; 726 -1.0; 777 -0.1; 832 -0.2; 890 -0.3; 952 -0.2; 1019 -0.2; 1090 -0.3; 1167 -0.4; 1248 -0.4; 1336 -0.6; 1429 -0.7; 1529 -0.8; 1636 -0.7; 1751 -0.3; 1873 0.2; 2004 0.8; 2145 1.4; 2295 1.9; 2455 2.7; 2627 3.2; 2811 3.2; 3008 3.4; 3219 3.1; 3444 2.4; 3685 1.0; 3943 -1.0; 4219 -3.3; 4514 -4.8; 4830 -5.4; 5168 -5.7; 5530 -7.3; 5917 -10.5; 6331 -13.1; 6775 -10.4; 7249 -7.3; 7756 -4.9; 8299 -4.1; 8880 -4.5; 9502 -4.9; 10167 -4.4; 10879 -2.5; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.7; 16326 -3.4; 17469 -3.8; 18692 -2.5; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.5492938977546005dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Classic Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.13 | -12.9 dB |
| Peaking | 3473 Hz  | 0.08 | 2.9 dB   |
| Peaking | 6257 Hz  | 2.13 | -15.0 dB |
| Peaking | 9842 Hz  | 3.58 | -4.7 dB  |
| Peaking | 17387 Hz | 1.58 | -5.8 dB  |
| Peaking | 725 Hz   | 1.49 | 1.1 dB   |
| Peaking | 1652 Hz  | 1.26 | -3.0 dB  |
| Peaking | 3054 Hz  | 1.19 | 3.6 dB   |
| Peaking | 4383 Hz  | 4.04 | -4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Classic%20Bass/Cyberdrive%20Forte%20Classic%20Bass.png)