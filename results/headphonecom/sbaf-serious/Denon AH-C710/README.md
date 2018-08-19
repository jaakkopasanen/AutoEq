# Denon AH-C710

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 10 -84; 20 -12.1; 22 -12.0; 23 -12.0; 25 -11.9; 26 -11.9; 28 -11.9; 30 -11.9; 32 -11.9; 35 -11.8; 37 -11.8; 40 -11.7; 42 -11.7; 45 -11.6; 49 -11.6; 52 -11.6; 56 -11.6; 59 -11.5; 64 -11.5; 68 -11.5; 73 -11.4; 78 -11.4; 83 -11.3; 89 -11.2; 95 -11.1; 102 -10.9; 109 -10.7; 117 -10.5; 125 -10.3; 134 -10.1; 143 -9.9; 153 -9.7; 164 -9.4; 175 -9.0; 188 -8.7; 201 -8.3; 215 -7.9; 230 -7.5; 246 -7.0; 263 -6.6; 282 -6.1; 301 -5.5; 323 -4.9; 345 -4.5; 369 -4.2; 395 -3.8; 423 -3.3; 452 -2.9; 484 -2.4; 518 -1.9; 554 -1.5; 593 -1.0; 635 -0.6; 679 -0.3; 726 -0.0; 777 0.2; 832 0.3; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.2; 1636 -2.6; 1751 -2.9; 1873 -3.1; 2004 -3.6; 2145 -4.0; 2295 -4.5; 2455 -5.2; 2627 -5.9; 2811 -6.2; 3008 -5.3; 3219 -3.5; 3444 -1.5; 3685 -0.3; 3943 -0.7; 4219 -2.0; 4514 -3.4; 4830 -4.5; 5168 -5.7; 5530 -8.2; 5917 -10.7; 6331 -8.1; 6775 -4.5; 7249 -2.4; 7756 -1.1; 8299 -1.0; 8880 -2.3; 9502 -4.3; 10167 -4.4; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.43261160214535266dB` and instead set Global volume in the UI for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.2  | -11.8 dB |
| Peaking | 171 Hz   | 0.67 | -4.4 dB  |
| Peaking | 2533 Hz  | 2.1  | -5.7 dB  |
| Peaking | 5896 Hz  | 3.59 | -10.4 dB |
| Peaking | 22222 Hz | 2.18 | -1.8 dB  |
| Peaking | 829 Hz   | 2.08 | 1.5 dB   |
| Peaking | 1649 Hz  | 3.51 | -1.5 dB  |
| Peaking | 7854 Hz  | 6.05 | 1.1 dB   |
| Peaking | 8032 Hz  | 0.22 | 0.3 dB   |
| Peaking | 9804 Hz  | 5.59 | -5.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)