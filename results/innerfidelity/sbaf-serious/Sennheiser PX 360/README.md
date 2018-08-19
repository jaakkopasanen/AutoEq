# Sennheiser PX 360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.7; 49 5.2; 52 4.9; 56 4.4; 59 4.1; 64 3.6; 68 3.2; 73 2.8; 78 2.3; 83 1.8; 89 1.4; 95 1.1; 102 0.8; 109 0.7; 117 0.5; 125 0.6; 134 1.2; 143 1.7; 153 2.4; 164 1.0; 175 3.0; 188 3.4; 201 2.3; 215 1.9; 230 1.1; 246 0.7; 263 0.2; 282 0.6; 301 0.6; 323 0.1; 345 0.1; 369 0.5; 395 1.0; 423 1.5; 452 1.7; 484 1.5; 518 1.6; 554 1.9; 593 2.0; 635 1.8; 679 1.7; 726 1.5; 777 1.6; 832 1.3; 890 0.9; 952 0.5; 1019 -0.2; 1090 -0.9; 1167 -1.9; 1248 -2.8; 1336 -4.0; 1429 -5.2; 1529 -6.5; 1636 -7.6; 1751 -8.4; 1873 -8.7; 2004 -8.0; 2145 -6.8; 2295 -5.1; 2455 -2.9; 2627 -1.2; 2811 -0.2; 3008 1.2; 3219 2.6; 3444 4.1; 3685 5.3; 3943 6.0; 4219 4.7; 4514 3.0; 4830 3.0; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -1.4; 10167 -2.3; 10879 -2.2; 11640 -0.5; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.57 | 6.4 dB   |
| Peaking | 777 Hz   | 0.66 | 2.8 dB   |
| Peaking | 1802 Hz  | 1.43 | -10.5 dB |
| Peaking | 3683 Hz  | 2.19 | 6.8 dB   |
| Peaking | 5871 Hz  | 3.76 | 6.1 dB   |
| Peaking | 105 Hz   | 3.25 | -1.1 dB  |
| Peaking | 185 Hz   | 4.87 | 2.7 dB   |
| Peaking | 332 Hz   | 4.28 | -1.0 dB  |
| Peaking | 9811 Hz  | 0.57 | 0.3 dB   |
| Peaking | 10280 Hz | 3.36 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)