# Audeze LCD XC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 2.4; 22 2.5; 23 2.5; 25 2.6; 26 2.7; 28 2.8; 30 2.8; 32 2.7; 35 2.4; 37 2.2; 40 2.1; 42 2.1; 45 2.2; 49 2.1; 52 2.0; 56 1.7; 59 1.5; 64 1.3; 68 1.1; 73 0.9; 78 0.8; 83 0.7; 89 0.5; 95 0.2; 102 -0.1; 109 -0.4; 117 -0.6; 125 -1.0; 134 -1.2; 143 -1.4; 153 -1.4; 164 -1.3; 175 -1.5; 188 -1.4; 201 -1.3; 215 -1.0; 230 -0.7; 246 -0.4; 263 0.1; 282 0.5; 301 0.7; 323 0.9; 345 1.3; 369 1.7; 395 2.0; 423 2.0; 452 2.1; 484 1.9; 518 1.9; 554 2.3; 593 2.3; 635 2.4; 679 2.2; 726 2.0; 777 1.7; 832 1.2; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.6; 1336 -2.4; 1429 -3.2; 1529 -3.8; 1636 -4.2; 1751 -4.1; 1873 -3.8; 2004 -2.9; 2145 -1.6; 2295 -0.6; 2455 0.5; 2627 1.8; 2811 2.0; 3008 2.6; 3219 2.6; 3444 1.3; 3685 0.0; 3943 -1.1; 4219 -0.3; 4514 3.5; 4830 4.5; 5168 4.6; 5530 4.9; 5917 4.7; 6331 4.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -2.3; 14260 -3.4; 15258 -2.3; 16326 -2.2; 17469 -4.0; 18692 -5.3; 20000 -4.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.96 | 2.9 dB  |
| Peaking | 1699 Hz  |  2.75 | -4.9 dB |
| Peaking | 2899 Hz  |  4.34 | 2.9 dB  |
| Peaking | 5702 Hz  |  2.47 | 5.7 dB  |
| Peaking | 19083 Hz |  0.72 | -5.0 dB |
| Peaking | 178 Hz   |  1.4  | -2.2 dB |
| Peaking | 637 Hz   |  0.67 | 4.0 dB  |
| Peaking | 1575 Hz  |  0.47 | -3.6 dB |
| Peaking | 4732 Hz  | 11.53 | 2.6 dB  |
| Peaking | 2180 Hz  |  1.04 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD%20XC/Audeze%20LCD%20XC.png)