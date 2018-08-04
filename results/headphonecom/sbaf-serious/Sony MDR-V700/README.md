# Sony MDR-V700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.3; 73 4.3; 78 3.3; 83 2.6; 89 1.8; 95 1.2; 102 0.9; 109 0.8; 117 0.6; 125 0.4; 134 0.4; 143 0.4; 153 0.5; 164 0.9; 175 1.3; 188 1.5; 201 1.7; 215 1.9; 230 2.3; 246 2.8; 263 3.2; 282 3.6; 301 3.7; 323 3.8; 345 3.8; 369 3.7; 395 4.8; 423 5.1; 452 4.1; 484 2.7; 518 1.0; 554 -0.1; 593 -0.6; 635 -0.6; 679 -0.5; 726 -0.0; 777 1.1; 832 -0.4; 890 -0.9; 952 -0.5; 1019 0.2; 1090 0.9; 1167 1.2; 1248 0.7; 1336 -0.3; 1429 -1.5; 1529 -2.4; 1636 -3.2; 1751 -3.7; 1873 -3.4; 2004 -4.0; 2145 -4.7; 2295 -5.0; 2455 -4.5; 2627 -4.2; 2811 -3.5; 3008 -2.0; 3219 -1.0; 3444 -0.1; 3685 1.2; 3943 3.1; 4219 4.1; 4514 5.6; 4830 6.0; 5168 6.0; 5530 5.3; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -3.4; 9502 -4.1; 10167 -1.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 36 Hz   | 0.67 | 6.9 dB  |
| Peaking | 359 Hz  | 1.66 | 4.6 dB  |
| Peaking | 2408 Hz | 1.37 | -6.4 dB |
| Peaking | 5059 Hz | 1.27 | 7.4 dB  |
| Peaking | 9171 Hz | 4.01 | -5.8 dB |
| Peaking | 65 Hz   | 2.13 | 3.7 dB  |
| Peaking | 86 Hz   | 0.66 | -2.1 dB |
| Peaking | 226 Hz  | 1.55 | 1.2 dB  |
| Peaking | 600 Hz  | 5.31 | -1.9 dB |
| Peaking | 1166 Hz | 6.55 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V700/Sony%20MDR-V700.png)