# Sennheiser HD555

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.6; 22 4.8; 23 4.4; 25 3.8; 26 3.5; 28 2.9; 30 2.5; 32 2.0; 35 1.5; 37 1.2; 40 0.8; 42 0.6; 45 0.2; 49 -0.1; 52 -0.3; 56 -0.2; 59 -0.3; 64 -0.2; 68 0.4; 73 0.4; 78 -0.5; 83 -1.0; 89 -1.2; 95 -1.3; 102 -1.4; 109 -1.4; 117 -1.3; 125 -1.3; 134 -1.4; 143 -1.4; 153 -1.4; 164 -1.2; 175 -1.3; 188 -1.3; 201 -1.4; 215 -1.4; 230 -1.3; 246 -1.3; 263 -1.3; 282 -1.2; 301 -1.1; 323 -0.9; 345 -0.8; 369 -0.7; 395 -0.5; 423 -0.2; 452 -0.1; 484 -0.2; 518 -0.1; 554 -0.0; 593 0.6; 635 0.4; 679 0.3; 726 0.3; 777 0.3; 832 0.4; 890 0.3; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.6; 1336 0.9; 1429 1.2; 1529 1.5; 1636 1.8; 1751 1.3; 1873 0.8; 2004 0.7; 2145 0.5; 2295 0.3; 2455 0.5; 2627 0.8; 2811 0.8; 3008 0.2; 3219 -0.7; 3444 -0.7; 3685 -0.1; 3943 2.0; 4219 3.4; 4514 0.5; 4830 -0.1; 5168 2.2; 5530 5.2; 5917 5.9; 6331 4.2; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.6; 18692 -3.5; 20000 -2.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.22 | 5.5 dB  |
| Peaking | 161 Hz   | 0.48 | -1.5 dB |
| Peaking | 623 Hz   | 1.88 | 0.7 dB  |
| Peaking | 1598 Hz  | 2.86 | 1.7 dB  |
| Peaking | 5920 Hz  | 4.08 | 6.2 dB  |
| Peaking | 70 Hz    | 6.92 | 0.8 dB  |
| Peaking | 3542 Hz  | 5.49 | -2.1 dB |
| Peaking | 4197 Hz  | 4.53 | 4.0 dB  |
| Peaking | 4671 Hz  | 7.46 | -3.6 dB |
| Peaking | 19250 Hz | 2.13 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD555/Sennheiser%20HD555.png)