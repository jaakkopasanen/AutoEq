# Meelectronics Air-Fi Matrix2 AF62 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.3; 30 4.5; 32 3.6; 35 2.3; 37 1.7; 40 0.8; 42 0.3; 45 -0.2; 49 -0.8; 52 -1.2; 56 -1.6; 59 -1.7; 64 -1.9; 68 -2.0; 73 -2.0; 78 -1.9; 83 -1.8; 89 -1.8; 95 -1.9; 102 -1.7; 109 -1.5; 117 -1.4; 125 -1.5; 134 -1.7; 143 -1.6; 153 -1.8; 164 -1.7; 175 -1.5; 188 -1.5; 201 -1.7; 215 -1.6; 230 -1.3; 246 -1.1; 263 -1.7; 282 -1.6; 301 -1.7; 323 -1.7; 345 -1.8; 369 -1.7; 395 -1.8; 423 -1.6; 452 -1.5; 484 -1.8; 518 -2.0; 554 -2.0; 593 -1.9; 635 -1.8; 679 -1.8; 726 -1.7; 777 -1.1; 832 -0.2; 890 -0.2; 952 0.0; 1019 -0.0; 1090 -0.3; 1167 -0.2; 1248 -0.1; 1336 -0.3; 1429 -0.4; 1529 -0.4; 1636 -0.1; 1751 0.6; 1873 1.6; 2004 2.1; 2145 2.5; 2295 2.7; 2455 2.9; 2627 3.3; 2811 3.1; 3008 2.6; 3219 2.0; 3444 2.0; 3685 3.2; 3943 4.1; 4219 4.2; 4514 5.7; 4830 6.0; 5168 4.8; 5530 1.8; 5917 2.6; 6331 4.1; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.6; 9502 -0.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.46 | 8.4 dB  |
| Peaking | 100 Hz   | 0.11 | -2.0 dB |
| Peaking | 2414 Hz  | 2.17 | 2.9 dB  |
| Peaking | 4713 Hz  | 2.04 | 5.5 dB  |
| Peaking | 24000 Hz | 2.22 | 1.7 dB  |
| Peaking | 13 Hz    | 2.2  | 2.2 dB  |
| Peaking | 60 Hz    | 2.72 | -0.8 dB |
| Peaking | 1553 Hz  | 7.42 | -0.6 dB |
| Peaking | 6639 Hz  | 6.51 | 4.5 dB  |
| Peaking | 7192 Hz  | 1.52 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth.png)