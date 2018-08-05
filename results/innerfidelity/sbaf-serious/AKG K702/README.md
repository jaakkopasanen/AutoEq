# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 2.7; 22 2.1; 23 1.8; 25 1.3; 26 1.1; 28 0.7; 30 0.3; 32 0.0; 35 -0.4; 37 -0.6; 40 -0.8; 42 -1.0; 45 -1.2; 49 -1.5; 52 -1.6; 56 -1.8; 59 -1.9; 64 -2.0; 68 -2.2; 73 -2.2; 78 -1.9; 83 -1.9; 89 -2.2; 95 -2.6; 102 -2.8; 109 -2.8; 117 -3.5; 125 -4.2; 134 -4.7; 143 -5.0; 153 -5.2; 164 -5.0; 175 -4.9; 188 -5.1; 201 -5.1; 215 -4.9; 230 -4.8; 246 -4.8; 263 -4.7; 282 -4.5; 301 -4.3; 323 -4.0; 345 -3.8; 369 -3.6; 395 -3.3; 423 -2.9; 452 -2.6; 484 -2.4; 518 -1.6; 554 0.1; 593 0.2; 635 0.4; 679 0.8; 726 1.1; 777 1.2; 832 0.8; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -0.7; 1248 -0.5; 1336 -1.0; 1429 -1.6; 1529 -2.4; 1636 -3.1; 1751 -3.9; 1873 -4.2; 2004 -5.3; 2145 -5.6; 2295 -5.3; 2455 -4.6; 2627 -3.3; 2811 -2.2; 3008 -0.9; 3219 0.2; 3444 0.2; 3685 -0.0; 3943 -0.8; 4219 -2.7; 4514 -3.5; 4830 -3.4; 5168 -2.7; 5530 -2.8; 5917 -4.6; 6331 -6.0; 6775 -6.4; 7249 -6.5; 7756 -6.6; 8299 -7.1; 8880 -6.3; 9502 -3.1; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -2.1; 17469 -4.8; 18692 -5.4; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.3dB` and instead set Global volume in the UI for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 188 Hz   | 0.7  | -5.5 dB |
| Peaking | 2116 Hz  | 2.63 | -5.8 dB |
| Peaking | 8435 Hz  | 5.11 | -5.3 dB |
| Peaking | 6641 Hz  | 2.32 | -5.8 dB |
| Peaking | 18626 Hz | 2    | -6.2 dB |
| Peaking | 22 Hz    | 2.64 | 2.6 dB  |
| Peaking | 740 Hz   | 2.99 | 2.3 dB  |
| Peaking | 3518 Hz  | 3.3  | 4.8 dB  |
| Peaking | 3692 Hz  | 1.65 | -3.1 dB |
| Peaking | 11839 Hz | 1.66 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702/AKG%20K702.png)