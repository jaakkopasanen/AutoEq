# Sennheiser Momentum Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.3; 22 4.1; 23 3.6; 25 2.9; 26 2.6; 28 2.4; 30 2.4; 32 2.6; 35 2.9; 37 3.2; 40 3.5; 42 3.6; 45 3.8; 49 4.1; 52 4.2; 56 4.4; 59 4.5; 64 4.6; 68 4.7; 73 4.7; 78 4.8; 83 4.8; 89 4.8; 95 4.8; 102 4.8; 109 4.9; 117 5.1; 125 5.0; 134 5.2; 143 5.3; 153 5.3; 164 5.4; 175 5.7; 188 5.9; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 5.4; 554 4.9; 593 4.3; 635 3.7; 679 2.9; 726 2.3; 777 2.0; 832 1.4; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.5; 1336 -2.4; 1429 -3.3; 1529 -4.3; 1636 -5.3; 1751 -5.4; 1873 -5.8; 2004 -5.6; 2145 -4.7; 2295 -3.3; 2455 -1.2; 2627 0.4; 2811 2.1; 3008 4.0; 3219 5.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 0.7; 5168 1.3; 5530 5.1; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 98 Hz   |  0.22 | 4.5 dB  |
| Peaking | 415 Hz  |  0.72 | 3.8 dB  |
| Peaking | 1889 Hz |  1.28 | -8.0 dB |
| Peaking | 3484 Hz |  1.67 | 8.4 dB  |
| Peaking | 6125 Hz |  5.32 | 5.3 dB  |
| Peaking | 36 Hz   |  2.66 | -0.6 dB |
| Peaking | 865 Hz  |  4.75 | -0.4 dB |
| Peaking | 4618 Hz |  5.57 | 3.5 dB  |
| Peaking | 4946 Hz | 12.23 | -6.7 dB |
| Peaking | 8344 Hz |  4.21 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Bluetooth/Sennheiser%20Momentum%20Wireless%20Bluetooth.png)