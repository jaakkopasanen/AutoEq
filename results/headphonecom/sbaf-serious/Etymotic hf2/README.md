# Etymotic hf2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.7; 37 5.6; 40 5.5; 42 5.4; 45 5.3; 49 5.1; 52 5.1; 56 5.0; 59 4.9; 64 4.7; 68 4.6; 73 4.6; 78 4.3; 83 4.0; 89 3.7; 95 3.3; 102 2.8; 109 2.3; 117 1.8; 125 1.2; 134 0.7; 143 0.4; 153 0.1; 164 -0.1; 175 -0.1; 188 -0.2; 201 -0.2; 215 -0.2; 230 -0.1; 246 -0.1; 263 -0.1; 282 -0.0; 301 0.1; 323 0.2; 345 0.4; 369 0.6; 395 0.8; 423 0.9; 452 1.0; 484 1.0; 518 0.9; 554 0.9; 593 1.1; 635 1.2; 679 1.0; 726 1.1; 777 1.2; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.5; 1336 -2.0; 1429 -2.6; 1529 -3.1; 1636 -3.5; 1751 -3.7; 1873 -3.6; 2004 -3.5; 2145 -3.3; 2295 -2.9; 2455 -2.1; 2627 -1.3; 2811 -0.1; 3008 1.7; 3219 3.2; 3444 4.7; 3685 5.5; 3943 5.6; 4219 4.5; 4514 4.0; 4830 4.6; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.29 | 6.2 dB  |
| Peaking | 654 Hz  | 0.49 | 10.1 dB |
| Peaking | 972 Hz  | 0.18 | -9.2 dB |
| Peaking | 5731 Hz | 1.96 | 8.4 dB  |
| Peaking | 3607 Hz | 2.1  | 8.9 dB  |
| Peaking | 86 Hz   | 2.63 | 0.6 dB  |
| Peaking | 144 Hz  | 3.9  | -0.7 dB |
| Peaking | 1144 Hz | 1.75 | 1.4 dB  |
| Peaking | 1452 Hz | 0.99 | -1.1 dB |
| Peaking | 2898 Hz | 3.75 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf2/Etymotic%20hf2.png)