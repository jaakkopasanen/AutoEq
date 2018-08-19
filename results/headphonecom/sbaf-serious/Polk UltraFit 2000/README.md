# Polk UltraFit 2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 5.0; 64 3.9; 68 3.0; 73 2.1; 78 1.3; 83 0.7; 89 0.0; 95 -0.4; 102 -0.8; 109 -1.2; 117 -1.3; 125 -1.6; 134 -1.6; 143 -1.8; 153 -1.7; 164 -1.6; 175 -1.4; 188 -1.1; 201 -0.9; 215 -0.6; 230 -0.4; 246 -0.1; 263 0.1; 282 0.3; 301 1.1; 323 2.3; 345 2.4; 369 2.7; 395 3.3; 423 3.9; 452 4.3; 484 4.5; 518 4.8; 554 5.1; 593 5.5; 635 5.7; 679 6.0; 726 5.8; 777 5.4; 832 4.5; 890 3.0; 952 1.1; 1019 -0.4; 1090 -1.8; 1167 -2.6; 1248 -3.1; 1336 -3.6; 1429 -4.0; 1529 -4.3; 1636 -4.6; 1751 -4.6; 1873 -5.0; 2004 -4.6; 2145 -3.5; 2295 -2.2; 2455 -0.2; 2627 1.5; 2811 2.7; 3008 3.9; 3219 4.2; 3444 3.8; 3685 2.9; 3943 2.3; 4219 3.1; 4514 5.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.5; 8880 -5.6; 9502 -5.8; 10167 -3.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.109994102968974dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk UltraFit 2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1.06 | 7.2 dB   |
| Peaking | 663 Hz  | 1.3  | 7.6 dB   |
| Peaking | 1624 Hz | 1.05 | -7.9 dB  |
| Peaking | 5220 Hz | 0.6  | 7.2 dB   |
| Peaking | 9117 Hz | 2.68 | -10.3 dB |
| Peaking | 57 Hz   | 2.57 | 3.2 dB   |
| Peaking | 136 Hz  | 0.74 | -2.5 dB  |
| Peaking | 380 Hz  | 2.29 | 1.8 dB   |
| Peaking | 3022 Hz | 5.22 | 2.3 dB   |
| Peaking | 3979 Hz | 7.03 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20UltraFit%202000/Polk%20UltraFit%202000.png)