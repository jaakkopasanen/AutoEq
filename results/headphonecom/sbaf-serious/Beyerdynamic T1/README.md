# Beyerdynamic T1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 3.5; 22 3.0; 23 2.8; 25 2.4; 26 2.3; 28 1.9; 30 1.7; 32 1.4; 35 1.1; 37 0.9; 40 0.6; 42 0.5; 45 0.3; 49 -0.0; 52 -0.2; 56 -0.3; 59 -0.3; 64 0.1; 68 0.3; 73 -0.6; 78 -1.2; 83 -1.7; 89 -2.1; 95 -2.2; 102 -2.5; 109 -2.8; 117 -2.9; 125 -3.1; 134 -3.2; 143 -3.6; 153 -3.7; 164 -3.6; 175 -3.7; 188 -3.7; 201 -3.7; 215 -3.7; 230 -3.8; 246 -3.9; 263 -3.7; 282 -3.6; 301 -3.5; 323 -3.4; 345 -3.3; 369 -3.0; 395 -2.8; 423 -2.8; 452 -2.6; 484 -2.4; 518 -2.0; 554 -1.7; 593 -1.8; 635 -1.5; 679 -1.1; 726 -0.8; 777 -0.5; 832 -0.4; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.2; 1336 1.5; 1429 1.0; 1529 0.3; 1636 -0.8; 1751 -1.4; 1873 -2.0; 2004 -2.0; 2145 -1.1; 2295 -0.1; 2455 0.4; 2627 0.5; 2811 -0.3; 3008 -0.7; 3219 -0.0; 3444 0.7; 3685 0.3; 3943 -0.3; 4219 -0.6; 4514 0.5; 4830 2.0; 5168 1.6; 5530 0.9; 5917 1.1; 6331 3.0; 6775 1.8; 7249 0.6; 7756 -4.1; 8299 -7.9; 8880 -9.3; 9502 -7.4; 10167 -2.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 -1.0; 14260 -1.9; 15258 -1.4; 16326 -0.1; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.578947203494647dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.57 | 4.7 dB   |
| Peaking | 202 Hz   | 0.53 | -4.1 dB  |
| Peaking | 1940 Hz  | 7.23 | -2.2 dB  |
| Peaking | 6641 Hz  | 2.22 | 4.3 dB   |
| Peaking | 8693 Hz  | 3.6  | -11.5 dB |
| Peaking | 68 Hz    | 5.62 | 1.2 dB   |
| Peaking | 1273 Hz  | 3.43 | 2.0 dB   |
| Peaking | 2448 Hz  | 0.11 | -0.1 dB  |
| Peaking | 11132 Hz | 5.69 | 2.1 dB   |
| Peaking | 14520 Hz | 4.74 | -1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)