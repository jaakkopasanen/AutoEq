# Mayflower Electronics T50RP Version 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 10 -84; 20 0.9; 22 0.8; 23 0.8; 25 0.8; 26 0.8; 28 0.9; 30 1.1; 32 1.3; 35 1.6; 37 1.7; 40 1.8; 42 1.8; 45 1.9; 49 1.9; 52 1.9; 56 1.6; 59 1.3; 64 1.1; 68 1.1; 73 1.1; 78 1.2; 83 1.1; 89 -0.0; 95 -1.4; 102 -3.3; 109 -4.5; 117 -5.3; 125 -5.7; 134 -5.8; 143 -5.5; 153 -5.0; 164 -4.1; 175 -5.6; 188 -5.8; 201 -5.6; 215 -5.3; 230 -5.0; 246 -4.9; 263 -4.7; 282 -4.3; 301 -4.1; 323 -3.7; 345 -3.1; 369 -2.2; 395 -1.5; 423 -1.1; 452 -1.0; 484 -1.2; 518 -0.6; 554 0.0; 593 0.8; 635 1.4; 679 1.6; 726 1.2; 777 0.5; 832 -0.2; 890 -0.6; 952 -0.3; 1019 -0.1; 1090 -0.9; 1167 -1.9; 1248 -2.5; 1336 -3.3; 1429 -4.3; 1529 -5.2; 1636 -5.4; 1751 -5.7; 1873 -6.0; 2004 -6.6; 2145 -7.0; 2295 -7.7; 2455 -7.8; 2627 -7.5; 2811 -8.6; 3008 -9.2; 3219 -9.2; 3444 -8.7; 3685 -8.2; 3943 -8.0; 4219 -7.8; 4514 -6.6; 4830 -4.7; 5168 -2.5; 5530 -1.8; 5917 -2.2; 6331 -3.5; 6775 -2.9; 7249 -2.4; 7756 -5.4; 8299 -10.7; 8880 -14.9; 9502 -14.5; 10167 -9.1; 10879 -1.7; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.974621316205702dB` and instead set Global volume in the UI for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mayflower Electronics T50RP Version 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 122 Hz   | 1.99 | -6.2 dB  |
| Peaking | 206 Hz   | 0.23 | 5.9 dB   |
| Peaking | 233 Hz   | 0.72 | -10.5 dB |
| Peaking | 2715 Hz  | 0.8  | -9.4 dB  |
| Peaking | 9136 Hz  | 4.99 | -16.1 dB |
| Peaking | 672 Hz   | 6.64 | 1.5 dB   |
| Peaking | 4288 Hz  | 3.31 | -2.7 dB  |
| Peaking | 5331 Hz  | 3.31 | 3.1 dB   |
| Peaking | 10004 Hz | 5.71 | -5.1 dB  |
| Peaking | 11189 Hz | 3.06 | 4.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Mayflower%20Electronics%20T50RP%20Version%202/Mayflower%20Electronics%20T50RP%20Version%202.png)