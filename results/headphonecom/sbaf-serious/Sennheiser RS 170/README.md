# Sennheiser RS 170

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.6; 22 1.6; 23 1.2; 25 0.3; 26 -0.1; 28 -0.9; 30 -1.5; 32 -2.1; 35 -2.8; 37 -3.2; 40 -3.8; 42 -4.2; 45 -4.7; 49 -5.2; 52 -5.5; 56 -5.9; 59 -6.0; 64 -6.2; 68 -6.4; 73 -6.7; 78 -6.8; 83 -6.5; 89 -6.2; 95 -5.6; 102 -5.2; 109 -5.3; 117 -5.8; 125 -6.3; 134 -6.7; 143 -6.7; 153 -6.7; 164 -6.3; 175 -6.0; 188 -6.3; 201 -6.1; 215 -5.3; 230 -4.4; 246 -4.0; 263 -3.6; 282 -3.3; 301 -2.7; 323 -2.1; 345 -1.7; 369 -1.4; 395 -1.5; 423 -1.7; 452 -1.8; 484 -1.7; 518 -1.3; 554 -0.6; 593 0.0; 635 0.4; 679 0.5; 726 0.7; 777 1.6; 832 2.6; 890 1.6; 952 0.4; 1019 -0.0; 1090 0.9; 1167 -0.1; 1248 -1.3; 1336 -2.2; 1429 -3.2; 1529 -4.2; 1636 -5.5; 1751 -4.3; 1873 -1.3; 2004 -3.2; 2145 -4.0; 2295 -4.4; 2455 -4.3; 2627 -4.2; 2811 -4.3; 3008 -3.6; 3219 -3.7; 3444 -3.5; 3685 -3.0; 3943 -1.4; 4219 0.3; 4514 4.5; 4830 6.0; 5168 2.5; 5530 2.0; 5917 2.1; 6331 0.3; 6775 -1.0; 7249 1.1; 7756 0.3; 8299 -1.3; 8880 -3.8; 9502 -4.8; 10167 -3.6; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 170 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.98 | -5.9 dB |
| Peaking | 170 Hz  | 1.1  | -5.6 dB |
| Peaking | 1619 Hz | 6.77 | -4.0 dB |
| Peaking | 4123 Hz | 0.85 | -9.4 dB |
| Peaking | 4762 Hz | 2.17 | 14.1 dB |
| Peaking | 18 Hz   | 2.82 | 2.9 dB  |
| Peaking | 836 Hz  | 2.24 | 3.3 dB  |
| Peaking | 1746 Hz | 0.16 | -0.6 dB |
| Peaking | 8987 Hz | 1.26 | 4.3 dB  |
| Peaking | 9444 Hz | 3.4  | -8.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20170/Sennheiser%20RS%20170.png)