# Phiaton Chord MS530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.9; 22 5.6; 23 5.5; 25 5.3; 26 5.2; 28 5.0; 30 4.8; 32 4.7; 35 4.5; 37 4.3; 40 4.1; 42 4.0; 45 3.9; 49 3.7; 52 3.5; 56 3.4; 59 3.2; 64 2.9; 68 2.8; 73 2.6; 78 2.4; 83 2.3; 89 2.5; 95 2.4; 102 1.9; 109 1.6; 117 1.5; 125 1.4; 134 1.3; 143 1.0; 153 1.0; 164 1.5; 175 1.6; 188 1.6; 201 2.0; 215 2.4; 230 2.7; 246 3.0; 263 3.3; 282 3.7; 301 3.9; 323 4.1; 345 4.2; 369 4.3; 395 4.0; 423 3.9; 452 3.9; 484 3.9; 518 3.7; 554 3.3; 593 3.2; 635 2.8; 679 2.4; 726 2.1; 777 1.9; 832 1.4; 890 0.9; 952 0.5; 1019 -0.2; 1090 -0.7; 1167 -1.1; 1248 -1.2; 1336 -1.6; 1429 -1.8; 1529 0.4; 1636 0.2; 1751 -2.4; 1873 -1.5; 2004 -0.6; 2145 0.4; 2295 1.4; 2455 2.8; 2627 3.9; 2811 4.7; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999028093dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  0.61 | 5.5 dB  |
| Peaking | 60 Hz   |  1.03 | 1.5 dB  |
| Peaking | 411 Hz  |  0.74 | 4.4 dB  |
| Peaking | 1629 Hz |  0.99 | -3.8 dB |
| Peaking | 3820 Hz |  0.91 | 7.6 dB  |
| Peaking | 1587 Hz | 10.89 | 4.5 dB  |
| Peaking | 1699 Hz |  3.94 | -2.0 dB |
| Peaking | 4085 Hz |  5.5  | -1.2 dB |
| Peaking | 6380 Hz |  2.26 | 5.3 dB  |
| Peaking | 7442 Hz |  1.7  | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530/Phiaton%20Chord%20MS530.png)