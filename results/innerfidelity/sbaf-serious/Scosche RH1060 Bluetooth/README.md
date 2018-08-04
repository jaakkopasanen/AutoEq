# Scosche RH1060 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.5; 23 -2.9; 25 -3.5; 26 -3.8; 28 -4.3; 30 -4.7; 32 -5.0; 35 -5.4; 37 -5.7; 40 -5.9; 42 -6.1; 45 -6.3; 49 -6.4; 52 -6.5; 56 -6.7; 59 -6.7; 64 -6.8; 68 -6.9; 73 -6.9; 78 -7.0; 83 -7.0; 89 -7.2; 95 -7.3; 102 -7.4; 109 -7.6; 117 -7.7; 125 -7.8; 134 -7.8; 143 -7.9; 153 -8.2; 164 -7.8; 175 -6.9; 188 -6.8; 201 -6.7; 215 -6.2; 230 -5.7; 246 -5.6; 263 -5.0; 282 -3.7; 301 -2.6; 323 -2.0; 345 -0.8; 369 0.6; 395 1.8; 423 3.3; 452 3.8; 484 4.1; 518 4.2; 554 4.6; 593 4.6; 635 3.9; 679 2.9; 726 2.1; 777 1.6; 832 1.1; 890 0.7; 952 0.2; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.3; 1336 -0.1; 1429 -0.3; 1529 -0.7; 1636 -1.3; 1751 -1.8; 1873 -1.9; 2004 -1.7; 2145 -1.5; 2295 -1.6; 2455 -1.7; 2627 -1.8; 2811 -2.0; 3008 -2.1; 3219 -2.6; 3444 -2.2; 3685 -1.9; 3943 -1.4; 4219 -0.8; 4514 -1.3; 4830 -2.7; 5168 -1.8; 5530 1.3; 5917 3.1; 6331 4.2; 6775 3.9; 7249 1.3; 7756 -0.7; 8299 -2.0; 8880 -1.2; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Scosche RH1060 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 41 Hz   |  0.75 | -3.7 dB |
| Peaking | 172 Hz  |  0.4  | -8.3 dB |
| Peaking | 493 Hz  |  1.08 | 9.0 dB  |
| Peaking | 3702 Hz |  0.48 | -2.4 dB |
| Peaking | 6395 Hz |  4.33 | 6.6 dB  |
| Peaking | 1297 Hz |  2.99 | 2.0 dB  |
| Peaking | 1306 Hz |  1.54 | -1.4 dB |
| Peaking | 4213 Hz | 12.46 | 1.2 dB  |
| Peaking | 8304 Hz |  6.36 | -2.4 dB |
| Peaking | 9789 Hz |  1.48 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Scosche%20RH1060%20Bluetooth/Scosche%20RH1060%20Bluetooth.png)