# Grado SR325

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.7; 49 4.8; 52 4.1; 56 3.3; 59 2.8; 64 2.1; 68 1.5; 73 1.0; 78 0.5; 83 0.2; 89 -0.1; 95 -0.4; 102 -0.6; 109 -0.7; 117 -0.6; 125 -0.6; 134 -0.7; 143 -0.7; 153 -0.7; 164 -0.6; 175 -0.5; 188 -0.5; 201 -0.5; 215 -0.5; 230 -0.4; 246 -0.3; 263 -0.3; 282 -0.2; 301 -0.1; 323 0.0; 345 0.2; 369 0.3; 395 0.4; 423 0.4; 452 0.5; 484 0.3; 518 0.5; 554 0.5; 593 0.5; 635 0.6; 679 0.6; 726 0.6; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.2; 1529 -3.1; 1636 -3.9; 1751 -4.6; 1873 -6.4; 2004 -8.2; 2145 -8.2; 2295 -7.0; 2455 -6.0; 2627 -4.9; 2811 -3.8; 3008 -2.8; 3219 -1.6; 3444 -0.8; 3685 -0.8; 3943 -3.4; 4219 -9.2; 4514 -13.2; 4830 -10.5; 5168 -7.1; 5530 -5.0; 5917 -4.0; 6331 -5.0; 6775 -6.1; 7249 -6.5; 7756 -7.2; 8299 -9.0; 8880 -11.4; 9502 -12.5; 10167 -11.5; 10879 -9.4; 11640 -7.3; 12455 -4.0; 13327 -0.3; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.18 | 10.3 dB  |
| Peaking | 115 Hz   | 0.42 | -10.4 dB |
| Peaking | 2084 Hz  | 2.53 | -8.4 dB  |
| Peaking | 4586 Hz  | 5.73 | -12.4 dB |
| Peaking | 9453 Hz  | 1.88 | -12.8 dB |
| Peaking | 2668 Hz  | 5.89 | -1.1 dB  |
| Peaking | 3722 Hz  | 4.34 | 4.7 dB   |
| Peaking | 4074 Hz  | 3.28 | -2.8 dB  |
| Peaking | 11768 Hz | 3.26 | -3.6 dB  |
| Peaking | 13311 Hz | 2    | 3.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR325/Grado%20SR325.png)