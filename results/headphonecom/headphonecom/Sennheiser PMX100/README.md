# Sennheiser PMX100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.9; 22 -2.6; 23 -2.9; 25 -3.5; 26 -3.8; 28 -4.3; 30 -4.7; 32 -5.0; 35 -5.5; 37 -5.8; 40 -6.1; 42 -6.3; 45 -6.6; 49 -6.8; 52 -7.0; 56 -7.2; 59 -7.3; 64 -7.5; 68 -7.6; 73 -7.6; 78 -7.7; 83 -7.8; 89 -7.8; 95 -7.8; 102 -7.8; 109 -7.6; 117 -7.6; 125 -7.5; 134 -7.3; 143 -7.3; 153 -7.1; 164 -7.0; 175 -6.5; 188 -6.3; 201 -6.2; 215 -5.9; 230 -5.7; 246 -5.2; 263 -4.7; 282 -4.4; 301 -4.1; 323 -3.7; 345 -3.6; 369 -3.3; 395 -3.0; 423 -2.6; 452 -2.2; 484 -1.8; 518 -1.5; 554 -1.0; 593 -0.7; 635 -0.5; 679 -0.2; 726 -0.0; 777 0.1; 832 0.2; 890 0.1; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 -0.0; 1248 0.1; 1336 0.4; 1429 0.5; 1529 0.4; 1636 0.2; 1751 -0.2; 1873 -0.5; 2004 -0.4; 2145 0.7; 2295 2.1; 2455 3.2; 2627 4.1; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 3.2; 4219 -2.3; 4514 -1.8; 4830 3.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 2 Hz    | 1.84 | -1.0 dB |
| Peaking | 62 Hz   | 0.48 | -6.6 dB |
| Peaking | 184 Hz  | 0.67 | -4.1 dB |
| Peaking | 3088 Hz | 2.92 | 6.8 dB  |
| Peaking | 5848 Hz | 3.87 | 6.6 dB  |
| Peaking | 777 Hz  | 2.53 | 0.8 dB  |
| Peaking | 1935 Hz | 7.72 | -1.4 dB |
| Peaking | 3780 Hz | 7.14 | 4.5 dB  |
| Peaking | 4334 Hz | 5.46 | -6.8 dB |
| Peaking | 5017 Hz | 8.29 | 4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PMX100/Sennheiser%20PMX100.png)