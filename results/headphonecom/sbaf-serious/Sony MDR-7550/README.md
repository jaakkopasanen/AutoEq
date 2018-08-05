# Sony MDR-7550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.2; 22 3.9; 23 3.8; 25 3.6; 26 3.5; 28 3.3; 30 3.2; 32 3.1; 35 3.0; 37 2.9; 40 2.8; 42 2.8; 45 2.7; 49 2.6; 52 2.6; 56 2.5; 59 2.4; 64 2.2; 68 2.1; 73 2.1; 78 1.9; 83 1.7; 89 1.4; 95 1.0; 102 0.5; 109 0.0; 117 -0.5; 125 -1.1; 134 -1.6; 143 -1.9; 153 -2.2; 164 -2.3; 175 -2.4; 188 -2.5; 201 -2.5; 215 -2.5; 230 -2.3; 246 -2.2; 263 -2.2; 282 -2.1; 301 -2.0; 323 -1.7; 345 -1.5; 369 -1.3; 395 -1.1; 423 -0.9; 452 -0.7; 484 -0.6; 518 -0.6; 554 -0.3; 593 0.1; 635 0.3; 679 0.3; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 -0.6; 1248 -1.3; 1336 -2.1; 1429 -2.9; 1529 -3.5; 1636 -4.0; 1751 -4.1; 1873 -3.7; 2004 -3.3; 2145 -2.4; 2295 -1.1; 2455 0.5; 2627 2.2; 2811 4.1; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.9; 4514 0.7; 4830 -2.3; 5168 -2.5; 5530 1.6; 5917 5.4; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 0.08 | 4.1 dB  |
| Peaking | 213 Hz  | 0.52 | -6.5 dB |
| Peaking | 1765 Hz | 1.68 | -5.5 dB |
| Peaking | 3277 Hz | 2.54 | 7.7 dB  |
| Peaking | 6287 Hz | 7.21 | 6.0 dB  |
| Peaking | 86 Hz   | 3.13 | 0.6 dB  |
| Peaking | 139 Hz  | 3.99 | -0.6 dB |
| Peaking | 4031 Hz | 7.42 | 3.5 dB  |
| Peaking | 5021 Hz | 4.77 | -5.5 dB |
| Peaking | 5737 Hz | 7.44 | 3.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)