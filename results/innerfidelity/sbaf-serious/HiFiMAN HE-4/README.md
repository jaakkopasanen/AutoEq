# HiFiMAN HE-4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 10 -84; 20 3.7; 22 3.4; 23 3.2; 25 3.0; 26 2.9; 28 2.7; 30 2.6; 32 2.5; 35 2.3; 37 2.3; 40 2.1; 42 2.1; 45 2.0; 49 2.0; 52 1.9; 56 1.8; 59 1.7; 64 1.6; 68 1.4; 73 1.3; 78 1.1; 83 0.8; 89 0.5; 95 0.4; 102 0.0; 109 -0.1; 117 -0.1; 125 -0.3; 134 -0.5; 143 -0.6; 153 -0.9; 164 -1.0; 175 -1.1; 188 -1.4; 201 -1.6; 215 -1.8; 230 -1.9; 246 -2.0; 263 -2.0; 282 -1.9; 301 -1.5; 323 -0.9; 345 -0.3; 369 -0.2; 395 -0.2; 423 -0.3; 452 -0.6; 484 -0.8; 518 -0.7; 554 -0.3; 593 -0.2; 635 -0.2; 679 1.2; 726 2.4; 777 2.5; 832 1.8; 890 1.3; 952 0.7; 1019 0.2; 1090 1.5; 1167 2.1; 1248 1.5; 1336 1.4; 1429 1.6; 1529 1.8; 1636 2.2; 1751 2.9; 1873 3.0; 2004 2.9; 2145 2.1; 2295 2.0; 2455 2.3; 2627 1.5; 2811 0.8; 3008 0.1; 3219 -1.0; 3444 -1.5; 3685 -2.0; 3943 -2.9; 4219 -4.5; 4514 -5.0; 4830 -4.2; 5168 1.8; 5530 3.3; 5917 -1.4; 6331 -5.4; 6775 -5.3; 7249 -5.1; 7756 -5.2; 8299 -6.8; 8880 -8.6; 9502 -8.1; 10167 -5.0; 10879 -2.3; 11640 -2.3; 12455 -4.2; 13327 -5.6; 14260 -5.2; 15258 -3.7; 16326 -2.9; 17469 -4.5; 18692 -8.1; 20000 -12.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.751214711756987dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.77 | 3.2 dB   |
| Peaking | 1825 Hz  | 1.09 | 2.8 dB   |
| Peaking | 4263 Hz  | 4.8  | -5.0 dB  |
| Peaking | 8759 Hz  | 2.11 | -7.7 dB  |
| Peaking | 20577 Hz | 0.73 | -12.9 dB |
| Peaking | 237 Hz   | 1.37 | -2.1 dB  |
| Peaking | 757 Hz   | 6.77 | 2.5 dB   |
| Peaking | 5501 Hz  | 9.64 | 6.7 dB   |
| Peaking | 6425 Hz  | 6.77 | -3.6 dB  |
| Peaking | 13591 Hz | 7.5  | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-4/HiFiMAN%20HE-4.png)