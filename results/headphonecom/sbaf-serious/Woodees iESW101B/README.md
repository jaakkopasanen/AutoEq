# Woodees iESW101B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 10 -84; 20 -9.4; 22 -9.4; 23 -9.3; 25 -9.3; 26 -9.2; 28 -9.2; 30 -9.1; 32 -9.0; 35 -8.9; 37 -8.9; 40 -8.8; 42 -8.8; 45 -8.7; 49 -8.7; 52 -8.6; 56 -8.6; 59 -8.5; 64 -8.5; 68 -8.5; 73 -8.4; 78 -8.3; 83 -8.3; 89 -8.2; 95 -8.0; 102 -7.8; 109 -7.7; 117 -7.5; 125 -7.3; 134 -7.1; 143 -6.9; 153 -6.7; 164 -6.4; 175 -6.0; 188 -5.7; 201 -5.3; 215 -5.0; 230 -4.6; 246 -4.2; 263 -3.8; 282 -3.3; 301 -2.8; 323 -2.3; 345 -1.9; 369 -1.3; 395 -0.9; 423 -0.4; 452 0.0; 484 0.4; 518 0.8; 554 1.1; 593 1.2; 635 1.4; 679 1.4; 726 1.3; 777 1.1; 832 0.9; 890 0.6; 952 0.4; 1019 -0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.6; 1429 -2.2; 1529 -2.9; 1636 -3.4; 1751 -3.8; 1873 -4.1; 2004 -4.6; 2145 -5.1; 2295 -5.7; 2455 -6.5; 2627 -7.3; 2811 -7.2; 3008 -5.1; 3219 -2.2; 3444 0.3; 3685 1.5; 3943 1.1; 4219 -0.4; 4514 -2.0; 4830 -3.5; 5168 -5.3; 5530 -9.4; 5917 -11.4; 6331 -6.1; 6775 -2.4; 7249 -0.5; 7756 0.2; 8299 -0.2; 8880 -2.3; 9502 -4.9; 10167 -4.7; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.2; 17469 -0.3; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.6884697052624582dB` and instead set Global volume in the UI for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW101B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.28 | -9.1 dB  |
| Peaking | 145 Hz   | 0.92 | -3.8 dB  |
| Peaking | 2412 Hz  | 2.23 | -7.1 dB  |
| Peaking | 5797 Hz  | 5.81 | -12.1 dB |
| Peaking | 21648 Hz | 1.79 | -2.2 dB  |
| Peaking | 669 Hz   | 0.84 | 5.7 dB   |
| Peaking | 745 Hz   | 0.43 | -3.6 dB  |
| Peaking | 3752 Hz  | 5.14 | 4.4 dB   |
| Peaking | 4906 Hz  | 5.68 | -0.9 dB  |
| Peaking | 9790 Hz  | 7.55 | -5.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW101B/Woodees%20iESW101B.png)