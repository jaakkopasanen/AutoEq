# Sennheiser PX 360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.6; 83 5.2; 89 4.8; 95 4.4; 102 4.2; 109 4.3; 117 5.1; 125 6.0; 134 5.5; 143 4.6; 153 4.4; 164 5.0; 175 6.0; 188 5.9; 201 5.3; 215 4.5; 230 4.0; 246 4.0; 263 3.4; 282 1.7; 301 0.3; 323 -0.3; 345 -0.5; 369 -0.5; 395 -1.2; 423 -1.7; 452 -1.5; 484 -1.0; 518 -0.5; 554 0.0; 593 0.5; 635 0.5; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.6; 1167 -1.5; 1248 -2.6; 1336 -4.2; 1429 -5.9; 1529 -7.7; 1636 -8.9; 1751 -9.7; 1873 -9.7; 2004 -9.0; 2145 -7.4; 2295 -5.4; 2455 -3.1; 2627 -1.2; 2811 -0.0; 3008 1.4; 3219 3.1; 3444 4.9; 3685 6.0; 3943 6.0; 4219 4.0; 4514 2.5; 4830 1.6; 5168 2.7; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.4; 10167 -2.8; 10879 -3.0; 11640 -1.6; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.44 | 5.3 dB   |
| Peaking | 78 Hz    | 0.69 | 3.6 dB   |
| Peaking | 186 Hz   | 2.06 | 4.4 dB   |
| Peaking | 1870 Hz  | 1.94 | -12.2 dB |
| Peaking | 3845 Hz  | 1.12 | 6.4 dB   |
| Peaking | 417 Hz   | 2.96 | -2.4 dB  |
| Peaking | 835 Hz   | 2.1  | 1.8 dB   |
| Peaking | 4812 Hz  | 6.35 | -3.6 dB  |
| Peaking | 6051 Hz  | 4.33 | 4.5 dB   |
| Peaking | 10437 Hz | 3.16 | -3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)