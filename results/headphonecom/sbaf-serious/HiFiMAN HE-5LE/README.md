# HiFiMAN HE-5LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 10 -84; 20 1.9; 22 1.4; 23 1.2; 25 0.9; 26 0.8; 28 0.7; 30 0.7; 32 0.8; 35 0.9; 37 1.0; 40 1.1; 42 1.2; 45 1.1; 49 1.0; 52 1.0; 56 1.0; 59 1.0; 64 1.0; 68 1.0; 73 0.7; 78 0.5; 83 0.6; 89 0.4; 95 0.2; 102 -0.1; 109 -0.2; 117 -0.4; 125 -0.8; 134 -1.3; 143 -1.8; 153 -2.3; 164 -2.9; 175 -3.1; 188 -3.3; 201 -3.3; 215 -3.3; 230 -3.5; 246 -3.6; 263 -3.7; 282 -3.6; 301 -3.6; 323 -3.6; 345 -3.4; 369 -3.4; 395 -3.5; 423 -3.4; 452 -3.4; 484 -3.6; 518 -4.4; 554 -4.7; 593 -3.3; 635 -0.7; 679 0.7; 726 1.3; 777 1.5; 832 1.0; 890 0.2; 952 -0.1; 1019 0.2; 1090 1.2; 1167 2.1; 1248 2.4; 1336 3.0; 1429 3.2; 1529 3.1; 1636 3.4; 1751 4.4; 1873 4.4; 2004 3.8; 2145 2.9; 2295 2.0; 2455 3.4; 2627 3.9; 2811 2.7; 3008 1.5; 3219 1.6; 3444 2.3; 3685 3.1; 3943 0.9; 4219 -1.8; 4514 -3.5; 4830 -3.3; 5168 -0.4; 5530 -0.1; 5917 -2.0; 6331 -4.0; 6775 -3.6; 7249 -3.2; 7756 -3.8; 8299 -5.6; 8880 -7.3; 9502 -6.5; 10167 -2.7; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -0.5; 16326 -1.2; 17469 -1.7; 18692 -2.0; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.759723298824743dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 343 Hz   |  0.69 | -4.4 dB |
| Peaking | 1774 Hz  |  0.78 | 4.2 dB  |
| Peaking | 3783 Hz  |  4.96 | 3.7 dB  |
| Peaking | 4426 Hz  |  3.19 | -4.9 dB |
| Peaking | 8717 Hz  |  2.73 | -7.3 dB |
| Peaking | 46 Hz    |  0.8  | 1.4 dB  |
| Peaking | 556 Hz   |  6.42 | -3.0 dB |
| Peaking | 708 Hz   |  5.06 | 2.6 dB  |
| Peaking | 6445 Hz  | 10.36 | -2.8 dB |
| Peaking | 18930 Hz |  1.9  | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)