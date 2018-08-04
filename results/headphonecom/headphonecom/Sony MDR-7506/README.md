# Sony MDR-7506

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.5; 32 4.9; 35 3.9; 37 3.3; 40 2.6; 42 2.2; 45 1.6; 49 1.0; 52 0.6; 56 0.0; 59 -0.2; 64 -0.2; 68 0.2; 73 0.3; 78 -0.0; 83 -0.2; 89 -0.3; 95 -0.3; 102 -0.3; 109 -0.3; 117 -0.1; 125 -0.0; 134 0.2; 143 0.5; 153 0.7; 164 0.8; 175 1.1; 188 1.2; 201 1.5; 215 1.5; 230 1.4; 246 1.2; 263 0.6; 282 0.1; 301 -0.2; 323 -1.0; 345 -1.7; 369 -2.3; 395 -2.9; 423 -3.1; 452 -3.0; 484 -3.1; 518 -3.2; 554 -2.7; 593 -2.1; 635 -1.6; 679 -1.6; 726 -1.4; 777 -1.3; 832 -1.0; 890 -0.7; 952 -0.1; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.4; 1336 0.6; 1429 1.1; 1529 1.2; 1636 1.3; 1751 1.4; 1873 1.4; 2004 1.7; 2145 1.7; 2295 2.0; 2455 1.9; 2627 1.4; 2811 0.8; 3008 0.2; 3219 0.5; 3444 0.3; 3685 1.4; 3943 2.4; 4219 1.4; 4514 0.4; 4830 1.7; 5168 4.7; 5530 6.0; 5917 5.9; 6331 5.1; 6775 1.8; 7249 0.8; 7756 0.3; 8299 -0.2; 8880 -1.9; 9502 -3.1; 10167 -1.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.42 | 6.6 dB  |
| Peaking | 487 Hz  | 1.94 | -3.6 dB |
| Peaking | 2033 Hz | 1.54 | 1.8 dB  |
| Peaking | 5769 Hz | 3.65 | 6.7 dB  |
| Peaking | 9399 Hz | 5.03 | -3.6 dB |
| Peaking | 6 Hz    | 0.61 | 0.4 dB  |
| Peaking | 95 Hz   | 0.78 | -0.9 dB |
| Peaking | 224 Hz  | 1.16 | 2.6 dB  |
| Peaking | 411 Hz  | 1.26 | -2.6 dB |
| Peaking | 478 Hz  | 2.65 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-7506/Sony%20MDR-7506.png)