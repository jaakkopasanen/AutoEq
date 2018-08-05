# Etymotic ER-4S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.8; 95 5.4; 102 4.8; 109 4.4; 117 3.8; 125 3.2; 134 2.7; 143 2.4; 153 1.9; 164 1.8; 175 1.7; 188 1.6; 201 1.6; 215 1.6; 230 1.7; 246 1.7; 263 1.7; 282 1.8; 301 1.9; 323 2.0; 345 2.2; 369 2.1; 395 2.1; 423 2.1; 452 2.1; 484 2.1; 518 2.0; 554 2.2; 593 2.4; 635 2.3; 679 2.1; 726 2.0; 777 1.9; 832 1.6; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.9; 1167 -1.6; 1248 -2.3; 1336 -3.2; 1429 -4.1; 1529 -5.0; 1636 -5.9; 1751 -6.9; 1873 -7.8; 2004 -8.6; 2145 -9.0; 2295 -9.0; 2455 -8.3; 2627 -7.2; 2811 -5.6; 3008 -3.7; 3219 -2.2; 3444 -1.2; 3685 -0.9; 3943 -1.4; 4219 -2.9; 4514 -3.4; 4830 -2.5; 5168 -0.6; 5530 1.1; 5917 1.9; 6331 1.6; 6775 0.3; 7249 -2.3; 7756 -4.3; 8299 -4.6; 8880 -3.1; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -3.2; 16326 -7.6; 17469 -3.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.09 | 6.3 dB  |
| Peaking | 2302 Hz  | 2.18 | -8.6 dB |
| Peaking | 1699 Hz  | 2.91 | -3.9 dB |
| Peaking | 31183 Hz | 3.9  | -3.6 dB |
| Peaking | 31713 Hz | 4.71 | -5.3 dB |
| Peaking | 168 Hz   | 2.4  | -1.8 dB |
| Peaking | 604 Hz   | 1.43 | 2.3 dB  |
| Peaking | 4584 Hz  | 4.36 | -4.6 dB |
| Peaking | 6535 Hz  | 1.22 | 4.7 dB  |
| Peaking | 7992 Hz  | 3.08 | -8.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4S/Etymotic%20ER-4S.png)