# Denon AH-C560R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -4.6; 22 -5.0; 23 -5.2; 25 -5.5; 26 -5.7; 28 -5.9; 30 -6.1; 32 -6.3; 35 -6.6; 37 -6.7; 40 -6.8; 42 -6.9; 45 -7.0; 49 -7.2; 52 -7.2; 56 -7.4; 59 -7.5; 64 -7.6; 68 -7.7; 73 -7.8; 78 -7.9; 83 -7.9; 89 -8.1; 95 -8.5; 102 -8.9; 109 -9.3; 117 -9.7; 125 -10.2; 134 -10.4; 143 -10.6; 153 -10.7; 164 -10.6; 175 -10.5; 188 -10.3; 201 -10.1; 215 -9.7; 230 -9.4; 246 -9.1; 263 -8.7; 282 -8.3; 301 -7.8; 323 -7.3; 345 -6.7; 369 -6.2; 395 -5.7; 423 -5.1; 452 -4.7; 484 -4.3; 518 -3.9; 554 -3.1; 593 -2.7; 635 -2.8; 679 -2.3; 726 -1.8; 777 -1.2; 832 -1.0; 890 -0.8; 952 -0.3; 1019 0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.8; 1636 -2.1; 1751 -2.2; 1873 -2.1; 2004 -2.1; 2145 -2.0; 2295 -1.9; 2455 -1.9; 2627 -2.2; 2811 -2.5; 3008 -2.4; 3219 -2.3; 3444 -1.8; 3685 -1.6; 3943 -1.9; 4219 -3.7; 4514 -5.3; 4830 -6.3; 5168 -7.2; 5530 -8.5; 5917 -8.6; 6331 -6.5; 6775 -4.7; 7249 -4.0; 7756 -4.7; 8299 -6.9; 8880 -8.7; 9502 -7.9; 10167 -3.7; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.5; 15258 -2.9; 16326 -0.8; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.6dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 5 Hz     | 1.86 | -3.8 dB |
| Peaking | 34 Hz    | 0.45 | -5.2 dB |
| Peaking | 180 Hz   | 0.53 | -9.8 dB |
| Peaking | 5526 Hz  | 1.79 | -8.0 dB |
| Peaking | 9038 Hz  | 4.88 | -8.1 dB |
| Peaking | 1046 Hz  | 1.25 | 3.6 dB  |
| Peaking | 1387 Hz  | 0.65 | -2.9 dB |
| Peaking | 3833 Hz  | 5.46 | 2.0 dB  |
| Peaking | 11499 Hz | 4.06 | 1.8 dB  |
| Peaking | 15181 Hz | 5.77 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)