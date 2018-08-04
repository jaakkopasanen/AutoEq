# Sony MDR-V700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.7; 52 4.9; 56 3.7; 59 3.1; 64 1.9; 68 0.9; 73 -0.1; 78 -1.0; 83 -1.6; 89 -2.2; 95 -2.5; 102 -2.5; 109 -2.3; 117 -2.3; 125 -2.1; 134 -1.7; 143 -1.5; 153 -1.2; 164 -0.7; 175 -0.2; 188 0.0; 201 0.2; 215 0.5; 230 0.8; 246 1.4; 263 1.9; 282 2.2; 301 2.3; 323 2.5; 345 2.4; 369 2.3; 395 3.5; 423 3.9; 452 3.1; 484 2.0; 518 0.5; 554 -0.6; 593 -1.0; 635 -0.9; 679 -0.6; 726 0.0; 777 1.0; 832 -0.5; 890 -0.9; 952 -0.5; 1019 0.2; 1090 1.0; 1167 1.4; 1248 1.3; 1336 1.1; 1429 0.6; 1529 0.3; 1636 -0.2; 1751 -0.7; 1873 -0.5; 2004 -1.0; 2145 -1.7; 2295 -1.9; 2455 -1.6; 2627 -1.2; 2811 -0.5; 3008 0.5; 3219 1.3; 3444 2.0; 3685 3.3; 3943 5.4; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.4; 9502 -1.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.41 | 7.8 dB  |
| Peaking | 92 Hz   | 0.99 | -7.4 dB |
| Peaking | 365 Hz  | 1.89 | 3.3 dB  |
| Peaking | 2404 Hz | 2.68 | -3.0 dB |
| Peaking | 4868 Hz | 1.66 | 7.1 dB  |
| Peaking | 456 Hz  | 4.18 | 3.0 dB  |
| Peaking | 535 Hz  | 1.85 | -2.4 dB |
| Peaking | 1218 Hz | 4.75 | 1.7 dB  |
| Peaking | 6400 Hz | 6.75 | 2.6 dB  |
| Peaking | 8875 Hz | 2.7  | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-V700/Sony%20MDR-V700.png)