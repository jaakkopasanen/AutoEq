# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.2dB
GraphicEQ: 10 -84; 20 6.7; 22 5.6; 23 5.1; 25 4.3; 26 3.9; 28 3.2; 30 2.6; 32 2.0; 35 0.9; 37 0.3; 40 -0.5; 42 -0.8; 45 -1.6; 49 -3.1; 52 -4.1; 56 -5.2; 59 -5.9; 64 -6.9; 68 -7.7; 73 -8.5; 78 -9.1; 83 -9.7; 89 -10.2; 95 -10.5; 102 -10.5; 109 -10.5; 117 -10.2; 125 -9.7; 134 -9.2; 143 -8.7; 153 -8.2; 164 -7.6; 175 -7.0; 188 -6.4; 201 -5.8; 215 -5.2; 230 -4.8; 246 -4.3; 263 -3.8; 282 -3.9; 301 -3.8; 323 -3.5; 345 -3.1; 369 -2.8; 395 -2.4; 423 -2.1; 452 -1.8; 484 -1.6; 518 -1.3; 554 -1.0; 593 -0.6; 635 -0.2; 679 0.0; 726 0.2; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 -0.0; 1090 0.0; 1167 0.1; 1248 0.5; 1336 0.9; 1429 1.3; 1529 1.5; 1636 2.2; 1751 2.3; 1873 1.6; 2004 1.7; 2145 1.6; 2295 1.8; 2455 1.9; 2627 1.8; 2811 1.6; 3008 1.4; 3219 1.4; 3444 0.6; 3685 -2.9; 3943 -2.8; 4219 0.2; 4514 0.9; 4830 -0.6; 5168 -1.4; 5530 -2.8; 5917 -4.7; 6331 -7.6; 6775 -8.9; 7249 -9.0; 7756 -8.4; 8299 -7.2; 8880 -5.8; 9502 -4.1; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.2dB` and instead set Global volume in the UI for both channels to **-72**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.2  | 8.5 dB   |
| Peaking | 72 Hz    | 0.55 | -4.2 dB  |
| Peaking | 97 Hz    | 0.55 | -10.5 dB |
| Peaking | 2062 Hz  | 0.97 | 2.3 dB   |
| Peaking | 7267 Hz  | 2.24 | -10.1 dB |
| Peaking | 3400 Hz  | 4.85 | 2.2 dB   |
| Peaking | 3786 Hz  | 5.88 | -5.4 dB  |
| Peaking | 4406 Hz  | 5.28 | 2.9 dB   |
| Peaking | 9271 Hz  | 3.93 | -2.8 dB  |
| Peaking | 10551 Hz | 2.27 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Grado%20GS1000/Grado%20GS1000.png)