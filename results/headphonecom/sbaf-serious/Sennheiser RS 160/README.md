# Sennheiser RS 160

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.9; 23 -1.0; 25 -1.1; 26 -1.2; 28 -1.3; 30 -1.3; 32 -1.4; 35 -1.4; 37 -1.5; 40 -1.4; 42 -1.4; 45 -1.5; 49 -1.4; 52 -1.3; 56 -1.1; 59 -1.1; 64 -1.0; 68 -1.0; 73 -0.8; 78 -0.6; 83 -0.4; 89 -0.2; 95 -0.4; 102 -1.2; 109 -2.3; 117 -2.7; 125 -2.3; 134 -2.7; 143 -3.4; 153 -3.3; 164 -2.7; 175 -2.0; 188 -2.2; 201 -2.3; 215 -1.9; 230 -1.5; 246 -1.2; 263 -0.8; 282 -0.3; 301 -0.0; 323 -0.0; 345 -0.2; 369 -0.5; 395 -0.7; 423 -0.7; 452 -0.4; 484 -0.1; 518 0.3; 554 1.0; 593 1.5; 635 1.6; 679 1.4; 726 1.6; 777 1.9; 832 1.7; 890 1.8; 952 0.9; 1019 -0.3; 1090 -0.8; 1167 -0.8; 1248 -0.8; 1336 -1.5; 1429 -2.3; 1529 -2.8; 1636 -3.7; 1751 -3.7; 1873 0.1; 2004 -1.7; 2145 -3.0; 2295 -3.3; 2455 -2.6; 2627 -1.7; 2811 -2.3; 3008 -1.7; 3219 -1.0; 3444 -0.3; 3685 0.6; 3943 1.6; 4219 0.5; 4514 0.3; 4830 2.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.1; 8880 -5.6; 9502 -6.2; 10167 -4.4; 10879 -1.8; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 147 Hz  |  1.45 | -3.2 dB |
| Peaking | 1618 Hz |  5.3  | -3.4 dB |
| Peaking | 2477 Hz |  2.34 | -3.0 dB |
| Peaking | 5870 Hz |  2.46 | 7.2 dB  |
| Peaking | 9307 Hz |  3.79 | -7.7 dB |
| Peaking | 37 Hz   |  0.78 | -1.4 dB |
| Peaking | 90 Hz   |  4.69 | 1.3 dB  |
| Peaking | 769 Hz  |  1.4  | 4.8 dB  |
| Peaking | 891 Hz  |  0.81 | -2.7 dB |
| Peaking | 1888 Hz | 16.53 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20160/Sennheiser%20RS%20160.png)