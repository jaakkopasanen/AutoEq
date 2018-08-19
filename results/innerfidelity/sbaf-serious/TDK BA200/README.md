# TDK BA200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.2; 22 0.2; 23 0.1; 25 0.1; 26 0.1; 28 0.0; 30 -0.0; 32 -0.1; 35 -0.2; 37 -0.3; 40 -0.4; 42 -0.4; 45 -0.5; 49 -0.7; 52 -0.8; 56 -1.0; 59 -1.1; 64 -1.4; 68 -1.6; 73 -1.9; 78 -2.1; 83 -2.4; 89 -2.7; 95 -3.0; 102 -3.2; 109 -3.3; 117 -3.4; 125 -3.7; 134 -3.9; 143 -3.9; 153 -4.1; 164 -4.1; 175 -4.1; 188 -4.2; 201 -4.2; 215 -4.1; 230 -4.0; 246 -3.9; 263 -3.8; 282 -3.6; 301 -3.4; 323 -3.3; 345 -3.1; 369 -2.9; 395 -2.7; 423 -2.3; 452 -1.9; 484 -1.7; 518 -1.5; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.4; 832 0.4; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.6; 1529 -2.0; 1636 -2.5; 1751 -2.7; 1873 -2.7; 2004 -2.4; 2145 -2.0; 2295 -1.3; 2455 -0.1; 2627 1.1; 2811 2.3; 3008 4.0; 3219 5.4; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.7; 4514 3.0; 4830 3.8; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.5; 8880 -3.9; 9502 -4.2; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999979483248dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK BA200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 180 Hz  | 0.6  | -4.4 dB |
| Peaking | 1915 Hz | 2.2  | -3.6 dB |
| Peaking | 3464 Hz | 2.46 | 6.3 dB  |
| Peaking | 5902 Hz | 2.62 | 6.1 dB  |
| Peaking | 9109 Hz | 4.39 | -5.6 dB |
| Peaking | 25 Hz   | 1.07 | 0.3 dB  |
| Peaking | 382 Hz  | 2.27 | -0.7 dB |
| Peaking | 795 Hz  | 1.73 | 1.1 dB  |
| Peaking | 1492 Hz | 4.91 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20BA200/TDK%20BA200.png)