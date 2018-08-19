# HiFiMAN IE400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.9; 22 3.8; 23 3.7; 25 3.7; 26 3.7; 28 3.6; 30 3.6; 32 3.5; 35 3.4; 37 3.3; 40 3.2; 42 3.1; 45 3.0; 49 2.8; 52 2.7; 56 2.5; 59 2.4; 64 2.1; 68 1.9; 73 1.6; 78 1.4; 83 1.1; 89 0.8; 95 0.5; 102 0.2; 109 0.1; 117 -0.1; 125 -0.3; 134 -0.5; 143 -0.7; 153 -0.9; 164 -1.0; 175 -1.0; 188 -1.1; 201 -1.2; 215 -1.1; 230 -1.1; 246 -1.1; 263 -1.0; 282 -0.9; 301 -0.8; 323 -0.7; 345 -0.6; 369 -0.5; 395 -0.3; 423 -0.1; 452 0.1; 484 0.1; 518 0.3; 554 0.6; 593 0.9; 635 1.0; 679 0.9; 726 1.0; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -2.1; 1429 -2.8; 1529 -3.6; 1636 -4.4; 1751 -4.9; 1873 -5.2; 2004 -5.1; 2145 -4.1; 2295 -2.3; 2455 -0.3; 2627 1.3; 2811 3.3; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.9; 4830 5.4; 5168 5.2; 5530 4.4; 5917 3.2; 6331 2.9; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715983dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN IE400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.65 | 3.6 dB  |
| Peaking | 54 Hz   | 1.26 | 1.4 dB  |
| Peaking | 187 Hz  | 1.27 | -1.5 dB |
| Peaking | 1943 Hz | 1.87 | -8.5 dB |
| Peaking | 3593 Hz | 1.02 | 7.9 dB  |
| Peaking | 752 Hz  | 1.87 | 1.5 dB  |
| Peaking | 1623 Hz | 1.76 | -1.2 dB |
| Peaking | 1852 Hz | 5.1  | 1.4 dB  |
| Peaking | 6777 Hz | 1.84 | 2.9 dB  |
| Peaking | 7743 Hz | 1.65 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20IE400/HiFiMAN%20IE400.png)