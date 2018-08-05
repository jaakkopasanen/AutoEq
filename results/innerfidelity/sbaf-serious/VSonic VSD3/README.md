# VSonic VSD3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 0.2; 22 -0.2; 23 -0.4; 25 -0.7; 26 -0.8; 28 -1.0; 30 -1.2; 32 -1.4; 35 -1.6; 37 -1.7; 40 -1.8; 42 -1.9; 45 -1.9; 49 -2.0; 52 -2.1; 56 -2.1; 59 -2.2; 64 -2.2; 68 -2.3; 73 -2.5; 78 -2.6; 83 -2.8; 89 -3.1; 95 -3.5; 102 -4.0; 109 -4.4; 117 -4.9; 125 -5.4; 134 -5.7; 143 -5.9; 153 -6.0; 164 -6.0; 175 -5.9; 188 -5.8; 201 -5.6; 215 -5.4; 230 -5.1; 246 -5.0; 263 -4.8; 282 -4.4; 301 -4.2; 323 -3.9; 345 -3.7; 369 -3.4; 395 -3.2; 423 -2.8; 452 -2.5; 484 -2.4; 518 -2.1; 554 -1.7; 593 -1.2; 635 -1.0; 679 -0.8; 726 -0.6; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 -0.1; 1248 -0.1; 1336 -0.1; 1429 -0.0; 1529 0.1; 1636 0.2; 1751 0.4; 1873 0.7; 2004 1.0; 2145 1.4; 2295 1.8; 2455 2.5; 2627 2.7; 2811 3.0; 3008 3.8; 3219 4.6; 3444 5.4; 3685 5.3; 3943 4.7; 4219 3.0; 4514 1.6; 4830 0.6; 5168 -0.2; 5530 -1.1; 5917 -1.8; 6331 -0.8; 6775 1.0; 7249 1.2; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -3.2; 10167 -5.2; 10879 -5.2; 11640 -3.6; 12455 -1.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 39 Hz    |  1.72 | -1.1 dB |
| Peaking | 179 Hz   |  0.59 | -6.0 dB |
| Peaking | 3523 Hz  |  1.58 | 5.5 dB  |
| Peaking | 5491 Hz  |  3.88 | -2.9 dB |
| Peaking | 10590 Hz |  3.99 | -6.2 dB |
| Peaking | 88 Hz    |  4.72 | 0.2 dB  |
| Peaking | 839 Hz   |  3.69 | 0.6 dB  |
| Peaking | 6245 Hz  |  7.27 | -1.9 dB |
| Peaking | 6950 Hz  |  3.64 | 1.8 dB  |
| Peaking | 9686 Hz  | 12.84 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3/VSonic%20VSD3.png)