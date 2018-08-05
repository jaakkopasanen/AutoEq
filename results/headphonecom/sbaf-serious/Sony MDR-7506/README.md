# Sony MDR-7506

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.6; 52 5.1; 56 4.6; 59 4.3; 64 4.3; 68 4.6; 73 4.6; 78 4.3; 83 4.0; 89 3.7; 95 3.5; 102 3.2; 109 2.9; 117 2.8; 125 2.4; 134 2.4; 143 2.4; 153 2.4; 164 2.4; 175 2.6; 188 2.7; 201 2.9; 215 3.0; 230 2.9; 246 2.6; 263 2.0; 282 1.5; 301 1.1; 323 0.3; 345 -0.3; 369 -1.0; 395 -1.7; 423 -1.8; 452 -2.0; 484 -2.4; 518 -2.6; 554 -2.2; 593 -1.6; 635 -1.3; 679 -1.5; 726 -1.4; 777 -1.1; 832 -0.9; 890 -0.7; 952 -0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.0; 1529 -1.5; 1636 -1.7; 1751 -1.6; 1873 -1.5; 2004 -1.3; 2145 -1.3; 2295 -1.1; 2455 -1.0; 2627 -1.6; 2811 -2.1; 3008 -2.3; 3219 -1.8; 3444 -1.8; 3685 -0.7; 3943 0.0; 4219 -2.2; 4514 -4.4; 4830 -3.8; 5168 -0.8; 5530 3.3; 5917 5.2; 6331 3.3; 6775 0.4; 7249 -0.3; 7756 -0.2; 8299 -1.4; 8880 -3.9; 9502 -5.7; 10167 -5.1; 10879 -2.2; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.26 | 6.2 dB  |
| Peaking | 221 Hz  | 2.07 | 3.2 dB  |
| Peaking | 1056 Hz | 0.11 | -1.6 dB |
| Peaking | 5948 Hz | 6.86 | 7.2 dB  |
| Peaking | 9667 Hz | 5.23 | -5.8 dB |
| Peaking | 490 Hz  | 3.16 | -1.7 dB |
| Peaking | 1060 Hz | 2.71 | 1.7 dB  |
| Peaking | 3206 Hz | 2.75 | -2.7 dB |
| Peaking | 4605 Hz | 4.91 | -7.0 dB |
| Peaking | 4122 Hz | 1.53 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7506/Sony%20MDR-7506.png)