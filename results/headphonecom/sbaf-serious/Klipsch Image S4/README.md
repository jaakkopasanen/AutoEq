# Klipsch Image S4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 -8.1; 22 -8.2; 23 -8.2; 25 -8.3; 26 -8.3; 28 -8.3; 30 -8.3; 32 -8.4; 35 -8.4; 37 -8.4; 40 -8.5; 42 -8.6; 45 -8.7; 49 -8.8; 52 -9.0; 56 -9.2; 59 -9.3; 64 -9.4; 68 -9.5; 73 -9.7; 78 -9.8; 83 -9.9; 89 -10.1; 95 -10.1; 102 -10.2; 109 -10.2; 117 -10.2; 125 -10.2; 134 -10.2; 143 -10.1; 153 -10.0; 164 -9.9; 175 -9.7; 188 -9.5; 201 -9.2; 215 -9.0; 230 -8.6; 246 -8.3; 263 -7.9; 282 -7.5; 301 -7.0; 323 -6.5; 345 -6.0; 369 -5.4; 395 -4.9; 423 -4.4; 452 -4.0; 484 -3.6; 518 -3.1; 554 -2.6; 593 -2.1; 635 -1.5; 679 -1.1; 726 -0.6; 777 -0.3; 832 0.0; 890 0.1; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.3; 1529 -1.8; 1636 -2.1; 1751 -2.3; 1873 -2.3; 2004 -2.5; 2145 -2.7; 2295 -2.5; 2455 -2.2; 2627 -1.8; 2811 -1.0; 3008 0.1; 3219 1.7; 3444 3.2; 3685 3.8; 3943 3.3; 4219 1.8; 4514 0.3; 4830 -0.6; 5168 -1.4; 5530 -2.7; 5917 -3.3; 6331 -1.4; 6775 1.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.2; 13327 -3.9; 14260 -6.7; 15258 -5.9; 16326 -1.8; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.943185664063502dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.32 | -7.1 dB |
| Peaking | 105 Hz   | 0.56 | -6.5 dB |
| Peaking | 241 Hz   | 0.75 | -4.9 dB |
| Peaking | 3694 Hz  | 6.8  | 4.6 dB  |
| Peaking | 14614 Hz | 3.62 | -7.7 dB |
| Peaking | 901 Hz   | 2.01 | 1.6 dB  |
| Peaking | 2266 Hz  | 1.17 | -4.5 dB |
| Peaking | 3260 Hz  | 0.87 | 2.9 dB  |
| Peaking | 5810 Hz  | 3.34 | -4.8 dB |
| Peaking | 6840 Hz  | 4.98 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4/Klipsch%20Image%20S4.png)