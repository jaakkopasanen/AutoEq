# Nixon RPM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.0; 32 4.4; 35 3.4; 37 2.9; 40 2.2; 42 1.7; 45 1.2; 49 0.6; 52 0.2; 56 0.0; 59 -0.1; 64 -0.5; 68 -0.9; 73 -1.4; 78 -1.6; 83 -1.8; 89 -2.0; 95 -2.2; 102 -2.0; 109 -2.0; 117 -2.0; 125 -2.3; 134 -2.3; 143 -2.3; 153 -2.3; 164 -2.2; 175 -2.1; 188 -2.1; 201 -2.1; 215 -2.0; 230 -1.8; 246 -1.8; 263 -1.7; 282 -1.4; 301 -1.5; 323 -2.4; 345 -2.5; 369 -1.9; 395 -1.5; 423 -1.3; 452 -1.0; 484 -0.6; 518 0.0; 554 0.5; 593 0.8; 635 0.8; 679 0.6; 726 0.4; 777 0.3; 832 -0.1; 890 -0.2; 952 -0.2; 1019 0.1; 1090 0.7; 1167 0.6; 1248 0.4; 1336 0.7; 1429 1.2; 1529 1.8; 1636 2.3; 1751 3.3; 1873 4.4; 2004 5.6; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.2; 4830 3.5; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nixon RPM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.93 | 7.7 dB  |
| Peaking | 228 Hz  | 0.1  | -2.6 dB |
| Peaking | 608 Hz  | 1.87 | 2.7 dB  |
| Peaking | 2718 Hz | 0.84 | 7.6 dB  |
| Peaking | 5797 Hz | 3.53 | 4.4 dB  |
| Peaking | 267 Hz  | 4.96 | 0.6 dB  |
| Peaking | 2063 Hz | 3.67 | 2.4 dB  |
| Peaking | 2285 Hz | 1.41 | -1.5 dB |
| Peaking | 4099 Hz | 4.98 | 1.6 dB  |
| Peaking | 8531 Hz | 2.92 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nixon%20RPM/Nixon%20RPM.png)