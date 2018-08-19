# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 3.0; 22 2.6; 23 2.4; 25 2.1; 26 1.9; 28 1.7; 30 1.5; 32 1.3; 35 1.1; 37 1.1; 40 1.1; 42 1.1; 45 1.1; 49 1.2; 52 1.2; 56 0.9; 59 0.7; 64 0.4; 68 0.5; 73 0.4; 78 0.4; 83 0.3; 89 -0.0; 95 -0.1; 102 -0.1; 109 -0.3; 117 -0.2; 125 -0.3; 134 -0.5; 143 -0.6; 153 -0.6; 164 -0.8; 175 -0.7; 188 -0.9; 201 -0.8; 215 -0.8; 230 -1.0; 246 -1.0; 263 -1.2; 282 -1.2; 301 -1.0; 323 -0.9; 345 -1.0; 369 -1.1; 395 -0.8; 423 -0.7; 452 -1.0; 484 -1.2; 518 -0.8; 554 -0.9; 593 -1.0; 635 -0.7; 679 -0.7; 726 0.2; 777 0.7; 832 0.3; 890 -0.2; 952 0.1; 1019 -0.2; 1090 -0.3; 1167 0.2; 1248 0.3; 1336 1.0; 1429 1.0; 1529 0.6; 1636 0.8; 1751 1.8; 1873 2.5; 2004 2.8; 2145 1.7; 2295 0.9; 2455 2.5; 2627 2.6; 2811 1.8; 3008 0.8; 3219 0.5; 3444 0.2; 3685 0.7; 3943 0.1; 4219 -1.2; 4514 -1.7; 4830 -1.1; 5168 1.3; 5530 2.6; 5917 2.0; 6331 0.6; 6775 -0.3; 7249 -0.1; 7756 -0.6; 8299 -2.8; 8880 -5.5; 9502 -5.7; 10167 -2.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.2; 18692 -3.8; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.0781246654818215dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.93 | 2.6 dB  |
| Peaking | 2236 Hz | 1.61 | 2.3 dB  |
| Peaking | 4669 Hz | 4.27 | -3.2 dB |
| Peaking | 5488 Hz | 4.15 | 3.6 dB  |
| Peaking | 9193 Hz | 5.24 | -6.7 dB |
| Peaking | 52 Hz   | 1.74 | 0.7 dB  |
| Peaking | 327 Hz  | 0.48 | -1.1 dB |
| Peaking | 771 Hz  | 8    | 1.3 dB  |
| Peaking | 1875 Hz | 9.6  | 1.0 dB  |
| Peaking | 6604 Hz | 5.12 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)