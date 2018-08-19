# Denon AH-C560R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 10 -84; 20 -4.6; 22 -5.1; 23 -5.3; 25 -5.6; 26 -5.8; 28 -6.1; 30 -6.3; 32 -6.5; 35 -6.9; 37 -7.0; 40 -7.3; 42 -7.4; 45 -7.6; 49 -7.9; 52 -8.1; 56 -8.3; 59 -8.6; 64 -8.9; 68 -9.1; 73 -9.3; 78 -9.5; 83 -9.5; 89 -9.7; 95 -9.9; 102 -9.9; 109 -10.0; 117 -10.1; 125 -10.2; 134 -10.1; 143 -10.2; 153 -10.2; 164 -10.1; 175 -10.0; 188 -9.8; 201 -9.6; 215 -9.3; 230 -9.1; 246 -8.8; 263 -8.5; 282 -8.1; 301 -7.6; 323 -7.2; 345 -6.6; 369 -6.1; 395 -5.6; 423 -5.1; 452 -4.7; 484 -4.2; 518 -3.7; 554 -3.1; 593 -2.8; 635 -2.9; 679 -2.2; 726 -1.7; 777 -1.3; 832 -1.0; 890 -0.8; 952 -0.3; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.8; 1636 -2.1; 1751 -2.2; 1873 -2.1; 2004 -2.1; 2145 -2.0; 2295 -1.9; 2455 -2.0; 2627 -2.2; 2811 -2.4; 3008 -2.5; 3219 -2.3; 3444 -1.7; 3685 -1.5; 3943 -2.2; 4219 -3.7; 4514 -5.2; 4830 -6.3; 5168 -7.2; 5530 -8.5; 5917 -8.5; 6331 -6.5; 6775 -4.8; 7249 -4.1; 7756 -4.7; 8299 -6.7; 8880 -8.6; 9502 -8.1; 10167 -3.9; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.5; 15258 -2.7; 16326 -0.7; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.11373330378243307dB` and instead set Global volume in the UI for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.43 | -4.7 dB |
| Peaking | 99 Hz    | 0.59 | -5.2 dB |
| Peaking | 233 Hz   | 0.62 | -6.4 dB |
| Peaking | 5545 Hz  | 1.74 | -7.9 dB |
| Peaking | 8980 Hz  | 4.95 | -8.0 dB |
| Peaking | 1058 Hz  | 1.54 | 2.6 dB  |
| Peaking | 1578 Hz  | 0.71 | -2.1 dB |
| Peaking | 3791 Hz  | 4.99 | 1.8 dB  |
| Peaking | 11587 Hz | 4.12 | 1.7 dB  |
| Peaking | 15145 Hz | 5.8  | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)