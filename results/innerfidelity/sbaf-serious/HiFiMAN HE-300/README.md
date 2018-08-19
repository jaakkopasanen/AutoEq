# HiFiMAN HE-300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.7; 23 -1.9; 25 -2.2; 26 -2.3; 28 -2.5; 30 -2.6; 32 -2.8; 35 -3.0; 37 -3.2; 40 -3.3; 42 -3.3; 45 -3.5; 49 -3.7; 52 -3.4; 56 -2.4; 59 -1.9; 64 -2.4; 68 -3.3; 73 -3.9; 78 -4.0; 83 -4.1; 89 -4.3; 95 -4.5; 102 -4.4; 109 -4.4; 117 -4.2; 125 -3.9; 134 -3.3; 143 -3.3; 153 -4.1; 164 -4.4; 175 -4.2; 188 -3.8; 201 -3.4; 215 -2.9; 230 -2.5; 246 -2.2; 263 -1.8; 282 -1.2; 301 -0.8; 323 -0.4; 345 0.0; 369 0.5; 395 0.9; 423 1.6; 452 2.1; 484 2.5; 518 3.1; 554 3.9; 593 4.7; 635 5.2; 679 4.9; 726 4.6; 777 5.3; 832 4.5; 890 2.9; 952 1.3; 1019 -0.4; 1090 -2.0; 1167 -3.6; 1248 -5.1; 1336 -5.9; 1429 -7.2; 1529 -8.2; 1636 -8.0; 1751 -6.5; 1873 -4.6; 2004 -4.9; 2145 -2.9; 2295 -2.5; 2455 -3.6; 2627 -4.6; 2811 -6.0; 3008 -7.6; 3219 -8.4; 3444 -7.7; 3685 -6.9; 3943 -6.0; 4219 -6.1; 4514 -6.0; 4830 -5.5; 5168 -4.9; 5530 -4.0; 5917 -1.9; 6331 1.9; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -1.4; 10167 -1.8; 10879 -0.8; 11640 -0.0; 12455 0.0; 13327 -0.5; 14260 -1.5; 15258 -0.4; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.415407480631528dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.34 | -2.6 dB |
| Peaking | 158 Hz   | 0.69 | -3.1 dB |
| Peaking | 701 Hz   | 1.13 | 6.9 dB  |
| Peaking | 1452 Hz  | 1.83 | -9.0 dB |
| Peaking | 3551 Hz  | 1.7  | -7.7 dB |
| Peaking | 3168 Hz  | 8.02 | -1.9 dB |
| Peaking | 3735 Hz  | 3.26 | 2.0 dB  |
| Peaking | 5228 Hz  | 2.47 | -3.3 dB |
| Peaking | 6649 Hz  | 5.22 | 6.5 dB  |
| Peaking | 10041 Hz | 7.62 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300/HiFiMAN%20HE-300.png)