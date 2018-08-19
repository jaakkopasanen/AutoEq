# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 6.0; 635 6.0; 679 6.0; 726 6.0; 777 5.4; 832 4.1; 890 2.5; 952 1.1; 1019 -0.3; 1090 -1.0; 1167 -1.3; 1248 -1.5; 1336 -1.4; 1429 -1.3; 1529 -1.0; 1636 3.3; 1751 2.4; 1873 1.2; 2004 1.3; 2145 1.1; 2295 1.3; 2455 1.4; 2627 2.2; 2811 3.3; 3008 4.3; 3219 4.6; 3444 4.5; 3685 4.0; 3943 4.2; 4219 5.9; 4514 6.0; 4830 6.0; 5168 -0.7; 5530 2.2; 5917 4.1; 6331 3.4; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.5; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 89 Hz   |  0.05 | 6.1 dB  |
| Peaking | 729 Hz  |  1.66 | 2.7 dB  |
| Peaking | 1148 Hz |  1.62 | -6.7 dB |
| Peaking | 3136 Hz |  4.82 | 2.5 dB  |
| Peaking | 4410 Hz |  2.3  | 4.9 dB  |
| Peaking | 1557 Hz |  5.22 | -2.9 dB |
| Peaking | 1651 Hz |  9.65 | 5.3 dB  |
| Peaking | 5303 Hz | 12.53 | -7.2 dB |
| Peaking | 5885 Hz |  1.75 | 5.6 dB  |
| Peaking | 6594 Hz |  0.88 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)