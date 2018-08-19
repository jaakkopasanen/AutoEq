# Etymotic ER-4P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.8; 42 5.6; 45 5.4; 49 5.1; 52 5.0; 56 4.7; 59 4.5; 64 4.1; 68 3.9; 73 3.7; 78 3.5; 83 3.1; 89 2.8; 95 2.6; 102 2.4; 109 2.3; 117 2.1; 125 1.9; 134 1.7; 143 1.5; 153 1.3; 164 1.2; 175 1.0; 188 1.0; 201 0.9; 215 0.9; 230 0.8; 246 0.8; 263 0.8; 282 0.8; 301 0.9; 323 1.0; 345 1.1; 369 1.3; 395 1.3; 423 1.4; 452 1.2; 484 1.3; 518 1.2; 554 1.3; 593 1.5; 635 1.5; 679 1.5; 726 1.5; 777 1.4; 832 1.2; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -1.8; 1336 -2.5; 1429 -3.3; 1529 -3.9; 1636 -4.4; 1751 -4.7; 1873 -4.9; 2004 -4.9; 2145 -4.8; 2295 -4.4; 2455 -3.7; 2627 -2.6; 2811 -1.1; 3008 0.8; 3219 2.9; 3444 4.5; 3685 5.4; 3943 5.0; 4219 4.0; 4514 3.3; 4830 3.8; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.8; 15258 -2.8; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.4  | 6.2 dB   |
| Peaking | 893 Hz   | 0.64 | 5.7 dB   |
| Peaking | 2268 Hz  | 0.45 | -10.2 dB |
| Peaking | 3570 Hz  | 1.68 | 11.5 dB  |
| Peaking | 5847 Hz  | 2.22 | 8.2 dB   |
| Peaking | 1587 Hz  | 5.52 | -0.1 dB  |
| Peaking | 7698 Hz  | 7.7  | -1.0 dB  |
| Peaking | 14024 Hz | 1.1  | 1.1 dB   |
| Peaking | 14855 Hz | 5.35 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4P/Etymotic%20ER-4P.png)