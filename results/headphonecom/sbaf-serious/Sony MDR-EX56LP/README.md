# Sony MDR-EX56LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.3; 22 -7.7; 23 -7.9; 25 -8.2; 26 -8.3; 28 -8.6; 30 -8.8; 32 -8.9; 35 -9.1; 37 -9.2; 40 -9.3; 42 -9.4; 45 -9.5; 49 -9.5; 52 -9.5; 56 -9.5; 59 -9.6; 64 -9.5; 68 -9.5; 73 -9.4; 78 -9.4; 83 -9.5; 89 -9.6; 95 -9.8; 102 -10.1; 109 -10.3; 117 -10.6; 125 -10.9; 134 -11.0; 143 -11.1; 153 -11.1; 164 -10.9; 175 -10.6; 188 -10.3; 201 -9.9; 215 -9.6; 230 -9.2; 246 -8.8; 263 -8.4; 282 -8.0; 301 -7.5; 323 -7.1; 345 -6.6; 369 -6.1; 395 -5.8; 423 -5.3; 452 -5.2; 484 -5.1; 518 -4.9; 554 -4.4; 593 -4.1; 635 -4.0; 679 -4.2; 726 -4.3; 777 -4.4; 832 -4.7; 890 -3.8; 952 -0.8; 1019 -0.2; 1090 -1.3; 1167 -2.4; 1248 -3.2; 1336 -4.3; 1429 -5.2; 1529 -6.1; 1636 -6.8; 1751 -7.5; 1873 -8.1; 2004 -8.4; 2145 -8.5; 2295 -8.1; 2455 -7.2; 2627 -6.1; 2811 -4.8; 3008 -3.2; 3219 -2.2; 3444 -1.4; 3685 -0.1; 3943 2.4; 4219 4.6; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.5; 6331 1.4; 6775 0.3; 7249 0.4; 7756 0.2; 8299 0.0; 8880 -0.8; 9502 -2.7; 10167 -3.7; 10879 -1.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -2.7; 16326 -3.3; 17469 -0.8; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX56LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 5 Hz     |  1.68 | -6.6 dB |
| Peaking | 30 Hz    |  0.52 | -7.0 dB |
| Peaking | 161 Hz   |  0.41 | -9.8 dB |
| Peaking | 2115 Hz  |  1.38 | -8.9 dB |
| Peaking | 4813 Hz  |  2.5  | 8.4 dB  |
| Peaking | 880 Hz   |  2.88 | -3.5 dB |
| Peaking | 990 Hz   |  4.75 | 5.5 dB  |
| Peaking | 5688 Hz  | 12.14 | 2.4 dB  |
| Peaking | 10013 Hz |  5.4  | -4.2 dB |
| Peaking | 32001 Hz |  4.32 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX56LP/Sony%20MDR-EX56LP.png)