# Massdrop Nobel X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.8; 23 -0.8; 25 -0.9; 26 -0.9; 28 -0.9; 30 -1.0; 32 -1.0; 35 -1.1; 37 -1.1; 40 -1.2; 42 -1.2; 45 -1.2; 49 -1.2; 52 -1.3; 56 -1.3; 59 -1.4; 64 -1.4; 68 -1.5; 73 -1.6; 78 -1.8; 83 -2.0; 89 -2.4; 95 -2.8; 102 -3.4; 109 -3.8; 117 -4.3; 125 -4.9; 134 -5.4; 143 -5.6; 153 -5.8; 164 -5.9; 175 -5.9; 188 -5.8; 201 -5.8; 215 -5.6; 230 -5.4; 246 -5.3; 263 -5.1; 282 -4.8; 301 -4.6; 323 -4.3; 345 -4.0; 369 -3.7; 395 -3.4; 423 -2.9; 452 -2.6; 484 -2.3; 518 -2.1; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.6; 726 -0.3; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.8; 1529 -1.1; 1636 -1.3; 1751 -1.3; 1873 -1.1; 2004 -0.9; 2145 -0.7; 2295 -0.3; 2455 0.6; 2627 1.3; 2811 2.2; 3008 3.6; 3219 4.9; 3444 6.0; 3685 6.0; 3943 5.2; 4219 3.1; 4514 1.0; 4830 0.5; 5168 1.6; 5530 2.9; 5917 4.1; 6331 4.3; 6775 3.7; 7249 1.3; 7756 -1.0; 8299 -3.9; 8880 -4.8; 9502 -4.0; 10167 -1.9; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Nobel X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.43 | -0.7 dB |
| Peaking | 192 Hz  | 0.65 | -6.1 dB |
| Peaking | 3536 Hz | 3.54 | 6.6 dB  |
| Peaking | 6384 Hz | 3.59 | 5.2 dB  |
| Peaking | 8799 Hz | 3.68 | -6.0 dB |
| Peaking | 79 Hz   | 4.34 | 0.5 dB  |
| Peaking | 852 Hz  | 2.45 | 1.1 dB  |
| Peaking | 1897 Hz | 1.59 | -2.2 dB |
| Peaking | 2667 Hz | 0.8  | 1.0 dB  |
| Peaking | 4695 Hz | 8.78 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20Nobel%20X/Massdrop%20Nobel%20X.png)