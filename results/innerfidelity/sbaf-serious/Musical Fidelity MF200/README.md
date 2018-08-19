# Musical Fidelity MF200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 3.2; 22 2.4; 23 2.1; 25 1.4; 26 1.1; 28 0.7; 30 0.2; 32 -0.2; 35 -0.7; 37 -1.0; 40 -1.3; 42 -1.5; 45 -1.8; 49 -2.0; 52 -2.2; 56 -2.3; 59 -2.3; 64 -2.5; 68 -2.7; 73 -2.9; 78 -2.9; 83 -3.0; 89 -3.0; 95 -2.9; 102 -3.1; 109 -3.1; 117 -3.0; 125 -2.9; 134 -2.5; 143 -2.3; 153 -2.4; 164 -2.2; 175 -1.8; 188 -1.7; 201 -1.6; 215 -1.2; 230 -0.9; 246 -0.6; 263 -0.2; 282 0.4; 301 1.0; 323 1.4; 345 1.6; 369 2.0; 395 2.1; 423 2.6; 452 3.1; 484 3.4; 518 3.9; 554 4.3; 593 4.0; 635 2.8; 679 1.8; 726 1.1; 777 0.7; 832 -0.0; 890 -0.6; 952 -0.4; 1019 0.1; 1090 -0.5; 1167 -0.2; 1248 0.3; 1336 0.5; 1429 0.9; 1529 0.8; 1636 0.7; 1751 0.6; 1873 0.6; 2004 0.3; 2145 0.1; 2295 -0.2; 2455 -0.1; 2627 0.1; 2811 -0.1; 3008 -0.1; 3219 -0.2; 3444 -0.3; 3685 -0.2; 3943 0.6; 4219 0.3; 4514 -1.9; 4830 -2.9; 5168 -0.2; 5530 1.3; 5917 4.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.793669004814444dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity MF200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.4  | 3.9 dB  |
| Peaking | 65 Hz   | 0.67 | -2.4 dB |
| Peaking | 131 Hz  | 1.05 | -1.8 dB |
| Peaking | 504 Hz  | 1.81 | 4.3 dB  |
| Peaking | 6300 Hz | 6.68 | 6.4 dB  |
| Peaking | 598 Hz  | 7.68 | 1.3 dB  |
| Peaking | 925 Hz  | 2.17 | -1.2 dB |
| Peaking | 1514 Hz | 3.16 | 1.0 dB  |
| Peaking | 4740 Hz | 8.2  | -3.8 dB |
| Peaking | 5752 Hz | 5.19 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Musical%20Fidelity%20MF200/Musical%20Fidelity%20MF200.png)