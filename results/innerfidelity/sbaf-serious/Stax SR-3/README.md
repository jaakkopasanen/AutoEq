# Stax SR-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.0; 102 3.0; 109 1.6; 117 0.3; 125 -0.8; 134 -1.8; 143 -2.4; 153 -2.7; 164 -2.6; 175 -2.7; 188 -2.6; 201 -2.4; 215 -2.1; 230 -1.6; 246 -1.1; 263 -0.8; 282 -0.4; 301 -0.1; 323 0.3; 345 0.6; 369 0.8; 395 1.0; 423 1.2; 452 1.2; 484 1.2; 518 1.3; 554 1.2; 593 0.5; 635 -1.0; 679 -0.6; 726 1.0; 777 1.8; 832 1.3; 890 0.9; 952 0.5; 1019 -0.2; 1090 -0.6; 1167 -0.4; 1248 0.1; 1336 0.1; 1429 -0.5; 1529 -0.4; 1636 0.3; 1751 0.7; 1873 -0.2; 2004 -0.6; 2145 -0.5; 2295 -0.4; 2455 -0.8; 2627 -1.2; 2811 -0.8; 3008 -1.7; 3219 -1.1; 3444 -1.2; 3685 -1.0; 3943 -0.1; 4219 0.7; 4514 0.7; 4830 3.9; 5168 4.8; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -0.4; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 65 Hz   |  0.3  | 8.0 dB  |
| Peaking | 160 Hz  |  1.05 | -8.8 dB |
| Peaking | 456 Hz  |  2.75 | 1.0 dB  |
| Peaking | 3268 Hz |  1.66 | -2.0 dB |
| Peaking | 5713 Hz |  2.79 | 6.9 dB  |
| Peaking | 19 Hz   |  1.22 | 2.3 dB  |
| Peaking | 42 Hz   |  0.47 | -1.1 dB |
| Peaking | 88 Hz   |  4.45 | 2.4 dB  |
| Peaking | 649 Hz  | 12.4  | -1.6 dB |
| Peaking | 8709 Hz |  3.4  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-3/Stax%20SR-3.png)