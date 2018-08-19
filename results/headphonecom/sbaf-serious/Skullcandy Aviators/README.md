# Skullcandy Aviators

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 4.9; 22 3.7; 23 3.2; 25 2.1; 26 1.7; 28 0.7; 30 -0.1; 32 -0.9; 35 -2.0; 37 -2.7; 40 -3.6; 42 -4.2; 45 -5.0; 49 -5.8; 52 -6.3; 56 -6.9; 59 -7.4; 64 -8.2; 68 -8.7; 73 -9.3; 78 -9.6; 83 -9.9; 89 -10.1; 95 -10.4; 102 -10.6; 109 -10.8; 117 -10.9; 125 -11.0; 134 -11.0; 143 -11.1; 153 -11.0; 164 -11.1; 175 -11.0; 188 -11.0; 201 -11.0; 215 -10.8; 230 -10.8; 246 -10.5; 263 -10.2; 282 -9.6; 301 -9.2; 323 -9.3; 345 -9.1; 369 -8.9; 395 -8.8; 423 -8.5; 452 -8.3; 484 -8.1; 518 -8.0; 554 -7.4; 593 -6.5; 635 -5.6; 679 -6.1; 726 -5.5; 777 -3.9; 832 -2.2; 890 -0.6; 952 0.3; 1019 -0.0; 1090 -0.5; 1167 -1.7; 1248 -3.3; 1336 -4.8; 1429 -6.1; 1529 -6.7; 1636 -7.3; 1751 -7.4; 1873 -7.4; 2004 -6.9; 2145 -6.4; 2295 -6.1; 2455 -5.6; 2627 -5.4; 2811 -6.0; 3008 -6.7; 3219 -7.2; 3444 -7.0; 3685 -6.5; 3943 -8.2; 4219 -11.4; 4514 -12.9; 4830 -11.8; 5168 -8.9; 5530 -6.2; 5917 -3.2; 6331 -1.4; 6775 -1.6; 7249 -0.8; 7756 -2.2; 8299 -5.5; 8880 -8.8; 9502 -10.1; 10167 -9.1; 10879 -7.6; 11640 -6.8; 12455 -6.5; 13327 -6.2; 14260 -5.4; 15258 -3.2; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.966988870860225dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 133 Hz   | 0.47 | -11.3 dB |
| Peaking | 423 Hz   | 1.17 | -4.7 dB  |
| Peaking | 1991 Hz  | 1.43 | -6.7 dB  |
| Peaking | 4473 Hz  | 3.13 | -11.8 dB |
| Peaking | 10729 Hz | 1.51 | -8.9 dB  |
| Peaking | 22 Hz    | 2.3  | 5.8 dB   |
| Peaking | 991 Hz   | 2.66 | 7.5 dB   |
| Peaking | 998 Hz   | 1.05 | -3.6 dB  |
| Peaking | 7157 Hz  | 3.66 | 3.8 dB   |
| Peaking | 9047 Hz  | 6.38 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Aviators/Skullcandy%20Aviators.png)