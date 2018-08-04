# Sony MDR-DS3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 5.6; 117 5.3; 125 4.8; 134 4.4; 143 4.3; 153 4.1; 164 4.0; 175 4.1; 188 4.0; 201 4.0; 215 4.2; 230 4.4; 246 4.4; 263 4.4; 282 4.8; 301 4.7; 323 4.8; 345 5.1; 369 4.5; 395 4.0; 423 3.7; 452 3.5; 484 3.2; 518 2.9; 554 2.9; 593 2.8; 635 2.5; 679 2.1; 726 1.7; 777 1.5; 832 1.5; 890 1.2; 952 0.5; 1019 0.0; 1090 -0.2; 1167 -0.4; 1248 -0.4; 1336 -0.5; 1429 -0.9; 1529 -1.8; 1636 -2.7; 1751 -4.4; 1873 -5.5; 2004 -5.9; 2145 -5.1; 2295 -3.3; 2455 -2.0; 2627 -1.8; 2811 -1.1; 3008 0.2; 3219 1.4; 3444 1.9; 3685 2.0; 3943 1.5; 4219 0.1; 4514 -1.6; 4830 0.4; 5168 3.5; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.25 | 6.3 dB  |
| Peaking | 372 Hz  | 0.81 | 3.4 dB  |
| Peaking | 1972 Hz | 2.57 | -6.4 dB |
| Peaking | 3450 Hz | 5.56 | 2.6 dB  |
| Peaking | 5976 Hz | 4.13 | 6.8 dB  |
| Peaking | 156 Hz  | 5.55 | -0.5 dB |
| Peaking | 4565 Hz | 7.45 | -4.8 dB |
| Peaking | 4794 Hz | 2.72 | 2.1 dB  |
| Peaking | 8217 Hz | 3.83 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS3000/Sony%20MDR-DS3000.png)