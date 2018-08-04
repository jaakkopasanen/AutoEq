# Sennheiser PX 100 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.0; 22 2.2; 23 1.8; 25 1.2; 26 0.9; 28 0.3; 30 -0.2; 32 -0.7; 35 -1.2; 37 -1.5; 40 -2.0; 42 -2.3; 45 -2.6; 49 -3.1; 52 -3.4; 56 -3.7; 59 -3.9; 64 -4.1; 68 -4.3; 73 -4.5; 78 -4.6; 83 -4.7; 89 -4.7; 95 -4.6; 102 -4.3; 109 -4.2; 117 -4.3; 125 -4.2; 134 -4.2; 143 -4.3; 153 -4.1; 164 -4.1; 175 -4.0; 188 -3.8; 201 -3.8; 215 -3.5; 230 -3.3; 246 -3.1; 263 -3.0; 282 -2.5; 301 -2.2; 323 -2.1; 345 -1.7; 369 -1.4; 395 -1.2; 423 -0.9; 452 -0.8; 484 -0.9; 518 -0.6; 554 -0.3; 593 -0.0; 635 0.1; 679 0.1; 726 0.2; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.9; 1429 -1.5; 1529 -2.0; 1636 -2.7; 1751 -3.0; 1873 -3.0; 2004 -2.5; 2145 -1.4; 2295 0.4; 2455 2.6; 2627 3.6; 2811 4.5; 3008 3.9; 3219 2.1; 3444 2.9; 3685 4.2; 3943 3.1; 4219 -1.4; 4514 -3.3; 4830 -0.3; 5168 3.7; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 52 Hz   | 2.28 | -1.8 dB |
| Peaking | 81 Hz   | 1.42 | -3.1 dB |
| Peaking | 173 Hz  | 0.78 | -3.6 dB |
| Peaking | 2881 Hz | 4.81 | 4.8 dB  |
| Peaking | 5970 Hz | 4.52 | 6.9 dB  |
| Peaking | 20 Hz   | 2.66 | 3.0 dB  |
| Peaking | 1800 Hz | 3.15 | -3.8 dB |
| Peaking | 4157 Hz | 2.45 | 5.2 dB  |
| Peaking | 4416 Hz | 6.37 | -9.5 dB |
| Peaking | 9063 Hz | 5.39 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20100%20II/Sennheiser%20PX%20100%20II.png)