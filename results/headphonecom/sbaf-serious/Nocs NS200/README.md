# Nocs NS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -10.1; 22 -9.9; 23 -9.8; 25 -9.6; 26 -9.5; 28 -9.3; 30 -9.1; 32 -8.9; 35 -8.7; 37 -8.5; 40 -8.3; 42 -8.2; 45 -8.0; 49 -7.8; 52 -7.7; 56 -7.5; 59 -7.5; 64 -7.4; 68 -7.3; 73 -7.3; 78 -7.3; 83 -7.2; 89 -7.1; 95 -7.1; 102 -7.0; 109 -6.9; 117 -6.9; 125 -6.8; 134 -6.7; 143 -6.7; 153 -6.6; 164 -6.5; 175 -6.4; 188 -6.2; 201 -6.1; 215 -5.8; 230 -5.6; 246 -5.3; 263 -5.1; 282 -4.7; 301 -4.4; 323 -4.0; 345 -3.6; 369 -3.2; 395 -2.9; 423 -2.5; 452 -2.2; 484 -1.8; 518 -1.5; 554 -1.1; 593 -0.7; 635 -0.3; 679 -0.0; 726 0.3; 777 0.4; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.2; 1336 -1.7; 1429 -2.1; 1529 -2.6; 1636 -3.1; 1751 -3.5; 1873 -3.6; 2004 -3.9; 2145 -4.1; 2295 -4.2; 2455 -4.0; 2627 -3.6; 2811 -2.5; 3008 -0.8; 3219 1.3; 3444 3.1; 3685 4.0; 3943 3.4; 4219 1.9; 4514 0.4; 4830 -0.6; 5168 -1.4; 5530 -2.5; 5917 -3.2; 6331 -1.7; 6775 0.5; 7249 1.1; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.099536150790273dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.13 | -9.3 dB |
| Peaking | 200 Hz  | 0.81 | -4.0 dB |
| Peaking | 2261 Hz | 1.56 | -4.9 dB |
| Peaking | 3650 Hz | 3.41 | 5.8 dB  |
| Peaking | 5715 Hz | 5.9  | -3.5 dB |
| Peaking | 13 Hz   | 0.43 | -0.9 dB |
| Peaking | 44 Hz   | 1.56 | 0.8 dB  |
| Peaking | 814 Hz  | 2.41 | 1.5 dB  |
| Peaking | 1552 Hz | 4.25 | -0.9 dB |
| Peaking | 7093 Hz | 9.57 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)