# Sennheiser EH250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.3; 42 4.8; 45 4.2; 49 3.5; 52 2.9; 56 2.1; 59 1.6; 64 1.1; 68 1.0; 73 0.6; 78 0.2; 83 -0.1; 89 -0.2; 95 -0.3; 102 -0.3; 109 -0.3; 117 -0.1; 125 0.2; 134 1.5; 143 2.5; 153 2.9; 164 3.2; 175 3.4; 188 3.6; 201 4.0; 215 4.5; 230 4.8; 246 5.0; 263 4.9; 282 4.3; 301 2.3; 323 1.1; 345 1.7; 369 2.1; 395 2.4; 423 2.4; 452 2.1; 484 1.4; 518 0.7; 554 0.6; 593 0.6; 635 0.5; 679 0.3; 726 0.4; 777 0.7; 832 0.6; 890 0.2; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.1; 1429 -0.1; 1529 -0.2; 1636 -0.3; 1751 -0.2; 1873 0.2; 2004 0.5; 2145 0.8; 2295 1.5; 2455 1.6; 2627 2.0; 2811 2.9; 3008 4.6; 3219 6.0; 3444 6.0; 3685 4.4; 3943 -0.7; 4219 -2.3; 4514 0.2; 4830 2.7; 5168 3.1; 5530 4.9; 5917 5.9; 6331 4.0; 6775 0.3; 7249 -1.3; 7756 -0.6; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.0; 13327 -2.7; 14260 -4.4; 15258 -3.9; 16326 -3.0; 17469 -2.3; 18692 -1.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.16 | 6.9 dB  |
| Peaking | 234 Hz   | 1.56 | 5.0 dB  |
| Peaking | 4351 Hz  | 0.7  | 3.2 dB  |
| Peaking | 12211 Hz | 2.47 | 5.0 dB  |
| Peaking | 13691 Hz | 1.09 | -6.5 dB |
| Peaking | 96 Hz    | 2.97 | -1.6 dB |
| Peaking | 3439 Hz  | 4.55 | 5.5 dB  |
| Peaking | 4128 Hz  | 4.82 | -7.1 dB |
| Peaking | 5971 Hz  | 4.23 | 5.0 dB  |
| Peaking | 7083 Hz  | 5.03 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH250/Sennheiser%20EH250.png)