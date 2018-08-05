# Vsonic VC1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 3.2; 22 3.1; 23 3.1; 25 3.0; 26 3.0; 28 3.0; 30 3.0; 32 3.0; 35 2.9; 37 2.8; 40 2.8; 42 2.8; 45 2.8; 49 2.8; 52 2.8; 56 2.7; 59 2.7; 64 2.6; 68 2.5; 73 2.3; 78 2.0; 83 1.8; 89 1.4; 95 0.9; 102 0.3; 109 -0.1; 117 -0.7; 125 -1.2; 134 -1.7; 143 -2.0; 153 -2.2; 164 -2.4; 175 -2.5; 188 -2.6; 201 -2.7; 215 -2.5; 230 -2.4; 246 -2.5; 263 -2.4; 282 -2.3; 301 -2.2; 323 -2.1; 345 -1.9; 369 -1.8; 395 -1.7; 423 -1.4; 452 -1.3; 484 -1.2; 518 -1.0; 554 -0.7; 593 -0.4; 635 -0.2; 679 -0.2; 726 -0.0; 777 0.3; 832 0.2; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.6; 1529 -0.6; 1636 -0.5; 1751 -0.4; 1873 -0.0; 2004 0.4; 2145 0.6; 2295 0.9; 2455 1.4; 2627 2.4; 2811 4.1; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.1; 4514 2.0; 4830 2.6; 5168 4.5; 5530 5.7; 5917 6.0; 6331 5.7; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -1.4; 10879 -3.6; 11640 -3.7; 12455 -1.2; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic VC1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  1.26 | 3.4 dB  |
| Peaking | 60 Hz    |  2.65 | 2.6 dB  |
| Peaking | 3411 Hz  |  2.54 | 6.6 dB  |
| Peaking | 5946 Hz  |  3.52 | 6.1 dB  |
| Peaking | 11231 Hz |  4.35 | -4.5 dB |
| Peaking | 43 Hz    |  3.6  | 1.0 dB  |
| Peaking | 89 Hz    |  2.37 | 1.9 dB  |
| Peaking | 199 Hz   |  0.69 | -2.9 dB |
| Peaking | 1639 Hz  |  2.77 | -0.9 dB |
| Peaking | 2919 Hz  | 13.42 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Vsonic%20VC1000/Vsonic%20VC1000.png)