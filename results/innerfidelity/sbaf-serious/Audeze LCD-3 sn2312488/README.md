# Audeze LCD-3 sn2312488

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.8; 22 2.9; 23 2.9; 25 2.9; 26 2.9; 28 2.8; 30 2.5; 32 2.3; 35 2.0; 37 2.0; 40 2.1; 42 2.1; 45 2.1; 49 1.7; 52 1.3; 56 1.1; 59 1.0; 64 1.0; 68 0.9; 73 0.7; 78 0.5; 83 0.3; 89 0.0; 95 -0.2; 102 -0.4; 109 -0.5; 117 -0.7; 125 -0.9; 134 -1.1; 143 -1.3; 153 -1.4; 164 -1.5; 175 -1.6; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.9; 246 -2.0; 263 -2.1; 282 -2.1; 301 -2.2; 323 -2.0; 345 -1.8; 369 -1.5; 395 -1.3; 423 -1.2; 452 -1.4; 484 -1.8; 518 -1.9; 554 -2.0; 593 -2.0; 635 -2.2; 679 -2.2; 726 -1.9; 777 -1.3; 832 -1.1; 890 -0.8; 952 -0.5; 1019 0.2; 1090 0.5; 1167 0.7; 1248 1.2; 1336 1.1; 1429 0.7; 1529 0.2; 1636 0.3; 1751 0.9; 1873 1.4; 2004 1.9; 2145 1.7; 2295 1.8; 2455 1.8; 2627 1.5; 2811 1.1; 3008 1.0; 3219 0.7; 3444 1.1; 3685 2.2; 3943 3.7; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.4; 5530 3.6; 5917 2.4; 6331 3.5; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.5; 17469 -3.9; 18692 -5.0; 20000 -4.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099990971483631dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312488 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.49 | 2.9 dB  |
| Peaking | 228 Hz   | 0.74 | -2.2 dB |
| Peaking | 637 Hz   | 2.82 | -1.9 dB |
| Peaking | 4724 Hz  | 1.87 | 6.1 dB  |
| Peaking | 18852 Hz | 1.65 | -5.5 dB |
| Peaking | 2276 Hz  | 2.13 | 1.5 dB  |
| Peaking | 3840 Hz  | 1.15 | -4.3 dB |
| Peaking | 4193 Hz  | 6.32 | 2.7 dB  |
| Peaking | 4764 Hz  | 0.47 | 2.5 dB  |
| Peaking | 8780 Hz  | 2.16 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312488/Audeze%20LCD-3%20sn2312488.png)