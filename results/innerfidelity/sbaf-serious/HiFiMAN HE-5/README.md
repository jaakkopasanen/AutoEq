# HiFiMAN HE-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.5; 22 5.8; 23 5.5; 25 5.0; 26 4.8; 28 4.4; 30 4.0; 32 3.8; 35 3.5; 37 3.4; 40 3.2; 42 3.1; 45 2.9; 49 2.8; 52 2.9; 56 3.1; 59 3.0; 64 2.3; 68 2.0; 73 1.9; 78 1.8; 83 1.6; 89 1.3; 95 1.1; 102 0.9; 109 0.8; 117 0.7; 125 0.5; 134 0.3; 143 0.1; 153 -0.1; 164 -0.2; 175 -0.3; 188 -0.4; 201 -0.6; 215 -0.7; 230 -0.8; 246 -1.0; 263 -1.0; 282 -0.9; 301 -0.9; 323 -0.8; 345 -0.8; 369 -1.0; 395 -1.3; 423 -1.1; 452 -0.8; 484 -0.7; 518 -0.9; 554 -1.2; 593 -0.8; 635 -0.8; 679 -0.8; 726 -0.3; 777 0.1; 832 -0.1; 890 -0.4; 952 -0.4; 1019 0.0; 1090 0.8; 1167 1.3; 1248 1.5; 1336 1.7; 1429 1.7; 1529 1.3; 1636 1.8; 1751 3.1; 1873 4.2; 2004 3.9; 2145 3.1; 2295 3.0; 2455 3.3; 2627 2.7; 2811 1.3; 3008 0.5; 3219 -0.2; 3444 -0.6; 3685 -0.8; 3943 -1.1; 4219 -3.0; 4514 -3.6; 4830 -2.2; 5168 -0.1; 5530 0.7; 5917 -2.5; 6331 -4.0; 6775 -4.5; 7249 -4.2; 7756 -4.5; 8299 -6.6; 8880 -9.1; 9502 -9.1; 10167 -6.1; 10879 -3.1; 11640 -2.8; 12455 -4.7; 13327 -6.6; 14260 -6.5; 15258 -4.3; 16326 -1.3; 17469 -0.0; 18692 -0.7; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.559941321112587dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 13 Hz    |  0.35 | 6.4 dB  |
| Peaking | 2081 Hz  |  1.73 | 4.3 dB  |
| Peaking | 4341 Hz  |  8.96 | -2.7 dB |
| Peaking | 9828 Hz  |  0.87 | -6.9 dB |
| Peaking | 20032 Hz |  4.21 | -4.5 dB |
| Peaking | 359 Hz   |  0.78 | -1.3 dB |
| Peaking | 5472 Hz  | 10.42 | 3.7 dB  |
| Peaking | 9269 Hz  |  5.62 | -4.0 dB |
| Peaking | 11186 Hz |  3.63 | 4.7 dB  |
| Peaking | 13934 Hz |  3.68 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)