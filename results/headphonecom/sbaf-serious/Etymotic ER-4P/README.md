# Etymotic ER-4P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.8; 56 5.7; 59 5.6; 64 5.4; 68 5.3; 73 5.3; 78 5.1; 83 4.7; 89 4.4; 95 4.0; 102 3.5; 109 3.0; 117 2.5; 125 1.9; 134 1.4; 143 1.0; 153 0.8; 164 0.6; 175 0.5; 188 0.5; 201 0.4; 215 0.5; 230 0.5; 246 0.5; 263 0.6; 282 0.7; 301 0.7; 323 0.9; 345 1.0; 369 1.2; 395 1.2; 423 1.4; 452 1.2; 484 1.2; 518 1.1; 554 1.3; 593 1.6; 635 1.6; 679 1.4; 726 1.4; 777 1.4; 832 1.2; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -1.8; 1336 -2.5; 1429 -3.3; 1529 -3.9; 1636 -4.4; 1751 -4.8; 1873 -4.8; 2004 -4.9; 2145 -4.8; 2295 -4.4; 2455 -3.6; 2627 -2.7; 2811 -1.1; 3008 0.9; 3219 2.9; 3444 4.4; 3685 5.3; 3943 5.2; 4219 4.0; 4514 3.2; 4830 3.7; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.9; 15258 -3.0; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.42 | 6.5 dB  |
| Peaking | 2023 Hz  | 1.63 | -6.1 dB |
| Peaking | 5792 Hz  | 3.08 | 6.3 dB  |
| Peaking | 3671 Hz  | 2.89 | 6.1 dB  |
| Peaking | 14941 Hz | 6.3  | -3.9 dB |
| Peaking | 168 Hz   | 2.33 | -1.2 dB |
| Peaking | 406 Hz   | 2.88 | 0.7 dB  |
| Peaking | 717 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1422 Hz  | 3.46 | -1.4 dB |
| Peaking | 8143 Hz  | 5.43 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4P/Etymotic%20ER-4P.png)