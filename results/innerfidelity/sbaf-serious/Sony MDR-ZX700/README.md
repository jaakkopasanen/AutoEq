# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.0; 52 4.1; 56 2.9; 59 2.1; 64 1.0; 68 0.4; 73 -0.1; 78 -0.5; 83 -0.8; 89 -1.0; 95 -1.7; 102 -2.4; 109 -2.4; 117 -2.6; 125 -3.5; 134 -3.9; 143 -4.1; 153 -4.0; 164 -3.1; 175 -2.8; 188 -3.5; 201 -3.6; 215 -3.5; 230 -3.3; 246 -3.3; 263 -3.1; 282 -2.8; 301 -2.7; 323 -3.7; 345 -3.2; 369 -2.6; 395 -2.3; 423 -2.1; 452 -1.9; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.2; 635 0.2; 679 0.5; 726 0.5; 777 0.7; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -1.1; 1336 -2.0; 1429 -3.1; 1529 -4.2; 1636 -5.6; 1751 -6.9; 1873 -7.6; 2004 -7.4; 2145 -6.4; 2295 -5.0; 2455 -3.6; 2627 -2.6; 2811 -1.8; 3008 -0.7; 3219 0.1; 3444 1.4; 3685 3.7; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.3; 5530 3.7; 5917 3.9; 6331 5.4; 6775 3.9; 7249 1.3; 7756 -2.0; 8299 -7.5; 8880 -10.7; 9502 -9.6; 10167 -4.3; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.5  | 7.5 dB   |
| Peaking | 1958 Hz | 1.98 | -8.3 dB  |
| Peaking | 4366 Hz | 2.28 | 7.1 dB   |
| Peaking | 6530 Hz | 3.29 | 5.2 dB   |
| Peaking | 8935 Hz | 4.17 | -13.0 dB |
| Peaking | 20 Hz   | 3    | 3.2 dB   |
| Peaking | 47 Hz   | 3.72 | 3.1 dB   |
| Peaking | 133 Hz  | 1.31 | -3.7 dB  |
| Peaking | 228 Hz  | 2.3  | -2.0 dB  |
| Peaking | 348 Hz  | 2.67 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)