# Etymotic ER-6i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.9; 22 5.8; 23 5.8; 25 5.7; 26 5.6; 28 5.6; 30 5.5; 32 5.5; 35 5.5; 37 5.5; 40 5.4; 42 5.4; 45 5.3; 49 5.3; 52 5.3; 56 5.3; 59 5.2; 64 5.0; 68 4.9; 73 4.8; 78 4.6; 83 4.5; 89 4.2; 95 3.8; 102 3.2; 109 2.8; 117 2.2; 125 1.6; 134 1.1; 143 0.8; 153 0.6; 164 0.4; 175 0.3; 188 0.2; 201 0.2; 215 0.2; 230 0.3; 246 0.3; 263 0.3; 282 0.4; 301 0.5; 323 0.7; 345 0.7; 369 0.7; 395 0.7; 423 0.7; 452 0.8; 484 0.7; 518 0.8; 554 1.1; 593 1.4; 635 1.3; 679 1.2; 726 1.2; 777 1.2; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -1.9; 1429 -2.5; 1529 -2.9; 1636 -3.5; 1751 -4.1; 1873 -4.4; 2004 -4.4; 2145 -4.3; 2295 -3.9; 2455 -3.1; 2627 -2.5; 2811 -1.4; 3008 0.0; 3219 1.3; 3444 2.4; 3685 2.7; 3943 2.3; 4219 0.8; 4514 0.1; 4830 0.8; 5168 2.9; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.48 | 5.7 dB  |
| Peaking | 75 Hz   | 1.39 | 2.7 dB  |
| Peaking | 2010 Hz | 1.81 | -5.0 dB |
| Peaking | 3543 Hz | 4.48 | 3.6 dB  |
| Peaking | 6003 Hz | 4    | 6.7 dB  |
| Peaking | 172 Hz  | 2.35 | -0.7 dB |
| Peaking | 716 Hz  | 1.31 | 1.6 dB  |
| Peaking | 1364 Hz | 2.48 | -0.9 dB |
| Peaking | 357 Hz  | 3.06 | 0.3 dB  |
| Peaking | 8173 Hz | 5.19 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i/Etymotic%20ER-6i.png)