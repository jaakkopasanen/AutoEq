# Sennheiser RS 160

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.4; 23 -5.5; 25 -5.7; 26 -5.7; 28 -5.8; 30 -5.9; 32 -5.9; 35 -6.0; 37 -6.0; 40 -6.0; 42 -6.0; 45 -6.0; 49 -6.0; 52 -5.9; 56 -5.7; 59 -5.6; 64 -5.5; 68 -5.4; 73 -5.2; 78 -4.9; 83 -4.6; 89 -4.2; 95 -4.1; 102 -4.7; 109 -5.5; 117 -5.6; 125 -4.8; 134 -4.8; 143 -5.3; 153 -5.1; 164 -4.3; 175 -3.6; 188 -3.6; 201 -3.7; 215 -3.3; 230 -2.9; 246 -2.6; 263 -2.2; 282 -1.7; 301 -1.4; 323 -1.4; 345 -1.7; 369 -1.8; 395 -1.9; 423 -1.9; 452 -1.5; 484 -0.8; 518 -0.2; 554 0.5; 593 1.1; 635 1.3; 679 1.4; 726 1.6; 777 1.7; 832 1.6; 890 1.8; 952 0.9; 1019 -0.3; 1090 -0.7; 1167 -0.5; 1248 -0.1; 1336 -0.2; 1429 -0.2; 1529 -0.1; 1636 -0.7; 1751 -0.6; 1873 3.0; 2004 1.2; 2145 0.1; 2295 -0.2; 2455 0.3; 2627 1.3; 2811 0.6; 3008 0.9; 3219 1.3; 3444 1.8; 3685 2.7; 3943 4.0; 4219 4.2; 4514 5.1; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -3.6; 9502 -3.6; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.41 | -6.1 dB |
| Peaking | 134 Hz  | 1.57 | -2.8 dB |
| Peaking | 225 Hz  | 1.41 | -1.5 dB |
| Peaking | 5395 Hz | 1.5  | 6.8 dB  |
| Peaking | 9044 Hz | 3.83 | -5.6 dB |
| Peaking | 424 Hz  | 2.88 | -2.1 dB |
| Peaking | 865 Hz  | 0.92 | 2.7 dB  |
| Peaking | 1081 Hz | 3.53 | -2.6 dB |
| Peaking | 1884 Hz | 8.78 | 5.4 dB  |
| Peaking | 1839 Hz | 2.39 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20RS%20160/Sennheiser%20RS%20160.png)