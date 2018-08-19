# Sennheiser Momentum M2 OEBT Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.9; 23 -4.1; 25 -4.5; 26 -4.7; 28 -5.1; 30 -5.4; 32 -5.6; 35 -5.8; 37 -6.0; 40 -6.3; 42 -6.5; 45 -6.6; 49 -6.6; 52 -6.7; 56 -6.8; 59 -7.0; 64 -4.6; 68 -2.0; 73 -4.6; 78 -5.6; 83 -4.9; 89 -4.5; 95 -4.1; 102 -3.5; 109 -3.0; 117 -2.4; 125 -2.1; 134 -1.8; 143 -1.3; 153 -0.9; 164 -0.3; 175 -0.1; 188 0.2; 201 0.4; 215 0.9; 230 1.2; 246 1.7; 263 2.4; 282 3.0; 301 3.5; 323 4.0; 345 4.3; 369 4.3; 395 4.3; 423 4.3; 452 4.1; 484 3.8; 518 3.5; 554 3.4; 593 3.3; 635 2.9; 679 2.4; 726 2.0; 777 1.7; 832 1.2; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -2.0; 1529 -2.8; 1636 -3.5; 1751 -4.0; 1873 -4.3; 2004 -4.7; 2145 -4.9; 2295 -4.7; 2455 -3.9; 2627 -3.2; 2811 -2.1; 3008 -0.7; 3219 0.8; 3444 2.3; 3685 3.5; 3943 5.5; 4219 6.0; 4514 5.7; 4830 3.8; 5168 1.7; 5530 2.8; 5917 4.5; 6331 4.2; 6775 2.5; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.3; 9502 -2.6; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099996068419182dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.66 | -4.7 dB |
| Peaking | 79 Hz   | 0.47 | -2.7 dB |
| Peaking | 398 Hz  | 0.71 | 5.1 dB  |
| Peaking | 2228 Hz | 1.06 | -6.6 dB |
| Peaking | 4133 Hz | 1.59 | 7.7 dB  |
| Peaking | 67 Hz   | 2.72 | -2.5 dB |
| Peaking | 68 Hz   | 8.49 | 5.8 dB  |
| Peaking | 5227 Hz | 8.03 | -2.9 dB |
| Peaking | 6140 Hz | 4.42 | 3.2 dB  |
| Peaking | 9148 Hz | 4.96 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wireless/Sennheiser%20Momentum%20M2%20OEBT%20Wireless.png)