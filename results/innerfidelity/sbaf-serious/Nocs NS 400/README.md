# Nocs NS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -12.4; 22 -12.3; 23 -12.2; 25 -12.1; 26 -12.1; 28 -12.0; 30 -11.8; 32 -11.7; 35 -11.5; 37 -11.4; 40 -11.2; 42 -11.0; 45 -10.8; 49 -10.5; 52 -10.3; 56 -10.1; 59 -9.9; 64 -9.6; 68 -9.4; 73 -9.2; 78 -9.0; 83 -8.9; 89 -8.9; 95 -9.1; 102 -9.2; 109 -9.3; 117 -9.4; 125 -9.5; 134 -9.7; 143 -9.6; 153 -9.4; 164 -9.1; 175 -8.7; 188 -8.3; 201 -7.9; 215 -7.4; 230 -7.0; 246 -6.5; 263 -6.1; 282 -5.6; 301 -5.1; 323 -4.6; 345 -4.1; 369 -3.7; 395 -3.2; 423 -2.7; 452 -2.2; 484 -1.9; 518 -1.5; 554 -1.1; 593 -0.5; 635 -0.2; 679 -0.1; 726 0.2; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.3; 1429 -1.6; 1529 -1.9; 1636 -2.2; 1751 -2.5; 1873 -2.7; 2004 -3.0; 2145 -3.8; 2295 -4.4; 2455 -4.2; 2627 -4.1; 2811 -3.4; 3008 -1.7; 3219 0.1; 3444 1.9; 3685 2.5; 3943 2.3; 4219 0.9; 4514 -0.4; 4830 -1.0; 5168 -1.7; 5530 -3.5; 5917 -5.8; 6331 -7.8; 6775 -6.2; 7249 -4.2; 7756 -2.5; 8299 -1.9; 8880 -2.2; 9502 -2.6; 10167 -1.9; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.3; 18692 -0.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 8 Hz    | 0.88 | -12.2 dB |
| Peaking | 31 Hz   | 0.31 | -10.0 dB |
| Peaking | 172 Hz  | 0.77 | -6.4 dB  |
| Peaking | 2274 Hz | 2.89 | -4.6 dB  |
| Peaking | 6450 Hz | 3.83 | -7.9 dB  |
| Peaking | 796 Hz  | 1.19 | 4.0 dB   |
| Peaking | 2814 Hz | 7.95 | -2.0 dB  |
| Peaking | 872 Hz  | 0.65 | -2.7 dB  |
| Peaking | 3699 Hz | 3.81 | 4.0 dB   |
| Peaking | 9532 Hz | 5.6  | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS%20400/Nocs%20NS%20400.png)