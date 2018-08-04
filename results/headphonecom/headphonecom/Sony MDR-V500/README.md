# Sony MDR-V500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.5; 83 4.9; 89 4.3; 95 3.7; 102 3.1; 109 2.7; 117 2.1; 125 1.6; 134 1.2; 143 1.2; 153 1.6; 164 1.6; 175 1.2; 188 1.2; 201 1.1; 215 1.7; 230 2.2; 246 2.0; 263 1.8; 282 1.4; 301 0.7; 323 0.6; 345 0.6; 369 0.6; 395 0.6; 423 0.7; 452 0.7; 484 0.6; 518 0.6; 554 0.6; 593 0.9; 635 1.2; 679 0.9; 726 0.6; 777 0.6; 832 1.1; 890 0.6; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 0.4; 1248 -0.1; 1336 -0.5; 1429 -0.3; 1529 0.0; 1636 0.4; 1751 0.1; 1873 0.1; 2004 0.1; 2145 0.1; 2295 0.0; 2455 -0.0; 2627 -0.1; 2811 -0.6; 3008 -1.6; 3219 -2.1; 3444 -2.0; 3685 -1.6; 3943 -0.8; 4219 0.7; 4514 2.6; 4830 4.4; 5168 5.8; 5530 5.9; 5917 4.0; 6331 1.1; 6775 1.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.54 | 6.0 dB  |
| Peaking | 70 Hz   | 1.58 | 3.4 dB  |
| Peaking | 313 Hz  | 0.54 | 0.8 dB  |
| Peaking | 3461 Hz | 3.07 | -2.9 dB |
| Peaking | 5266 Hz | 3.5  | 6.7 dB  |
| Peaking | 133 Hz  | 7.19 | -0.6 dB |
| Peaking | 246 Hz  | 3.96 | 1.4 dB  |
| Peaking | 337 Hz  | 1.18 | -0.8 dB |
| Peaking | 966 Hz  | 0.81 | 1.2 dB  |
| Peaking | 1138 Hz | 1.42 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-V500/Sony%20MDR-V500.png)