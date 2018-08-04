# Sennheiser PXC350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.2; 22 -1.0; 23 -1.3; 25 -1.9; 26 -2.1; 28 -2.5; 30 -2.7; 32 -2.9; 35 -3.0; 37 -3.0; 40 -2.9; 42 -2.9; 45 -2.8; 49 -2.6; 52 -2.5; 56 -2.3; 59 -2.1; 64 -1.9; 68 -1.7; 73 -1.5; 78 -1.1; 83 -0.8; 89 -0.7; 95 -0.8; 102 -0.6; 109 -0.3; 117 -0.1; 125 0.1; 134 0.3; 143 0.4; 153 0.6; 164 1.1; 175 1.4; 188 1.6; 201 1.9; 215 2.3; 230 2.3; 246 2.1; 263 2.0; 282 1.9; 301 1.7; 323 1.6; 345 1.5; 369 1.2; 395 0.9; 423 0.6; 452 0.2; 484 -0.3; 518 -0.5; 554 -0.5; 593 -0.3; 635 -0.5; 679 -0.6; 726 -0.5; 777 -0.2; 832 0.1; 890 0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.3; 1336 -0.0; 1429 -0.5; 1529 -1.2; 1636 -2.3; 1751 -3.6; 1873 -4.0; 2004 0.7; 2145 6.0; 2295 4.6; 2455 -2.5; 2627 -5.3; 2811 -3.0; 3008 0.5; 3219 2.6; 3444 2.7; 3685 2.5; 3943 4.4; 4219 6.0; 4514 5.8; 4830 2.6; 5168 3.8; 5530 6.0; 5917 2.0; 6331 0.5; 6775 -0.6; 7249 0.1; 7756 0.2; 8299 -0.3; 8880 -1.7; 9502 -2.6; 10167 -2.5; 10879 -1.6; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 1.22 | -3.3 dB |
| Peaking | 1871 Hz | 4.44 | -7.3 dB |
| Peaking | 2166 Hz | 4.95 | 10.2 dB |
| Peaking | 2589 Hz | 6.14 | -8.4 dB |
| Peaking | 4325 Hz | 2.25 | 5.8 dB  |
| Peaking | 71 Hz   | 1.52 | -0.7 dB |
| Peaking | 234 Hz  | 1.48 | 2.5 dB  |
| Peaking | 5552 Hz | 8.9  | 7.0 dB  |
| Peaking | 5551 Hz | 3.03 | -2.7 dB |
| Peaking | 9813 Hz | 3.83 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC350/Sennheiser%20PXC350.png)