# TDK BA200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.3; 22 0.2; 23 0.2; 25 0.2; 26 0.2; 28 0.2; 30 0.1; 32 0.1; 35 0.1; 37 0.1; 40 0.0; 42 0.0; 45 0.0; 49 0.0; 52 0.0; 56 -0.0; 59 -0.0; 64 -0.1; 68 -0.2; 73 -0.3; 78 -0.5; 83 -0.8; 89 -1.2; 95 -1.6; 102 -2.2; 109 -2.5; 117 -3.0; 125 -3.7; 134 -4.1; 143 -4.3; 153 -4.6; 164 -4.7; 175 -4.7; 188 -4.7; 201 -4.6; 215 -4.5; 230 -4.3; 246 -4.2; 263 -4.1; 282 -3.8; 301 -3.6; 323 -3.4; 345 -3.2; 369 -3.0; 395 -2.8; 423 -2.3; 452 -2.0; 484 -1.8; 518 -1.5; 554 -1.1; 593 -0.6; 635 -0.3; 679 -0.2; 726 0.0; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.6; 1529 -2.0; 1636 -2.5; 1751 -2.7; 1873 -2.7; 2004 -2.4; 2145 -2.0; 2295 -1.3; 2455 -0.1; 2627 1.1; 2811 2.3; 3008 4.0; 3219 5.4; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.7; 4514 3.0; 4830 3.8; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.5; 8880 -3.9; 9502 -4.2; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK BA200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 200 Hz  | 0.81 | -5.0 dB |
| Peaking | 1911 Hz | 2.13 | -3.6 dB |
| Peaking | 3462 Hz | 2.46 | 6.3 dB  |
| Peaking | 5896 Hz | 2.62 | 6.1 dB  |
| Peaking | 9022 Hz | 4.39 | -5.6 dB |
| Peaking | 82 Hz   | 0.71 | 1.1 dB  |
| Peaking | 132 Hz  | 1.48 | -1.5 dB |
| Peaking | 208 Hz  | 1.71 | 0.8 dB  |
| Peaking | 379 Hz  | 1.65 | -0.8 dB |
| Peaking | 790 Hz  | 2.34 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20BA200/TDK%20BA200.png)