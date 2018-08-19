# FLC Technologies FLC8 Bk Gy Bk

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.9; 22 -2.1; 23 -2.2; 25 -2.3; 26 -2.4; 28 -2.5; 30 -2.5; 32 -2.6; 35 -2.6; 37 -2.6; 40 -2.6; 42 -2.6; 45 -2.6; 49 -2.7; 52 -2.7; 56 -2.7; 59 -2.7; 64 -2.7; 68 -2.8; 73 -2.8; 78 -2.9; 83 -3.0; 89 -3.1; 95 -3.1; 102 -3.1; 109 -3.0; 117 -3.0; 125 -3.0; 134 -2.9; 143 -2.9; 153 -2.8; 164 -2.7; 175 -2.5; 188 -2.4; 201 -2.3; 215 -2.2; 230 -1.9; 246 -1.8; 263 -1.6; 282 -1.4; 301 -1.2; 323 -1.0; 345 -0.8; 369 -0.6; 395 -0.5; 423 -0.2; 452 -0.0; 484 0.1; 518 0.2; 554 0.5; 593 0.8; 635 0.9; 679 0.8; 726 0.8; 777 1.2; 832 1.2; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.6; 1429 -0.5; 1529 -0.2; 1636 0.3; 1751 1.0; 1873 1.7; 2004 2.2; 2145 2.5; 2295 2.6; 2455 2.9; 2627 2.8; 2811 3.0; 3008 5.2; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.7; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.1; 6775 1.9; 7249 -1.3; 7756 -3.6; 8299 -4.9; 8880 -5.4; 9502 -5.3; 10167 -4.0; 10879 -1.7; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999997757682dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 Bk Gy Bk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.63 | -1.9 dB  |
| Peaking | 120 Hz  | 0.49 | -2.8 dB  |
| Peaking | 626 Hz  | 2.53 | 1.2 dB   |
| Peaking | 5249 Hz | 0.78 | 8.5 dB   |
| Peaking | 8563 Hz | 1.86 | -10.6 dB |
| Peaking | 825 Hz  | 6.21 | 1.0 dB   |
| Peaking | 1322 Hz | 2.6  | -1.7 dB  |
| Peaking | 3265 Hz | 5.41 | 2.0 dB   |
| Peaking | 5740 Hz | 1.71 | -1.4 dB  |
| Peaking | 6116 Hz | 5.79 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk.png)