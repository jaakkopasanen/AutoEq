# PSB M4U 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.0; 23 -1.0; 25 -0.9; 26 -0.9; 28 -0.8; 30 -0.7; 32 -0.6; 35 -0.4; 37 -0.3; 40 -0.1; 42 0.1; 45 0.3; 49 0.6; 52 0.8; 56 1.1; 59 1.3; 64 1.7; 68 2.0; 73 2.2; 78 2.3; 83 2.0; 89 0.6; 95 -1.4; 102 -2.7; 109 -2.6; 117 -2.0; 125 -2.1; 134 -2.7; 143 -2.8; 153 -2.4; 164 -1.3; 175 -2.4; 188 -2.7; 201 -2.2; 215 -1.9; 230 -1.5; 246 -1.2; 263 -0.6; 282 -0.3; 301 0.8; 323 1.3; 345 0.0; 369 0.6; 395 1.6; 423 2.7; 452 2.5; 484 1.7; 518 1.8; 554 2.2; 593 2.8; 635 2.8; 679 2.0; 726 1.8; 777 1.5; 832 0.4; 890 -0.0; 952 -0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -1.0; 1529 -1.3; 1636 -1.5; 1751 -1.7; 1873 -1.6; 2004 -1.4; 2145 -1.4; 2295 -1.5; 2455 -1.3; 2627 -1.4; 2811 -1.6; 3008 -1.9; 3219 -2.2; 3444 -2.8; 3685 -3.4; 3943 -3.6; 4219 -3.9; 4514 -3.5; 4830 -1.9; 5168 -0.8; 5530 0.9; 5917 2.2; 6331 2.1; 6775 1.3; 7249 -1.6; 7756 -3.9; 8299 -5.5; 8880 -5.9; 9502 -4.2; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.037209834492693dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 1.4  | 7.6 dB  |
| Peaking | 96 Hz   | 0.68 | -5.9 dB |
| Peaking | 499 Hz  | 1.4  | 3.0 dB  |
| Peaking | 3689 Hz | 2.03 | -3.6 dB |
| Peaking | 8693 Hz | 5.22 | -6.7 dB |
| Peaking | 20 Hz   | 1.73 | -0.7 dB |
| Peaking | 640 Hz  | 7.09 | 1.1 dB  |
| Peaking | 1703 Hz | 1.85 | -1.5 dB |
| Peaking | 6248 Hz | 4.47 | 3.8 dB  |
| Peaking | 7735 Hz | 6.93 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%201/PSB%20M4U%201.png)