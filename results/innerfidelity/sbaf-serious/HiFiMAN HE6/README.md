# HiFiMAN HE6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 4.3; 22 3.9; 23 3.8; 25 3.5; 26 3.4; 28 3.3; 30 3.2; 32 3.1; 35 3.0; 37 3.0; 40 3.0; 42 3.0; 45 2.9; 49 2.8; 52 2.8; 56 2.8; 59 2.8; 64 2.8; 68 2.6; 73 2.2; 78 2.0; 83 1.9; 89 1.7; 95 1.4; 102 1.2; 109 1.2; 117 1.1; 125 0.9; 134 0.7; 143 0.7; 153 0.6; 164 0.6; 175 0.6; 188 0.6; 201 0.5; 215 0.6; 230 0.7; 246 0.6; 263 0.5; 282 0.6; 301 0.5; 323 0.4; 345 0.3; 369 0.2; 395 0.2; 423 0.2; 452 0.4; 484 0.2; 518 0.1; 554 0.3; 593 0.5; 635 0.5; 679 0.2; 726 0.2; 777 0.3; 832 0.1; 890 -0.2; 952 -0.3; 1019 -0.0; 1090 0.6; 1167 1.0; 1248 0.7; 1336 1.0; 1429 1.1; 1529 1.7; 1636 2.0; 1751 2.6; 1873 3.3; 2004 3.0; 2145 2.4; 2295 2.5; 2455 2.8; 2627 2.3; 2811 1.6; 3008 1.0; 3219 0.1; 3444 0.1; 3685 -0.1; 3943 -1.5; 4219 -1.4; 4514 -1.3; 4830 0.2; 5168 -1.2; 5530 -4.9; 5917 -5.6; 6331 -4.9; 6775 -4.4; 7249 -3.3; 7756 -3.4; 8299 -5.3; 8880 -7.3; 9502 -6.5; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 -0.1; 13327 -1.5; 14260 -2.7; 15258 -2.3; 16326 -0.8; 17469 -0.0; 18692 -1.2; 20000 -4.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.399304581352623dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 1.05 | 3.5 dB  |
| Peaking | 52 Hz    | 0.63 | 2.4 dB  |
| Peaking | 2048 Hz  | 1.69 | 3.2 dB  |
| Peaking | 6066 Hz  | 3.26 | -5.4 dB |
| Peaking | 8998 Hz  | 4.15 | -7.4 dB |
| Peaking | 2625 Hz  | 7.17 | 0.8 dB  |
| Peaking | 4185 Hz  | 4.25 | -1.3 dB |
| Peaking | 4897 Hz  | 9.21 | 2.6 dB  |
| Peaking | 11242 Hz | 3.99 | 2.4 dB  |
| Peaking | 20570 Hz | 0.22 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)