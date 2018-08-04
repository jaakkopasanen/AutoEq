# Stax SR-007 SZ3-1576

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.1; 37 4.6; 40 4.2; 42 4.0; 45 4.0; 49 4.3; 52 4.7; 56 5.2; 59 5.3; 64 4.9; 68 4.0; 73 3.1; 78 3.2; 83 3.6; 89 3.9; 95 3.9; 102 3.7; 109 3.6; 117 3.4; 125 3.2; 134 3.1; 143 3.0; 153 2.9; 164 2.8; 175 2.8; 188 2.8; 201 2.8; 215 2.9; 230 2.9; 246 2.8; 263 2.8; 282 2.9; 301 2.7; 323 2.7; 345 2.7; 369 2.6; 395 2.5; 423 2.5; 452 2.3; 484 2.2; 518 3.0; 554 4.4; 593 3.4; 635 2.5; 679 1.9; 726 1.5; 777 1.2; 832 0.6; 890 0.1; 952 -0.0; 1019 0.3; 1090 0.5; 1167 1.1; 1248 3.4; 1336 5.0; 1429 4.1; 1529 0.8; 1636 -0.0; 1751 1.0; 1873 3.0; 2004 4.2; 2145 4.7; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.2; 4830 3.8; 5168 4.3; 5530 5.8; 5917 5.7; 6331 4.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 SZ3-1576 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.63 | 4.1 dB  |
| Peaking | 85 Hz   | 0.2  | 3.2 dB  |
| Peaking | 561 Hz  | 5.63 | 2.8 dB  |
| Peaking | 3087 Hz | 1.03 | 6.5 dB  |
| Peaking | 5803 Hz | 4.42 | 3.9 dB  |
| Peaking | 1028 Hz | 1.78 | -3.4 dB |
| Peaking | 1353 Hz | 5.68 | 4.3 dB  |
| Peaking | 1619 Hz | 5.15 | -4.3 dB |
| Peaking | 1208 Hz | 0.81 | 2.0 dB  |
| Peaking | 8667 Hz | 2.9  | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007%20SZ3-1576/Stax%20SR-007%20SZ3-1576.png)