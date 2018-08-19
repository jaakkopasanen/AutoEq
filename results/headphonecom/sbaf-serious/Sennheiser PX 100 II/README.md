# Sennheiser PX 100 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.6; 25 5.1; 26 4.9; 28 4.3; 30 3.8; 32 3.3; 35 2.7; 37 2.3; 40 1.9; 42 1.6; 45 1.2; 49 0.7; 52 0.3; 56 -0.1; 59 -0.4; 64 -0.8; 68 -1.1; 73 -1.5; 78 -1.8; 83 -2.1; 89 -2.4; 95 -2.4; 102 -2.4; 109 -2.6; 117 -2.9; 125 -3.1; 134 -3.3; 143 -3.5; 153 -3.5; 164 -3.6; 175 -3.6; 188 -3.5; 201 -3.5; 215 -3.3; 230 -3.2; 246 -3.0; 263 -2.8; 282 -2.4; 301 -2.2; 323 -2.0; 345 -1.7; 369 -1.4; 395 -1.1; 423 -0.9; 452 -0.9; 484 -0.8; 518 -0.5; 554 -0.3; 593 -0.1; 635 0.0; 679 0.2; 726 0.3; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.5; 1529 -2.1; 1636 -2.7; 1751 -3.0; 1873 -3.0; 2004 -2.5; 2145 -1.4; 2295 0.5; 2455 2.5; 2627 3.7; 2811 4.6; 3008 3.8; 3219 2.1; 3444 3.0; 3685 4.2; 3943 2.8; 4219 -1.4; 4514 -3.2; 4830 -0.3; 5168 3.6; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.02 | 6.0 dB  |
| Peaking | 157 Hz  | 0.67 | -3.8 dB |
| Peaking | 1868 Hz | 2.55 | -4.2 dB |
| Peaking | 2787 Hz | 2.62 | 5.2 dB  |
| Peaking | 5983 Hz | 4.65 | 6.8 dB  |
| Peaking | 755 Hz  | 2.12 | 0.8 dB  |
| Peaking | 3808 Hz | 7.2  | 4.4 dB  |
| Peaking | 4466 Hz | 4.81 | -5.5 dB |
| Peaking | 5271 Hz | 7.42 | 3.2 dB  |
| Peaking | 9116 Hz | 6.56 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20100%20II/Sennheiser%20PX%20100%20II.png)