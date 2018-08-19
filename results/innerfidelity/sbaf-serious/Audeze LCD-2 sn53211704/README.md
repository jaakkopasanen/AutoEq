# Audeze LCD-2 sn53211704

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 2.4; 22 2.5; 23 2.5; 25 2.5; 26 2.5; 28 2.5; 30 2.6; 32 2.6; 35 2.7; 37 2.7; 40 2.4; 42 2.2; 45 2.1; 49 2.2; 52 2.2; 56 1.9; 59 1.6; 64 1.2; 68 1.0; 73 0.8; 78 0.7; 83 0.6; 89 0.3; 95 0.0; 102 -0.2; 109 -0.3; 117 -0.5; 125 -0.8; 134 -0.9; 143 -1.0; 153 -1.2; 164 -1.3; 175 -1.4; 188 -1.5; 201 -1.7; 215 -1.8; 230 -1.9; 246 -2.0; 263 -2.0; 282 -1.9; 301 -2.0; 323 -2.1; 345 -1.9; 369 -1.6; 395 -1.5; 423 -1.2; 452 -0.9; 484 -0.9; 518 -0.9; 554 -1.0; 593 -1.1; 635 -1.5; 679 -1.9; 726 -2.2; 777 -2.2; 832 -2.4; 890 -2.0; 952 -0.9; 1019 0.3; 1090 0.8; 1167 0.9; 1248 1.1; 1336 0.5; 1429 -0.4; 1529 -0.7; 1636 -0.4; 1751 0.2; 1873 0.8; 2004 1.2; 2145 1.2; 2295 1.7; 2455 2.0; 2627 2.5; 2811 2.3; 3008 2.5; 3219 2.8; 3444 3.6; 3685 4.5; 3943 5.3; 4219 4.9; 4514 4.4; 4830 3.9; 5168 3.1; 5530 2.2; 5917 1.6; 6331 4.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -0.1; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.5; 17469 -3.3; 18692 -5.1; 20000 -4.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3879701347276825dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn53211704 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.6  | 2.8 dB  |
| Peaking | 240 Hz   | 0.71 | -2.1 dB |
| Peaking | 780 Hz   | 3.86 | -2.3 dB |
| Peaking | 3969 Hz  | 1.58 | 5.0 dB  |
| Peaking | 6591 Hz  | 9.31 | 3.6 dB  |
| Peaking | 1222 Hz  | 2.78 | 3.4 dB  |
| Peaking | 1441 Hz  | 1.38 | -3.4 dB |
| Peaking | 2035 Hz  | 1.29 | 2.0 dB  |
| Peaking | 3286 Hz  | 5.54 | -1.0 dB |
| Peaking | 19128 Hz | 1.76 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn53211704/Audeze%20LCD-2%20sn53211704.png)