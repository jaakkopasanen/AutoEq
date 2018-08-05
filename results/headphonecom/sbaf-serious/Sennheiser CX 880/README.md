# Sennheiser CX 880

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 10 -84; 20 -4.3; 22 -4.8; 23 -5.0; 25 -5.3; 26 -5.5; 28 -5.8; 30 -6.0; 32 -6.2; 35 -6.4; 37 -6.5; 40 -6.7; 42 -6.8; 45 -6.9; 49 -7.0; 52 -7.0; 56 -7.0; 59 -7.1; 64 -7.1; 68 -7.2; 73 -7.3; 78 -7.3; 83 -7.4; 89 -7.6; 95 -7.8; 102 -8.1; 109 -8.4; 117 -8.8; 125 -9.2; 134 -9.4; 143 -9.5; 153 -9.5; 164 -9.3; 175 -9.1; 188 -8.8; 201 -8.5; 215 -8.0; 230 -7.7; 246 -7.2; 263 -6.9; 282 -6.4; 301 -5.9; 323 -5.3; 345 -4.8; 369 -4.2; 395 -3.7; 423 -3.3; 452 -2.9; 484 -2.6; 518 -2.2; 554 -1.6; 593 -1.0; 635 -0.6; 679 -0.4; 726 -0.1; 777 0.3; 832 0.3; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.8; 1336 -1.0; 1429 -1.3; 1529 -1.8; 1636 -2.1; 1751 -2.3; 1873 -2.2; 2004 -2.1; 2145 -1.8; 2295 -1.5; 2455 -0.8; 2627 -0.4; 2811 0.3; 3008 1.4; 3219 2.4; 3444 3.2; 3685 3.2; 3943 2.4; 4219 0.1; 4514 -1.9; 4830 -3.0; 5168 -4.1; 5530 -5.5; 5917 -6.9; 6331 -6.5; 6775 -5.2; 7249 -4.7; 7756 -5.7; 8299 -8.4; 8880 -10.6; 9502 -9.7; 10167 -5.5; 10879 -0.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.8dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 3 Hz     | 1.85 | -3.5 dB  |
| Peaking | 43 Hz    | 0.31 | -5.8 dB  |
| Peaking | 182 Hz   | 0.72 | -6.9 dB  |
| Peaking | 5999 Hz  | 3.77 | -6.5 dB  |
| Peaking | 8965 Hz  | 3.86 | -11.1 dB |
| Peaking | 843 Hz   | 2.05 | 1.6 dB   |
| Peaking | 1900 Hz  | 1.44 | -2.5 dB  |
| Peaking | 3668 Hz  | 2.42 | 5.6 dB   |
| Peaking | 4654 Hz  | 2.68 | -2.8 dB  |
| Peaking | 11468 Hz | 5.98 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20880/Sennheiser%20CX%20880.png)