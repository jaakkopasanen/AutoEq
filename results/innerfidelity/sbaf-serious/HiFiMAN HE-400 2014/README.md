# HiFiMAN HE-400 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 3.4; 22 3.2; 23 3.1; 25 3.0; 26 3.0; 28 2.9; 30 2.8; 32 2.8; 35 2.7; 37 2.7; 40 2.6; 42 2.6; 45 2.6; 49 2.5; 52 2.4; 56 2.4; 59 2.3; 64 2.0; 68 1.7; 73 1.2; 78 0.8; 83 0.6; 89 0.4; 95 0.1; 102 -0.2; 109 -0.3; 117 -0.5; 125 -0.7; 134 -0.8; 143 -0.9; 153 -1.0; 164 -1.1; 175 -1.1; 188 -1.3; 201 -1.6; 215 -1.7; 230 -1.7; 246 -2.0; 263 -2.1; 282 -2.1; 301 -2.2; 323 -2.1; 345 -1.8; 369 -1.5; 395 -1.4; 423 -1.6; 452 -2.0; 484 -2.4; 518 -2.5; 554 -2.2; 593 -1.9; 635 -1.4; 679 -1.3; 726 -1.6; 777 -1.5; 832 -1.3; 890 -0.8; 952 -0.4; 1019 0.0; 1090 0.3; 1167 0.6; 1248 1.2; 1336 1.4; 1429 1.7; 1529 1.7; 1636 1.8; 1751 2.0; 1873 1.3; 2004 0.6; 2145 0.1; 2295 0.3; 2455 -0.1; 2627 -0.8; 2811 -1.1; 3008 -0.9; 3219 -0.3; 3444 -0.3; 3685 -0.1; 3943 0.8; 4219 -1.4; 4514 -1.7; 4830 -1.8; 5168 -0.7; 5530 0.9; 5917 0.6; 6331 -2.3; 6775 -3.5; 7249 -3.6; 7756 -4.1; 8299 -5.2; 8880 -5.4; 9502 -2.7; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.2; 20000 -4.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.4531743910923964dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.77 | 3.1 dB  |
| Peaking | 55 Hz    | 1.79 | 1.8 dB  |
| Peaking | 247 Hz   | 0.91 | -2.0 dB |
| Peaking | 540 Hz   | 2.38 | -1.9 dB |
| Peaking | 8192 Hz  | 2.9  | -5.6 dB |
| Peaking | 801 Hz   | 4.43 | -1.2 dB |
| Peaking | 1556 Hz  | 1.88 | 2.1 dB  |
| Peaking | 2789 Hz  | 3.8  | -1.3 dB |
| Peaking | 10555 Hz | 6.43 | 1.5 dB  |
| Peaking | 19940 Hz | 3.46 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-400%202014/HiFiMAN%20HE-400%202014.png)