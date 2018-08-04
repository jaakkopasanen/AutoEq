# Sony MDR-DS6000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 5.0; 42 4.3; 45 3.3; 49 2.0; 52 1.2; 56 0.4; 59 0.0; 64 -0.8; 68 -1.7; 73 -2.7; 78 -3.3; 83 -3.9; 89 -4.4; 95 -4.8; 102 -5.0; 109 -5.2; 117 -5.3; 125 -5.3; 134 -5.0; 143 -4.8; 153 -4.6; 164 -4.2; 175 -3.7; 188 -3.9; 201 -3.7; 215 -2.7; 230 -3.2; 246 -3.0; 263 -2.8; 282 -2.5; 301 -2.2; 323 -2.1; 345 -2.0; 369 -1.8; 395 -1.6; 423 -0.9; 452 -0.7; 484 -0.8; 518 -0.9; 554 -1.0; 593 -1.0; 635 -1.1; 679 -1.4; 726 -1.5; 777 -1.7; 832 -1.5; 890 -0.9; 952 0.1; 1019 -0.2; 1090 -1.0; 1167 -1.5; 1248 -1.9; 1336 -1.5; 1429 -1.0; 1529 -1.0; 1636 -1.4; 1751 -1.8; 1873 -2.4; 2004 -2.7; 2145 -2.3; 2295 -1.3; 2455 0.2; 2627 1.8; 2811 3.3; 3008 4.3; 3219 5.3; 3444 5.9; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.55 | 8.6 dB  |
| Peaking | 96 Hz   | 0.56 | -7.7 dB |
| Peaking | 4024 Hz | 0.26 | -3.9 dB |
| Peaking | 2070 Hz | 2.75 | -4.2 dB |
| Peaking | 4205 Hz | 0.72 | 11.0 dB |
| Peaking | 8919 Hz | 0.29 | 0.6 dB  |
| Peaking | 1251 Hz | 9.2  | -1.1 dB |
| Peaking | 4356 Hz | 4.2  | -1.3 dB |
| Peaking | 6410 Hz | 3.46 | 3.5 dB  |
| Peaking | 7464 Hz | 1.97 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)