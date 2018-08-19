# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.2; 23 4.9; 25 4.2; 26 4.0; 28 3.5; 30 3.0; 32 2.6; 35 2.0; 37 1.6; 40 1.0; 42 0.6; 45 0.1; 49 -0.5; 52 -0.8; 56 -1.0; 59 -1.0; 64 -0.4; 68 -0.2; 73 -1.5; 78 -2.9; 83 -3.7; 89 -4.2; 95 -4.3; 102 -4.4; 109 -5.0; 117 -5.4; 125 -5.6; 134 -5.8; 143 -5.8; 153 -5.8; 164 -5.5; 175 -5.3; 188 -5.2; 201 -5.1; 215 -5.1; 230 -4.4; 246 -3.2; 263 -2.3; 282 -1.8; 301 -1.7; 323 -1.1; 345 -0.1; 369 0.8; 395 1.5; 423 1.8; 452 1.6; 484 1.6; 518 1.5; 554 1.5; 593 1.5; 635 1.3; 679 1.2; 726 1.1; 777 0.9; 832 0.8; 890 0.6; 952 0.4; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.5; 1429 -2.0; 1529 -2.7; 1636 -3.7; 1751 -4.1; 1873 -4.2; 2004 -4.3; 2145 -4.0; 2295 -3.3; 2455 -2.3; 2627 -1.0; 2811 0.0; 3008 0.6; 3219 0.9; 3444 1.0; 3685 0.7; 3943 0.4; 4219 0.4; 4514 1.3; 4830 -0.3; 5168 -0.4; 5530 1.0; 5917 4.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -4.3; 8880 -5.2; 9502 -2.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.051324326468099dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.29 | 5.6 dB  |
| Peaking | 138 Hz  | 1.05 | -6.5 dB |
| Peaking | 1900 Hz | 2.71 | -4.9 dB |
| Peaking | 6345 Hz | 4.72 | 6.4 dB  |
| Peaking | 8674 Hz | 6.05 | -6.4 dB |
| Peaking | 31 Hz   | 2.41 | 0.6 dB  |
| Peaking | 224 Hz  | 3.25 | -2.3 dB |
| Peaking | 501 Hz  | 1.03 | 2.5 dB  |
| Peaking | 2354 Hz | 0.63 | -0.9 dB |
| Peaking | 3248 Hz | 2.77 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)