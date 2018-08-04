# Bose QC3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.8; 23 -9.0; 25 -9.1; 26 -9.2; 28 -9.2; 30 -9.2; 32 -9.2; 35 -9.1; 37 -9.0; 40 -8.9; 42 -8.8; 45 -8.7; 49 -8.5; 52 -8.4; 56 -8.2; 59 -8.1; 64 -8.1; 68 -8.1; 73 -7.9; 78 -7.9; 83 -7.9; 89 -7.8; 95 -7.8; 102 -7.7; 109 -7.6; 117 -7.6; 125 -7.5; 134 -7.3; 143 -7.1; 153 -7.0; 164 -6.7; 175 -6.4; 188 -6.2; 201 -5.9; 215 -5.5; 230 -5.1; 246 -4.7; 263 -4.3; 282 -4.0; 301 -3.6; 323 -3.3; 345 -2.9; 369 -2.6; 395 -2.3; 423 -1.9; 452 -1.6; 484 -1.4; 518 -1.1; 554 -0.8; 593 -0.6; 635 -0.6; 679 -0.6; 726 -0.6; 777 -0.6; 832 -0.3; 890 -0.1; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 0.0; 1336 0.6; 1429 2.1; 1529 3.7; 1636 4.1; 1751 5.2; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.7; 3943 5.1; 4219 5.0; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.1  | -8.8 dB |
| Peaking | 172 Hz  | 1.34 | -0.9 dB |
| Peaking | 2471 Hz | 1.08 | 6.5 dB  |
| Peaking | 5320 Hz | 2.08 | 5.2 dB  |
| Peaking | 1229 Hz | 1.98 | -3.3 dB |
| Peaking | 2178 Hz | 0.83 | 4.6 dB  |
| Peaking | 2442 Hz | 1.96 | -4.8 dB |
| Peaking | 6438 Hz | 4.24 | 4.5 dB  |
| Peaking | 6731 Hz | 1.44 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Bose%20QC3/Bose%20QC3.png)