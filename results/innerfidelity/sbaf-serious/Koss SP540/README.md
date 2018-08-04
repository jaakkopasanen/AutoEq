# Koss SP540

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 10 -84; 20 -8.7; 22 -9.1; 23 -9.2; 25 -9.5; 26 -9.6; 28 -9.8; 30 -10.0; 32 -10.1; 35 -10.2; 37 -10.3; 40 -10.4; 42 -10.5; 45 -10.6; 49 -10.6; 52 -10.6; 56 -10.6; 59 -10.7; 64 -10.7; 68 -10.7; 73 -10.8; 78 -10.8; 83 -10.9; 89 -11.1; 95 -11.2; 102 -11.4; 109 -11.5; 117 -11.7; 125 -11.8; 134 -11.9; 143 -12.0; 153 -12.3; 164 -12.3; 175 -11.4; 188 -11.1; 201 -11.0; 215 -10.9; 230 -11.0; 246 -11.3; 263 -11.1; 282 -10.1; 301 -9.3; 323 -9.6; 345 -9.2; 369 -8.2; 395 -7.1; 423 -6.2; 452 -5.7; 484 -5.2; 518 -4.6; 554 -3.9; 593 -3.1; 635 -2.8; 679 -2.6; 726 -2.3; 777 -1.8; 832 -1.5; 890 -1.0; 952 -0.5; 1019 0.2; 1090 0.8; 1167 1.4; 1248 1.4; 1336 1.2; 1429 0.8; 1529 -0.0; 1636 -1.0; 1751 -1.8; 1873 -2.4; 2004 -2.9; 2145 -3.7; 2295 -4.7; 2455 -5.5; 2627 -6.2; 2811 -7.0; 3008 -7.3; 3219 -7.7; 3444 -6.7; 3685 -5.9; 3943 -4.5; 4219 -2.7; 4514 -0.2; 4830 1.8; 5168 -1.1; 5530 -2.5; 5917 0.3; 6331 1.1; 6775 -0.2; 7249 -1.9; 7756 -1.9; 8299 -1.8; 8880 -1.9; 9502 -1.3; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -1.6; 17469 -2.3; 18692 -2.7; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.4dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 0.93 | -8.5 dB |
| Peaking | 43 Hz   | 0.38 | -8.9 dB |
| Peaking | 153 Hz  | 0.76 | -7.3 dB |
| Peaking | 314 Hz  | 1.19 | -5.7 dB |
| Peaking | 3017 Hz | 2.09 | -8.1 dB |
| Peaking | 1258 Hz | 2.87 | 2.8 dB  |
| Peaking | 1895 Hz | 3.92 | -0.9 dB |
| Peaking | 2277 Hz | 6.39 | -1.2 dB |
| Peaking | 6620 Hz | 2.39 | 3.2 dB  |
| Peaking | 7536 Hz | 2.42 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP540/Koss%20SP540.png)