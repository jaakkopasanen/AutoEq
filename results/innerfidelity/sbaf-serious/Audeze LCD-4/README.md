# Audeze LCD-4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.8; 22 4.7; 23 4.7; 25 4.6; 26 4.6; 28 4.5; 30 4.3; 32 4.3; 35 4.2; 37 4.2; 40 4.2; 42 4.1; 45 4.1; 49 4.0; 52 3.9; 56 3.9; 59 3.9; 64 3.8; 68 3.8; 73 3.7; 78 3.6; 83 3.4; 89 3.1; 95 2.8; 102 2.4; 109 2.2; 117 1.8; 125 1.4; 134 1.1; 143 0.8; 153 0.7; 164 0.5; 175 0.5; 188 0.5; 201 0.4; 215 0.4; 230 0.6; 246 0.5; 263 0.4; 282 0.5; 301 0.3; 323 0.3; 345 0.3; 369 0.4; 395 0.3; 423 0.2; 452 0.1; 484 -0.0; 518 0.0; 554 0.1; 593 0.2; 635 0.2; 679 0.0; 726 0.2; 777 0.2; 832 0.0; 890 0.1; 952 0.1; 1019 0.1; 1090 0.0; 1167 -0.2; 1248 -0.2; 1336 -0.3; 1429 -0.6; 1529 -1.2; 1636 -1.3; 1751 -0.9; 1873 -0.5; 2004 -0.4; 2145 -0.5; 2295 0.2; 2455 1.4; 2627 2.1; 2811 2.3; 3008 3.4; 3219 4.9; 3444 5.1; 3685 5.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.8; 5917 4.8; 6331 3.9; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.7; 18692 -4.9; 20000 -7.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.42 | 4.5 dB  |
| Peaking | 76 Hz    |  1.3  | 1.9 dB  |
| Peaking | 3755 Hz  |  1.65 | 5.3 dB  |
| Peaking | 1777 Hz  |  1.92 | -1.8 dB |
| Peaking | 5427 Hz  |  2.73 | 4.3 dB  |
| Peaking | 824 Hz   |  1.69 | 0.2 dB  |
| Peaking | 6600 Hz  | 12.07 | 1.0 dB  |
| Peaking | 19713 Hz |  1.95 | -7.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-4/Audeze%20LCD-4.png)