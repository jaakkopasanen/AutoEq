# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.4; 59 4.8; 64 3.8; 68 3.4; 73 3.2; 78 3.6; 83 3.7; 89 3.5; 95 2.2; 102 0.6; 109 -0.3; 117 -1.0; 125 -1.5; 134 -2.0; 143 -2.2; 153 -2.3; 164 -1.3; 175 -1.6; 188 -2.2; 201 -2.4; 215 -2.6; 230 -2.7; 246 -2.7; 263 -2.6; 282 -2.6; 301 -3.1; 323 -3.4; 345 -4.5; 369 -3.9; 395 -3.6; 423 -3.4; 452 -3.3; 484 -3.1; 518 -2.8; 554 -2.1; 593 -1.3; 635 -0.7; 679 -0.3; 726 -0.1; 777 -0.1; 832 0.1; 890 0.1; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.5; 1529 -2.5; 1636 -3.6; 1751 -5.1; 1873 -6.0; 2004 -7.2; 2145 -7.5; 2295 -7.0; 2455 -6.0; 2627 -5.3; 2811 -4.6; 3008 -3.4; 3219 -1.8; 3444 -0.2; 3685 2.3; 3943 5.4; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.1; 5530 3.0; 5917 4.2; 6331 3.9; 6775 3.6; 7249 1.0; 7756 -4.7; 8299 -10.0; 8880 -11.3; 9502 -8.2; 10167 -3.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 35 Hz   | 0.94 | 7.2 dB   |
| Peaking | 2282 Hz | 1.53 | -8.3 dB  |
| Peaking | 6719 Hz | 1.14 | 7.0 dB   |
| Peaking | 4229 Hz | 3.36 | 6.2 dB   |
| Peaking | 8633 Hz | 3.4  | -17.3 dB |
| Peaking | 87 Hz   | 1.66 | 3.1 dB   |
| Peaking | 124 Hz  | 1.78 | -3.2 dB  |
| Peaking | 215 Hz  | 1.73 | -1.3 dB  |
| Peaking | 389 Hz  | 1.3  | -3.8 dB  |
| Peaking | 953 Hz  | 1.38 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)