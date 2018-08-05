# Koss BT540i Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.0; 22 -6.5; 23 -6.8; 25 -7.1; 26 -7.3; 28 -7.6; 30 -7.8; 32 -8.1; 35 -8.3; 37 -8.4; 40 -8.6; 42 -8.6; 45 -8.7; 49 -8.7; 52 -8.7; 56 -8.6; 59 -8.6; 64 -8.5; 68 -8.4; 73 -8.3; 78 -8.3; 83 -8.3; 89 -8.3; 95 -8.3; 102 -8.2; 109 -8.2; 117 -8.3; 125 -8.3; 134 -8.4; 143 -8.5; 153 -8.5; 164 -8.4; 175 -7.5; 188 -7.4; 201 -7.7; 215 -7.2; 230 -6.9; 246 -6.2; 263 -5.7; 282 -4.9; 301 -3.8; 323 -3.3; 345 -3.2; 369 -2.1; 395 -1.2; 423 -0.4; 452 0.2; 484 0.7; 518 1.1; 554 1.6; 593 1.8; 635 1.5; 679 1.1; 726 0.7; 777 0.5; 832 0.2; 890 -0.0; 952 -0.0; 1019 0.1; 1090 0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.1; 1529 -1.3; 1636 -1.8; 1751 -2.2; 1873 -2.4; 2004 -2.6; 2145 -2.9; 2295 -3.5; 2455 -3.8; 2627 -4.3; 2811 -5.0; 3008 -5.1; 3219 -4.8; 3444 -3.6; 3685 -2.2; 3943 -0.4; 4219 0.9; 4514 3.0; 4830 5.8; 5168 4.9; 5530 2.0; 5917 3.4; 6331 4.2; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.0; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 -0.4; 13327 -1.1; 14260 -0.2; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.45 | -8.6 dB |
| Peaking | 140 Hz  |  1.28 | -5.0 dB |
| Peaking | 231 Hz  |  2.36 | -4.0 dB |
| Peaking | 3072 Hz |  1.4  | -6.6 dB |
| Peaking | 4938 Hz |  1.91 | 7.1 dB  |
| Peaking | 332 Hz  |  3.1  | -1.3 dB |
| Peaking | 565 Hz  |  1.89 | 2.6 dB  |
| Peaking | 6508 Hz |  3.2  | 3.1 dB  |
| Peaking | 5507 Hz | 12.49 | -3.2 dB |
| Peaking | 8156 Hz |  1.55 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Bluetooth/Koss%20BT540i%20Bluetooth.png)