# Beyerdynamic T70

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.2; 22 1.0; 23 0.9; 25 0.7; 26 0.6; 28 0.5; 30 0.4; 32 0.3; 35 0.2; 37 0.1; 40 0.0; 42 0.0; 45 -0.0; 49 -0.1; 52 -0.2; 56 -0.3; 59 -0.3; 64 -0.5; 68 -0.6; 73 -0.6; 78 -0.7; 83 -0.8; 89 -0.9; 95 -0.9; 102 -0.9; 109 -0.9; 117 -0.9; 125 -1.2; 134 -1.8; 143 -2.2; 153 -2.3; 164 -1.5; 175 -1.0; 188 -1.5; 201 -1.3; 215 -1.1; 230 -0.8; 246 -0.5; 263 -0.3; 282 -0.2; 301 -0.1; 323 -0.2; 345 -0.3; 369 -0.3; 395 -0.5; 423 -0.7; 452 -0.8; 484 -0.7; 518 0.1; 554 0.6; 593 0.4; 635 0.3; 679 0.3; 726 0.2; 777 0.2; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.3; 1336 -0.6; 1429 -1.0; 1529 -1.4; 1636 -1.6; 1751 -1.3; 1873 -0.3; 2004 1.7; 2145 3.8; 2295 4.6; 2455 4.8; 2627 4.4; 2811 4.0; 3008 3.8; 3219 3.6; 3444 3.3; 3685 3.9; 3943 5.9; 4219 4.2; 4514 2.9; 4830 4.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.4; 6775 0.9; 7249 -4.0; 7756 -7.2; 8299 -9.3; 8880 -10.3; 9502 -9.9; 10167 -7.7; 10879 -3.3; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099998700090227dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 149 Hz   | 1.27 | -1.8 dB  |
| Peaking | 2462 Hz  | 4.01 | 4.7 dB   |
| Peaking | 3850 Hz  | 2.66 | 4.1 dB   |
| Peaking | 5875 Hz  | 2.8  | 8.6 dB   |
| Peaking | 8679 Hz  | 2.4  | -12.7 dB |
| Peaking | 20 Hz    | 1.67 | 1.1 dB   |
| Peaking | 1619 Hz  | 4.71 | -2.4 dB  |
| Peaking | 10205 Hz | 5.19 | -4.4 dB  |
| Peaking | 11371 Hz | 2.36 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70/Beyerdynamic%20T70.png)