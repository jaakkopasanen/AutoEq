# Fidue A81

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 10 -84; 20 -1.8; 22 -2.3; 23 -2.4; 25 -2.7; 26 -2.9; 28 -3.1; 30 -3.2; 32 -3.4; 35 -3.6; 37 -3.7; 40 -3.9; 42 -3.9; 45 -4.0; 49 -4.1; 52 -4.2; 56 -4.3; 59 -4.3; 64 -4.4; 68 -4.4; 73 -4.5; 78 -4.7; 83 -4.9; 89 -5.1; 95 -5.6; 102 -6.0; 109 -6.4; 117 -6.8; 125 -7.2; 134 -7.5; 143 -7.7; 153 -7.7; 164 -7.6; 175 -7.5; 188 -7.2; 201 -7.0; 215 -6.7; 230 -6.4; 246 -6.0; 263 -5.7; 282 -5.3; 301 -4.9; 323 -4.5; 345 -4.0; 369 -3.6; 395 -3.3; 423 -2.7; 452 -2.3; 484 -2.0; 518 -1.6; 554 -1.1; 593 -0.6; 635 -0.3; 679 -0.2; 726 -0.0; 777 0.4; 832 0.5; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.0; 1529 -2.7; 1636 -3.2; 1751 -3.7; 1873 -4.1; 2004 -4.5; 2145 -5.1; 2295 -5.8; 2455 -6.0; 2627 -6.1; 2811 -5.2; 3008 -3.2; 3219 -1.4; 3444 -0.1; 3685 -0.2; 3943 -1.6; 4219 -4.7; 4514 -8.4; 4830 -11.7; 5168 -9.9; 5530 -4.9; 5917 -1.2; 6331 0.6; 6775 1.2; 7249 0.5; 7756 -2.1; 8299 -5.8; 8880 -8.3; 9502 -7.7; 10167 -5.6; 10879 -4.0; 11640 -2.3; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.7dB` and instead set Global volume in the UI for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A81 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.31 | -3.1 dB  |
| Peaking | 180 Hz   | 0.77 | -6.2 dB  |
| Peaking | 2298 Hz  | 2.1  | -6.0 dB  |
| Peaking | 4897 Hz  | 5.37 | -12.2 dB |
| Peaking | 22062 Hz | 1.68 | -6.4 dB  |
| Peaking | 831 Hz   | 2.21 | 1.4 dB   |
| Peaking | 1607 Hz  | 4.23 | -1.4 dB  |
| Peaking | 10522 Hz | 0.34 | 1.3 dB   |
| Peaking | 6993 Hz  | 3.46 | 5.1 dB   |
| Peaking | 9070 Hz  | 2.12 | -10.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A81/Fidue%20A81.png)