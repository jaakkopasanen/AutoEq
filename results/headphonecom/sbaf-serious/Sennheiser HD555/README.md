# Sennheiser HD555

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.5; 37 5.2; 40 4.8; 42 4.6; 45 4.2; 49 3.9; 52 3.7; 56 3.7; 59 3.7; 64 3.6; 68 4.3; 73 4.1; 78 3.1; 83 2.5; 89 2.0; 95 1.6; 102 1.1; 109 0.6; 117 0.3; 125 -0.1; 134 -0.6; 143 -0.9; 153 -1.0; 164 -0.9; 175 -1.1; 188 -1.2; 201 -1.3; 215 -1.4; 230 -1.3; 246 -1.3; 263 -1.3; 282 -1.2; 301 -1.1; 323 -0.9; 345 -0.8; 369 -0.7; 395 -0.5; 423 -0.2; 452 -0.1; 484 -0.2; 518 -0.1; 554 -0.0; 593 0.6; 635 0.4; 679 0.3; 726 0.3; 777 0.3; 832 0.4; 890 0.3; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.6; 1336 0.9; 1429 1.2; 1529 1.5; 1636 1.8; 1751 1.3; 1873 0.8; 2004 0.7; 2145 0.5; 2295 0.3; 2455 0.5; 2627 0.8; 2811 0.8; 3008 0.2; 3219 -0.7; 3444 -0.7; 3685 -0.1; 3943 2.0; 4219 3.4; 4514 0.5; 4830 -0.1; 5168 2.2; 5530 5.2; 5917 5.9; 6331 4.2; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.6; 18692 -3.5; 20000 -2.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.97 | 6.6 dB  |
| Peaking | 69 Hz    | 3.24 | 3.1 dB  |
| Peaking | 1587 Hz  | 3.06 | 1.0 dB  |
| Peaking | 1616 Hz  | 2.77 | 0.7 dB  |
| Peaking | 5926 Hz  | 4.08 | 6.2 dB  |
| Peaking | 215 Hz   | 1.28 | -1.7 dB |
| Peaking | 2717 Hz  | 6.18 | 1.0 dB  |
| Peaking | 4132 Hz  | 7.54 | 6.0 dB  |
| Peaking | 4038 Hz  | 2.57 | -2.8 dB |
| Peaking | 19125 Hz | 2.18 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD555/Sennheiser%20HD555.png)