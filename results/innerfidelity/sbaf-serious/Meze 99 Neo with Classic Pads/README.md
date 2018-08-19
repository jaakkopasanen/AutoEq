# Meze 99 Neo with Classic Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.6; 52 5.2; 56 4.7; 59 4.5; 64 4.2; 68 4.2; 73 4.1; 78 3.9; 83 3.5; 89 3.0; 95 2.7; 102 2.5; 109 2.3; 117 2.1; 125 1.8; 134 1.6; 143 1.4; 153 1.1; 164 1.3; 175 1.3; 188 1.2; 201 1.1; 215 1.3; 230 1.4; 246 1.9; 263 2.6; 282 2.9; 301 3.3; 323 3.8; 345 4.3; 369 4.5; 395 4.4; 423 4.0; 452 3.3; 484 2.2; 518 1.5; 554 0.9; 593 0.6; 635 0.3; 679 -0.0; 726 -0.2; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.1; 1248 0.1; 1336 0.1; 1429 -0.1; 1529 -0.2; 1636 -0.4; 1751 -0.4; 1873 -0.4; 2004 -0.1; 2145 -0.0; 2295 -0.2; 2455 0.1; 2627 1.1; 2811 1.3; 3008 1.6; 3219 2.2; 3444 3.4; 3685 4.4; 3943 4.4; 4219 1.9; 4514 1.6; 4830 2.3; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Neo with Classic Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.43 | 6.3 dB  |
| Peaking | 366 Hz  | 2.12 | 4.6 dB  |
| Peaking | 3671 Hz | 4.54 | 3.9 dB  |
| Peaking | 5933 Hz | 2.74 | 7.0 dB  |
| Peaking | 7838 Hz | 1.8  | -1.4 dB |
| Peaking | 446 Hz  | 7.08 | 0.8 dB  |
| Peaking | 675 Hz  | 1.98 | -0.6 dB |
| Peaking | 1699 Hz | 4.51 | -0.5 dB |
| Peaking | 2513 Hz | 2.26 | -1.0 dB |
| Peaking | 2741 Hz | 4.16 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2099%20Neo%20with%20Classic%20Pads/Meze%2099%20Neo%20with%20Classic%20Pads.png)