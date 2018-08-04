# Sennheiser HD600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 10 -84; 20 6.4; 22 5.6; 23 5.2; 25 4.5; 26 4.2; 28 3.5; 30 3.0; 32 2.5; 35 1.9; 37 1.5; 40 1.0; 42 0.7; 45 0.3; 49 -0.1; 52 -0.2; 56 0.0; 59 0.0; 64 -1.0; 68 -1.7; 73 -2.1; 78 -2.3; 83 -2.4; 89 -2.6; 95 -2.7; 102 -2.7; 109 -2.5; 117 -2.5; 125 -2.7; 134 -2.5; 143 -2.2; 153 -2.3; 164 -2.2; 175 -2.1; 188 -2.0; 201 -1.9; 215 -1.7; 230 -1.5; 246 -1.5; 263 -1.3; 282 -1.2; 301 -0.9; 323 -0.7; 345 -0.5; 369 -0.2; 395 -0.1; 423 0.2; 452 0.3; 484 0.3; 518 0.2; 554 0.4; 593 0.7; 635 0.8; 679 0.8; 726 0.9; 777 0.9; 832 0.7; 890 0.4; 952 0.1; 1019 0.2; 1090 0.4; 1167 0.2; 1248 0.1; 1336 -0.1; 1429 -0.4; 1529 -0.5; 1636 -0.7; 1751 -0.6; 1873 -0.7; 2004 -0.7; 2145 -0.9; 2295 -1.3; 2455 -1.4; 2627 -1.8; 2811 -2.2; 3008 -2.6; 3219 -3.5; 3444 -4.2; 3685 -4.5; 3943 -4.0; 4219 -4.3; 4514 -4.7; 4830 -4.1; 5168 -2.2; 5530 0.9; 5917 2.7; 6331 1.8; 6775 1.3; 7249 1.1; 7756 0.3; 8299 -0.1; 8880 -0.4; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.2; 13327 -3.0; 14260 -5.6; 15258 -5.2; 16326 -2.1; 17469 -0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.0dB` and instead set Global volume in the UI for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.94 | 6.8 dB  |
| Peaking | 110 Hz   | 0.73 | -3.1 dB |
| Peaking | 4452 Hz  | 1.38 | -6.6 dB |
| Peaking | 5966 Hz  | 2.43 | 6.1 dB  |
| Peaking | 14731 Hz | 3.61 | -6.5 dB |
| Peaking | 247 Hz   | 2.45 | -0.6 dB |
| Peaking | 678 Hz   | 1.19 | 1.0 dB  |
| Peaking | 3877 Hz  | 2.38 | -1.3 dB |
| Peaking | 4061 Hz  | 6.4  | 2.3 dB  |
| Peaking | 11666 Hz | 4.5  | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD600/Sennheiser%20HD600.png)