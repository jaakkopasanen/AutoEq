# Sony MDR-ZX1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.4; 68 4.9; 73 4.2; 78 3.8; 83 3.3; 89 2.9; 95 2.6; 102 2.2; 109 1.8; 117 1.1; 125 0.4; 134 -0.1; 143 -0.4; 153 -0.4; 164 0.2; 175 0.7; 188 0.8; 201 1.1; 215 1.3; 230 1.7; 246 1.8; 263 1.6; 282 1.7; 301 1.4; 323 0.7; 345 0.2; 369 -0.3; 395 -0.5; 423 -0.6; 452 -0.6; 484 -0.7; 518 -0.7; 554 -0.5; 593 -0.1; 635 0.1; 679 0.1; 726 -0.1; 777 0.0; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.6; 1336 -1.3; 1429 -2.2; 1529 -3.1; 1636 -4.0; 1751 -4.7; 1873 -4.8; 2004 -4.6; 2145 -4.2; 2295 -3.5; 2455 -2.6; 2627 -1.6; 2811 -0.7; 3008 0.3; 3219 1.4; 3444 3.5; 3685 5.3; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.4; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.6; 8299 -4.3; 8880 -6.6; 9502 -6.6; 10167 -3.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.62 | 6.9 dB   |
| Peaking | 259 Hz  | 4.38 | 1.6 dB   |
| Peaking | 2111 Hz | 1.36 | -7.6 dB  |
| Peaking | 4931 Hz | 0.71 | 8.2 dB   |
| Peaking | 8992 Hz | 2.86 | -11.1 dB |
| Peaking | 66 Hz   | 3.36 | 1.2 dB   |
| Peaking | 140 Hz  | 4.3  | -1.8 dB  |
| Peaking | 469 Hz  | 2.97 | -1.0 dB  |
| Peaking | 1153 Hz | 1.14 | 0.8 dB   |
| Peaking | 1627 Hz | 4.34 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX1000/Sony%20MDR-ZX1000.png)