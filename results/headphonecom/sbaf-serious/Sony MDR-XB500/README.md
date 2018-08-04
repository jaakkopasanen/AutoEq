# Sony MDR-XB500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -9.1; 22 -9.3; 23 -9.4; 25 -9.5; 26 -9.6; 28 -9.7; 30 -9.8; 32 -9.8; 35 -9.9; 37 -9.9; 40 -9.9; 42 -9.9; 45 -9.9; 49 -10.0; 52 -10.0; 56 -9.9; 59 -9.9; 64 -9.7; 68 -9.6; 73 -9.6; 78 -10.0; 83 -10.4; 89 -10.9; 95 -11.1; 102 -10.8; 109 -11.1; 117 -11.8; 125 -12.5; 134 -13.0; 143 -13.5; 153 -13.8; 164 -13.1; 175 -12.6; 188 -12.6; 201 -13.2; 215 -13.7; 230 -13.6; 246 -13.3; 263 -12.9; 282 -12.7; 301 -12.5; 323 -12.2; 345 -11.8; 369 -11.5; 395 -11.0; 423 -10.3; 452 -9.7; 484 -9.1; 518 -8.2; 554 -7.0; 593 -5.7; 635 -4.4; 679 -3.2; 726 -1.7; 777 -0.2; 832 0.8; 890 1.0; 952 0.7; 1019 -0.1; 1090 -1.1; 1167 -1.7; 1248 -2.9; 1336 -4.3; 1429 -4.9; 1529 -5.2; 1636 -5.0; 1751 -4.3; 1873 -3.6; 2004 -2.8; 2145 -1.7; 2295 -0.8; 2455 0.6; 2627 2.0; 2811 3.2; 3008 4.5; 3219 5.8; 3444 6.0; 3685 6.0; 3943 4.8; 4219 1.9; 4514 -1.0; 4830 -2.5; 5168 -1.8; 5530 -0.7; 5917 0.3; 6331 0.7; 6775 -0.1; 7249 -2.2; 7756 -1.4; 8299 -0.0; 8880 0.0; 9502 -0.0; 10167 -0.8; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 6 Hz     | 1.31 | -8.8 dB |
| Peaking | 28 Hz    | 0.15 | -8.7 dB |
| Peaking | 220 Hz   | 0.65 | -9.2 dB |
| Peaking | 414 Hz   | 1.89 | -4.3 dB |
| Peaking | 3414 Hz  | 4.24 | 7.4 dB  |
| Peaking | 917 Hz   | 1.79 | 7.2 dB  |
| Peaking | 1742 Hz  | 0.69 | -8.9 dB |
| Peaking | 2610 Hz  | 1.06 | 6.9 dB  |
| Peaking | 4851 Hz  | 7.19 | -3.5 dB |
| Peaking | 25755 Hz | 1.7  | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)