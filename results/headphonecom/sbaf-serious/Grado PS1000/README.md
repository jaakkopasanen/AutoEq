# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 4.9; 37 4.3; 40 3.3; 42 2.7; 45 1.9; 49 0.9; 52 0.2; 56 -0.7; 59 -1.3; 64 -2.1; 68 -2.7; 73 -3.3; 78 -3.7; 83 -4.1; 89 -4.4; 95 -4.6; 102 -4.8; 109 -4.9; 117 -4.8; 125 -4.8; 134 -4.6; 143 -4.4; 153 -4.1; 164 -3.7; 175 -3.3; 188 -2.9; 201 -2.6; 215 -2.3; 230 -1.9; 246 -1.7; 263 -1.5; 282 -1.2; 301 -0.8; 323 -0.5; 345 0.1; 369 0.4; 395 -0.0; 423 0.0; 452 0.1; 484 0.0; 518 0.1; 554 0.4; 593 0.6; 635 0.5; 679 0.5; 726 0.5; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -2.6; 1751 -1.6; 1873 -1.2; 2004 -1.1; 2145 -1.1; 2295 -1.0; 2455 -1.0; 2627 -1.1; 2811 -1.1; 3008 -1.1; 3219 -1.0; 3444 -0.0; 3685 -2.8; 3943 -7.8; 4219 -8.2; 4514 -6.3; 4830 -6.6; 5168 -7.2; 5530 -8.1; 5917 -8.9; 6331 -11.9; 6775 -11.6; 7249 -10.1; 7756 -9.3; 8299 -9.0; 8880 -8.6; 9502 -7.2; 10167 -5.1; 10879 -2.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 27 Hz    |  0.91 | 7.1 dB   |
| Peaking | 103 Hz   |  0.82 | -5.8 dB  |
| Peaking | 1580 Hz  |  5.3  | -2.4 dB  |
| Peaking | 4147 Hz  |  6.68 | -5.4 dB  |
| Peaking | 6918 Hz  |  1.49 | -11.8 dB |
| Peaking | 3 Hz     |  1.32 | 0.2 dB   |
| Peaking | 605 Hz   |  1.3  | 0.9 dB   |
| Peaking | 3457 Hz  | 10.43 | 2.8 dB   |
| Peaking | 9522 Hz  |  3.71 | -3.8 dB  |
| Peaking | 11776 Hz |  1.64 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)