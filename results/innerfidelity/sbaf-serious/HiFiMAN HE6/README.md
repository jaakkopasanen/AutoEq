# HiFiMAN HE6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 4.3; 22 4.0; 23 3.8; 25 3.6; 26 3.5; 28 3.3; 30 3.2; 32 3.1; 35 3.1; 37 3.1; 40 3.1; 42 3.1; 45 3.1; 49 3.0; 52 3.0; 56 3.1; 59 3.2; 64 3.3; 68 3.2; 73 2.9; 78 2.8; 83 2.7; 89 2.5; 95 2.1; 102 1.8; 109 1.6; 117 1.3; 125 0.9; 134 0.6; 143 0.5; 153 0.3; 164 0.3; 175 0.3; 188 0.4; 201 0.4; 215 0.5; 230 0.6; 246 0.5; 263 0.4; 282 0.5; 301 0.4; 323 0.4; 345 0.2; 369 0.2; 395 0.2; 423 0.2; 452 0.4; 484 0.2; 518 0.1; 554 0.3; 593 0.5; 635 0.5; 679 0.2; 726 0.2; 777 0.3; 832 0.1; 890 -0.2; 952 -0.3; 1019 -0.0; 1090 0.6; 1167 1.0; 1248 0.7; 1336 1.0; 1429 1.1; 1529 1.7; 1636 2.0; 1751 2.6; 1873 3.3; 2004 3.0; 2145 2.4; 2295 2.5; 2455 2.8; 2627 2.3; 2811 1.6; 3008 1.0; 3219 0.1; 3444 0.1; 3685 -0.1; 3943 -1.5; 4219 -1.4; 4514 -1.3; 4830 0.2; 5168 -1.2; 5530 -4.9; 5917 -5.6; 6331 -4.9; 6775 -4.4; 7249 -3.3; 7756 -3.4; 8299 -5.3; 8880 -7.3; 9502 -6.5; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 -0.1; 13327 -1.5; 14260 -2.7; 15258 -2.3; 16326 -0.8; 17469 -0.0; 18692 -1.2; 20000 -4.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 14 Hz    |  0.39 | 4.2 dB  |
| Peaking | 69 Hz    |  1.19 | 2.2 dB  |
| Peaking | 2049 Hz  |  1.69 | 3.2 dB  |
| Peaking | 6107 Hz  |  3.26 | -5.4 dB |
| Peaking | 8937 Hz  |  4.16 | -7.4 dB |
| Peaking | 2628 Hz  |  7.64 | 0.8 dB  |
| Peaking | 4131 Hz  |  4.83 | -1.3 dB |
| Peaking | 4919 Hz  | 10.87 | 2.5 dB  |
| Peaking | 11241 Hz |  4.43 | 2.2 dB  |
| Peaking | 21142 Hz |  0.21 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)