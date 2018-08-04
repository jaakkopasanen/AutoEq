# Sennheiser EH350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.7; 59 5.1; 64 4.0; 68 3.4; 73 3.0; 78 2.6; 83 2.1; 89 1.5; 95 1.0; 102 0.4; 109 0.2; 117 0.0; 125 -0.3; 134 -0.1; 143 0.6; 153 0.6; 164 0.3; 175 0.3; 188 0.1; 201 0.1; 215 -0.1; 230 -0.0; 246 -0.1; 263 -0.2; 282 -0.3; 301 -0.4; 323 -0.5; 345 -0.6; 369 -0.6; 395 -0.5; 423 -0.5; 452 -0.5; 484 -0.2; 518 0.1; 554 0.6; 593 0.5; 635 0.8; 679 1.2; 726 0.7; 777 0.2; 832 -0.0; 890 0.0; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.4; 1248 0.2; 1336 0.6; 1429 0.9; 1529 1.2; 1636 1.4; 1751 2.1; 1873 3.1; 2004 3.5; 2145 4.0; 2295 4.3; 2455 4.5; 2627 4.3; 2811 4.2; 3008 3.8; 3219 3.1; 3444 3.4; 3685 5.5; 3943 6.0; 4219 6.0; 4514 1.9; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.7; 7249 -0.1; 7756 -2.0; 8299 -1.2; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -1.2; 14260 -2.3; 15258 -0.4; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.77 | 7.0 dB  |
| Peaking | 2384 Hz  | 1.84 | 4.3 dB  |
| Peaking | 3907 Hz  | 4.79 | 4.1 dB  |
| Peaking | 5960 Hz  | 2.2  | 6.8 dB  |
| Peaking | 7726 Hz  | 3.71 | -4.6 dB |
| Peaking | 55 Hz    | 4.17 | 1.5 dB  |
| Peaking | 114 Hz   | 3.29 | -1.3 dB |
| Peaking | 530 Hz   | 0.83 | -1.2 dB |
| Peaking | 624 Hz   | 2.31 | 1.9 dB  |
| Peaking | 14082 Hz | 5.69 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20EH350/Sennheiser%20EH350.png)