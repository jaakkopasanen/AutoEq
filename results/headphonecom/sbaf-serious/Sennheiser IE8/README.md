# Sennheiser IE8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.6; 23 -2.8; 25 -3.4; 26 -3.6; 28 -4.0; 30 -4.4; 32 -4.7; 35 -5.1; 37 -5.4; 40 -5.7; 42 -5.9; 45 -6.2; 49 -6.5; 52 -6.7; 56 -6.9; 59 -7.1; 64 -7.3; 68 -7.5; 73 -7.7; 78 -7.9; 83 -8.0; 89 -8.5; 95 -9.0; 102 -9.3; 109 -9.7; 117 -10.3; 125 -10.8; 134 -11.1; 143 -11.4; 153 -11.5; 164 -11.4; 175 -11.3; 188 -11.1; 201 -10.9; 215 -10.5; 230 -10.2; 246 -9.9; 263 -9.5; 282 -9.0; 301 -8.5; 323 -7.9; 345 -7.2; 369 -6.6; 395 -6.1; 423 -5.6; 452 -5.2; 484 -4.8; 518 -4.2; 554 -3.4; 593 -2.7; 635 -2.1; 679 -1.7; 726 -1.3; 777 -0.7; 832 -0.4; 890 -0.3; 952 -0.3; 1019 0.0; 1090 -0.0; 1167 -0.4; 1248 -0.8; 1336 -1.5; 1429 -2.3; 1529 -3.0; 1636 -3.5; 1751 -3.8; 1873 -3.7; 2004 -3.5; 2145 -3.4; 2295 -2.9; 2455 -2.3; 2627 -1.8; 2811 -1.0; 3008 0.1; 3219 0.8; 3444 1.4; 3685 1.0; 3943 -0.0; 4219 -1.3; 4514 -0.8; 4830 1.5; 5168 3.4; 5530 3.8; 5917 2.4; 6331 1.3; 6775 1.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -0.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.3; 15258 -1.5; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 2 Hz    | 1.93 | -0.7 dB |
| Peaking | 78 Hz   | 0.32 | -5.8 dB |
| Peaking | 201 Hz  | 0.67 | -7.4 dB |
| Peaking | 1908 Hz | 2.49 | -3.9 dB |
| Peaking | 5475 Hz | 4.55 | 4.1 dB  |
| Peaking | 458 Hz  | 2    | -1.1 dB |
| Peaking | 1065 Hz | 1.15 | 2.6 dB  |
| Peaking | 1409 Hz | 1.45 | -2.0 dB |
| Peaking | 3445 Hz | 5.71 | 1.9 dB  |
| Peaking | 4302 Hz | 8.87 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20IE8/Sennheiser%20IE8.png)