# Sennheiser HD 419

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.6; 22 -10.9; 23 -11.0; 25 -11.3; 26 -11.4; 28 -11.5; 30 -11.6; 32 -11.8; 35 -11.9; 37 -12.0; 40 -12.1; 42 -12.1; 45 -12.2; 49 -12.2; 52 -12.2; 56 -12.1; 59 -12.1; 64 -11.9; 68 -11.9; 73 -11.7; 78 -11.2; 83 -10.2; 89 -7.9; 95 -8.3; 102 -11.1; 109 -12.1; 117 -12.3; 125 -12.1; 134 -11.9; 143 -12.1; 153 -12.0; 164 -11.3; 175 -11.8; 188 -11.9; 201 -11.7; 215 -11.7; 230 -11.5; 246 -10.7; 263 -9.8; 282 -9.0; 301 -8.1; 323 -7.3; 345 -6.7; 369 -5.4; 395 -4.1; 423 -3.5; 452 -3.1; 484 -2.9; 518 -3.2; 554 -3.5; 593 -3.1; 635 -2.3; 679 -1.5; 726 -1.2; 777 -1.3; 832 -1.1; 890 -0.2; 952 -0.3; 1019 0.0; 1090 -0.5; 1167 -0.6; 1248 0.3; 1336 0.3; 1429 0.6; 1529 0.8; 1636 1.1; 1751 0.9; 1873 0.6; 2004 1.4; 2145 2.7; 2295 4.2; 2455 4.7; 2627 4.2; 2811 5.0; 3008 4.8; 3219 4.4; 3444 4.1; 3685 3.9; 3943 5.5; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 5 Hz    | 1.64 | -10.1 dB |
| Peaking | 12 Hz   | 1.28 | -11.3 dB |
| Peaking | 42 Hz   | 0.46 | -10.5 dB |
| Peaking | 194 Hz  | 0.73 | -10.0 dB |
| Peaking | 4132 Hz | 0.88 | 6.2 dB   |
| Peaking | 5 Hz    | 2.06 | 0.2 dB   |
| Peaking | 2438 Hz | 6.22 | 2.0 dB   |
| Peaking | 3640 Hz | 7.08 | -2.0 dB  |
| Peaking | 6313 Hz | 2.43 | 5.0 dB   |
| Peaking | 7392 Hz | 1.54 | -4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)