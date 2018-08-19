# Steelseries Flux InEar Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 1.4; 22 1.4; 23 1.4; 25 1.4; 26 1.4; 28 1.3; 30 1.2; 32 1.1; 35 1.0; 37 1.0; 40 0.9; 42 0.8; 45 0.7; 49 0.6; 52 0.4; 56 0.3; 59 0.1; 64 -0.1; 68 -0.4; 73 -0.6; 78 -0.9; 83 -1.2; 89 -1.5; 95 -1.8; 102 -2.0; 109 -2.2; 117 -2.3; 125 -2.4; 134 -2.7; 143 -2.9; 153 -2.9; 164 -3.0; 175 -3.1; 188 -3.1; 201 -3.1; 215 -3.0; 230 -2.9; 246 -2.9; 263 -2.8; 282 -2.6; 301 -2.5; 323 -2.3; 345 -2.1; 369 -1.9; 395 -1.7; 423 -1.4; 452 -1.2; 484 -1.1; 518 -0.9; 554 -0.5; 593 -0.0; 635 0.2; 679 0.2; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.3; 1429 -1.7; 1529 -2.1; 1636 -2.4; 1751 -2.5; 1873 -2.6; 2004 -2.7; 2145 -2.6; 2295 -2.3; 2455 -1.2; 2627 -0.2; 2811 0.8; 3008 2.4; 3219 3.8; 3444 4.6; 3685 4.0; 3943 2.5; 4219 0.1; 4514 -1.2; 4830 -0.2; 5168 2.6; 5530 4.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.996527551284992dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Steelseries Flux InEar Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.62 | 1.6 dB  |
| Peaking | 178 Hz   | 0.7  | -3.4 dB |
| Peaking | 1953 Hz  | 1.95 | -3.2 dB |
| Peaking | 3379 Hz  | 4.36 | 5.3 dB  |
| Peaking | 6061 Hz  | 4.58 | 6.6 dB  |
| Peaking | 788 Hz   | 2.74 | 1.3 dB  |
| Peaking | 1469 Hz  | 5.02 | -0.7 dB |
| Peaking | 4561 Hz  | 6.06 | -4.8 dB |
| Peaking | 4591 Hz  | 2.48 | 2.1 dB  |
| Peaking | 24000 Hz | 1.69 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Steelseries%20Flux%20InEar%20Pro/Steelseries%20Flux%20InEar%20Pro.png)