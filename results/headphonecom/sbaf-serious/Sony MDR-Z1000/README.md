# Sony MDR-Z1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.9; 68 5.4; 73 4.8; 78 4.3; 83 3.9; 89 3.5; 95 3.3; 102 2.8; 109 2.1; 117 1.4; 125 0.6; 134 -0.1; 143 -0.4; 153 -0.5; 164 -0.1; 175 0.2; 188 0.3; 201 0.5; 215 0.8; 230 1.1; 246 1.5; 263 2.3; 282 2.5; 301 1.7; 323 0.9; 345 0.5; 369 0.2; 395 -0.2; 423 -0.2; 452 -0.4; 484 -0.6; 518 -0.6; 554 -0.3; 593 -0.0; 635 0.1; 679 0.1; 726 0.1; 777 0.0; 832 0.1; 890 0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 -0.2; 1248 -0.6; 1336 -1.3; 1429 -2.1; 1529 -3.0; 1636 -3.8; 1751 -4.3; 1873 -4.1; 2004 -3.8; 2145 -2.9; 2295 -1.4; 2455 -0.4; 2627 0.4; 2811 1.5; 3008 2.7; 3219 3.6; 3444 5.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.7; 8880 -5.7; 9502 -6.9; 10167 -3.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.6  | 6.9 dB   |
| Peaking | 275 Hz  | 6.54 | 2.4 dB   |
| Peaking | 1918 Hz | 1.7  | -6.7 dB  |
| Peaking | 4660 Hz | 0.72 | 7.4 dB   |
| Peaking | 9170 Hz | 3.46 | -10.1 dB |
| Peaking | 37 Hz   | 1.21 | -3.4 dB  |
| Peaking | 26 Hz   | 0.18 | 2.5 dB   |
| Peaking | 141 Hz  | 1.93 | -2.9 dB  |
| Peaking | 463 Hz  | 3.09 | -0.9 dB  |
| Peaking | 1099 Hz | 4.78 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)