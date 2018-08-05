# Steelseries Flux In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 10 -84; 20 -5.3; 22 -5.3; 23 -5.3; 25 -5.3; 26 -5.3; 28 -5.3; 30 -5.3; 32 -5.2; 35 -5.2; 37 -5.2; 40 -5.2; 42 -5.1; 45 -5.0; 49 -5.0; 52 -4.9; 56 -4.9; 59 -4.8; 64 -4.7; 68 -4.7; 73 -4.7; 78 -4.7; 83 -4.8; 89 -5.0; 95 -5.3; 102 -5.7; 109 -5.9; 117 -6.2; 125 -6.6; 134 -6.8; 143 -6.9; 153 -6.9; 164 -6.8; 175 -6.5; 188 -6.3; 201 -6.0; 215 -5.7; 230 -5.3; 246 -5.0; 263 -4.7; 282 -4.2; 301 -3.9; 323 -3.5; 345 -3.1; 369 -2.8; 395 -2.4; 423 -1.9; 452 -1.5; 484 -1.3; 518 -1.0; 554 -0.6; 593 -0.1; 635 0.1; 679 0.2; 726 0.3; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.0; 1336 -1.6; 1429 -2.1; 1529 -2.6; 1636 -2.9; 1751 -3.3; 1873 -3.4; 2004 -3.5; 2145 -3.8; 2295 -4.1; 2455 -3.6; 2627 -3.0; 2811 -3.8; 3008 -3.0; 3219 -1.0; 3444 0.8; 3685 1.5; 3943 1.7; 4219 0.7; 4514 0.1; 4830 0.2; 5168 0.8; 5530 0.9; 5917 0.4; 6331 -0.4; 6775 -0.6; 7249 0.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.9; 14260 -2.8; 15258 -2.7; 16326 -2.2; 17469 -2.6; 18692 -1.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.3dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Steelseries Flux In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  0.27 | -5.2 dB |
| Peaking | 169 Hz   |  0.81 | -5.9 dB |
| Peaking | 2330 Hz  |  1.43 | -4.5 dB |
| Peaking | 3801 Hz  |  3.17 | 3.2 dB  |
| Peaking | 16456 Hz |  1.48 | -2.9 dB |
| Peaking | 342 Hz   |  1.74 | -0.9 dB |
| Peaking | 781 Hz   |  1.72 | 1.2 dB  |
| Peaking | 1557 Hz  |  3    | -1.4 dB |
| Peaking | 2920 Hz  | 10.08 | -1.7 dB |
| Peaking | 1790 Hz  |  0.13 | 0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Steelseries%20Flux%20In-Ear/Steelseries%20Flux%20In-Ear.png)