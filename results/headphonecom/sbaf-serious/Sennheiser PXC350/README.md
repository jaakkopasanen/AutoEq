# Sennheiser PXC350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.8; 22 3.0; 23 2.7; 25 2.1; 26 1.9; 28 1.5; 30 1.2; 32 1.1; 35 1.0; 37 0.9; 40 1.0; 42 1.0; 45 1.1; 49 1.1; 52 1.2; 56 1.3; 59 1.4; 64 1.5; 68 1.5; 73 1.6; 78 1.8; 83 1.9; 89 1.7; 95 1.4; 102 1.3; 109 1.3; 117 1.2; 125 1.2; 134 1.2; 143 1.2; 153 1.3; 164 1.7; 175 1.8; 188 1.9; 201 2.2; 215 2.5; 230 2.4; 246 2.2; 263 2.1; 282 1.9; 301 1.8; 323 1.7; 345 1.5; 369 1.2; 395 0.9; 423 0.6; 452 0.1; 484 -0.2; 518 -0.4; 554 -0.5; 593 -0.4; 635 -0.5; 679 -0.5; 726 -0.4; 777 -0.3; 832 0.1; 890 0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.3; 1336 -0.0; 1429 -0.5; 1529 -1.2; 1636 -2.3; 1751 -3.5; 1873 -4.0; 2004 0.7; 2145 6.0; 2295 4.6; 2455 -2.6; 2627 -5.2; 2811 -2.9; 3008 0.4; 3219 2.6; 3444 2.8; 3685 2.6; 3943 4.2; 4219 5.9; 4514 5.9; 4830 2.7; 5168 4.0; 5530 6.0; 5917 2.1; 6331 0.5; 6775 -0.8; 7249 -0.1; 7756 0.2; 8299 -0.2; 8880 -1.6; 9502 -2.8; 10167 -2.6; 10879 -1.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999964dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.06 | 1.7 dB  |
| Peaking | 1871 Hz | 4.05 | -7.5 dB |
| Peaking | 2163 Hz | 4.96 | 10.7 dB |
| Peaking | 2592 Hz | 6.14 | -8.4 dB |
| Peaking | 4341 Hz | 2.26 | 5.8 dB  |
| Peaking | 255 Hz  | 2.03 | 1.2 dB  |
| Peaking | 568 Hz  | 2.25 | -1.3 dB |
| Peaking | 5510 Hz | 8.89 | 6.7 dB  |
| Peaking | 5701 Hz | 2.85 | -2.5 dB |
| Peaking | 9756 Hz | 4.37 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC350/Sennheiser%20PXC350.png)