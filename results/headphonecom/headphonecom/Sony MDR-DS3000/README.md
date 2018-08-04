# Sony MDR-DS3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.7; 68 5.4; 73 4.7; 78 4.0; 83 3.6; 89 3.2; 95 2.9; 102 2.6; 109 2.5; 117 2.4; 125 2.4; 134 2.3; 143 2.4; 153 2.3; 164 2.4; 175 2.6; 188 2.6; 201 2.6; 215 2.8; 230 2.9; 246 3.0; 263 3.1; 282 3.4; 301 3.4; 323 3.5; 345 3.6; 369 3.1; 395 2.7; 423 2.5; 452 2.5; 484 2.4; 518 2.4; 554 2.4; 593 2.3; 635 2.2; 679 2.0; 726 1.7; 777 1.4; 832 1.4; 890 1.2; 952 0.5; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 0.3; 1336 0.9; 1429 1.2; 1529 0.9; 1636 0.3; 1751 -1.4; 1873 -2.6; 2004 -3.0; 2145 -2.1; 2295 -0.2; 2455 0.9; 2627 1.2; 2811 1.8; 3008 2.8; 3219 3.7; 3444 4.0; 3685 4.1; 3943 3.8; 4219 3.7; 4514 3.2; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.48 | 6.5 dB  |
| Peaking | 354 Hz  | 0.7  | 3.0 dB  |
| Peaking | 1992 Hz | 4.7  | -4.2 dB |
| Peaking | 3486 Hz | 1.97 | 3.5 dB  |
| Peaking | 5641 Hz | 2.77 | 6.1 dB  |
| Peaking | 62 Hz   | 1.05 | -1.6 dB |
| Peaking | 63 Hz   | 2.23 | 2.5 dB  |
| Peaking | 1110 Hz | 3.37 | -2.8 dB |
| Peaking | 1166 Hz | 1.82 | 1.9 dB  |
| Peaking | 8349 Hz | 4.48 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-DS3000/Sony%20MDR-DS3000.png)