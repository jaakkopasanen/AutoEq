# Sennheiser Momentum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.7; 22 3.4; 23 3.3; 25 3.1; 26 3.0; 28 2.8; 30 2.7; 32 2.6; 35 2.5; 37 2.4; 40 2.3; 42 2.2; 45 2.1; 49 2.0; 52 1.9; 56 1.8; 59 1.7; 64 1.6; 68 1.6; 73 1.4; 78 1.2; 83 1.1; 89 1.0; 95 0.7; 102 0.4; 109 0.2; 117 0.1; 125 -0.1; 134 -0.3; 143 -0.6; 153 -1.1; 164 -1.3; 175 -0.9; 188 -1.2; 201 -1.4; 215 -1.4; 230 -1.2; 246 -1.1; 263 -0.9; 282 -0.4; 301 -0.3; 323 0.1; 345 0.7; 369 1.2; 395 1.4; 423 1.6; 452 1.7; 484 1.6; 518 1.5; 554 1.6; 593 1.7; 635 1.4; 679 0.9; 726 0.5; 777 0.5; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 -0.1; 1336 -0.7; 1429 -1.2; 1529 -1.5; 1636 -1.5; 1751 -1.5; 1873 -1.1; 2004 -0.4; 2145 0.5; 2295 1.8; 2455 3.4; 2627 4.8; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.04 | 3.4 dB  |
| Peaking | 58 Hz   | 1.96 | 1.4 dB  |
| Peaking | 507 Hz  | 2.41 | 1.8 dB  |
| Peaking | 1748 Hz | 1.95 | -4.1 dB |
| Peaking | 3759 Hz | 0.86 | 7.2 dB  |
| Peaking | 198 Hz  | 2.04 | -1.7 dB |
| Peaking | 2806 Hz | 5.59 | 1.4 dB  |
| Peaking | 3816 Hz | 2.7  | -1.0 dB |
| Peaking | 6264 Hz | 2.43 | 5.2 dB  |
| Peaking | 7387 Hz | 1.49 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)