# AKG K376

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 10 -84; 20 -13.2; 22 -13.1; 23 -13.0; 25 -12.9; 26 -12.8; 28 -12.7; 30 -12.6; 32 -12.5; 35 -12.3; 37 -12.2; 40 -12.1; 42 -12.0; 45 -11.9; 49 -11.7; 52 -11.6; 56 -11.5; 59 -11.4; 64 -11.2; 68 -11.1; 73 -11.0; 78 -11.0; 83 -10.9; 89 -10.8; 95 -10.7; 102 -10.5; 109 -10.2; 117 -10.0; 125 -9.8; 134 -9.5; 143 -9.3; 153 -9.1; 164 -8.8; 175 -8.3; 188 -8.0; 201 -7.6; 215 -7.2; 230 -6.7; 246 -6.3; 263 -5.9; 282 -5.4; 301 -5.0; 323 -4.5; 345 -4.0; 369 -3.6; 395 -3.2; 423 -2.6; 452 -2.1; 484 -1.8; 518 -1.5; 554 -0.9; 593 -0.4; 635 0.0; 679 0.2; 726 0.4; 777 0.8; 832 0.8; 890 0.6; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.4; 1636 -3.0; 1751 -3.4; 1873 -3.7; 2004 -4.0; 2145 -4.6; 2295 -5.2; 2455 -5.6; 2627 -5.7; 2811 -4.6; 3008 -2.1; 3219 0.3; 3444 2.2; 3685 2.2; 3943 1.4; 4219 -0.2; 4514 -2.3; 4830 -4.2; 5168 -5.6; 5530 -6.2; 5917 -3.4; 6331 -0.4; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6735557557546707dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K376 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.6dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.18 | -12.7 dB |
| Peaking | 165 Hz  | 0.73 | -4.2 dB  |
| Peaking | 2505 Hz | 1.76 | -6.9 dB  |
| Peaking | 3515 Hz | 2.97 | 5.5 dB   |
| Peaking | 5261 Hz | 5.02 | -6.8 dB  |
| Peaking | 337 Hz  | 2.15 | -0.8 dB  |
| Peaking | 780 Hz  | 1.63 | 1.8 dB   |
| Peaking | 1623 Hz | 3.88 | -1.3 dB  |
| Peaking | 5785 Hz | 5.77 | -1.7 dB  |
| Peaking | 6782 Hz | 5.86 | 3.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K376/AKG%20K376.png)