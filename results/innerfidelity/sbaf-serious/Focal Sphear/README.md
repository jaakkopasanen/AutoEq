# Focal Sphear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 0.5; 22 -0.0; 23 -0.3; 25 -0.7; 26 -0.9; 28 -1.3; 30 -1.6; 32 -1.9; 35 -2.2; 37 -2.5; 40 -2.7; 42 -2.9; 45 -3.2; 49 -3.5; 52 -3.7; 56 -4.0; 59 -4.2; 64 -4.4; 68 -4.6; 73 -4.9; 78 -5.2; 83 -5.5; 89 -5.8; 95 -5.9; 102 -6.1; 109 -6.1; 117 -6.2; 125 -6.3; 134 -6.4; 143 -6.4; 153 -6.4; 164 -6.4; 175 -6.2; 188 -6.0; 201 -5.9; 215 -5.7; 230 -5.4; 246 -5.2; 263 -4.9; 282 -4.5; 301 -4.2; 323 -3.9; 345 -3.5; 369 -3.1; 395 -2.8; 423 -2.3; 452 -1.9; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.1; 679 0.0; 726 0.3; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.3; 1429 -1.8; 1529 -2.4; 1636 -2.8; 1751 -2.9; 1873 -2.9; 2004 -2.8; 2145 -2.9; 2295 -2.8; 2455 -2.1; 2627 -1.4; 2811 -0.4; 3008 1.3; 3219 2.6; 3444 3.5; 3685 3.2; 3943 2.1; 4219 -0.3; 4514 -2.5; 4830 -4.4; 5168 -5.6; 5530 -5.1; 5917 -2.4; 6331 -0.5; 6775 1.0; 7249 1.2; 7756 0.3; 8299 -0.8; 8880 -2.6; 9502 -3.0; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6385650599264507dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Sphear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 101 Hz  | 0.56 | -5.5 dB |
| Peaking | 229 Hz  | 1.08 | -3.0 dB |
| Peaking | 2041 Hz | 1.79 | -3.5 dB |
| Peaking | 3519 Hz | 3.21 | 5.0 dB  |
| Peaking | 5125 Hz | 4.1  | -6.5 dB |
| Peaking | 17 Hz   | 1.97 | 1.3 dB  |
| Peaking | 788 Hz  | 0.71 | -1.9 dB |
| Peaking | 792 Hz  | 1.27 | 3.2 dB  |
| Peaking | 7086 Hz | 5.89 | 2.4 dB  |
| Peaking | 9299 Hz | 6.11 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Sphear/Focal%20Sphear.png)