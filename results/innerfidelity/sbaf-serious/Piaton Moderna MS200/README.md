# Piaton Moderna MS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.3; 22 0.7; 23 0.4; 25 -0.2; 26 -0.5; 28 -1.0; 30 -1.5; 32 -1.9; 35 -2.5; 37 -2.8; 40 -3.3; 42 -3.7; 45 -4.1; 49 -4.6; 52 -4.9; 56 -5.4; 59 -5.7; 64 -6.2; 68 -6.6; 73 -7.0; 78 -7.4; 83 -7.8; 89 -8.1; 95 -8.6; 102 -8.9; 109 -9.2; 117 -9.2; 125 -9.4; 134 -9.7; 143 -9.9; 153 -10.0; 164 -10.1; 175 -10.0; 188 -10.1; 201 -10.0; 215 -10.0; 230 -9.8; 246 -9.7; 263 -9.5; 282 -9.3; 301 -9.0; 323 -8.7; 345 -8.4; 369 -8.1; 395 -7.5; 423 -6.8; 452 -6.2; 484 -6.5; 518 -6.3; 554 -5.6; 593 -4.8; 635 -4.0; 679 -3.5; 726 -2.7; 777 -1.9; 832 -1.2; 890 -0.7; 952 -0.3; 1019 0.1; 1090 0.3; 1167 0.4; 1248 0.4; 1336 0.0; 1429 -1.0; 1529 -1.8; 1636 -2.3; 1751 -2.9; 1873 -3.3; 2004 -3.5; 2145 -3.6; 2295 -3.3; 2455 -2.0; 2627 -0.4; 2811 1.6; 3008 3.5; 3219 5.0; 3444 5.9; 3685 6.0; 3943 5.6; 4219 3.8; 4514 2.3; 4830 1.8; 5168 2.1; 5530 2.3; 5917 1.2; 6331 -0.8; 6775 -1.9; 7249 -2.9; 7756 -3.5; 8299 -3.7; 8880 -3.6; 9502 -3.2; 10167 -2.5; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999529967255dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton Moderna MS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 139 Hz  | 0.43 | -9.0 dB  |
| Peaking | 421 Hz  | 0.66 | -4.9 dB  |
| Peaking | 2161 Hz | 1.04 | -17.1 dB |
| Peaking | 2980 Hz | 0.41 | 16.3 dB  |
| Peaking | 7659 Hz | 0.92 | -9.9 dB  |
| Peaking | 20 Hz   | 2.05 | 2.0 dB   |
| Peaking | 2681 Hz | 6.11 | -1.2 dB  |
| Peaking | 3759 Hz | 2.5  | 2.2 dB   |
| Peaking | 4557 Hz | 3.17 | -3.1 dB  |
| Peaking | 5613 Hz | 5.53 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Piaton%20Moderna%20MS200/Piaton%20Moderna%20MS200.png)