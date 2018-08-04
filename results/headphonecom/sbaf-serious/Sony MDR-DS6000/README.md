# Sony MDR-DS6000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.7; 56 5.0; 59 4.6; 64 3.7; 68 2.7; 73 1.7; 78 1.0; 83 0.3; 89 -0.4; 95 -1.0; 102 -1.6; 109 -2.0; 117 -2.4; 125 -2.8; 134 -2.9; 143 -2.9; 153 -2.9; 164 -2.6; 175 -2.2; 188 -2.5; 201 -2.2; 215 -1.3; 230 -1.7; 246 -1.6; 263 -1.4; 282 -1.1; 301 -0.9; 323 -0.7; 345 -0.5; 369 -0.4; 395 -0.3; 423 0.3; 452 0.3; 484 -0.1; 518 -0.3; 554 -0.5; 593 -0.5; 635 -0.7; 679 -1.3; 726 -1.5; 777 -1.5; 832 -1.4; 890 -0.9; 952 0.1; 1019 -0.2; 1090 -1.1; 1167 -1.8; 1248 -2.6; 1336 -2.8; 1429 -3.1; 1529 -3.7; 1636 -4.4; 1751 -4.9; 1873 -5.3; 2004 -5.7; 2145 -5.3; 2295 -4.3; 2455 -2.7; 2627 -1.2; 2811 0.4; 3008 1.7; 3219 3.0; 3444 4.1; 3685 5.8; 3943 6.0; 4219 5.1; 4514 3.7; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.37 | 7.9 dB  |
| Peaking | 116 Hz  | 0.75 | -7.1 dB |
| Peaking | 1988 Hz | 1.43 | -6.6 dB |
| Peaking | 3697 Hz | 1.94 | 6.5 dB  |
| Peaking | 5754 Hz | 3.05 | 5.6 dB  |
| Peaking | 442 Hz  | 5.87 | 1.0 dB  |
| Peaking | 773 Hz  | 3.16 | -1.2 dB |
| Peaking | 975 Hz  | 5.71 | 1.7 dB  |
| Peaking | 1248 Hz | 7.46 | -0.7 dB |
| Peaking | 8235 Hz | 4.68 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)