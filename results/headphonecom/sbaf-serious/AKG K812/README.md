# AKG K812

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -0.6; 22 -1.0; 23 -1.1; 25 -1.4; 26 -1.5; 28 -1.7; 30 -1.9; 32 -2.0; 35 -2.2; 37 -2.3; 40 -2.4; 42 -2.5; 45 -2.6; 49 -2.8; 52 -2.9; 56 -3.0; 59 -3.1; 64 -3.4; 68 -3.5; 73 -3.5; 78 -3.6; 83 -3.7; 89 -3.9; 95 -4.1; 102 -4.2; 109 -4.5; 117 -4.7; 125 -4.9; 134 -5.0; 143 -5.2; 153 -5.3; 164 -5.3; 175 -5.2; 188 -5.3; 201 -5.3; 215 -5.3; 230 -5.3; 246 -5.1; 263 -5.0; 282 -4.9; 301 -4.6; 323 -4.5; 345 -4.2; 369 -4.0; 395 -3.9; 423 -3.7; 452 -3.5; 484 -3.3; 518 -3.0; 554 -2.8; 593 -2.5; 635 -2.1; 679 -1.8; 726 -1.4; 777 -1.0; 832 -0.6; 890 -0.5; 952 -0.3; 1019 -0.0; 1090 0.4; 1167 1.0; 1248 1.2; 1336 1.2; 1429 0.1; 1529 -1.0; 1636 -0.9; 1751 0.1; 1873 0.4; 2004 0.2; 2145 0.1; 2295 -0.2; 2455 1.7; 2627 5.2; 2811 2.4; 3008 -0.6; 3219 -0.8; 3444 -0.5; 3685 -2.5; 3943 -3.3; 4219 0.9; 4514 2.1; 4830 -0.1; 5168 -2.8; 5530 -5.4; 5917 -7.7; 6331 -7.0; 6775 -1.5; 7249 0.5; 7756 0.0; 8299 -1.9; 8880 -4.3; 9502 -6.4; 10167 -5.9; 10879 -2.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -1.9; 16326 -1.6; 17469 0.0; 18692 -0.0; 20000 -7.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.421499176158574dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 99 Hz    | 0.29 | -2.8 dB  |
| Peaking | 253 Hz   | 0.52 | -3.2 dB  |
| Peaking | 3858 Hz  | 0.54 | 4.8 dB   |
| Peaking | 5804 Hz  | 0.67 | -7.3 dB  |
| Peaking | 20029 Hz | 5.01 | -6.9 dB  |
| Peaking | 3890 Hz  | 4.17 | -5.9 dB  |
| Peaking | 4403 Hz  | 5.54 | 5.6 dB   |
| Peaking | 6088 Hz  | 3.31 | -12.5 dB |
| Peaking | 6977 Hz  | 1.26 | 10.1 dB  |
| Peaking | 9436 Hz  | 3.43 | -8.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K812/AKG%20K812.png)