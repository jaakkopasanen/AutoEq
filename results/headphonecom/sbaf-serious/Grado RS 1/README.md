# Grado RS 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.7; 32 5.1; 35 4.0; 37 3.3; 40 2.3; 42 1.7; 45 0.8; 49 -0.1; 52 -0.7; 56 -1.6; 59 -2.2; 64 -3.1; 68 -3.7; 73 -4.4; 78 -4.8; 83 -5.1; 89 -5.3; 95 -5.3; 102 -5.4; 109 -5.3; 117 -5.2; 125 -5.0; 134 -4.7; 143 -4.4; 153 -4.1; 164 -3.7; 175 -3.2; 188 -3.1; 201 -3.0; 215 -2.7; 230 -2.4; 246 -2.2; 263 -1.8; 282 -1.4; 301 -0.6; 323 -0.3; 345 -1.6; 369 -1.6; 395 -1.3; 423 -0.9; 452 -0.8; 484 -0.6; 518 -0.6; 554 -0.3; 593 -0.0; 635 0.1; 679 0.1; 726 0.1; 777 0.3; 832 0.3; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.8; 1529 -2.5; 1636 -3.9; 1751 -7.0; 1873 -9.4; 2004 -8.4; 2145 -7.7; 2295 -7.0; 2455 -6.1; 2627 -5.1; 2811 -4.0; 3008 -2.3; 3219 -1.1; 3444 0.0; 3685 0.6; 3943 -0.5; 4219 -5.6; 4514 -11.7; 4830 -13.7; 5168 -10.1; 5530 -9.3; 5917 -8.1; 6331 -4.0; 6775 -0.2; 7249 -0.6; 7756 -3.7; 8299 -8.4; 8880 -12.0; 9502 -12.7; 10167 -10.5; 10879 -6.7; 11640 -3.5; 12455 -2.6; 13327 -3.9; 14260 -5.1; 15258 -3.6; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.78 | 7.5 dB   |
| Peaking | 93 Hz    | 0.66 | -6.5 dB  |
| Peaking | 2012 Hz  | 2.84 | -9.3 dB  |
| Peaking | 4873 Hz  | 4.74 | -13.5 dB |
| Peaking | 38404 Hz | 2.81 | -13.1 dB |
| Peaking | 2607 Hz  | 6.41 | -2.2 dB  |
| Peaking | 3699 Hz  | 6.27 | 4.2 dB   |
| Peaking | 5831 Hz  | 7.34 | -4.6 dB  |
| Peaking | 6993 Hz  | 7.25 | 4.9 dB   |
| Peaking | 14411 Hz | 4.81 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS%201/Grado%20RS%201.png)