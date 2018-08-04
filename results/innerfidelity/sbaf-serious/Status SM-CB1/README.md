# Status SM-CB1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.7; 23 5.5; 25 4.9; 26 4.6; 28 4.0; 30 3.3; 32 2.8; 35 2.0; 37 1.5; 40 0.9; 42 0.6; 45 0.1; 49 -0.4; 52 -0.7; 56 -1.0; 59 -1.1; 64 -1.4; 68 -1.4; 73 -1.4; 78 -1.5; 83 -1.6; 89 -1.8; 95 -1.8; 102 -1.7; 109 -1.6; 117 -1.8; 125 -2.3; 134 -2.7; 143 -2.9; 153 -3.1; 164 -2.7; 175 -2.6; 188 -2.8; 201 -2.8; 215 -2.8; 230 -2.6; 246 -2.5; 263 -2.3; 282 -1.6; 301 -1.3; 323 -1.0; 345 -0.8; 369 -0.4; 395 0.1; 423 0.6; 452 0.9; 484 1.0; 518 0.9; 554 0.7; 593 0.3; 635 -0.2; 679 -0.5; 726 -0.8; 777 -0.8; 832 -1.1; 890 -1.0; 952 -0.2; 1019 -0.3; 1090 -1.3; 1167 -1.4; 1248 -1.5; 1336 -1.6; 1429 -1.7; 1529 -1.8; 1636 -1.9; 1751 -1.9; 1873 -1.6; 2004 -0.9; 2145 -0.1; 2295 0.6; 2455 1.7; 2627 2.8; 2811 2.7; 3008 1.3; 3219 0.5; 3444 0.7; 3685 0.8; 3943 1.2; 4219 1.8; 4514 2.2; 4830 3.4; 5168 3.7; 5530 3.1; 5917 1.1; 6331 1.9; 6775 3.5; 7249 1.3; 7756 0.3; 8299 -1.9; 8880 -4.6; 9502 -3.6; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-CB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.66 | 6.0 dB  |
| Peaking | 153 Hz  | 0.74 | -2.9 dB |
| Peaking | 6783 Hz | 6.88 | 2.7 dB  |
| Peaking | 4986 Hz | 2.54 | 3.4 dB  |
| Peaking | 8966 Hz | 6.04 | -5.5 dB |
| Peaking | 60 Hz   | 3.63 | -0.8 dB |
| Peaking | 478 Hz  | 2.16 | 2.4 dB  |
| Peaking | 889 Hz  | 0.34 | -0.8 dB |
| Peaking | 1660 Hz | 2.01 | -1.6 dB |
| Peaking | 2647 Hz | 4.19 | 3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-CB1/Status%20SM-CB1.png)