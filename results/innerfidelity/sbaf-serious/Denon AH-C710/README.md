# Denon AH-C710

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 10 -84; 20 -10.8; 22 -10.8; 23 -10.8; 25 -10.9; 26 -10.9; 28 -10.8; 30 -10.8; 32 -10.8; 35 -10.8; 37 -10.8; 40 -10.8; 42 -10.8; 45 -10.7; 49 -10.7; 52 -10.7; 56 -10.6; 59 -10.6; 64 -10.6; 68 -10.6; 73 -10.6; 78 -10.6; 83 -10.7; 89 -10.7; 95 -10.7; 102 -10.6; 109 -10.4; 117 -10.2; 125 -10.1; 134 -10.0; 143 -9.8; 153 -9.5; 164 -9.3; 175 -8.9; 188 -8.6; 201 -8.3; 215 -7.8; 230 -7.4; 246 -7.0; 263 -6.6; 282 -6.1; 301 -5.7; 323 -5.2; 345 -4.7; 369 -4.2; 395 -3.8; 423 -3.2; 452 -2.7; 484 -2.4; 518 -2.0; 554 -1.5; 593 -1.0; 635 -0.6; 679 -0.4; 726 -0.1; 777 0.2; 832 0.3; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.0; 1248 0.2; 1336 -0.4; 1429 -1.0; 1529 -1.4; 1636 -1.9; 1751 -2.2; 1873 -2.3; 2004 -2.4; 2145 -2.9; 2295 -3.5; 2455 -4.2; 2627 -5.0; 2811 -5.4; 3008 -4.6; 3219 -3.2; 3444 -1.6; 3685 -1.3; 3943 -1.9; 4219 -3.8; 4514 -5.7; 4830 -7.7; 5168 -10.1; 5530 -11.8; 5917 -8.4; 6331 -4.8; 6775 -2.5; 7249 -1.6; 7756 -2.9; 8299 -5.9; 8880 -7.8; 9502 -5.8; 10167 -0.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.3808763661371447dB` and instead set Global volume in the UI for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.11 | -11.0 dB |
| Peaking | 643 Hz   | 0.78 | 2.9 dB   |
| Peaking | 2589 Hz  | 2.1  | -4.7 dB  |
| Peaking | 5405 Hz  | 3.89 | -11.8 dB |
| Peaking | 8836 Hz  | 5.7  | -7.6 dB  |
| Peaking | 1669 Hz  | 7.07 | -1.0 dB  |
| Peaking | 3731 Hz  | 4.64 | 3.5 dB   |
| Peaking | 4021 Hz  | 2.23 | -2.0 dB  |
| Peaking | 7093 Hz  | 8.36 | 1.6 dB   |
| Peaking | 10817 Hz | 7.17 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)