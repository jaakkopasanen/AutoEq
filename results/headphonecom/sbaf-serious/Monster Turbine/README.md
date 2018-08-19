# Monster Turbine

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 -13.2; 22 -13.0; 23 -12.9; 25 -12.8; 26 -12.7; 28 -12.5; 30 -12.4; 32 -12.2; 35 -11.9; 37 -11.8; 40 -11.5; 42 -11.4; 45 -11.2; 49 -10.9; 52 -10.8; 56 -10.6; 59 -10.4; 64 -10.2; 68 -10.1; 73 -9.9; 78 -9.7; 83 -9.5; 89 -9.3; 95 -9.0; 102 -8.7; 109 -8.5; 117 -8.2; 125 -8.0; 134 -7.7; 143 -7.4; 153 -7.2; 164 -7.1; 175 -6.8; 188 -6.4; 201 -6.0; 215 -5.6; 230 -5.2; 246 -4.8; 263 -4.4; 282 -4.0; 301 -3.6; 323 -3.1; 345 -2.6; 369 -2.2; 395 -1.8; 423 -1.4; 452 -1.1; 484 -0.8; 518 -0.5; 554 -0.2; 593 0.2; 635 0.5; 679 0.6; 726 0.7; 777 0.9; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.6; 1336 -2.1; 1429 -2.1; 1529 -2.9; 1636 -3.6; 1751 -4.6; 1873 -5.3; 2004 -5.8; 2145 -6.4; 2295 -6.8; 2455 -7.3; 2627 -7.6; 2811 -7.3; 3008 -6.4; 3219 -5.1; 3444 -4.1; 3685 -4.2; 3943 -5.4; 4219 -7.0; 4514 -7.8; 4830 -6.3; 5168 -3.1; 5530 0.5; 5917 3.3; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -2.5; 9502 -3.3; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -2.4; 16326 -0.8; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.080339529794665dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.21 | -12.7 dB |
| Peaking | 165 Hz   | 0.94 | -3.1 dB  |
| Peaking | 2460 Hz  | 1.54 | -7.5 dB  |
| Peaking | 4542 Hz  | 3.7  | -7.2 dB  |
| Peaking | 6253 Hz  | 4.58 | 7.0 dB   |
| Peaking | 284 Hz   | 2.2  | -0.8 dB  |
| Peaking | 747 Hz   | 1.56 | 1.9 dB   |
| Peaking | 1708 Hz  | 3.74 | -1.1 dB  |
| Peaking | 9310 Hz  | 7.64 | -3.7 dB  |
| Peaking | 15407 Hz | 7.25 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)