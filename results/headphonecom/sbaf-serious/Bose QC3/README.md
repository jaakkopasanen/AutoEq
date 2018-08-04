# Bose QC3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.3; 23 -4.4; 25 -4.6; 26 -4.7; 28 -4.7; 30 -4.7; 32 -4.7; 35 -4.6; 37 -4.5; 40 -4.3; 42 -4.2; 45 -4.1; 49 -3.9; 52 -3.8; 56 -3.7; 59 -3.6; 64 -3.6; 68 -3.6; 73 -3.5; 78 -3.6; 83 -3.7; 89 -3.8; 95 -4.1; 102 -4.3; 109 -4.4; 117 -4.7; 125 -5.0; 134 -5.2; 143 -5.2; 153 -5.3; 164 -5.1; 175 -4.8; 188 -4.7; 201 -4.4; 215 -4.0; 230 -3.7; 246 -3.3; 263 -2.9; 282 -2.6; 301 -2.3; 323 -1.9; 345 -1.5; 369 -1.3; 395 -1.0; 423 -0.7; 452 -0.6; 484 -0.6; 518 -0.6; 554 -0.3; 593 -0.1; 635 -0.3; 679 -0.6; 726 -0.6; 777 -0.4; 832 -0.2; 890 -0.1; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.8; 1429 -0.0; 1529 1.0; 1636 1.1; 1751 2.1; 1873 3.5; 2004 4.6; 2145 5.5; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 5.9; 3219 5.6; 3444 4.8; 3685 3.7; 3943 2.8; 4219 1.4; 4514 1.9; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.53 | -4.4 dB |
| Peaking | 156 Hz  | 0.8  | -4.8 dB |
| Peaking | 7918 Hz | 2.13 | -1.8 dB |
| Peaking | 2608 Hz | 1.75 | 6.6 dB  |
| Peaking | 5884 Hz | 2.44 | 6.6 dB  |
| Peaking | 1306 Hz | 3.28 | -1.6 dB |
| Peaking | 2015 Hz | 6.86 | 1.3 dB  |
| Peaking | 4456 Hz | 9.82 | -2.8 dB |
| Peaking | 4305 Hz | 3.02 | 2.4 dB  |
| Peaking | 4177 Hz | 7.73 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QC3/Bose%20QC3.png)