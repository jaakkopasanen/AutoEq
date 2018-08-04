# Sennheiser PX 100 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.6; 25 5.1; 26 4.9; 28 4.3; 30 3.8; 32 3.3; 35 2.8; 37 2.4; 40 2.0; 42 1.7; 45 1.3; 49 0.9; 52 0.6; 56 0.3; 59 0.1; 64 -0.2; 68 -0.5; 73 -0.8; 78 -1.0; 83 -1.3; 89 -1.6; 95 -1.7; 102 -1.8; 109 -2.1; 117 -2.7; 125 -3.1; 134 -3.4; 143 -3.7; 153 -3.7; 164 -3.8; 175 -3.8; 188 -3.7; 201 -3.7; 215 -3.4; 230 -3.3; 246 -3.1; 263 -2.9; 282 -2.5; 301 -2.2; 323 -2.1; 345 -1.7; 369 -1.4; 395 -1.2; 423 -0.9; 452 -0.8; 484 -0.9; 518 -0.6; 554 -0.3; 593 -0.0; 635 0.1; 679 0.1; 726 0.2; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.9; 1429 -1.5; 1529 -2.0; 1636 -2.7; 1751 -3.0; 1873 -3.0; 2004 -2.5; 2145 -1.4; 2295 0.4; 2455 2.6; 2627 3.6; 2811 4.5; 3008 3.9; 3219 2.1; 3444 2.9; 3685 4.2; 3943 3.1; 4219 -1.4; 4514 -3.3; 4830 -0.3; 5168 3.7; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.99 | 5.9 dB  |
| Peaking | 169 Hz  | 0.83 | -4.1 dB |
| Peaking | 1866 Hz | 2.52 | -4.2 dB |
| Peaking | 2787 Hz | 2.61 | 5.2 dB  |
| Peaking | 5982 Hz | 4.66 | 6.8 dB  |
| Peaking | 776 Hz  | 2.33 | 0.8 dB  |
| Peaking | 3829 Hz | 7.2  | 4.6 dB  |
| Peaking | 4462 Hz | 4.88 | -5.7 dB |
| Peaking | 5279 Hz | 7.7  | 3.3 dB  |
| Peaking | 9108 Hz | 6.87 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20100%20II/Sennheiser%20PX%20100%20II.png)