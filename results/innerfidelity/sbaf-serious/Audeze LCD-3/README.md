# Audeze LCD-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 3.6; 22 3.5; 23 3.4; 25 3.1; 26 2.9; 28 2.4; 30 2.0; 32 1.8; 35 1.6; 37 1.6; 40 1.5; 42 1.5; 45 1.5; 49 1.4; 52 1.1; 56 1.0; 59 1.0; 64 1.0; 68 1.0; 73 0.9; 78 0.8; 83 0.7; 89 0.4; 95 0.1; 102 -0.3; 109 -0.5; 117 -0.9; 125 -1.4; 134 -1.7; 143 -1.9; 153 -2.0; 164 -2.2; 175 -2.3; 188 -2.4; 201 -2.4; 215 -2.4; 230 -2.3; 246 -2.3; 263 -2.3; 282 -2.2; 301 -2.2; 323 -2.1; 345 -1.9; 369 -1.8; 395 -1.9; 423 -1.9; 452 -2.0; 484 -2.2; 518 -2.2; 554 -2.1; 593 -1.9; 635 -1.8; 679 -1.9; 726 -1.7; 777 -1.4; 832 -1.2; 890 -0.8; 952 -0.4; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.8; 1336 0.5; 1429 0.1; 1529 -0.2; 1636 -0.1; 1751 0.5; 1873 1.0; 2004 1.3; 2145 1.0; 2295 1.2; 2455 1.4; 2627 1.5; 2811 1.4; 3008 1.2; 3219 1.4; 3444 2.7; 3685 4.3; 3943 5.2; 4219 5.2; 4514 4.7; 4830 4.3; 5168 3.6; 5530 1.5; 5917 1.1; 6331 2.5; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -2.0; 17469 -4.5; 18692 -5.5; 20000 -3.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 10 Hz    |  0.17 | 3.0 dB  |
| Peaking | 200 Hz   |  0.8  | -2.7 dB |
| Peaking | 561 Hz   |  1.6  | -1.8 dB |
| Peaking | 4275 Hz  |  1.68 | 5.1 dB  |
| Peaking | 18672 Hz |  1.74 | -6.1 dB |
| Peaking | 7 Hz     |  1.49 | 1.3 dB  |
| Peaking | 2449 Hz  |  1.29 | 1.8 dB  |
| Peaking | 3891 Hz  |  3.84 | 2.2 dB  |
| Peaking | 3368 Hz  |  1.23 | -2.6 dB |
| Peaking | 6714 Hz  | 12    | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)