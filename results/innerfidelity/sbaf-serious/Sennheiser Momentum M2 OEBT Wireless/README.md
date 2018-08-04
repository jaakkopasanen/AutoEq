# Sennheiser Momentum M2 OEBT Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.9; 23 -4.1; 25 -4.5; 26 -4.7; 28 -5.1; 30 -5.3; 32 -5.5; 35 -5.8; 37 -5.9; 40 -6.2; 42 -6.3; 45 -6.4; 49 -6.4; 52 -6.4; 56 -6.4; 59 -6.6; 64 -4.1; 68 -1.4; 73 -4.0; 78 -4.8; 83 -4.1; 89 -3.7; 95 -3.4; 102 -2.9; 109 -2.6; 117 -2.2; 125 -2.1; 134 -1.9; 143 -1.5; 153 -1.1; 164 -0.6; 175 -0.3; 188 -0.0; 201 0.3; 215 0.7; 230 1.1; 246 1.6; 263 2.3; 282 3.0; 301 3.5; 323 4.0; 345 4.2; 369 4.3; 395 4.3; 423 4.3; 452 4.1; 484 3.8; 518 3.5; 554 3.4; 593 3.3; 635 2.9; 679 2.4; 726 2.0; 777 1.7; 832 1.2; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -2.0; 1529 -2.8; 1636 -3.5; 1751 -4.0; 1873 -4.3; 2004 -4.7; 2145 -4.9; 2295 -4.7; 2455 -3.9; 2627 -3.2; 2811 -2.1; 3008 -0.7; 3219 0.8; 3444 2.3; 3685 3.5; 3943 5.5; 4219 6.0; 4514 5.7; 4830 3.8; 5168 1.7; 5530 2.8; 5917 4.5; 6331 4.2; 6775 2.5; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.3; 9502 -2.6; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.66 | -6.1 dB |
| Peaking | 176 Hz  | 0.52 | -2.4 dB |
| Peaking | 376 Hz  | 0.67 | 6.0 dB  |
| Peaking | 2232 Hz | 1.04 | -6.6 dB |
| Peaking | 4128 Hz | 1.58 | 7.8 dB  |
| Peaking | 68 Hz   | 8.7  | 5.5 dB  |
| Peaking | 65 Hz   | 2.58 | -2.1 dB |
| Peaking | 5194 Hz | 8    | -2.9 dB |
| Peaking | 6097 Hz | 4.41 | 3.2 dB  |
| Peaking | 9085 Hz | 4.95 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wireless/Sennheiser%20Momentum%20M2%20OEBT%20Wireless.png)