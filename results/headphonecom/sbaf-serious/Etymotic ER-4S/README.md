# Etymotic ER-4S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.7; 64 5.5; 68 5.3; 73 5.1; 78 4.7; 83 4.4; 89 4.2; 95 4.0; 102 3.8; 109 3.6; 117 3.5; 125 3.2; 134 3.0; 143 2.8; 153 2.4; 164 2.3; 175 2.2; 188 2.1; 201 2.0; 215 2.0; 230 2.0; 246 2.0; 263 2.0; 282 2.0; 301 2.1; 323 2.2; 345 2.3; 369 2.2; 395 2.2; 423 2.1; 452 2.1; 484 2.2; 518 2.1; 554 2.2; 593 2.3; 635 2.3; 679 2.2; 726 2.1; 777 1.8; 832 1.5; 890 1.1; 952 0.4; 1019 -0.2; 1090 -0.9; 1167 -1.6; 1248 -2.3; 1336 -3.2; 1429 -4.1; 1529 -5.1; 1636 -5.9; 1751 -6.8; 1873 -7.8; 2004 -8.6; 2145 -9.0; 2295 -9.0; 2455 -8.4; 2627 -7.1; 2811 -5.5; 3008 -3.8; 3219 -2.2; 3444 -1.1; 3685 -0.9; 3943 -1.7; 4219 -2.8; 4514 -3.3; 4830 -2.4; 5168 -0.7; 5530 1.1; 5917 2.0; 6331 1.6; 6775 0.2; 7249 -2.4; 7756 -4.3; 8299 -4.4; 8880 -3.0; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -3.0; 16326 -7.5; 17469 -3.2; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.06 | 5.2 dB  |
| Peaking | 1669 Hz  | 2.87 | -3.6 dB |
| Peaking | 2276 Hz  | 2.12 | -8.7 dB |
| Peaking | 8387 Hz  | 3.52 | -3.2 dB |
| Peaking | 16195 Hz | 4.24 | -4.9 dB |
| Peaking | 170 Hz   | 1.58 | -1.4 dB |
| Peaking | 634 Hz   | 1.51 | 2.1 dB  |
| Peaking | 4563 Hz  | 6.67 | -2.8 dB |
| Peaking | 5963 Hz  | 5.79 | 3.3 dB  |
| Peaking | 16616 Hz | 5.53 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4S/Etymotic%20ER-4S.png)