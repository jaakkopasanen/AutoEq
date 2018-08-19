# Sony MDR-V6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.6; 35 4.8; 37 4.3; 40 3.5; 42 3.1; 45 2.6; 49 1.9; 52 1.5; 56 1.4; 59 1.6; 64 1.4; 68 0.9; 73 0.5; 78 0.2; 83 0.1; 89 -0.1; 95 -0.2; 102 -0.2; 109 -0.2; 117 -0.3; 125 -0.2; 134 -0.3; 143 -0.2; 153 -0.2; 164 0.4; 175 1.3; 188 2.6; 201 2.7; 215 2.1; 230 1.3; 246 1.1; 263 1.6; 282 1.7; 301 1.6; 323 1.4; 345 1.0; 369 0.3; 395 -0.3; 423 -0.6; 452 -0.8; 484 -0.8; 518 -0.9; 554 -0.8; 593 -0.6; 635 -0.4; 679 -0.3; 726 -0.3; 777 -0.3; 832 -0.2; 890 -0.3; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -1.1; 1336 -1.3; 1429 -1.9; 1529 -2.8; 1636 -3.4; 1751 -3.9; 1873 -4.1; 2004 -4.2; 2145 -4.3; 2295 -4.1; 2455 -3.8; 2627 -4.3; 2811 -4.8; 3008 -5.0; 3219 -4.3; 3444 -3.6; 3685 -2.4; 3943 -2.4; 4219 -4.7; 4514 -6.2; 4830 -4.2; 5168 -0.9; 5530 1.8; 5917 3.0; 6331 2.0; 6775 -0.7; 7249 -2.6; 7756 -3.4; 8299 -4.8; 8880 -7.2; 9502 -8.9; 10167 -7.7; 10879 -3.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.2  | 6.6 dB  |
| Peaking | 211 Hz   | 2.99 | 2.4 dB  |
| Peaking | 1869 Hz  | 2.16 | -3.2 dB |
| Peaking | 3130 Hz  | 1.45 | -4.1 dB |
| Peaking | 9484 Hz  | 4.02 | -9.6 dB |
| Peaking | 302 Hz   | 6.49 | 1.4 dB  |
| Peaking | 4606 Hz  | 5.84 | -6.4 dB |
| Peaking | 6066 Hz  | 2.1  | 7.4 dB  |
| Peaking | 7175 Hz  | 2.21 | -5.0 dB |
| Peaking | 11953 Hz | 5.9  | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)