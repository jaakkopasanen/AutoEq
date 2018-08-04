# Meelectronics Air-Fi Matrix2 AF62 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.3; 30 4.5; 32 3.6; 35 2.4; 37 1.7; 40 0.9; 42 0.5; 45 -0.1; 49 -0.6; 52 -0.9; 56 -1.2; 59 -1.3; 64 -1.4; 68 -1.4; 73 -1.3; 78 -1.1; 83 -1.0; 89 -1.0; 95 -1.1; 102 -1.2; 109 -1.1; 117 -1.2; 125 -1.5; 134 -1.8; 143 -1.8; 153 -2.0; 164 -1.9; 175 -1.7; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.5; 246 -1.2; 263 -1.8; 282 -1.7; 301 -1.8; 323 -1.8; 345 -1.8; 369 -1.7; 395 -1.8; 423 -1.6; 452 -1.6; 484 -1.8; 518 -2.0; 554 -2.0; 593 -1.9; 635 -1.8; 679 -1.8; 726 -1.7; 777 -1.1; 832 -0.2; 890 -0.2; 952 0.0; 1019 -0.0; 1090 -0.3; 1167 -0.2; 1248 -0.1; 1336 -0.3; 1429 -0.4; 1529 -0.4; 1636 -0.1; 1751 0.6; 1873 1.6; 2004 2.1; 2145 2.5; 2295 2.7; 2455 2.9; 2627 3.3; 2811 3.1; 3008 2.6; 3219 2.0; 3444 2.0; 3685 3.2; 3943 4.1; 4219 4.2; 4514 5.7; 4830 6.0; 5168 4.8; 5530 1.8; 5917 2.6; 6331 4.1; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.6; 9502 -0.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  1.33 | 7.9 dB  |
| Peaking | 130 Hz   |  0.13 | -1.9 dB |
| Peaking | 2420 Hz  |  2.11 | 2.9 dB  |
| Peaking | 4719 Hz  |  2.04 | 5.4 dB  |
| Peaking | 24000 Hz |  2.23 | 1.7 dB  |
| Peaking | 758 Hz   |  1.67 | -1.5 dB |
| Peaking | 875 Hz   |  2.67 | 2.1 dB  |
| Peaking | 5541 Hz  | 12.84 | -2.5 dB |
| Peaking | 6579 Hz  |  7.25 | 3.3 dB  |
| Peaking | 8690 Hz  |  2.61 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth.png)