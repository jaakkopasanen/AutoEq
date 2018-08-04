# Sennheiser HD595

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.6; 42 5.3; 45 4.8; 49 4.4; 52 4.3; 56 4.4; 59 4.3; 64 3.8; 68 4.3; 73 4.8; 78 3.6; 83 2.7; 89 2.1; 95 1.6; 102 1.1; 109 0.6; 117 0.3; 125 -0.3; 134 -0.7; 143 -1.1; 153 -1.2; 164 -1.1; 175 -1.3; 188 -1.4; 201 -1.4; 215 -1.4; 230 -1.3; 246 -1.4; 263 -1.5; 282 -1.4; 301 -1.3; 323 -1.2; 345 -0.9; 369 -0.7; 395 -0.5; 423 -0.1; 452 0.1; 484 -0.2; 518 -0.4; 554 -0.4; 593 -0.2; 635 -0.2; 679 0.7; 726 0.3; 777 0.3; 832 0.3; 890 0.2; 952 0.0; 1019 0.0; 1090 0.2; 1167 0.5; 1248 0.7; 1336 1.1; 1429 1.3; 1529 1.4; 1636 1.5; 1751 1.7; 1873 1.5; 2004 0.9; 2145 0.6; 2295 0.4; 2455 1.0; 2627 1.7; 2811 1.7; 3008 1.4; 3219 1.0; 3444 1.2; 3685 1.9; 3943 2.7; 4219 3.5; 4514 3.4; 4830 2.5; 5168 3.1; 5530 5.4; 5917 5.9; 6331 5.1; 6775 0.9; 7249 0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.8; 20000 -5.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.2  | 6.3 dB  |
| Peaking | 159 Hz  | 0.63 | -4.5 dB |
| Peaking | 439 Hz  | 3.12 | 0.3 dB  |
| Peaking | 2916 Hz | 0.6  | 1.6 dB  |
| Peaking | 5810 Hz | 4.47 | 5.5 dB  |
| Peaking | 196 Hz  | 4.5  | 0.3 dB  |
| Peaking | 1781 Hz | 2.6  | 1.6 dB  |
| Peaking | 2098 Hz | 2.47 | -1.6 dB |
| Peaking | 4299 Hz | 7.29 | 2.1 dB  |
| Peaking | 8194 Hz | 1.84 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD595/Sennheiser%20HD595.png)