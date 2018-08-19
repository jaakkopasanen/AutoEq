# PSB M4U 2 passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 -0.2; 22 -0.2; 23 -0.2; 25 -0.2; 26 -0.2; 28 -0.2; 30 -0.2; 32 -0.1; 35 -0.0; 37 0.1; 40 0.3; 42 0.3; 45 0.5; 49 0.7; 52 0.8; 56 1.1; 59 1.3; 64 1.8; 68 2.1; 73 2.4; 78 2.6; 83 2.2; 89 0.7; 95 -1.0; 102 -2.2; 109 -2.4; 117 -2.0; 125 -1.7; 134 -1.7; 143 -1.6; 153 -1.1; 164 -0.2; 175 -1.3; 188 -1.3; 201 -0.8; 215 -0.4; 230 0.1; 246 0.5; 263 1.2; 282 2.0; 301 2.1; 323 2.3; 345 2.7; 369 2.5; 395 3.0; 423 3.6; 452 3.5; 484 3.1; 518 2.9; 554 2.7; 593 2.6; 635 2.5; 679 1.9; 726 1.5; 777 1.2; 832 0.6; 890 0.2; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.0; 1336 -0.3; 1429 -0.5; 1529 -0.5; 1636 -0.5; 1751 -0.2; 1873 0.4; 2004 0.9; 2145 1.1; 2295 1.3; 2455 1.7; 2627 2.0; 2811 2.2; 3008 1.9; 3219 1.1; 3444 0.4; 3685 -0.4; 3943 -0.6; 4219 0.1; 4514 0.2; 4830 0.7; 5168 1.5; 5530 3.4; 5917 3.9; 6331 3.2; 6775 2.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.286490606673125dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 1.69 | 7.2 dB  |
| Peaking | 98 Hz   | 1.19 | -6.0 dB |
| Peaking | 436 Hz  | 1.27 | 3.7 dB  |
| Peaking | 2700 Hz | 4.19 | 2.3 dB  |
| Peaking | 6020 Hz | 4.03 | 4.2 dB  |
| Peaking | 192 Hz  | 6.93 | -0.9 dB |
| Peaking | 287 Hz  | 8.13 | 0.8 dB  |
| Peaking | 631 Hz  | 7.99 | 0.7 dB  |
| Peaking | 1433 Hz | 3.13 | -0.9 dB |
| Peaking | 3918 Hz | 6.91 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202%20passive/PSB%20M4U%202%20passive.png)