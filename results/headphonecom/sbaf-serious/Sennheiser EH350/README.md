# Sennheiser EH350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.6; 64 4.6; 68 4.0; 73 3.6; 78 3.3; 83 2.8; 89 2.3; 95 1.9; 102 1.4; 109 1.3; 117 1.3; 125 1.0; 134 1.2; 143 1.9; 153 1.9; 164 1.7; 175 1.7; 188 1.5; 201 1.5; 215 1.3; 230 1.4; 246 1.3; 263 1.1; 282 1.1; 301 1.0; 323 0.9; 345 0.9; 369 0.8; 395 0.8; 423 0.7; 452 0.5; 484 0.5; 518 0.6; 554 1.0; 593 1.0; 635 1.1; 679 1.3; 726 0.7; 777 0.3; 832 0.1; 890 0.1; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.1; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.5; 1636 -1.6; 1751 -1.0; 1873 0.1; 2004 0.5; 2145 1.0; 2295 1.3; 2455 1.6; 2627 1.3; 2811 1.3; 3008 1.3; 3219 0.8; 3444 1.3; 3685 3.7; 3943 6.0; 4219 4.5; 4514 -2.9; 4830 -0.4; 5168 1.9; 5530 2.5; 5917 4.8; 6331 5.6; 6775 2.8; 7249 -1.1; 7756 -3.0; 8299 -2.6; 8880 -0.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -1.5; 13327 -6.3; 14260 -8.7; 15258 -7.9; 16326 -5.9; 17469 -4.7; 18692 -4.0; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.44 | 6.4 dB  |
| Peaking | 4124 Hz  | 4.04 | 8.6 dB  |
| Peaking | 6176 Hz  | 6.74 | 6.3 dB  |
| Peaking | 4516 Hz  | 8.26 | -8.8 dB |
| Peaking | 15303 Hz | 1.57 | -8.6 dB |
| Peaking | 103 Hz   | 2.33 | -1.7 dB |
| Peaking | 1518 Hz  | 3.23 | -2.4 dB |
| Peaking | 424 Hz   | 0.11 | 0.7 dB  |
| Peaking | 7872 Hz  | 7.16 | -3.8 dB |
| Peaking | 11353 Hz | 4.09 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH350/Sennheiser%20EH350.png)