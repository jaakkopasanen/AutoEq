# Sennheiser CX 300-II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.1; 22 -2.4; 23 -2.6; 25 -2.9; 26 -3.0; 28 -3.2; 30 -3.4; 32 -3.6; 35 -3.8; 37 -4.0; 40 -4.2; 42 -4.3; 45 -4.5; 49 -4.8; 52 -5.0; 56 -5.3; 59 -5.4; 64 -5.7; 68 -5.9; 73 -6.1; 78 -6.3; 83 -6.5; 89 -6.8; 95 -6.9; 102 -7.2; 109 -7.3; 117 -7.5; 125 -7.5; 134 -7.7; 143 -7.7; 153 -7.8; 164 -7.8; 175 -7.8; 188 -7.7; 201 -7.6; 215 -7.4; 230 -7.2; 246 -7.0; 263 -6.8; 282 -6.5; 301 -6.2; 323 -5.8; 345 -5.4; 369 -5.0; 395 -4.6; 423 -4.1; 452 -3.8; 484 -3.4; 518 -2.9; 554 -2.4; 593 -2.0; 635 -1.5; 679 -1.1; 726 -0.7; 777 -0.3; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.1; 1429 0.0; 1529 0.0; 1636 0.1; 1751 0.2; 1873 0.5; 2004 0.8; 2145 1.2; 2295 1.8; 2455 2.5; 2627 3.3; 2811 4.0; 3008 4.8; 3219 5.6; 3444 6.0; 3685 5.8; 3943 4.4; 4219 2.6; 4514 0.8; 4830 -0.3; 5168 -1.2; 5530 -2.8; 5917 -5.8; 6331 -6.3; 6775 -3.1; 7249 -0.7; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.107254871097875dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 300-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.38 | -4.6 dB |
| Peaking | 172 Hz  | 0.75 | -4.4 dB |
| Peaking | 331 Hz  | 1.22 | -2.6 dB |
| Peaking | 3357 Hz | 2.04 | 6.5 dB  |
| Peaking | 6056 Hz | 4.55 | -7.6 dB |
| Peaking | 512 Hz  | 3.7  | -0.5 dB |
| Peaking | 830 Hz  | 2.63 | 0.7 dB  |
| Peaking | 4737 Hz | 9.71 | -1.1 dB |
| Peaking | 7681 Hz | 9.2  | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20300-II/Sennheiser%20CX%20300-II.png)