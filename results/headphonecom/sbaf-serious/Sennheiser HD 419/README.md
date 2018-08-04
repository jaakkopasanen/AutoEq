# Sennheiser HD 419

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.1; 22 -10.4; 23 -10.5; 25 -10.7; 26 -10.8; 28 -11.0; 30 -11.1; 32 -11.2; 35 -11.3; 37 -11.4; 40 -11.5; 42 -11.5; 45 -11.6; 49 -11.6; 52 -11.6; 56 -11.6; 59 -11.5; 64 -11.3; 68 -11.3; 73 -11.1; 78 -10.6; 83 -9.4; 89 -7.1; 95 -7.5; 102 -10.1; 109 -10.9; 117 -11.1; 125 -10.8; 134 -10.6; 143 -10.7; 153 -10.7; 164 -10.0; 175 -10.5; 188 -10.6; 201 -10.3; 215 -10.3; 230 -10.0; 246 -9.3; 263 -8.5; 282 -7.6; 301 -6.8; 323 -5.9; 345 -5.3; 369 -4.0; 395 -2.8; 423 -2.3; 452 -2.1; 484 -2.2; 518 -2.7; 554 -3.0; 593 -2.6; 635 -2.0; 679 -1.4; 726 -1.2; 777 -1.1; 832 -1.0; 890 -0.2; 952 -0.3; 1019 0.0; 1090 -0.5; 1167 -0.9; 1248 -0.4; 1336 -1.0; 1429 -1.6; 1529 -1.9; 1636 -1.9; 1751 -2.2; 1873 -2.3; 2004 -1.6; 2145 -0.3; 2295 1.1; 2455 1.7; 2627 1.1; 2811 2.0; 3008 2.2; 3219 2.1; 3444 2.0; 3685 1.8; 3943 3.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.0; 5530 5.2; 5917 5.5; 6331 4.9; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 5 Hz    | 1.64 | -9.5 dB  |
| Peaking | 12 Hz   | 1.12 | -10.7 dB |
| Peaking | 44 Hz   | 0.51 | -10.0 dB |
| Peaking | 190 Hz  | 0.77 | -8.7 dB  |
| Peaking | 4931 Hz | 1.77 | 6.5 dB   |
| Peaking | 92 Hz   | 8.72 | 3.7 dB   |
| Peaking | 115 Hz  | 3.76 | -1.8 dB  |
| Peaking | 2347 Hz | 2.04 | 2.2 dB   |
| Peaking | 1854 Hz | 2.46 | -3.7 dB  |
| Peaking | 8496 Hz | 4.27 | -1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)