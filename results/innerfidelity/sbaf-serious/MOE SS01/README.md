# MOE SS01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.3; 23 -5.3; 25 -5.4; 26 -5.4; 28 -5.4; 30 -5.5; 32 -5.5; 35 -5.5; 37 -5.6; 40 -5.6; 42 -5.6; 45 -5.6; 49 -5.7; 52 -5.7; 56 -5.8; 59 -5.8; 64 -6.0; 68 -6.1; 73 -6.2; 78 -6.3; 83 -6.4; 89 -6.6; 95 -6.7; 102 -6.7; 109 -6.7; 117 -6.7; 125 -6.7; 134 -6.7; 143 -6.6; 153 -6.5; 164 -6.4; 175 -6.2; 188 -6.0; 201 -5.8; 215 -5.6; 230 -5.2; 246 -5.0; 263 -4.7; 282 -4.3; 301 -4.0; 323 -3.7; 345 -3.2; 369 -2.9; 395 -2.6; 423 -2.1; 452 -1.7; 484 -1.4; 518 -1.1; 554 -0.6; 593 -0.2; 635 0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.3; 1429 -1.7; 1529 -2.3; 1636 -2.4; 1751 -2.2; 1873 -2.0; 2004 -2.2; 2145 -2.6; 2295 -2.9; 2455 -2.9; 2627 -3.2; 2811 -3.6; 3008 -3.2; 3219 -2.0; 3444 -0.7; 3685 -0.6; 3943 -1.3; 4219 -3.3; 4514 -5.2; 4830 -6.4; 5168 -6.6; 5530 -5.8; 5917 -3.7; 6331 -2.1; 6775 -0.9; 7249 -0.4; 7756 -0.9; 8299 -2.2; 8880 -3.3; 9502 -2.9; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.6972028208932208dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MOE SS01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.28 | -5.2 dB |
| Peaking | 132 Hz  | 0.81 | -4.1 dB |
| Peaking | 256 Hz  | 1.4  | -2.4 dB |
| Peaking | 2322 Hz | 1.53 | -2.9 dB |
| Peaking | 5116 Hz | 3.17 | -6.8 dB |
| Peaking | 784 Hz  | 2.7  | 1.2 dB  |
| Peaking | 1532 Hz | 4.25 | -1.5 dB |
| Peaking | 2873 Hz | 8.22 | -1.7 dB |
| Peaking | 4498 Hz | 0.28 | 0.5 dB  |
| Peaking | 9023 Hz | 5.22 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MOE%20SS01/MOE%20SS01.png)