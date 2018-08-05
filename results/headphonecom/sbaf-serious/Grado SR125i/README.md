# Grado SR125i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.4; 59 4.8; 64 3.9; 68 3.2; 73 2.5; 78 1.9; 83 1.4; 89 0.8; 95 0.3; 102 -0.2; 109 -0.5; 117 -0.8; 125 -1.1; 134 -1.3; 143 -1.2; 153 -1.2; 164 -1.1; 175 -1.0; 188 -0.9; 201 -0.8; 215 -0.5; 230 -0.3; 246 -0.1; 263 0.1; 282 0.6; 301 0.5; 323 -0.4; 345 -0.3; 369 0.0; 395 0.1; 423 0.3; 452 0.3; 484 0.3; 518 0.3; 554 0.6; 593 0.7; 635 0.8; 679 0.6; 726 0.6; 777 0.7; 832 0.6; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.4; 1529 -3.1; 1636 -3.9; 1751 -4.6; 1873 -5.2; 2004 -5.7; 2145 -6.1; 2295 -6.2; 2455 -5.2; 2627 -4.8; 2811 -3.3; 3008 -2.5; 3219 -1.8; 3444 -1.6; 3685 -1.7; 3943 -1.6; 4219 -1.7; 4514 -3.9; 4830 -5.1; 5168 -4.4; 5530 -7.8; 5917 -6.8; 6331 -6.2; 6775 -6.7; 7249 -6.0; 7756 -6.2; 8299 -8.2; 8880 -10.1; 9502 -9.7; 10167 -6.2; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.1; 18692 -3.2; 20000 -8.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 71 Hz    | 0.22 | 11.0 dB  |
| Peaking | 125 Hz   | 0.5  | -11.2 dB |
| Peaking | 2096 Hz  | 1.88 | -6.3 dB  |
| Peaking | 5932 Hz  | 2.15 | -6.4 dB  |
| Peaking | 9054 Hz  | 3.76 | -10.0 dB |
| Peaking | 363 Hz   | 3.71 | -0.7 dB  |
| Peaking | 811 Hz   | 2.97 | 0.6 dB   |
| Peaking | 3862 Hz  | 6.12 | 0.9 dB   |
| Peaking | 11843 Hz | 4.58 | 2.1 dB   |
| Peaking | 19922 Hz | 3.15 | -8.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)