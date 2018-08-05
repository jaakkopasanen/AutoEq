# Radius HP-TWF41

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.4; 22 3.8; 23 3.6; 25 3.2; 26 3.0; 28 2.7; 30 2.4; 32 2.2; 35 1.9; 37 1.7; 40 1.5; 42 1.4; 45 1.2; 49 1.0; 52 0.9; 56 0.7; 59 0.6; 64 0.4; 68 0.3; 73 0.1; 78 -0.2; 83 -0.4; 89 -0.9; 95 -1.5; 102 -2.1; 109 -2.6; 117 -3.1; 125 -3.8; 134 -4.3; 143 -4.6; 153 -4.9; 164 -5.1; 175 -5.2; 188 -5.2; 201 -5.3; 215 -5.2; 230 -5.1; 246 -5.1; 263 -5.0; 282 -4.9; 301 -4.7; 323 -4.7; 345 -4.5; 369 -4.4; 395 -4.2; 423 -3.9; 452 -3.7; 484 -3.6; 518 -3.4; 554 -2.9; 593 -2.4; 635 -2.1; 679 -1.8; 726 -1.1; 777 -0.6; 832 -0.4; 890 -0.2; 952 -0.0; 1019 0.0; 1090 0.2; 1167 0.3; 1248 0.3; 1336 0.3; 1429 0.2; 1529 0.1; 1636 0.1; 1751 0.3; 1873 0.6; 2004 1.0; 2145 1.3; 2295 1.5; 2455 2.1; 2627 2.4; 2811 2.8; 3008 4.0; 3219 4.9; 3444 5.5; 3685 5.2; 3943 4.5; 4219 3.3; 4514 3.0; 4830 4.2; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.4; 9502 -2.0; 10167 -1.5; 10879 -1.0; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.4; 16326 -3.2; 17469 -1.2; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF41 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.15 | 3.4 dB  |
| Peaking | 212 Hz   | 0.53 | -6.0 dB |
| Peaking | 3366 Hz  | 1.87 | 4.7 dB  |
| Peaking | 5955 Hz  | 2.22 | 7.0 dB  |
| Peaking | 8707 Hz  | 1.14 | -2.7 dB |
| Peaking | 14 Hz    | 2.54 | 0.8 dB  |
| Peaking | 511 Hz   | 2.48 | -0.9 dB |
| Peaking | 930 Hz   | 1.66 | 1.0 dB  |
| Peaking | 13616 Hz | 2.21 | 1.1 dB  |
| Peaking | 16263 Hz | 3.71 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF41/Radius%20HP-TWF41.png)