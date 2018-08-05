# Etymotic hf3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.8; 45 5.7; 49 5.5; 52 5.5; 56 5.3; 59 5.2; 64 5.2; 68 5.1; 73 4.8; 78 4.6; 83 4.4; 89 4.1; 95 3.8; 102 3.2; 109 2.8; 117 2.2; 125 1.6; 134 1.0; 143 0.6; 153 0.3; 164 0.1; 175 0.1; 188 -0.0; 201 -0.0; 215 -0.0; 230 0.1; 246 0.1; 263 0.1; 282 0.2; 301 0.3; 323 0.4; 345 0.6; 369 0.7; 395 0.9; 423 1.0; 452 1.0; 484 0.9; 518 1.0; 554 1.3; 593 1.6; 635 1.6; 679 1.4; 726 1.5; 777 1.5; 832 1.2; 890 0.8; 952 0.4; 1019 -0.0; 1090 -0.5; 1167 -1.1; 1248 -1.5; 1336 -2.1; 1429 -2.7; 1529 -3.3; 1636 -3.8; 1751 -4.0; 1873 -3.9; 2004 -3.8; 2145 -3.6; 2295 -3.2; 2455 -2.3; 2627 -1.5; 2811 -0.2; 3008 1.6; 3219 3.3; 3444 4.7; 3685 5.5; 3943 5.6; 4219 4.5; 4514 4.0; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.49 | 6.5 dB  |
| Peaking | 772 Hz  | 1.21 | 2.7 dB  |
| Peaking | 2048 Hz | 0.8  | -5.4 dB |
| Peaking | 5746 Hz | 2.88 | 6.1 dB  |
| Peaking | 3618 Hz | 1.97 | 7.5 dB  |
| Peaking | 40 Hz   | 0.82 | -4.0 dB |
| Peaking | 56 Hz   | 0.28 | 3.6 dB  |
| Peaking | 164 Hz  | 0.98 | -3.2 dB |
| Peaking | 8206 Hz | 5.33 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf3/Etymotic%20hf3.png)