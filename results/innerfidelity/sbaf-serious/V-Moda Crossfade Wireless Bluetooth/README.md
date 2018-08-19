# V-Moda Crossfade Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.0; 22 1.9; 23 1.4; 25 0.5; 26 0.0; 28 -0.8; 30 -1.5; 32 -2.0; 35 -2.7; 37 -3.0; 40 -3.4; 42 -3.7; 45 -3.9; 49 -4.2; 52 -4.4; 56 -4.5; 59 -4.5; 64 -4.3; 68 -4.0; 73 -4.2; 78 -5.0; 83 -5.6; 89 -6.0; 95 -6.0; 102 -5.4; 109 -5.5; 117 -5.9; 125 -6.2; 134 -6.3; 143 -6.3; 153 -6.2; 164 -5.6; 175 -5.4; 188 -5.2; 201 -4.7; 215 -3.9; 230 -3.0; 246 -2.1; 263 -1.1; 282 0.4; 301 1.8; 323 3.0; 345 4.1; 369 5.0; 395 5.5; 423 5.2; 452 5.4; 484 5.4; 518 5.3; 554 5.0; 593 4.9; 635 4.6; 679 4.0; 726 3.4; 777 2.8; 832 1.8; 890 1.1; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.0; 1336 -1.3; 1429 -1.5; 1529 -1.7; 1636 -1.7; 1751 -1.5; 1873 -1.0; 2004 -0.5; 2145 -0.5; 2295 -0.9; 2455 -1.0; 2627 -0.2; 2811 -0.3; 3008 -0.7; 3219 -1.6; 3444 -3.1; 3685 -3.8; 3943 -1.8; 4219 -0.4; 4514 2.6; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -2.7; 9502 -4.5; 10167 -4.5; 10879 -2.5; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099566618642664dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 2.05 | -2.1 dB |
| Peaking | 148 Hz  | 0.52 | -7.2 dB |
| Peaking | 419 Hz  | 1.15 | 8.9 dB  |
| Peaking | 5748 Hz | 3.28 | 7.4 dB  |
| Peaking | 9777 Hz | 4.06 | -5.6 dB |
| Peaking | 445 Hz  | 6.62 | -1.4 dB |
| Peaking | 669 Hz  | 2    | 1.9 dB  |
| Peaking | 1382 Hz | 1.29 | -2.2 dB |
| Peaking | 3648 Hz | 4.71 | -4.6 dB |
| Peaking | 4816 Hz | 8.44 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Bluetooth/V-Moda%20Crossfade%20Wireless%20Bluetooth.png)