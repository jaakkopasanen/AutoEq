# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.4; 22 -0.7; 23 -0.9; 25 -1.2; 26 -1.3; 28 -1.6; 30 -1.8; 32 -1.9; 35 -2.1; 37 -2.2; 40 -2.3; 42 -2.3; 45 -2.3; 49 -2.1; 52 -1.8; 56 -1.6; 59 -1.7; 64 -2.0; 68 -2.5; 73 -3.2; 78 -3.5; 83 -3.5; 89 -3.7; 95 -3.8; 102 -4.0; 109 -4.1; 117 -4.3; 125 -4.4; 134 -4.4; 143 -4.5; 153 -4.6; 164 -3.9; 175 -3.8; 188 -3.9; 201 -3.5; 215 -2.8; 230 -1.7; 246 -0.6; 263 0.2; 282 0.3; 301 0.1; 323 -0.2; 345 -0.3; 369 0.0; 395 -0.0; 423 0.0; 452 0.8; 484 1.2; 518 0.7; 554 0.6; 593 0.5; 635 0.4; 679 0.2; 726 -0.0; 777 -0.0; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.5; 1336 -0.9; 1429 -1.5; 1529 -2.0; 1636 -2.4; 1751 -2.7; 1873 -3.1; 2004 -2.9; 2145 -1.9; 2295 -0.8; 2455 -0.8; 2627 -1.0; 2811 -1.0; 3008 -0.4; 3219 0.4; 3444 1.8; 3685 3.2; 3943 4.2; 4219 4.9; 4514 5.8; 4830 6.0; 5168 5.2; 5530 3.3; 5917 1.6; 6331 0.0; 6775 1.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -0.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0998568309251455dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.3  | -1.6 dB |
| Peaking | 163 Hz  | 0.78 | -6.0 dB |
| Peaking | 253 Hz  | 0.65 | 3.7 dB  |
| Peaking | 1864 Hz | 1.92 | -3.2 dB |
| Peaking | 4590 Hz | 2.62 | 6.6 dB  |
| Peaking | 209 Hz  | 4    | -1.5 dB |
| Peaking | 298 Hz  | 1.38 | 2.4 dB  |
| Peaking | 337 Hz  | 2.41 | -2.8 dB |
| Peaking | 2910 Hz | 6.54 | -1.1 dB |
| Peaking | 3712 Hz | 9.2  | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)