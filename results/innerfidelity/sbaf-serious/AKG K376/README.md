# AKG K376

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 -13.1; 22 -13.0; 23 -12.9; 25 -12.8; 26 -12.7; 28 -12.6; 30 -12.4; 32 -12.3; 35 -12.1; 37 -11.9; 40 -11.7; 42 -11.5; 45 -11.3; 49 -11.0; 52 -10.8; 56 -10.5; 59 -10.3; 64 -9.9; 68 -9.7; 73 -9.5; 78 -9.3; 83 -9.2; 89 -9.2; 95 -9.3; 102 -9.4; 109 -9.5; 117 -9.7; 125 -9.8; 134 -9.8; 143 -9.8; 153 -9.6; 164 -9.3; 175 -8.8; 188 -8.5; 201 -8.1; 215 -7.6; 230 -7.1; 246 -6.6; 263 -6.2; 282 -5.6; 301 -5.1; 323 -4.6; 345 -4.2; 369 -3.7; 395 -3.2; 423 -2.6; 452 -2.2; 484 -1.9; 518 -1.5; 554 -1.0; 593 -0.5; 635 0.0; 679 0.2; 726 0.4; 777 0.8; 832 0.8; 890 0.6; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.4; 1636 -3.0; 1751 -3.4; 1873 -3.7; 2004 -4.0; 2145 -4.6; 2295 -5.2; 2455 -5.6; 2627 -5.7; 2811 -4.6; 3008 -2.1; 3219 0.3; 3444 2.2; 3685 2.2; 3943 1.4; 4219 -0.2; 4514 -2.3; 4830 -4.2; 5168 -5.6; 5530 -6.2; 5917 -3.4; 6331 -0.4; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K376 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.91 | -12.9 dB |
| Peaking | 31 Hz   | 0.32 | -10.3 dB |
| Peaking | 171 Hz  | 0.79 | -6.4 dB  |
| Peaking | 2285 Hz | 2.56 | -5.9 dB  |
| Peaking | 5340 Hz | 6.34 | -6.7 dB  |
| Peaking | 780 Hz  | 1.22 | 4.0 dB   |
| Peaking | 796 Hz  | 0.62 | -2.3 dB  |
| Peaking | 3804 Hz | 1.27 | -3.0 dB  |
| Peaking | 3626 Hz | 3.45 | 7.0 dB   |
| Peaking | 6900 Hz | 6.77 | 3.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K376/AKG%20K376.png)