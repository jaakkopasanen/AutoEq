# HiFiMAN RE-300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.0; 22 -0.1; 23 -0.2; 25 -0.3; 26 -0.3; 28 -0.4; 30 -0.5; 32 -0.6; 35 -0.7; 37 -0.8; 40 -0.9; 42 -0.9; 45 -1.0; 49 -1.2; 52 -1.3; 56 -1.6; 59 -1.7; 64 -2.0; 68 -2.2; 73 -2.4; 78 -2.6; 83 -2.8; 89 -3.1; 95 -3.4; 102 -3.6; 109 -3.7; 117 -3.9; 125 -4.0; 134 -4.2; 143 -4.3; 153 -4.3; 164 -4.4; 175 -4.3; 188 -4.3; 201 -4.3; 215 -4.1; 230 -3.9; 246 -3.8; 263 -3.7; 282 -3.4; 301 -3.2; 323 -2.9; 345 -2.6; 369 -2.3; 395 -2.0; 423 -1.6; 452 -1.2; 484 -1.0; 518 -0.7; 554 -0.2; 593 0.3; 635 0.6; 679 0.7; 726 0.8; 777 1.1; 832 0.9; 890 0.7; 952 0.3; 1019 -0.2; 1090 -0.8; 1167 -0.3; 1248 -0.6; 1336 -1.9; 1429 -2.8; 1529 -3.5; 1636 -3.5; 1751 -2.8; 1873 -1.3; 2004 0.9; 2145 3.2; 2295 5.6; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.5; 6331 2.6; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999035dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 100 Hz  | 0.77 | -1.3 dB |
| Peaking | 200 Hz  | 0.56 | -3.8 dB |
| Peaking | 686 Hz  | 1.9  | 1.5 dB  |
| Peaking | 1622 Hz | 2.25 | -7.6 dB |
| Peaking | 3097 Hz | 0.72 | 7.6 dB  |
| Peaking | 1948 Hz | 6.54 | -1.0 dB |
| Peaking | 2329 Hz | 4.71 | 1.9 dB  |
| Peaking | 3213 Hz | 2.72 | -1.1 dB |
| Peaking | 5555 Hz | 2.72 | 3.6 dB  |
| Peaking | 7599 Hz | 1.11 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-300/HiFiMAN%20RE-300.png)