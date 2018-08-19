# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.5; 45 5.0; 49 4.3; 52 3.9; 56 3.4; 59 3.5; 64 4.5; 68 4.1; 73 2.6; 78 1.9; 83 1.4; 89 1.1; 95 0.8; 102 0.5; 109 0.2; 117 -0.1; 125 -0.5; 134 -0.7; 143 -0.9; 153 -1.0; 164 -1.1; 175 -1.2; 188 -1.4; 201 -1.3; 215 -1.3; 230 -1.4; 246 -1.4; 263 -1.2; 282 -1.1; 301 -1.0; 323 -0.9; 345 -0.8; 369 -0.6; 395 -0.6; 423 -0.4; 452 -0.2; 484 -0.1; 518 -0.0; 554 1.2; 593 1.7; 635 1.0; 679 1.1; 726 1.0; 777 0.7; 832 0.5; 890 0.3; 952 -0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.6; 1429 -1.1; 1529 -1.6; 1636 -1.9; 1751 -2.5; 1873 -3.4; 2004 -4.2; 2145 -4.7; 2295 -4.5; 2455 -4.0; 2627 -3.2; 2811 -2.6; 3008 -2.5; 3219 -2.1; 3444 -2.1; 3685 -1.9; 3943 -2.4; 4219 -2.9; 4514 -2.9; 4830 -1.9; 5168 -2.1; 5530 -4.0; 5917 -5.7; 6331 -5.3; 6775 -3.9; 7249 -4.1; 7756 -4.4; 8299 -4.0; 8880 -3.3; 9502 -2.2; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.45 | 6.3 dB  |
| Peaking | 163 Hz   | 0.91 | -2.3 dB |
| Peaking | 2237 Hz  | 1.94 | -4.6 dB |
| Peaking | 6094 Hz  | 2.27 | -4.7 dB |
| Peaking | 8250 Hz  | 3.71 | -2.9 dB |
| Peaking | 469 Hz   | 1.09 | -1.1 dB |
| Peaking | 611 Hz   | 1.71 | 2.4 dB  |
| Peaking | 4530 Hz  | 2.97 | -1.7 dB |
| Peaking | 5005 Hz  | 6.94 | 2.5 dB  |
| Peaking | 11090 Hz | 4.44 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K701/AKG%20K701.png)