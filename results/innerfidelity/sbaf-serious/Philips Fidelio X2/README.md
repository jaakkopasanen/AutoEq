# Philips Fidelio X2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.4; 22 3.5; 23 3.0; 25 2.2; 26 1.8; 28 1.0; 30 0.3; 32 -0.3; 35 -1.2; 37 -1.7; 40 -2.3; 42 -2.7; 45 -3.2; 49 -3.7; 52 -4.0; 56 -4.2; 59 -4.3; 64 -4.4; 68 -4.5; 73 -4.5; 78 -4.5; 83 -4.5; 89 -4.4; 95 -4.4; 102 -4.3; 109 -4.1; 117 -3.9; 125 -3.8; 134 -3.7; 143 -3.7; 153 -3.6; 164 -3.4; 175 -2.9; 188 -2.8; 201 -3.1; 215 -3.8; 230 -4.1; 246 -3.5; 263 -3.1; 282 -2.8; 301 -2.6; 323 -2.5; 345 -2.4; 369 -2.3; 395 -2.3; 423 -2.1; 452 -2.1; 484 -2.3; 518 -2.4; 554 -2.2; 593 -2.1; 635 -2.2; 679 -2.3; 726 -2.2; 777 -1.8; 832 -1.7; 890 -1.0; 952 -0.3; 1019 0.1; 1090 0.6; 1167 1.4; 1248 1.2; 1336 0.3; 1429 -1.0; 1529 -2.4; 1636 -2.7; 1751 -2.7; 1873 -2.1; 2004 -1.6; 2145 -1.5; 2295 -1.6; 2455 -0.9; 2627 0.6; 2811 3.7; 3008 3.0; 3219 1.5; 3444 1.6; 3685 0.6; 3943 -0.1; 4219 -1.6; 4514 -4.2; 4830 -3.5; 5168 1.0; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -4.1; 8880 -6.8; 9502 -6.0; 10167 -1.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  0.88 | 6.0 dB  |
| Peaking | 57 Hz   |  0.62 | -4.0 dB |
| Peaking | 233 Hz  |  0.31 | -2.6 dB |
| Peaking | 6138 Hz |  4.64 | 7.3 dB  |
| Peaking | 8976 Hz |  5.15 | -8.1 dB |
| Peaking | 1219 Hz |  2.41 | 5.6 dB  |
| Peaking | 1514 Hz |  1.15 | -4.2 dB |
| Peaking | 2939 Hz |  4.26 | 4.7 dB  |
| Peaking | 4677 Hz |  6.21 | -5.8 dB |
| Peaking | 5444 Hz | 10.46 | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X2/Philips%20Fidelio%20X2.png)