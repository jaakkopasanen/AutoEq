# Sennheiser RS 180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 3.1; 22 2.3; 23 2.0; 25 1.3; 26 1.0; 28 0.5; 30 0.0; 32 -0.4; 35 -0.9; 37 -1.2; 40 -1.6; 42 -1.8; 45 -2.1; 49 -2.5; 52 -2.6; 56 -2.5; 59 -2.6; 64 -3.2; 68 -3.7; 73 -3.6; 78 -3.4; 83 -3.8; 89 -4.0; 95 -4.4; 102 -4.8; 109 -5.0; 117 -5.1; 125 -5.3; 134 -5.6; 143 -5.9; 153 -6.0; 164 -5.9; 175 -5.9; 188 -6.0; 201 -5.8; 215 -5.4; 230 -4.9; 246 -4.7; 263 -4.7; 282 -4.4; 301 -4.1; 323 -3.8; 345 -3.5; 369 -3.3; 395 -3.1; 423 -2.7; 452 -2.5; 484 -2.4; 518 -2.2; 554 -1.9; 593 -1.6; 635 -1.4; 679 -1.4; 726 -1.5; 777 -0.7; 832 1.0; 890 0.3; 952 0.1; 1019 0.0; 1090 0.3; 1167 0.4; 1248 0.6; 1336 1.0; 1429 0.7; 1529 -0.7; 1636 -2.4; 1751 -3.9; 1873 -4.9; 2004 -5.7; 2145 -6.2; 2295 -5.7; 2455 -4.2; 2627 -2.5; 2811 0.4; 3008 2.2; 3219 -1.8; 3444 -0.6; 3685 2.2; 3943 1.4; 4219 0.5; 4514 -2.1; 4830 -5.5; 5168 -4.8; 5530 -2.6; 5917 -2.3; 6331 -3.1; 6775 1.7; 7249 1.3; 7756 -2.0; 8299 -6.2; 8880 -8.7; 9502 -7.5; 10167 -3.4; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.32 | 3.3 dB  |
| Peaking | 156 Hz   | 0.5  | -5.9 dB |
| Peaking | 2109 Hz  | 3.73 | -6.8 dB |
| Peaking | 9004 Hz  | 4.73 | -9.6 dB |
| Peaking | 24000 Hz | 2.11 | -5.9 dB |
| Peaking | 1216 Hz  | 2.81 | 1.7 dB  |
| Peaking | 4110 Hz  | 2.82 | 6.5 dB  |
| Peaking | 4798 Hz  | 2.5  | -8.1 dB |
| Peaking | 7061 Hz  | 9.59 | 5.0 dB  |
| Peaking | 11224 Hz | 6.49 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20180/Sennheiser%20RS%20180.png)