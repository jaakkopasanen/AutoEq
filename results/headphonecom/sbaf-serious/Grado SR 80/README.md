# Grado SR 80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.3; 49 4.3; 52 3.5; 56 2.7; 59 2.1; 64 1.4; 68 0.8; 73 0.0; 78 -0.6; 83 -1.0; 89 -1.5; 95 -1.8; 102 -1.8; 109 -1.9; 117 -1.9; 125 -2.0; 134 -1.9; 143 -1.9; 153 -1.8; 164 -1.5; 175 -1.3; 188 -1.1; 201 -1.0; 215 -1.0; 230 -0.8; 246 -0.6; 263 -0.4; 282 -0.2; 301 -0.2; 323 -0.0; 345 0.1; 369 0.2; 395 0.3; 423 0.5; 452 0.5; 484 0.5; 518 0.5; 554 0.6; 593 0.8; 635 0.8; 679 0.6; 726 0.6; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -1.0; 1336 -1.6; 1429 -2.4; 1529 -3.1; 1636 -3.9; 1751 -4.6; 1873 -5.2; 2004 -5.9; 2145 -6.1; 2295 -6.1; 2455 -5.5; 2627 -5.3; 2811 -5.0; 3008 -4.3; 3219 -4.2; 3444 -4.5; 3685 -6.9; 3943 -10.0; 4219 -7.9; 4514 -4.9; 4830 -4.4; 5168 -4.6; 5530 -6.0; 5917 -6.8; 6331 -3.8; 6775 -4.3; 7249 -5.9; 7756 -7.5; 8299 -9.4; 8880 -10.7; 9502 -10.6; 10167 -8.8; 10879 -5.5; 11640 -1.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-9.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 30 Hz    |  1.37 | 7.2 dB   |
| Peaking | 2099 Hz  |  1.96 | -5.7 dB  |
| Peaking | 4054 Hz  |  2.23 | -6.9 dB  |
| Peaking | 8959 Hz  |  2.32 | -11.1 dB |
| Peaking | 27146 Hz |  2.95 | -8.3 dB  |
| Peaking | 19 Hz    |  2.58 | 2.8 dB   |
| Peaking | 48 Hz    |  2.73 | 2.7 dB   |
| Peaking | 115 Hz   |  1.16 | -2.6 dB  |
| Peaking | 5795 Hz  | 12.75 | -3.9 dB  |
| Peaking | 12693 Hz |  3.93 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR%2080/Grado%20SR%2080.png)