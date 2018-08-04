# Sennheiser PMX100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.7; 22 1.9; 23 1.6; 25 1.0; 26 0.7; 28 0.3; 30 -0.1; 32 -0.5; 35 -1.0; 37 -1.2; 40 -1.5; 42 -1.7; 45 -2.0; 49 -2.3; 52 -2.5; 56 -2.7; 59 -2.8; 64 -3.0; 68 -3.2; 73 -3.2; 78 -3.4; 83 -3.6; 89 -3.8; 95 -4.1; 102 -4.3; 109 -4.4; 117 -4.7; 125 -5.1; 134 -5.2; 143 -5.4; 153 -5.4; 164 -5.4; 175 -5.0; 188 -4.8; 201 -4.7; 215 -4.5; 230 -4.2; 246 -3.8; 263 -3.3; 282 -3.0; 301 -2.8; 323 -2.4; 345 -2.1; 369 -1.9; 395 -1.7; 423 -1.4; 452 -1.2; 484 -1.1; 518 -0.9; 554 -0.5; 593 -0.3; 635 -0.1; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.3; 1636 -2.9; 1751 -3.3; 1873 -3.4; 2004 -3.3; 2145 -2.3; 2295 -1.0; 2455 0.3; 2627 1.1; 2811 3.2; 3008 5.3; 3219 6.0; 3444 6.0; 3685 5.6; 3943 0.9; 4219 -5.9; 4514 -6.6; 4830 -2.1; 5168 2.3; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 141 Hz  | 0.61 | -5.4 dB  |
| Peaking | 1916 Hz | 2.35 | -4.7 dB  |
| Peaking | 3496 Hz | 2.17 | 9.4 dB   |
| Peaking | 4392 Hz | 4.53 | -13.4 dB |
| Peaking | 5855 Hz | 3.51 | 7.2 dB   |
| Peaking | 17 Hz   | 1.43 | 3.4 dB   |
| Peaking | 47 Hz   | 1.7  | -1.1 dB  |
| Peaking | 807 Hz  | 1.66 | 0.8 dB   |
| Peaking | 1523 Hz | 6.6  | -0.7 dB  |
| Peaking | 8234 Hz | 4.77 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX100/Sennheiser%20PMX100.png)