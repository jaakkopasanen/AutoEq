# Fostex TH900mk2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -2.6; 22 -2.9; 23 -3.0; 25 -3.3; 26 -3.4; 28 -3.6; 30 -3.7; 32 -3.9; 35 -4.0; 37 -4.1; 40 -4.1; 42 -4.2; 45 -4.2; 49 -4.2; 52 -4.2; 56 -4.2; 59 -4.2; 64 -4.0; 68 -4.0; 73 -4.0; 78 -4.2; 83 -4.4; 89 -4.6; 95 -4.6; 102 -4.7; 109 -4.6; 117 -4.5; 125 -4.6; 134 -4.5; 143 -4.4; 153 -4.2; 164 -3.8; 175 -3.6; 188 -3.5; 201 -3.2; 215 -2.9; 230 -2.6; 246 -2.3; 263 -1.9; 282 -1.5; 301 -1.1; 323 -0.6; 345 -0.1; 369 0.4; 395 1.0; 423 1.6; 452 2.0; 484 2.1; 518 2.1; 554 2.0; 593 1.9; 635 1.5; 679 0.7; 726 0.3; 777 1.1; 832 1.0; 890 0.3; 952 0.0; 1019 0.1; 1090 0.3; 1167 0.8; 1248 1.1; 1336 1.4; 1429 1.4; 1529 1.4; 1636 1.4; 1751 1.3; 1873 1.5; 2004 1.6; 2145 1.6; 2295 2.1; 2455 3.2; 2627 3.6; 2811 2.8; 3008 1.6; 3219 0.3; 3444 1.2; 3685 2.0; 3943 1.7; 4219 0.5; 4514 -0.6; 4830 -1.5; 5168 -2.6; 5530 -4.9; 5917 -5.9; 6331 -3.4; 6775 -1.4; 7249 -2.4; 7756 -3.7; 8299 -2.8; 8880 -0.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -1.8; 18692 -4.5; 20000 -7.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.743895865374489dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.6dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.62 | -3.2 dB |
| Peaking | 129 Hz  |  0.55 | -4.1 dB |
| Peaking | 477 Hz  |  1.63 | 3.1 dB  |
| Peaking | 2765 Hz |  0.91 | 2.8 dB  |
| Peaking | 5843 Hz |  2.36 | -5.9 dB |
| Peaking | 980 Hz  |  8.25 | -0.7 dB |
| Peaking | 3212 Hz |  6.29 | -4.2 dB |
| Peaking | 3258 Hz |  2.66 | 2.3 dB  |
| Peaking | 6708 Hz | 11.08 | 2.1 dB  |
| Peaking | 7880 Hz |  8.46 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2/Fostex%20TH900mk2.png)