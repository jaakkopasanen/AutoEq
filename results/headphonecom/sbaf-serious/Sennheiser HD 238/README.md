# Sennheiser HD 238

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 4.6; 22 3.8; 23 3.5; 25 2.8; 26 2.5; 28 1.9; 30 1.5; 32 1.1; 35 0.5; 37 0.2; 40 -0.2; 42 -0.3; 45 -0.5; 49 -0.9; 52 -1.3; 56 -1.7; 59 -1.9; 64 -1.9; 68 -2.1; 73 -2.5; 78 -2.9; 83 -3.2; 89 -3.5; 95 -3.7; 102 -4.0; 109 -4.1; 117 -4.3; 125 -4.4; 134 -4.4; 143 -4.4; 153 -4.4; 164 -4.5; 175 -4.6; 188 -4.4; 201 -4.4; 215 -4.2; 230 -4.1; 246 -3.9; 263 -3.8; 282 -3.5; 301 -3.3; 323 -3.0; 345 -2.7; 369 -2.4; 395 -2.1; 423 -1.9; 452 -1.8; 484 -1.5; 518 -1.4; 554 -1.0; 593 -0.8; 635 -0.4; 679 -0.3; 726 -0.2; 777 -0.0; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.1; 1636 -1.4; 1751 -1.5; 1873 -1.2; 2004 -0.5; 2145 0.7; 2295 1.7; 2455 2.2; 2627 1.2; 2811 -0.5; 3008 -2.3; 3219 -3.6; 3444 -2.1; 3685 1.0; 3943 1.2; 4219 -2.4; 4514 -4.2; 4830 -2.1; 5168 -0.0; 5530 -0.1; 5917 -1.4; 6331 -1.9; 6775 -1.4; 7249 -0.7; 7756 -0.3; 8299 -1.2; 8880 -2.7; 9502 -2.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.7; 15258 -2.2; 16326 -1.6; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.725346108764685dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.32 | 4.7 dB  |
| Peaking | 118 Hz   | 0.66 | -3.8 dB |
| Peaking | 251 Hz   | 0.97 | -2.3 dB |
| Peaking | 6069 Hz  | 0.57 | -1.4 dB |
| Peaking | 21623 Hz | 1.51 | -1.2 dB |
| Peaking | 1705 Hz  | 2.61 | -2.4 dB |
| Peaking | 2567 Hz  | 2.04 | 4.1 dB  |
| Peaking | 2930 Hz  | 5.38 | -3.2 dB |
| Peaking | 3201 Hz  | 9.54 | -3.7 dB |
| Peaking | 15543 Hz | 5.65 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20238/Sennheiser%20HD%20238.png)