# AKG K81 DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 5.9; 164 5.5; 175 5.6; 188 5.5; 201 5.5; 215 5.9; 230 5.9; 246 5.5; 263 5.2; 282 4.5; 301 4.0; 323 3.1; 345 2.0; 369 1.1; 395 0.2; 423 -0.2; 452 -0.4; 484 -0.2; 518 0.0; 554 0.1; 593 0.1; 635 0.4; 679 0.4; 726 0.5; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -1.8; 1751 -1.4; 1873 -1.2; 2004 -1.2; 2145 -1.7; 2295 -1.3; 2455 -0.0; 2627 0.9; 2811 1.8; 3008 2.9; 3219 3.7; 3444 3.8; 3685 2.7; 3943 1.3; 4219 0.2; 4514 0.2; 4830 2.0; 5168 4.5; 5530 5.6; 5917 1.6; 6331 -1.2; 6775 -2.0; 7249 -0.9; 7756 0.1; 8299 0.0; 8880 -0.2; 9502 -1.0; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -3.1; 15258 -6.2; 16326 -5.9; 17469 -3.9; 18692 -2.3; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81 DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 68 Hz    | 0.17 | 6.5 dB  |
| Peaking | 4095 Hz  | 0.85 | 5.2 dB  |
| Peaking | 4453 Hz  | 0.08 | -2.6 dB |
| Peaking | 13266 Hz | 1.5  | 5.6 dB  |
| Peaking | 15518 Hz | 1.79 | -7.7 dB |
| Peaking | 427 Hz   | 5.2  | -2.3 dB |
| Peaking | 3346 Hz  | 3.49 | 4.5 dB  |
| Peaking | 4252 Hz  | 1.66 | -4.5 dB |
| Peaking | 5440 Hz  | 4.7  | 6.9 dB  |
| Peaking | 6475 Hz  | 6.42 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K81%20DJ/AKG%20K81%20DJ.png)