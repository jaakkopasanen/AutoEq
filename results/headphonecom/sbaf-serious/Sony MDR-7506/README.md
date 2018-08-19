# Sony MDR-7506

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.4; 52 4.9; 56 4.2; 59 3.9; 64 3.8; 68 4.0; 73 3.9; 78 3.5; 83 3.2; 89 2.9; 95 2.8; 102 2.6; 109 2.5; 117 2.6; 125 2.4; 134 2.5; 143 2.6; 153 2.7; 164 2.7; 175 2.8; 188 2.9; 201 3.1; 215 3.1; 230 3.0; 246 2.7; 263 2.1; 282 1.5; 301 1.2; 323 0.4; 345 -0.3; 369 -0.9; 395 -1.6; 423 -1.9; 452 -2.0; 484 -2.3; 518 -2.5; 554 -2.2; 593 -1.7; 635 -1.4; 679 -1.4; 726 -1.3; 777 -1.2; 832 -1.0; 890 -0.6; 952 -0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.0; 1529 -1.5; 1636 -1.7; 1751 -1.6; 1873 -1.5; 2004 -1.3; 2145 -1.3; 2295 -1.1; 2455 -1.1; 2627 -1.6; 2811 -2.0; 3008 -2.4; 3219 -1.8; 3444 -1.7; 3685 -0.6; 3943 -0.2; 4219 -2.2; 4514 -4.2; 4830 -3.7; 5168 -0.8; 5530 3.3; 5917 5.2; 6331 3.3; 6775 0.3; 7249 -0.4; 7756 -0.2; 8299 -1.2; 8880 -3.7; 9502 -5.8; 10167 -5.3; 10879 -2.0; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.3  | 6.2 dB  |
| Peaking | 211 Hz  | 1.64 | 3.7 dB  |
| Peaking | 1037 Hz | 0.11 | -1.6 dB |
| Peaking | 5951 Hz | 7.01 | 7.3 dB  |
| Peaking | 9682 Hz | 5.51 | -6.1 dB |
| Peaking | 487 Hz  | 2.98 | -1.6 dB |
| Peaking | 1057 Hz | 2.7  | 1.7 dB  |
| Peaking | 3168 Hz | 3.22 | -2.2 dB |
| Peaking | 4252 Hz | 1.49 | 3.1 dB  |
| Peaking | 4577 Hz | 4.99 | -6.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7506/Sony%20MDR-7506.png)