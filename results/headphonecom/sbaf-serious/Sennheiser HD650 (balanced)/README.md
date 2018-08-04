# Sennheiser HD650 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.6; 25 5.1; 26 4.9; 28 4.3; 30 3.9; 32 3.5; 35 3.0; 37 2.8; 40 2.5; 42 2.3; 45 2.2; 49 2.2; 52 2.0; 56 1.4; 59 1.0; 64 0.7; 68 0.8; 73 0.7; 78 0.2; 83 -0.1; 89 -0.6; 95 -1.0; 102 -1.4; 109 -1.6; 117 -2.0; 125 -2.6; 134 -2.9; 143 -3.1; 153 -3.3; 164 -3.0; 175 -3.0; 188 -3.1; 201 -3.0; 215 -3.0; 230 -2.8; 246 -2.6; 263 -2.6; 282 -2.3; 301 -2.2; 323 -2.1; 345 -1.7; 369 -1.6; 395 -1.3; 423 -1.1; 452 -0.8; 484 -0.9; 518 -0.9; 554 -0.8; 593 -0.5; 635 -0.4; 679 -0.5; 726 -0.6; 777 -0.5; 832 -0.6; 890 -0.8; 952 -0.1; 1019 -0.1; 1090 -0.6; 1167 -0.9; 1248 -1.1; 1336 -1.2; 1429 -1.5; 1529 -1.7; 1636 -2.0; 1751 -2.1; 1873 -2.2; 2004 -2.3; 2145 -2.1; 2295 -1.9; 2455 -1.8; 2627 -1.8; 2811 -1.9; 3008 -1.5; 3219 -1.8; 3444 -1.6; 3685 -0.7; 3943 0.5; 4219 0.1; 4514 -1.1; 4830 -0.6; 5168 2.1; 5530 3.1; 5917 1.4; 6331 -0.8; 6775 -0.9; 7249 -0.6; 7756 -0.8; 8299 -2.1; 8880 -3.2; 9502 -1.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD650 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.3  | 7.0 dB  |
| Peaking | 174 Hz   | 0.72 | -3.5 dB |
| Peaking | 1854 Hz  | 1.81 | -2.2 dB |
| Peaking | 2966 Hz  | 3.58 | -1.4 dB |
| Peaking | 8903 Hz  | 6.31 | -3.4 dB |
| Peaking | 76 Hz    | 4.32 | 0.5 dB  |
| Peaking | 5531 Hz  | 5.9  | 5.5 dB  |
| Peaking | 5830 Hz  | 2.11 | -1.9 dB |
| Peaking | 37722 Hz | 4.25 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD650%20(balanced)/Sennheiser%20HD650%20(balanced).png)