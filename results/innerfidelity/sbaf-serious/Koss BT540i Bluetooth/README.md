# Koss BT540i Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -6.0; 22 -6.5; 23 -6.8; 25 -7.2; 26 -7.3; 28 -7.6; 30 -7.9; 32 -8.1; 35 -8.4; 37 -8.5; 40 -8.7; 42 -8.8; 45 -8.9; 49 -8.9; 52 -8.9; 56 -9.0; 59 -9.0; 64 -9.0; 68 -9.0; 73 -9.0; 78 -9.0; 83 -9.1; 89 -9.1; 95 -9.0; 102 -8.8; 109 -8.6; 117 -8.5; 125 -8.3; 134 -8.3; 143 -8.3; 153 -8.3; 164 -8.2; 175 -7.3; 188 -7.2; 201 -7.5; 215 -7.1; 230 -6.7; 246 -6.1; 263 -5.7; 282 -4.8; 301 -3.8; 323 -3.3; 345 -3.1; 369 -2.1; 395 -1.2; 423 -0.3; 452 0.2; 484 0.7; 518 1.1; 554 1.6; 593 1.8; 635 1.6; 679 1.1; 726 0.7; 777 0.5; 832 0.2; 890 -0.0; 952 -0.0; 1019 0.1; 1090 0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.1; 1529 -1.3; 1636 -1.8; 1751 -2.2; 1873 -2.4; 2004 -2.6; 2145 -2.9; 2295 -3.5; 2455 -3.8; 2627 -4.3; 2811 -5.0; 3008 -5.1; 3219 -4.8; 3444 -3.6; 3685 -2.2; 3943 -0.4; 4219 0.9; 4514 3.0; 4830 5.8; 5168 4.9; 5530 2.0; 5917 3.4; 6331 4.2; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.0; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 -0.4; 13327 -1.1; 14260 -0.2; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099566618642662dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 36 Hz   |  0.42 | -6.8 dB |
| Peaking | 185 Hz  |  0.37 | -7.2 dB |
| Peaking | 521 Hz  |  0.91 | 5.5 dB  |
| Peaking | 3273 Hz |  1.06 | -7.4 dB |
| Peaking | 4850 Hz |  1.7  | 8.9 dB  |
| Peaking | 850 Hz  |  3.83 | -0.4 dB |
| Peaking | 1102 Hz |  4.05 | 0.5 dB  |
| Peaking | 5557 Hz | 13.65 | -2.8 dB |
| Peaking | 6542 Hz |  4.78 | 2.7 dB  |
| Peaking | 8733 Hz |  2.14 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Bluetooth/Koss%20BT540i%20Bluetooth.png)