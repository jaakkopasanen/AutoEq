# Oppo PM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.5; 22 3.1; 23 2.9; 25 2.7; 26 2.6; 28 2.4; 30 2.2; 32 2.1; 35 1.9; 37 1.9; 40 2.0; 42 2.1; 45 2.5; 49 3.1; 52 2.7; 56 1.2; 59 0.3; 64 0.1; 68 -0.0; 73 -0.1; 78 -0.4; 83 -0.6; 89 -0.8; 95 -1.1; 102 -1.3; 109 -1.4; 117 -1.5; 125 -1.6; 134 -1.9; 143 -2.0; 153 -2.1; 164 -2.0; 175 -2.3; 188 -2.3; 201 -2.2; 215 -2.1; 230 -1.9; 246 -1.9; 263 -2.1; 282 -2.4; 301 -2.4; 323 -2.3; 345 -1.8; 369 -1.2; 395 -0.5; 423 -0.0; 452 -0.5; 484 -1.0; 518 -1.2; 554 -1.2; 593 -1.0; 635 -0.9; 679 -1.0; 726 -1.1; 777 -1.2; 832 -1.4; 890 -1.3; 952 -0.5; 1019 0.2; 1090 0.8; 1167 0.9; 1248 1.1; 1336 0.2; 1429 -0.1; 1529 0.0; 1636 -0.0; 1751 0.3; 1873 0.8; 2004 1.1; 2145 1.4; 2295 2.0; 2455 2.6; 2627 2.9; 2811 2.8; 3008 3.1; 3219 3.1; 3444 3.1; 3685 3.1; 3943 3.1; 4219 3.2; 4514 3.5; 4830 4.6; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -2.3; 9502 -2.0; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.090907327114606dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.43 | 3.7 dB  |
| Peaking | 134 Hz  | 0.35 | -3.0 dB |
| Peaking | 2926 Hz | 1.6  | 2.6 dB  |
| Peaking | 5740 Hz | 1.99 | 6.2 dB  |
| Peaking | 8962 Hz | 3.3  | -3.5 dB |
| Peaking | 310 Hz  | 5.2  | -0.7 dB |
| Peaking | 412 Hz  | 5.93 | 1.5 dB  |
| Peaking | 880 Hz  | 2.37 | -1.9 dB |
| Peaking | 1154 Hz | 1.99 | 2.2 dB  |
| Peaking | 1450 Hz | 2.83 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)