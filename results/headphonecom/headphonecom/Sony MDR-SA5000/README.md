# Sony MDR-SA5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 4.9; 64 3.8; 68 3.2; 73 2.7; 78 2.2; 83 1.6; 89 1.3; 95 1.2; 102 1.1; 109 1.3; 117 1.3; 125 1.6; 134 1.9; 143 2.0; 153 2.2; 164 2.7; 175 2.9; 188 3.1; 201 3.1; 215 3.4; 230 3.4; 246 3.6; 263 3.8; 282 4.0; 301 4.2; 323 4.2; 345 3.1; 369 3.2; 395 3.4; 423 3.5; 452 3.4; 484 3.3; 518 3.0; 554 2.6; 593 2.2; 635 2.0; 679 1.7; 726 1.3; 777 0.8; 832 0.3; 890 -0.1; 952 -0.3; 1019 0.2; 1090 1.5; 1167 3.1; 1248 4.5; 1336 5.7; 1429 6.0; 1529 6.0; 1636 6.0; 1751 5.8; 1873 5.1; 2004 4.1; 2145 3.6; 2295 2.6; 2455 0.0; 2627 -2.8; 2811 -4.0; 3008 -2.4; 3219 -0.9; 3444 0.7; 3685 4.1; 3943 4.1; 4219 1.7; 4514 3.1; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 0.1; 7756 -2.2; 8299 -2.8; 8880 -2.7; 9502 -1.6; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.7  | 6.7 dB  |
| Peaking | 264 Hz  | 1.21 | 3.6 dB  |
| Peaking | 476 Hz  | 2.39 | 2.2 dB  |
| Peaking | 1561 Hz | 2.51 | 6.8 dB  |
| Peaking | 5457 Hz | 3.18 | 7.0 dB  |
| Peaking | 949 Hz  | 6.62 | -1.9 dB |
| Peaking | 2295 Hz | 2.49 | 3.6 dB  |
| Peaking | 2726 Hz | 3.48 | -7.2 dB |
| Peaking | 3756 Hz | 8.25 | 4.5 dB  |
| Peaking | 8467 Hz | 4.88 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-SA5000/Sony%20MDR-SA5000.png)