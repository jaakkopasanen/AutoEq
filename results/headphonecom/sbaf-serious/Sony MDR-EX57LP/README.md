# Sony MDR-EX57LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 1.1; 22 0.6; 23 0.3; 25 -0.1; 26 -0.3; 28 -0.7; 30 -1.1; 32 -1.4; 35 -1.8; 37 -2.1; 40 -2.5; 42 -2.7; 45 -3.0; 49 -3.3; 52 -3.6; 56 -4.0; 59 -4.2; 64 -4.6; 68 -4.9; 73 -5.2; 78 -5.4; 83 -5.6; 89 -5.9; 95 -6.1; 102 -6.3; 109 -6.4; 117 -6.6; 125 -6.8; 134 -6.9; 143 -7.0; 153 -7.0; 164 -7.0; 175 -7.0; 188 -6.9; 201 -6.7; 215 -6.5; 230 -6.4; 246 -6.1; 263 -5.9; 282 -5.6; 301 -5.2; 323 -4.8; 345 -4.4; 369 -3.9; 395 -3.5; 423 -3.1; 452 -2.7; 484 -2.3; 518 -1.9; 554 -1.5; 593 -1.0; 635 -0.6; 679 -0.3; 726 -0.2; 777 0.0; 832 0.8; 890 0.6; 952 0.3; 1019 0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.4; 1529 -3.2; 1636 -3.7; 1751 -4.1; 1873 -4.0; 2004 -3.5; 2145 -3.2; 2295 -3.2; 2455 -3.4; 2627 -3.7; 2811 -4.0; 3008 -3.9; 3219 -2.9; 3444 -1.9; 3685 -1.4; 3943 -2.1; 4219 -3.8; 4514 -5.8; 4830 -7.4; 5168 -8.4; 5530 -6.9; 5917 -3.2; 6331 -0.0; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.5; 10879 -3.0; 11640 -3.6; 12455 -2.0; 13327 -0.2; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.572218547451555dB` and instead set Global volume in the UI for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX57LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 109 Hz   | 0.58 | -5.9 dB |
| Peaking | 248 Hz   | 1.06 | -3.6 dB |
| Peaking | 1762 Hz  | 2.95 | -3.8 dB |
| Peaking | 2763 Hz  | 2.82 | -3.4 dB |
| Peaking | 5047 Hz  | 4.41 | -8.9 dB |
| Peaking | 21 Hz    | 2.05 | 1.6 dB  |
| Peaking | 855 Hz   | 3.56 | 1.6 dB  |
| Peaking | 5615 Hz  | 7.47 | -2.3 dB |
| Peaking | 6776 Hz  | 4.6  | 3.6 dB  |
| Peaking | 11435 Hz | 5.29 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX57LP/Sony%20MDR-EX57LP.png)